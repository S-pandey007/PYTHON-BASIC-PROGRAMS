
def Divide(num1,num2):
    try:
        if num2==0:
            pass
    except ZeroDivisionError:
        print("Divide by zero error")
    else:
        print(f"{num1/num2}")
        
Divide(90,90)
        