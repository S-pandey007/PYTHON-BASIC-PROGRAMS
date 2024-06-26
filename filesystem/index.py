
f = open('numbers.txt','r')
while(True):
    data = f.readline()
    if int(data)%2==0:
        f=open('even.txt','w')
        f.write(str(data))
        
    else:
        nd=str(data)
        f=open('odd.txt','w')
        f.write(str(data))
    f.close()