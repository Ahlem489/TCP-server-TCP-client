#!/usr/bin/python3
import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host IP address of your Windows machine
host = '192.168.1.16'  # Windows machine IP
port = 444  # Port on which the server will listen

# Bind the server socket to the address and port
serversocket.bind((host, port))

# Start listening for incoming connections
serversocket.listen(3)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from a client
    clientsocket, address = serversocket.accept()
    print(f"Received connection from {address}")

    # Send a message to the client
    message = 'Thank you for connecting to the server.\r\n'
    clientsocket.send(message.encode('ascii'))

    # Close the client socket after communication
    clientsocket.close()