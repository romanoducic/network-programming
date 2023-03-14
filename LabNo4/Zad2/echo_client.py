# -- coding: utf-8 --
import socket
import datetime
from local_machine_info import print_machine_info


host = socket.gethostname()
port = 12345
client_socket = socket.socket()     # TCP socket

client_socket.connect((host,port))

client_socket.sendall('Hello Server'.encode())

data = client_socket.recv(1024)     # Tekst koji je primljen od servera

while True:
    try:
        textInput = input("Text input: ")

        if textInput == 'grgo_jelavic':
        	raise ValueError
    except ValueError:
        print("Value error!")
    else:
        break
 
print (data)                        # Ispis podataka

print(datetime.datetime.now())      

client_socket.close()               # Close the connection