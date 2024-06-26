import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Qemp']
collection = db['student']



# data=[
#     {'roll_no':10,'name':'raj','address':'pune','phone':'9874563212','subject':'java'},
#     {'roll_no':11,'name':'raju','address':'mumbai','phone':'9874563212','subject':'python'},
#     {'roll_no':12,'name':'ramesh','address':'ranchi','phone':'9874563212','subject':'html'},
#     {'roll_no':13,'name':'kamlesh','address':'raipur','phone':'9874563212','subject':'python'},
#     {'roll_no':14,'name':'rajkumar','address':'delhi','phone':'9874563212','subject':'c++'},
#     {'roll_no':15,'name':'rameshwar','address':'pune','phone':'9874563212','subject':'java'}
# ]

# if(collection.insert_many(data)):
#     print("data inserted successfully")
# else:
#     print("something error")


# #print student who read python 
# data = collection.find({'subject':'python'})
# for i in data:
#     print(i)

# #student roll number 15 are deleted
# if(collection.delete_one({'roll_no':15})):
#     print("student (Roll number : 15) data are deleted successfully")
# else:
#     print("something wrong")


# # update roll no 10 phone number
# data = {'roll_no':10}
# new_data={'$set':{'phone':'9770337151'}}
# collection.update_one(data,new_data)

