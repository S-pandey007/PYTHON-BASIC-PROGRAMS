# password
import re
lowercase = re.compile(r'[a-z]')
uppercase = re.compile(r'[A-Z]')
numeric = re.compile(r'\d')
special = re.compile(r'[@,#,$,_]')

password = input("Enter password : ")
if (len(password)<8) or (len(password)>20):
    print("Password length mmore then 8 charecter and less then 20 character")
elif not lowercase.search(password):
    print("Please add atleast one lowercase character")
elif not uppercase.search(password):
    print("Please add atleast one uppercase character")
elif not numeric.search(password):
    print("Please use atleast on numeric value")
elif not special.search(password):
    print("Please use some special character ")
else:
    print("Password in valide for use")