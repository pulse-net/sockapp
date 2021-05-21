"""
Server receiver of the file
"""
import socket
import tqdm
import os

from ..constants import *

class UDPReceiver:
    def __init__(self, port=PORT):
        self.__port = port

    def receive_file(self):
        # Create the server socket
        # TCP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind the socket to our local address
        s.bind((SERVER_HOST, self.__port))

        # Address to receive from
        addr = (SERVER_HOST, PORT)

        # Receive the file infos
        # Receive using client socket, not server socket
        received = str(s.recvfrom(BUFFER_SIZE)[0])
        filename, filesize = received.split(SEPARATOR)
        filename = filename[2:]
        filesize = filesize[:-1]

        # Remove absolute path if there is
        filename = os.path.basename(filename)

        # Convert to integer
        filesize = int(filesize)

        # Start receiving the file from the socket and writing to the file stream
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

        with open(filename, "wb") as f:
            while True:
                # Read 1024 bytes from the socket (receive)
                bytes_read = s.recvfrom(BUFFER_SIZE)[0]

                if bytes_read.decode("UTF-8") == "<END>": 
                    # Nothing is received file transmitting is done
                    break

                # Write to the file the bytes we just received
                f.write(bytes_read)

                # Update the progress bar
                progress.update(len(bytes_read))
