from sockapp.receiver.udp_receiver import UDPReceiver
from ..constants import *
from ..utils import error
from .tcp_receiver import TCPReceiver
from .udp_receiver import UDPReceiver

class Receiver:
    @staticmethod
    def get_receiver(port=PORT, protocol=PROTOCOL):
        if protocol == "TCP":
            return TCPReceiver(port=port)
        elif protocol == "UDP":
            return UDPReceiver(port=port)
        else:
            raise error.InvalidSocketProtocol(message=f"Protocol {protocol} not known, cannot create receiver instance!")