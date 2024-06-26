import _thread
import time

def fun(thname , num):
    for i in range(1,11):
        print(f"{thname}=> {num}*{i} : {num*i}")
        time.sleep(1)
_thread.start_new_thread(fun,("thread1",5, ))
_thread.start_new_thread(fun,("thread2",2, ))


while True:
    pass