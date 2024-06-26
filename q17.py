def of():
    f = open("data.txt","r")
    # print(f.readlines())
    data = f.readlines()
    numofline=len(data)
    numofwords = sum(len(data.split()))
    return numofline,numofwords
print(of())