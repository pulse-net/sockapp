from ..constants import *
from ..utils import error
from .tcp_sender import TCPSender

class Sender:
    @staticmethod
    def get_sender(filename, host, port=PORT, protocol=PROTOCOL):
        if protocol == "TCP":
            return TCPSender(filename=filename, host=host, port=port)
        elif protocol == "UDP":
            pass
        else:
            raise error.InvalidSocketProtocol(message=f"Protocol {protocol} not known, cannot create sender instance!")