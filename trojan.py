import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Local ip address
host = "127.0.0.1"
port = 1234

server.bind((host,port))
server.listen(5)
run = True

client, addr = server.accept()
print("Got Connection from ",addr)
while run:
    try:
        data = input(">>>")
        client.send(data.encode('utf-8'))
        message = client.recv(1024)
        print(message.decode("utf-8"))
    except ConnectionError:
        print("Client lost... Trying to connect...")
        client, addr = server.accept()
        print("Got Connection from ",addr)



