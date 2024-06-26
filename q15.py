import threading
import time

def evenNum():
    for i in range(2,9):
        if(i%2==0):
            print(f"Even number is : {i}")
            time.sleep(1)
            
def oddNum():
    for i in range(1,8):
        if(i%2!=0):
            print(f"Odd number is : {i}")
            time.sleep(1)
    
    
thread1=threading.Thread(target=evenNum)
thread2=threading.Thread(target=oddNum)

thread1.start()
thread2.start()

thread1.join()
thread2.join()