class Bank:
    def  __init__(self,bank_name,branch,city,managerName):
        self.bank_name=bank_name
        self.branch=branch
        self.city=city
        self.managerName=managerName
        
    def ChangeManagerName(self,ChangedManagerName):
        self.managerName=ChangedManagerName
        
    def DisplayInfo(self):
        print(f"Bank Name : {self.bank_name}")
        print(f"Bank Brach : {self.branch}")
        print(f"Bank City : {self.city}")
        print(f"Bank Manager :{self.managerName} ")
        
        
obj = Bank("SBI","Gudhiyari","Raipur","Shubham Pandey")
obj.DisplayInfo()
obj.ChangeManagerName("Virat kohli")
obj.DisplayInfo()