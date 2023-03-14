
from socket import *

socket = socket(type=SOCK_DGRAM)

socket.bind(('localhost',5001))

while True:
    data,addr = socket.recvfrom(1024)
    print(data,addr)
    socket.sendto(data,addr)