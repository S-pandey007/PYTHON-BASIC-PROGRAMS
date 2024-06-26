Ustring = input("Enter String : ")
subString = input("Enter Sub String for search : ")
data=[]
data=Ustring.split()
co = data.count(subString)
print(f"Number of occurance : {co}")
a=0
for i in data:
    
    if i==subString:
        print(f"Given sub String position {a}")
    a+=1