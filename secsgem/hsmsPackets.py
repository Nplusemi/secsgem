#####################################################################
# hsmsPackets.py
#
# (c) Copyright 2015, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""Contains objects that encapsulate hsms messages"""

import struct


class HsmsHeader:
    """Generic HSMS header

    Base for different specific headers

    :param system: message ID
    :type system: integer
    :param session_id: device / session ID
    :type session_id: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsHeader(3, 100)
        secsgem.hsmsPackets.HsmsHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 3, 'sessionID': 100, 'requireResponse': False, 'sType': 1})

    """
    def __init__(self, system, session_id):
        self.sessionID = session_id
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x01
        self.system = system

    def __str__(self):
        return '{sessionID:0x%04x, stream:%02d, function:%02d, pType:0x%02x, sType:0x%02x, system:0x%08x, requireResponse:%01d}' % \
            (self.sessionID, self.stream, self.function, self.pType, self.sType, self.system, self.requireResponse)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class HsmsSelectReqHeader(HsmsHeader):
    """Header for Select Request

    Header for message with SType 1.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsSelectReqHeader(14)
        secsgem.hsmsPackets.HsmsSelectReqHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 14, 'sessionID': 65535, 'requireResponse': False, 'sType': 1})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x01


class HsmsSelectRspHeader(HsmsHeader):
    """Header for Select Response

    Header for message with SType 2.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsSelectRspHeader(24)
        secsgem.hsmsPackets.HsmsSelectRspHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 24, 'sessionID': 65535, 'requireResponse': False, 'sType': 2})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x02


class HsmsDeselectReqHeader(HsmsHeader):
    """Header for Deselect Request

    Header for message with SType 3.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsDeselectReqHeader(1)
        secsgem.hsmsPackets.HsmsDeselectReqHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 1, 'sessionID': 65535, 'requireResponse': False, 'sType': 3})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x03


class HsmsDeselectRspHeader(HsmsHeader):
    """Header for Deselect Response

    Header for message with SType 4.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsDeselectRspHeader(1)
        secsgem.hsmsPackets.HsmsDeselectRspHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 1, 'sessionID': 65535, 'requireResponse': False, 'sType': 4})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x04


class HsmsLinktestReqHeader(HsmsHeader):
    """Header for Linktest Request

    Header for message with SType 5.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsLinktestReqHeader(2)
        secsgem.hsmsPackets.HsmsLinktestReqHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 2, 'sessionID': 65535, 'requireResponse': False, 'sType': 5})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x05


class HsmsLinktestRspHeader(HsmsHeader):
    """Header for Linktest Response

    Header for message with SType 6.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsLinktestRspHeader(10)
        secsgem.hsmsPackets.HsmsLinktestRspHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 10, 'sessionID': 65535, 'requireResponse': False, 'sType': 6})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x06


class HsmsRejectReqHeader(HsmsHeader):
    """Header for Reject Request

    Header for message with SType 7.

    :param system: message ID
    :type system: integer
    :param s_type: sType of rejected message
    :type s_type: integer
    :param reason: reason for rejection
    :type reason: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsRejectReqHeader(17, 3, 4)
        secsgem.hsmsPackets.HsmsRejectReqHeader({'function': 4, 'stream': 3, 'pType': 0, 'system': 17, 'sessionID': 65535, 'requireResponse': False, 'sType': 7})

    """

    def __init__(self, system, s_type, reason):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = s_type
        self.function = reason
        self.pType = 0x00
        self.sType = 0x07


class HsmsSeparateReqHeader(HsmsHeader):
    """Header for Separate Request

    Header for message with SType 9.

    :param system: message ID
    :type system: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsSeparateReqHeader(17)
        secsgem.hsmsPackets.HsmsSeparateReqHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 17, 'sessionID': 65535, 'requireResponse': False, 'sType': 9})

    """

    def __init__(self, system):
        HsmsHeader.__init__(self, system, 0xFFFF)
        self.requireResponse = False
        self.stream = 0x00
        self.function = 0x00
        self.pType = 0x00
        self.sType = 0x09


