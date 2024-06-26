import re

lowercase = re.compile(r'[a-z]')
uppercase = re.compile(r'[A-Z]')
integer = re.compile(r'\d')
specialCh = re.compile(r'[$#@*]')

pas = input("Enter password :")

if not (len(pas)>=8) and (len(pas)<=20):
    print("invalide password length must atleast 8")
elif not lowercase.search(pas):
    print("invalide password must contain atleast one lowercase letter")
elif not uppercase.search(pas):
    print("invalide password must contain atleast one uppercase ")
elif not integer.search(pas):
    print("invalide password must contain numeric value")
elif not specialCh.search(pas):
    print("invalid password must contain special corrector")
else:
    print("valid password")