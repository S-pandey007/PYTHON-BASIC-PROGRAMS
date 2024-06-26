def prime(num):
    if num<2:
        return False
    for i in range(2,int(num*0.5)+1):
        if num%i==0:
            return False   
    return True
        
        
fn=int(input("First number"))
sn=int(input("second number"))

for i in range(fn,sn):
    if prime(i):
        print(f" {i} ")



# def is_prime(num):
#     # Numbers less than 2 are not prime
#     if num < 2:
#         return False
    
#     # Check divisibility from 2 to the square root of the number
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False  # If divisible, not a prime
    
#     return True  # No divisors found, so it's a prime

# # Get input for the range
# first_number = int(input("First number: "))
# second_number = int(input("Second number: "))

# # Ensure proper range, inclusive of both ends
# for i in range(first_number, second_number + 1):
#     if is_prime(i):
#         print(f"{i} is a prime number")
