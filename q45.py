a = int(input("enter number"))
b=a
rev=0
while(a>0):
    rem = a%10
    rev=rev*10+rem
    a=int(a/10)
    
if(rev==b):
    print("number is palindrome")
else:
    print("number is not palindrome")