class HsmsStreamFunctionHeader(HsmsHeader):
    """Header for SECS message

    Header for message with SType 0.

    :param system: message ID
    :type system: integer
    :param stream: messages stream
    :type stream: integer
    :param function: messages function
    :type function: integer
    :param require_response: is response expected from remote
    :type require_response: boolean
    :param session_id: device / session ID
    :type session_id: integer

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsStreamFunctionHeader(22, 1, 1, True, 100)
        secsgem.hsmsPackets.HsmsStreamFunctionHeader({'function': 1, 'stream': 1, 'pType': 0, 'system': 22, 'sessionID': 100, 'requireResponse': True, 'sType': 0})

    """

    def __init__(self, system, stream, function, require_response, session_id):
        HsmsHeader.__init__(self, system, session_id)
        self.sessionID = session_id
        self.requireResponse = require_response
        self.stream = stream
        self.function = function
        self.pType = 0x00
        self.sType = 0x00
        self.system = system


class HsmsPacket:
    """Class for hsms packet.

    Contains all required data and functions.

    :param header: header used for this packet
    :type header: :class:`secsgem.hsmsPackets.HsmsHeader` and derived
    :param data: data part used for streams and functions (SType 0)
    :type data: string

    **Example**::

        >>> import secsgem
        >>>
        >>> secsgem.hsmsPackets.HsmsPacket(secsgem.hsmsPackets.HsmsLinktestReqHeader(2))
        secsgem.hsmsPackets.HsmsPacket({'header': secsgem.hsmsPackets.HsmsLinktestReqHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 2, 'sessionID': 65535, 'requireResponse': False, 'sType': 5}), 'data': ''})

    """
    def __init__(self, header=None, data=""):
        if header is None:
            self.header = HsmsHeader(0, 0)
        else:
            self.header = header

        self.data = data

    def __str__(self):
        data = "header: " + self.header.__str__()
        return data

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def encode(self):
        """Encode packet data to hsms packet

        :returns: encoded packet
        :rtype: string

        **Example**::

            >>> import secsgem
            >>>
            >>> packet = secsgem.hsmsPackets.HsmsPacket(secsgem.hsmsPackets.HsmsLinktestReqHeader(2))
            >>> secsgem.common.format_hex(packet.encode())
            '00:00:00:0a:ff:ff:00:00:00:05:00:00:00:02'

        """
        length = 10 + len(self.data)
        data_length_text = str(len(self.data)) + "s"

        header_stream = self.header.stream
        if self.header.requireResponse:
            header_stream |= 0b10000000

        return struct.pack(">LHBBBBL" + data_length_text, length, self.header.sessionID, header_stream, self.header.function, self.header.pType, self.header.sType, self.header.system, self.data)

    @staticmethod
    def decode(text):
        """Decode byte array hsms packet to HsmsPacket object

        :returns: received packet object
        :rtype: :class:`secsgem.hsmsPackets.hsmsPacket`

        **Example**::

            >>> import secsgem
            >>>
            >>> packetData = "\\x00\\x00\\x00\\x0b\\xff\\xff\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x02"
            >>>
            >>> secsgem.format_hex(packetData)
            '00:00:00:0b:ff:ff:00:00:00:05:00:00:00:02'
            >>>
            >>> secsgem.hsmsPackets.HsmsPacket.decode(packetData)
            secsgem.hsmsPackets.HsmsPacket({'header': secsgem.hsmsPackets.HsmsHeader({'function': 0, 'stream': 0, 'pType': 0, 'system': 2, 'sessionID': 65535, 'requireResponse': False, 'sType': 5}), 'data': ''})


        """
        data_length = len(text) - 14
        data_length_text = str(data_length) + "s"

        res = struct.unpack(">LHBBBBL" + data_length_text, text)

        result = HsmsPacket(HsmsHeader(res[6], res[1]))
        result.header.requireResponse = (((res[2] & 0b10000000) >> 7) == 1)
        result.header.stream = res[2] & 0b01111111
        result.header.function = res[3]
        result.header.pType = res[4]
        result.header.sType = res[5]
        result.data = res[7]

        return result
