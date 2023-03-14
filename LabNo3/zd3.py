import socket
client_socket = socket.socket()
host = socket.gethostbyname('www.google.hr')
port = 80

client_socket.connect((host,port))
print ('The socket has succesfully connected to Google on port', port, 'and Ip address', host)

client_socket.close()