import threading
import time
import datetime
from localMachineInfo import print_machine_info

print(datetime.datetime.now())

print_machine_info()

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting thread:" + self.name)
      # Synchronization lock
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Synchronization relesa - unlock
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()

# Append thread into treads
threads.append(thread1)
threads.append(thread2)

# Wait until all threads are done
for t in threads:
    t.join()
print ("Main thread exit")