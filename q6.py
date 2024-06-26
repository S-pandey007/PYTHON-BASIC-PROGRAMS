#  Write a python program using mongoDB database to create a “student”
# collection having fields: Student-ID, Name, Course, Mobile, Address. (a
# dict with keys like area, city, country, pin) Accept input from user to
# insert documents.
# c) Write a MongoDB program to delete selected documents given in

import pymongo

client= pymongo.MongoClient("mongodb://localhost:27017/")
db=client["mydb2"]
collection = db["Student2"]

# print("Enter Student data : ")
# stu_id = input("Enter Student Id :")
# name = input("Enter Student name : ")
# course = input("Enter course : ")
# mobile  = input("Enter moblie number : ")
# Address = {}
# area = input("Enter area : ")
# city = input("Enter city :")
# country = input("Enter country :")
# pin = input("Enter PIN number : ")
# Address["area"]=area
# Address["city"]=city
# Address["country"]=country
# Address["pin"]=pin

# data={
#     'stu_id':stu_id,
#     'name':name,
#     'course':course,
#     'mobile':mobile,
#     'Address':Address,
# }

# if(collection.insert_one(data)):
#     print("Student data successfully stored")
# else:
#     print("Something wrong")

deleteData={'stu_id':'01'}
if(collection.delete_one(deleteData)):
    print("Selected document deleted")
else:
    print("something wrong")