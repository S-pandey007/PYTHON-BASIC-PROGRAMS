import pymongo

clinet= pymongo.MongoClient("mongodb://localhost:27017/")
db=clinet["Qemp"]
collection = db["Qemployee"]

print("Enter Employee Details : ")

emp_id = input("Enter Employee ID :")
name = input("Enter Employee name :")
Designation = input("Enter Employee Designation : ")
mobile = input("Enter Employee mobile : ")
department = input("Enter Department  :")

data = {
    'emp_id':emp_id,
    'name':name,
    'Designation':Designation,
    'mobile':mobile,
    'department':department
}

if(collection.insert_one(data)):
    print("Details Successfully inserted !")
else:
    print("something wrong")
