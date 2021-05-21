from sockapp.sender.udp_sender import UDPSender
from ..constants import *
from ..utils import error
from .tcp_sender import TCPSender
from .udp_sender import UDPSender


class Sender:
    @staticmethod
    def get_sender(filename, host, port=PORT, protocol=PROTOCOL):
        if protocol == "TCP":
            return TCPSender(filename=filename, host=host, port=port)
        elif protocol == "UDP":
            return UDPSender(filename=filename, host=host, port=port)
        else:
            raise error.InvalidSocketProtocol(
                message=f"Protocol {protocol} not known, cannot create sender instance!"
            )
