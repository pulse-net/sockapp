"""
Client that sends the message
"""
import socket
import tqdm
import os

from ..constants import *


class TCPMessageSender:
    def __init__(self, message, host, port=PORT):
        self.__message = message
        self.__host = host
        self.__port = port

    def send_message(self):
        # Create the client TCP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        print(f"[+] Connecting to {self.__host}:{self.__port}")
        s.connect((self.__host, self.__port))
        print("[+] Connected.")

        # Send the message
        s.send(self.__message.encode())

        # Close the socket
        s.close()
