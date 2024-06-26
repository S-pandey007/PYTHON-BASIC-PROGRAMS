fs = open("data.txt","r")
data = fs.read()
countString=data.count("a")
print(countString)