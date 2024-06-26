# Function to check if a number is a Niven number
def is_niven(number):
    # Calculate the sum of the digits of the number
    sum_of_digits = sum(int(digit) for digit in str(number))
    
    # Check if the number is divisible by the sum of its digits
    return number % sum_of_digits == 0

# Prompt the user for a number
number = int(input("Enter a number: "))

# Ask for a choice
choice = input("Enter 'A' to check if it's a Niven number: ")

# Check if the choice is 'A'
if choice.upper() == 'A':
    # Determine if the number is a Niven number
    if is_niven(number):
        print(f"{number} is a Niven number.")
    else:
        print(f"{number} is not a Niven number.")
else:
    print("Invalid choice. Please enter 'A' to check for a Niven number.")
email_pattern = r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$"