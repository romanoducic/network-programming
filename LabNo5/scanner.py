import socket
import datetime

print(datetime.datetime.now())

from localMachineInfo import print_machine_info

print_machine_info()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inputHost = input("Insert host address: ")
print("Port scanning for: ", inputHost)

print("Insert start port and end port for scanning:")

startPort = input("Start port=> ")
endPort = input("End port => ")

startPort = int(startPort)
endPort = int(endPort)

def scanner(port):
    try:
        sock.connect((inputHost,port))
        return True
    except:
        return False

for portNumber in range(startPort,endPort):
    print("Scanning port: ", portNumber)
    if scanner(portNumber):
        print('Port: ',portNumber,'/tcp',' is open!')