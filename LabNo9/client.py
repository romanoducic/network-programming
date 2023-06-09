import socket
import ssl
import datetime
from localMachineInfo import print_machine_info
from server import HOST as SERVER_HOST
from server import PORT as SERVER_PORT

print("Date and time", datetime.datetime.now())

print_machine_info()

HOST = "127.0.0.1"
PORT = 60002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client = ssl.wrap_socket(client, keyfile="key.pem", certfile="cert.pem")

if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep

        client.send("Hello from client!".encode("utf-8"))
        sleep(1)