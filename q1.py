# def leep_year(year):
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         print(f"{year} is leep year")
#     else:
#         print(f"{year} is not leep year")
        
# try:
#     year =int(input("Enter year for check leep year or not : "))
#     if year<0:
#         raise ValueError("Not Valid number")
#     else:
#         leep_year(year)
        
# except ValueError as e:
#     print(e)









# def fact(num):
#     if num==1:
#         return 1
#     else:
#         return num*fact(num-1)

# print(fact(4))












# def sumNatural(num):
#     if num==0:
#         return 0
#     else:
#         return num+sumNatural(num-1)

# print(sumNatural(5))





# Open the file for reading
with open("data.txt", "r") as file:
    # Read all lines and store them in a list
    lines = file.readlines()

# Open the file for writing (truncate the file)
with open("data.txt", "w") as file:
    # Iterate through each line
    for line in lines:
        # Split the line into words, reverse each word, and join them back
        reversed_line = ' '.join(word[::-1] for word in line.split())
        # Write the reversed line back to the file
        file.write(reversed_line + '\n')
