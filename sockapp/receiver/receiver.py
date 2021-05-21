from ..constants import *
from ..utils import error
from .tcp_receiver import TCPReceiver

class Receiver:
    @staticmethod
    def get_receiver(port=PORT, protocol=PROTOCOL):
        if protocol == "TCP":
            return TCPReceiver(port=port)
        elif protocol == "UDP":
            pass
        else:
            raise error.InvalidSocketProtocol(message=f"Protocol {protocol} not known, cannot create receiver instance!")