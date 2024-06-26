import re
email_pattern = re.compile(r"^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$")
email = input("Enter email for validation : ")
if email_pattern.search(email):
    print(f"{email} : valid email")
else:
    print(f"{email}  : Invalid ! email")



# Regular Expression:
# The pattern ^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$ is used for email validation.
# ^ and $ ensure the pattern matches the entire string.
# [\w\.-]+ matches one or more word characters, periods, or hyphens for the local part.
# @[a-zA-Z\d-]+ ensures the domain starts with @ and contains letters, digits, or hyphens.
# \.[a-zA-Z]{2,}$ checks for a top-level domain with at least two characters.
# Validation Function: The validate_email function checks if the email matches the pattern.
# Testing: A list of test emails is validated to demonstrate the function's behavior with valid and invalid email addresses.