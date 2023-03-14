import socket
import threading
import datetime
from localMachineInfo import print_machine_info
from queue import Queue

print(datetime.datetime.now())
print_machine_info()

inputHost = input("Insert host address: ")
print("Port scanning for: ", inputHost)

print("Insert start port and end port for scanning:")

startPort = input("Start port=> ")
endPort = input("End port => ")

startPort = int(startPort)
endPort = int(endPort)

def scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn = sock.connect((inputHost, port))
        with print_lock:
            print('Port' , port, ' je otvoren!!!')
        conn.close()
    except:
        pass

q = Queue()

def threader():
    while True:
        worker = q.get()
        scanner(worker)
        q.task_done()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(startPort,endPort):
    q.put(worker)

q.join()

timeStart = datetime.datetime.now()
timeEnd = datetime.datetime.now()

print('Process time: {}'.format(timeStart - timeEnd))