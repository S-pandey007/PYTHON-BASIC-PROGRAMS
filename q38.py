class deptExcp(Exception):
    pass

class salExcp(Exception):
    pass


def check_emp(dep , sal):
    try:    
        if dep.upper()=='HR' or dep.upper()=='SALES':
            print(f"{dep} is your Department")
        else:
            raise deptExcp
        if sal<=0:
            raise salExcp
        else:
            print(f"{sal} is your salary")
    except deptExcp :
        print("Department information wrong")
        
    except salExcp:
        print("Salary not less than equal to zero")        
    


dep = input("Enter your Department : ")
sal = int(input("Enter your salary : "))
check_emp(dep,sal)