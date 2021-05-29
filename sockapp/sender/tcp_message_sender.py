"""
Client that sends the message
"""
import socket

from ..constants import *
from ..utils.error import ConnectionFailure


class TCPMessageSender:
    def __init__(self, message, host, port=PORT):
        self.__message = message
        self.__host = host
        self.__port = port

    def send_message(self):
        # Create the client TCP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        print(f"[+] Connecting to {self.__host}:{self.__port}")
        s.settimeout(MAX_TIMEOUT)

        try:
            s.connect((self.__host, self.__port))
        except socket.timeout:
            raise ConnectionFailure("Connection timed out, make sure the receiver is in same network!")
        except ConnectionRefusedError:
            raise ConnectionFailure("Connection refused by receiver, make sure you have pressed receive in receiver!")

        s.settimeout(None)
        print("[+] Connected.")

        # Send the message
        s.send(self.__message.encode())

        # Close the socket
        s.close()
