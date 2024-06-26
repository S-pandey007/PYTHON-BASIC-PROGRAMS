def gross(base,incre):
    grossSalary = base+(base*incre)/100
    return grossSalary

def net(grossSa , deductionAmt):
    netSalary = grossSa - deductionAmt
    return netSalary