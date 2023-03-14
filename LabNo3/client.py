import socket
client_socket = socket.socket()
host = socket.gethostname()
port = 9999

client_socket.connect((host,port))
print (client_socket.recv(1024))

client_socket.close()

# Odgovor: client_socket.connect((host,port)) govori serveru na koji ce se socket povezati