import Queue
import threading
import time
import datetime
from localMachineInfo import print_machine_info

print(datetime.datetime.now())

print_machine_info()

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# Kreiramo nove threadove
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Napuniti red cekanja
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Cekati da se red cekanja isprazni
while not workQueue.empty():
   pass

# Obavijesti niti da je vrijeme za izlazak
exitFlag = 1

# Cekaj dok se sve niti ne izvrse
for t in threads:
   t.join()
print ("Main thread exit")