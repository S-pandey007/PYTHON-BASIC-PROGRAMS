def store(collegeName,contaact,address):    
    fs = open('college.txt','w')
    fs.write(f"college_name:{collegeName}\n")
    fs.write(f"contact:{contaact}\n")
    fs.write(f"address:{address}")
    fs.close()
    
def display():
    fs = open('college.txt','r')
    data = fs.read()
    fs.close()
    return data


store('SIMCA','9874563211','narhe pune')
print(display())




