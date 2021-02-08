"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

def send_file(filename, host, port):
    # Get the file size
    filesize = os.path.getsize(filename)

    # Create the client socket
    s = socket.socket()
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

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)