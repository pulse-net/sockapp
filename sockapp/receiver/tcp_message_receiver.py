"""
Server receiver of the file
"""
import socket
import tqdm
import os

from ..constants import *


class TCPMessageReceiver:
    def __init__(self, port=PORT):
        self.__port = port

    def receive_message(self):
        # Create the server socket
        # TCP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # Bind the socket to our local address
        s.bind((SERVER_HOST, self.__port))

        # Enabling our server to accept connections
        # 5 here is the number of unaccepted connections that
        # the system will allow before refusing new connections
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{self.__port}")

        # Accept connection if there is any
        client_socket, address = s.accept()

        # If below code is executed, that means the sender is connected
        print(f"[+] {address} is connected.")

        # Receive the message
        # Receive using client socket, not server socket
        received = client_socket.recv(BUFFER_SIZE).decode()

        # Close the client socket
        client_socket.close()

        # Close the server socket
        s.close()

        return received
