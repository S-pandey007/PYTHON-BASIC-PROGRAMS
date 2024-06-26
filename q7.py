# if(number<0):
#     print(f"Pleas! enter Valid Age")

number = int(input("Enter your age"))
try:
    if(number<18):
        raise notValide
    else:
        print("You are eligible for Voting")
        exit()
            
except notValide:
        print("Not eligible for Voting")
        
        
        