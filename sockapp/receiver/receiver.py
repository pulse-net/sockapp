from ..constants import *
from ..utils import error
from .tcp_file_receiver import TCPFileReceiver
from .tcp_message_receiver import TCPMessageReceiver
from .udp_file_receiver import UDPFileReceiver
from .udp_message_receiver import UDPMessageReceiver


class Receiver:
    @staticmethod
    def get_receiver(port=PORT, protocol=PROTOCOL, is_message=False):
        if protocol == "TCP":
            if not is_message:
                return TCPFileReceiver(port=port)

            return TCPMessageReceiver(port=port)            
        elif protocol == "UDP":
            if not is_message:
                return UDPFileReceiver(port=port)

            return UDPMessageReceiver(port=port)
        else:
            raise error.InvalidSocketProtocol(
                message=f"Protocol {protocol} not known, cannot create receiver instance!"
            )
