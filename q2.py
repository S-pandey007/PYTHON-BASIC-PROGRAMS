# Write a python program using MongoDB database to create a “Books”
# collection having fields: title, Author (a list), Publisher, PubAddress, (a
# dict with keys like area, city, country), Price, ISBN. Accept input from
# user to insert documents


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client["mydb"]
collection=db["books"]

# print("Enter book detalis one by one:")
# title=input("Enter book title : ")
# author=input("Enter authors name :  ").split(",")
# publisher = input("Enter publisher : ")
# pubAddress={}
# area=input("Enter area : ")
# city=input("Enter city : ")
# country=input("Enter country : ")
# pubAddress["area"]=area
# pubAddress["city"]=city
# pubAddress["country"]=country
# price=input("Enter price : ")
# isbn=input("Enter ISBN : ")

# data = {
#     "title":title,
#     "author":author,
#     "publisher":publisher,
#     "pubAddress":pubAddress,
#     "price":price,
#     "isbn":isbn
# }

# if(collection.insert_one(data)):
#     print("Book Details Successfully uploades in database")
# else:
#     print("something wrong") 

pre_price={'price':"1000"}
curr_price={"$set":{'price':"2000"}}
if(collection.update_one(pre_price,curr_price)):
    print("Successfully Updated")
else:
    print("Something wrong")