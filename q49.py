f=open("Ndata.txt" ,'a')
f.write("Programming")
f.close()
f=open("Ndata.txt",'r')
data=f.read()
# for i in data:
#     print(i,end="")
print(data)
