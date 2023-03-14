import thread
import time
import datetime
from localMachineInfo import print_machine_info

print(datetime.datetime.now())

print_machine_info()

def print_time( threadName, delay):
   counter = 0
   while counter < 5:
      time.sleep(delay)
      counter += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error message: thread is unable to start!"

while 1:
   pass