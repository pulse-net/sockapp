# Change logs

## v0.1-alpha-0

- Basic build.
- Simple web application with sending and receiving capabilities.

## 0.1-alpha-1

- Open sockapp in default browser on running flask server.
- Fix receiving button to be highlighted till transaction is complete.
- Alerts replaced with sweet alerts.

## 0.1-alpha-2

- Show own hostname and IP address.
- Add option to change port from command line while running sockapp server.

## 0.1-alpha-5

- Add option to change between TCP/IP and UDP as protocol.
- Dynamic dispatch receivers and senders based on protocol.
- Actually use the port passed by user in sockets.
- UDP sockets are experimental and can have bugs (use at own risk).

# 0.1-alpha-6

- Check if receiver's IP is equal to sender's IP while sending file.
- Send a directory without having to compress it explicitly.
- Fix window's style path error.
- Allow sending messages instead of files too (Experimental, will be improved in future).