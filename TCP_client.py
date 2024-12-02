#!/usr/bin/python3
import socket

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host IP address of your Windows server
host = '192.168.1.16'  # Replace with your Windows machine's IP
port = 444  # Port on which the server is listening

# Connect to the server
clientsocket.connect((host, port))

# Receive data from the server
message = clientsocket.recv(1024)

# Close the socket after receiving the message
clientsocket.close()

# Print the received message (assuming it's in ASCII)
print(message.decode('ascii'))
