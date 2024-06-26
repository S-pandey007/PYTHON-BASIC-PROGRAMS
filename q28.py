# i=1
# while(i<5):
#     if(i==3):
#         print("Breaking Loop")
#         break
#     print(i)
#     i=i+1



for i in range(1,10):
    if(i%2==0):
        continue
    print(i)
    i=i+1