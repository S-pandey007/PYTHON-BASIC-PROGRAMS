# f=open("employee.txt",'w')
# f.write("Employee name : Shubham pandey\n")
# f.write("Employee address : pune")
# f.close()

# myset ={"a","b","c","e"}
# print(myset)
# myset.add("r")
# # myset[0]="m"
# print(myset)


import threading

# Shared counter variable
counter = 0

# Create a lock
lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    # Acquire the lock before accessing the shared resource
    lock.acquire()
    try:
        # Increment the counter
        counter += 1
    finally:
        # Release the lock after accessing the shared resource
        lock.release()

# Create two threads to increment the counter
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final counter value:", counter)
