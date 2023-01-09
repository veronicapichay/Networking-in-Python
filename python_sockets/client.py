import socket

# server's ip addy and port
HOST = ''
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("This is client, can you hear me? OVER!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))