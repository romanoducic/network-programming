from socket import *

socket = socket(type=SOCK_DGRAM)

socket.sendto(b'Hello Server',('localhost',5001))

data,addr = socket.recvfrom(1024)

print(data,addr)