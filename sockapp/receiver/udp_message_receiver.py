"""
Server receiver of the message
"""
import socket

from ..constants import *


class UDPMessageReceiver:
    def __init__(self, port=PORT):
        self.__port = port

    def receive_message(self):
        # Create the server socket
        # UDP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind the socket to our local address
        s.bind((SERVER_HOST, self.__port))

        # Receive the file infos
        # Receive using client socket, not server socket
        received = str(s.recvfrom(BUFFER_SIZE)[0].decode())

        return received
