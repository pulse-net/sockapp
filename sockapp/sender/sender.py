from ..constants import *
from ..utils import error
from .tcp_file_sender import TCPFileSender
from .tcp_message_sender import TCPMessageSender
from .udp_file_sender import UDPFileSender


class Sender:
    @staticmethod
    def get_sender(host, message=None, filename=None, port=PORT, protocol=PROTOCOL):
        if protocol == "TCP":
            if filename != None:
                return TCPFileSender(filename=filename, host=host, port=port)

            return TCPMessageSender(message=message, host=host, port=port)
        elif protocol == "UDP":
            if filename != None:
                return UDPFileSender(filename=filename, host=host, port=port)

            raise error.OperationNotSupported(
                message="Messaging is available in TCP only, UDP support for messaging will be added in future version!"
            )
        else:
            raise error.InvalidSocketProtocol(
                message=f"Protocol {protocol} not known, cannot create sender instance!"
            )
