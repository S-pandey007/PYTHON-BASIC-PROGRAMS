import threading
import time

start_time=time.time()
def squre():
    for i in range(1,6):
        print(f"Squre of given number : {i*i}")
        time.sleep(1)
    
def cube():
    for i in range(1,6):
        print(f"Cube of given number :{i*i*i}")
        time.sleep(1)
    
thread1 = threading.Thread(target=squre)
thread2 = threading.Thread(target=cube)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
ending_time=time.time()
print(f"Total time is {ending_time-start_time}")