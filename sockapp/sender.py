"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

def send_file(filename, host, port=5001):
    # Get the file size
    filesize = os.path.getsize(filename)

    # Create the client socket
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # Send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # Start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
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