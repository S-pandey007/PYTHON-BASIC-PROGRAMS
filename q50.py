import emp 

baseSalary = int(input("Enter Base salary : "))
incre = int(input("Enter increment in salary : "))
deduction = int(input("Enter Deduction [TAX , STATE , LOCAL TAX , OTHER] : "))
grossSalary = emp.gross(baseSalary,incre)
print(f"Gross Salary of employe : {grossSalary}")
print(f"Net Salary of employe : {emp.net(grossSalary,deduction)}")
