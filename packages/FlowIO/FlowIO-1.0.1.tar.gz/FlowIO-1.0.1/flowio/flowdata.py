import array
from operator import and_
from struct import calcsize, iter_unpack
from warnings import warn
import os
import re
from functools import reduce
from .create_fcs import create_fcs

try:
    # noinspection PyUnresolvedReferences, PyUnboundLocalVariable
    basestring
except NameError:
    # noinspection PyShadowingBuiltins
    basestring = str


class FlowData(object):
    """
    Object representing a Flow Cytometry Standard (FCS) file.
    FCS versions 2.0, 3.0, and 3.1 are supported.

    Note:
        Some FCS files incorrectly report the location of the last data byte
        as the last byte exclusive of the data section rather than the last
        byte inclusive of the data section. Technically, these are invalid
        FCS files but these are not corrupted data files. To attempt to read
        in these files, set the `ignore_offset_error` option to True.

    :param filename_or_handle: a path string or a file handle for an FCS file
    :param ignore_offset_error: option to ignore data offset error (see above note), default is False
    :param only_text: option to only read the "text" segment of the FCS file without loading event data,
        default is False
    """
    def __init__(self, filename_or_handle, ignore_offset_error=False, only_text=False):
        if isinstance(filename_or_handle, basestring):
            self._fh = open(str(filename_or_handle), 'rb')
        else:
            self._fh = filename_or_handle

        current_offset = 0

        self._ignore_offset = ignore_offset_error

        try:
            unused_path, self.name = os.path.split(self._fh.name)
        except (AttributeError, TypeError):
            self.name = 'InMemoryFile'

        # Get actual file size for sanity check of data section
        self._fh.seek(0, os.SEEK_END)
        self.file_size = self._fh.tell()
        self._fh.seek(current_offset)  # reset to beginning before parsing

        # parse headers
        self.header = self.__parse_header(current_offset)

        # parse text
        self.text = self.__parse_text(
            current_offset,
            self.header['text_start'],
            self.header['text_stop'])

        self.channel_count = int(self.text['par'])
        self.event_count = int(self.text['tot'])

        # parse analysis
        try:
            a_start = int(self.text['beginanalysis'])
        except KeyError:
            a_start = self.header['analysis_start']
        try:
            a_stop = int(self.text['endanalysis'])
        except KeyError:
            a_stop = self.header['analysis_end']

        self.analysis = self.__parse_analysis(current_offset, a_start, a_stop)

        # parse data
        try:
            d_start = int(self.text['begindata'])
        except KeyError:
            d_start = self.header['data_start']
        try:
            d_stop = int(self.text['enddata'])
        except KeyError:
            d_stop = self.header['data_end']

        if d_stop > self.file_size:
            raise EOFError("FCS header indicates data section greater than file size")

        if only_text:
            self.events = None
        else:
            self.events = self.__parse_data(
                current_offset,
                d_start,
                d_stop,
                self.text
            )

        self.channels = self._parse_channels()

        self._fh.close()

    def __repr__(self):
        if hasattr(self, 'name'):
            name = self.name
        else:
            name = "Unread FCS data"

        return '%s(%s)' % (self.__class__.__name__, name)

    def __read_bytes(self, offset, start, stop):
        """Read in bytes from start to stop inclusive."""
        self._fh.seek(offset + start)

        data = self._fh.read(stop - start + 1)

        return data

    def __parse_header(self, offset):
        """
        Parse the FlowData FCS file at the offset (supporting multiple
        data segments in a file
        """
        header = dict()
        header['version'] = float(self.__read_bytes(offset, 3, 5))
        header['text_start'] = int(self.__read_bytes(offset, 10, 17))
        header['text_stop'] = int(self.__read_bytes(offset, 18, 25))
        header['data_start'] = int(self.__read_bytes(offset, 26, 33))
        header['data_end'] = int(self.__read_bytes(offset, 34, 41))
        try:
            header['analysis_start'] = int(self.__read_bytes(offset, 42, 49))
        except ValueError:
            header['analysis_start'] = -1
        try:
            header['analysis_end'] = int(self.__read_bytes(offset, 50, 57))
        except ValueError:
            header['analysis_end'] = -1

        return header

    def __parse_text(self, offset, start, stop):
        """return parsed text segment of FCS file"""
        num_items = (stop - start + 1)
        self._fh.seek(offset + start)
        tmp = array.array('b')
        tmp.fromfile(self._fh, int(num_items))
        tmp = tmp.tobytes()

        try:
            # try UTF-8 first
            tmp = tmp.decode()
        except UnicodeDecodeError:
            # next best guess is Latin-1, if not that either, we throw the exception
            tmp = tmp.decode("ISO-8859-1")
        return self.__parse_pairs(tmp)

    def __parse_analysis(self, offset, start, stop):
        """return parsed analysis segment of FCS file"""
        if start == stop:
            return {}
        else:
            num_items = (stop - start + 1)
            self._fh.seek(offset + start)
            tmp = array.array('b')
            tmp.fromfile(self._fh, int(num_items))
            tmp = tmp.tobytes()

            try:
                # try UTF-8 first
                tmp = tmp.decode()
            except UnicodeDecodeError:
                # next best guess is Latin-1, if not that either, we throw the exception
                tmp = tmp.decode("ISO-8859-1")

            return self.__parse_pairs(tmp)

    def __parse_data(self, offset, start, stop, text):
        """
        Return array of data segment of FCS file
        """
        data_type = text['datatype']
        mode = text['mode']
        if mode == 'c' or mode == 'u':
            raise NotImplementedError(
                "FCS data stored as type \'%s\' is unsupported" % mode
            )

        if text['byteord'] == '1,2,3,4' or text['byteord'] == '1,2':
            order = '<'
        elif text['byteord'] == '4,3,2,1' or text['byteord'] == '2,1':
            order = '>'
        else:
            warn("unsupported byte order %s , using default @" % text['byteord'])
            order = '@'
            # from here on out we assume mode "l" (list)

        bit_width = []
        for i in range(1, int(text['par']) + 1):
            bit_width.append(int(text['p%db' % i]))

        if data_type.lower() == 'i':
            data = self.__parse_int_data(
                offset,
                start,
                stop,
                bit_width,
                order
            )
        else:
            data = self.__parse_non_int_data(
                offset,
                start,
                stop,
                data_type.lower(),
                order
            )

        return data

    def __calc_data_item_count(self, start, stop, data_type_size):
        # calculate how much data to read in.
        data_sect_size = stop - start + 1
        data_mod = data_sect_size % data_type_size

        if data_mod > 0:
            # Some FCS files incorrectly report the location of the last data byte
            # as the last byte exclusive of the data section rather than the last
            # byte inclusive of the data section. This means the stop location will
            # be off by +1. Technically, this is an invalid FCS file, but since
            # it is so common, we will try to parse these files. For any discrepancy
            # other than +1 we throw an error
            if data_mod == 1 and self._ignore_offset:
                # warn user that the offset is off
                warn_msg = "FCS file %s reported incorrect data offset. " % self.name
                warn_msg += "Attempting to parse data section, but event data should be "
                warn_msg += "reviewed before trusting this file."
                warn(warn_msg)

                stop = stop - 1
                data_sect_size = data_sect_size - 1
            elif data_mod == 1 and not self._ignore_offset:
                # attempt to close file handle before raising error
                self._fh.close()

                err_msg = "FCS file %s reports a data offset that is off by 1. " % self.name
                err_msg += "Set `ignore_offset_error=True` to force reading in this file."
                raise ValueError(err_msg)
            else:
                # attempt to close file handle before raising error
                self._fh.close()

                raise ValueError("Unable to determine the correct byte offsets for event data")

        num_items = data_sect_size / data_type_size

        return num_items, stop

    def __parse_int_data(self, offset, start, stop, bit_width, order):
        """Parse out and return integer list data from FCS file"""

        if reduce(and_, [item in [8, 16, 32] for item in bit_width]):
            # We have a uniform bit width for all parameters,
            # use the first value to determine the number of actual events
            if len(set(bit_width)) == 1:
                data_type_size = bit_width[0] / 8
                num_items, stop = self.__calc_data_item_count(start, stop, data_type_size)

                self._fh.seek(offset + start)
                tmp = array.array(self.__format_integer(bit_width[0]))
                tmp.fromfile(self._fh, int(num_items))
                if order == '>':
                    tmp.byteswap()

            # parameter sizes are different
            # e.g. 8, 8, 16, 8, 32 ...
            else:
                # can't use array for heterogeneous bit widths
                tmp = self.__extract_var_length_int(bit_width, offset, order, start, stop)

        else:  # non standard bit width...  Does this happen?
            warn('Non-standard bit width for data segments')
            return None
        return tmp

    def __extract_var_length_int(self, bit_width, offset, order, start, stop):
        data_format = order
        for cur_width in bit_width:
            data_format += '%s' % self.__format_integer(cur_width)

        # array module doesn't have a function to heterogeneous bit widths,
        # so fall back to the slower unpack approach
        tuple_tmp = iter_unpack(data_format, self.__read_bytes(offset, start, stop))
        tmp = [ti for t in tuple_tmp for ti in t]
        return tmp

    def __parse_non_int_data(self, offset, start, stop, data_type, order):
        """Parse out and return float or ASCII list data from FCS file"""
        data_type_size = calcsize(data_type)
        num_items, stop = self.__calc_data_item_count(start, stop, data_type_size)

        self._fh.seek(offset + start)
        tmp = array.array(data_type)
        tmp.fromfile(self._fh, int(num_items))
        if order == '>':
            tmp.byteswap()
        return tmp

    @staticmethod
    def __parse_pairs(text):
        """return key/value pairs from a delimited string"""
        delimiter = text[0]

        if delimiter == r'|':
            delimiter = r'\|'
        elif delimiter == r'\a'[0]:  # test for delimiter being \
            delimiter = '\\\\'  # regex will require it to be \\
        elif delimiter == r'*':
            delimiter = r'\*'

        tmp = text[1:-1].replace('$', '')
        # match the delimited character unless it's doubled
        regex = re.compile('(?<=[^%s])%s(?!%s)' % (
            delimiter, delimiter, delimiter))
        tmp = regex.split(tmp)
        return dict(
            zip(
                [x.lower().replace(
                    delimiter + delimiter, delimiter) for x in tmp[::2]],
                [x.replace(delimiter + delimiter, delimiter) for x in tmp[1::2]]
            )
        )

    @staticmethod
    def __format_integer(b):
        """return binary format of an integer"""
        if b == 8:
            return 'B'
        elif b == 16:
            return 'H'
        elif b == 32:
            return 'I'
        else:
            raise ValueError(
                "Invalid integer bit size (%d) for event data. Compatible sizes are 8, 16, & 32." % b
            )

    def _parse_channels(self):
        """
        Returns a dictionary of channels, with key as channel number
        and value is a dictionary of the PnN and PnS text
        """
        channels = dict()
        regex_pnn = re.compile(r"^p(\d+)n$", re.IGNORECASE)

        for i in self.text.keys():
            match = regex_pnn.match(i)
            if not match:
                continue

            channel_num = match.groups()[0]
            channels[channel_num] = dict()

            channels[channel_num]['PnN'] = self.text[match.group()]

            # now check for PnS field, which is optional so may not exist
            regex_pns = re.compile("^p%ss$" % channel_num, re.IGNORECASE)
            for j in self.text.keys():
                match = regex_pns.match(j)
                if match:
                    channels[channel_num]['PnS'] = self.text[match.group()]

        return channels

    def write_fcs(self, filename, metadata=None):
        """
        Export FlowData instance as a new FCS file.

        By default, the output FCS file will include the $cyt, $date, and $spill
        keywords (and values) from the FlowData instance. To exclude these keys,
        specify a custom `metadata` dictionary (including an empty dictionary for
        the bare minimum metadata).

        :param filename: name of exported FCS file
        :param metadata: an optional dictionary for adding metadata keywords/values
        :return: None
        """
        if self.events is None:
            raise AttributeError(
                "FlowData instance does not contain event data. This might"
                "occur if the FCS file was read with the only_text=True option."
            )

        if metadata is None:
            metadata = {}

            # by default, we'll add the $cyt, $date, & $spillover (or $spill) metadata
            if 'spillover' in self.text:
                metadata['spillover'] = self.text['spillover']
            elif 'spill' in self.text:
                metadata['spillover'] = self.text['spill']

            if 'date' in self.text:
                metadata['date'] = self.text['date']

            if 'cyt' in self.text:
                metadata['cyt'] = self.text['cyt']

        pnn_labels = [''] * len(self.channels)
        pns_labels = [''] * len(self.channels)

        for k in self.channels:
            pnn_labels[int(k) - 1] = self.channels[k]['PnN']

            if 'PnS' in self.channels[k]:
                pns_labels[int(k) - 1] = self.channels[k]['PnS']

        fh = open(filename, 'wb')
        fh = create_fcs(
            fh,
            self.events,
            pnn_labels,
            opt_channel_names=pns_labels,
            metadata_dict=metadata
        )
        fh.close()
