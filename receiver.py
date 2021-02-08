"""
Server receiver of the file
"""
import socket
import tqdm
import os

# Device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

# Receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def receive():
    # Create the server socket
    # TCP socket
    s = socket.socket()

    # Bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))

    # Enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    # Accept connection if there is any
    client_socket, address = s.accept() 

    # If below code is executed, that means the sender is connected
    print(f"[+] {address} is connected.")

    # Receive the file infos
    # Receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)

    # Remove absolute path if there is
    filename = os.path.basename(filename)

    # Convert to integer
    filesize = int(filesize)

    # Start receiving the file from the socket and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "wb") as f:
        while True:
            # Read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)

            if not bytes_read:    
                # Nothing is received file transmitting is done
                break

            # Write to the file the bytes we just received
            f.write(bytes_read)

            # Update the progress bar
            progress.update(len(bytes_read))

    # Close the client socket
    client_socket.close()

    # Close the server socket
    s.close()

if __name__ == "__main__":
    receive()