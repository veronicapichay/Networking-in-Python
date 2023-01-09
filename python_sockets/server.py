import socket

PORT = 9090

## automatically gets private ip addy dynamically
# only works when not using a virtual box
# host = socket.gethostbyname(socket.gethostname())
HOST = ''

# specify the type of socket - TCP - Socket for accepting connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# passing a tuple of host and port 
server.bind((HOST, PORT))

server.listen(5) # number of acceptable connections

while True:
    # comms socket 
    # returns the addy of the client who is connecting and a socket that we can use to talk to client
    communication_socket, address = server.accept()
    print(f"Connected to  {address}")
    # specify buffer size and decode for accepting - ascii can be use
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"This is server, I can hear you LAC!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")