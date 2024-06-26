# def niven(num):
#     temp = num
#     sum=0
#     while temp > 0:
#         digit = temp % 10
#         sum= sum + digit
#         temp = temp / 10
        
#     return num%sum==0

# def neon(num):
#     mul= num*num
#     sum=0
#     while mul >0:
#         digit=mul%10
#         sum=sum+digit
#         mul+=mul/10
#     return sum==num



# ch = input(f"For Niven Enter 'A' and Neon 'B' : ")
# if ch=='A':
#     a=int(input("Enter the number : "))
#     if niven(a):
#         print(f"{a} is a Niven number")
#     else:
#         print(f"{a} is not a Niven number")
# elif ch=='B':
#     a=int(input("Enter the number : "))
#     if neon(a):
#         print(f"{a} is a Neon number")   
#     else:
#         print(f"{a} is a not Neon number")   
           
           
def niven(num):
    temp = num
    digit_sum = 0  # Use more descriptive variable names
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10  # Correct integer division
    
    return num % digit_sum == 0

def neon(num):
    square = num ** 2  # Square the number
    digit_sum = 0
    while square > 0:
        digit = square % 10
        digit_sum += digit
        square //= 10  # Correct integer division
    
    return digit_sum == num

# Asking user for choice
choice = input("For Niven, enter 'A'; for Neon, enter 'B': ")

if choice.upper() == 'A':  # Case-insensitive comparison
    number = int(input("Enter the number: "))
    if niven(number):
        print(f"{number} is a Niven number.")
    else:
        print(f"{number} is not a Niven number.")
elif choice.upper() == 'B':
    number = int(input("Enter the number: "))
    if neon(number):
        print(f"{number} is a Neon number.")   
    else:
        print(f"{number} is not a Neon number.")   
else:
    print("Invalid choice. Please enter 'A' or 'B'.")
