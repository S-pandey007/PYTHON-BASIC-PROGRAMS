# import threading
# import math
# import time

# def squre(number):
#     print(f"squre of {number}:{number**2}")
    
# def fact(number):
#     print(f"Factorial of {number}:{math.factorial(number)}")
    
# number=5    
# start_time=time.time()
# thread1 = threading.Thread(target=squre,args=(number,))
# thread2 = threading.Thread(target=fact,args=(number,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# end_time=time.time()

# total_time= end_time-start_time
# print("Totall time of running these program : ",total_time)

a=lambda x,y,z:x+y+z
print(a(1,2,3))