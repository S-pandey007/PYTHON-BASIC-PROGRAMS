def fun(Cstring,num):
    result=[]
    data = Cstring.split()
    for datas in data:
        if len(datas)<num:
            result.append(datas)
    return result

    
    
    
a = int(input("Enter number : "))
b = "Python Programming language has lot of applications in data analytics"
print(fun(b,a))