try:
    import threading
    import time
    def sum(num1,num2):
        print(f"Sum of given number : {num1+num2}")
        time.sleep(1)
    def multi(num1,num2):
        print(f"multiply of given number : {num1*num2}")
        time.sleep(1)
    def sub(num1,num2):
        print(f"Subtraction of given number : {num1-num2}")
        time.sleep(1)
    def divde(num1,num2):
        try:
            if num2==0:
                raise ZeroDivisionError("can't divide")
            else:
                print(f"divide of given number : {num1/num2}")
                time.sleep(1)
        except ZeroDivisionError as e:
            print(e)
        
        
    
    a=1
    try:
        num1 = int(input("Enter First number : "))
        num2 = int(input("Enter second number : "))
    except ValueError as e:
        print(e)
    try:
        if type(num1)==type(a) and type(num2)==type(a):
            pass
        else:
            raise TypeError("Please Enter integer value")
    except TypeError as e:
        print(e)
        
    
    t1=threading.Thread(target=sum,args=(num1,num2))
    t2=threading.Thread(target=multi,args=(num1,num2))
    t3=threading.Thread(target=sub,args=(num1,num2))
    t4=threading.Thread(target=divde,args=(num1,num2))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
 
except ImportError as e:
    print(e)