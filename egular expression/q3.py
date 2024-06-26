# # Emial validation 
# import re
# # pattern = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,7}$')
# pattern = re.compile(r'^[0-9]{10}$')
# email = input("Enter your email : ")

# if pattern.search(email):
#     print("Valid Email")
# else:
#     print("Invalide email ! Try again")


def fibonacci(n):
    # Initialize first two terms of the sequence
    a, b = 0, 1
    # Initialize an empty list to store the Fibonacci sequence
    fibonacci_sequence = []

    # Generate Fibonacci sequence up to the nth term
    for _ in range(n):
        fibonacci_sequence.append(a)
        temp = a
        a = b
        b = temp + b

    return fibonacci_sequence

# Number of terms in the Fibonacci sequence
n = int(input("Enter the number of terms: "))

# Print Fibonacci sequence up to the first 'n' terms
print("Fibonacci Sequence up to the first", n, "terms:")
print(fibonacci(n))
