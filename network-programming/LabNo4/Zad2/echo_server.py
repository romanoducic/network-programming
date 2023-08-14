import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

host = socket.gethostname()
port = 12345

echo_server = socket.socket()       # TCP socket
echo_server.bind((host, port))
echo_server.listen(5)

print ("Cekam klijenta")

conn, addr = echo_server.accept()   # Prihvacanje konekcije kada se klijent spoji

print ("Spojen: "), addr

while True:
    data = conn.recv(1024)         # Prihvacanje podataka od klijenta
    if not data: break             # ako nema podataka izađi
    conn.sendall(data)             # Vrati primljene podatke klijentu


print(datetime.datetime.now())

conn.close()