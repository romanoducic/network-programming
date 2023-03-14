import multiprocessing
from multiprocessing import Pool
import socket
from localMachineInfo import print_machine_info
import datetime

def scan(x):
    target_ip, port = x

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try: 
        sock.connect((target_ip, port))
        sock.close()

        return port, True

    except (socket.timeout, socket.error):
        return port, False

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Program starts at: ' , datetime.datetime.now())
    print('Program is running on this PC: ')
    print_machine_info()

    print('--------------------------------------------------------------')

    hostAddress = input('Please input the host address: ')
    ipAddress = socket.gethostbyname(hostAddress)
    print ('Host scanning: ', hostAddress, ' IP address: ', ipAddress)

    portNum1 = int(input('Start port >> '))
    portNum2 = int(input('End port >> '))

    ports = range(int(portNum1), int(portNum2))
    scanlist = [(hostAddress, port) for port in ports]

    pool = Pool(multiprocessing.cpu_count()*2)

    for port, status in pool.imap(scan, scanlist):
        if status:
            print("Port: ", port, " is open.")
    print("Scanning is done ", hostAddress)

    end_time = datetime.datetime.now()
    print(f"Done for {(end_time-start_time).total_seconds()} sec.")