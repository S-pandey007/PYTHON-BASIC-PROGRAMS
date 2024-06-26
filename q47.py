import threading

def fun(thname , num):
    lock.acquire()
    # with lock:
    for i in range(1,11):
        print(f"{thname}=> {num}*{i} : {num*i}")
        
    lock.release()
        
lock = threading.Lock()
th1 =threading.Thread(target=fun,args=("threade1",5, ))
th2 =threading.Thread(target=fun,args=("threade2" , 2 , ))

th1.start()
th2.start()

th1.join()
th2.join()