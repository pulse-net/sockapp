"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os

from ..constants import *
from ..utils.error import ConnectionFailure


class TCPFileSender:
    def __init__(self, filename, host, port=PORT):
        self.__filename = filename
        self.__host = host
        self.__port = port

    def send_file(self):
        # Get the file size
        filesize = os.path.getsize(self.__filename)

        # Create the client TCP socket
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        print(f"[+] Connecting to {self.__host}:{self.__port}")
        s.settimeout(MAX_TIMEOUT)

        try:
            s.connect((self.__host, self.__port))
        except Exception as e:
            raise ConnectionFailure("Connection timed out")

        s.settimeout(None)
        print("[+] Connected.")

        # Send the filename and filesize
        s.send(f"{self.__filename}{SEPARATOR}{filesize}".encode())

        # Start sending the file
        progress = tqdm.tqdm(
            range(filesize),
            f"Sending {self.__filename}",
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        )
        with open(self.__filename, "rb") as f:
            while True:
                # Read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # File transmitting is done
                    break

                # We use sendall to assure transimission in busy networks
                s.sendall(bytes_read)

                # Update the progress bar
                progress.update(len(bytes_read))

        # Close the socket
        s.close()
