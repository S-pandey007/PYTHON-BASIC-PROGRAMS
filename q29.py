import threading
def table(num1):
    for i in range(1,11):
        print(f"{num1} x {i} = {num1*i}")
            
        
th1 = threading.Thread(target=table,args=(2,))
th2 = threading.Thread(target=table,args=(5,))

th1.start()
th2.start()

th1.join()
th1.join()