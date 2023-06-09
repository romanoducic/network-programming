
from multiprocessing import Process, Queue
import random
import datetime
from localMachineInfo import print_machine_info

print("Date and time:" , datetime.datetime.now())

def rand_num(queue):
    num = random.random()
    queue.put(num)

if __name__ == '__main__':
    queue = Queue()

    processes = [Process(target=rand_num, args=(queue,)) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for p in processes]

    print(results)