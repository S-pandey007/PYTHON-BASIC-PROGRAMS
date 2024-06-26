import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client['AirlineRS-DB']
collection = db['“PassengerTB']
# -------------------------------------------------------------------------------------------------------------------
# # insert data
# data=[
#     {'name':'shubham','mobile':'1236547890','source':'pune','destination':'raipur','bill-amt':'2500'},
#     {'name':'manoj ','mobile':'9874563210','source':'mumbai','destination':'banglore','bill-amt':'2500'},
#     {'name':'suresh','mobile':'9632587410','source':'pune','destination':'raipur','bill-amt':'2500'},
#     {'name':'sumit','mobile':'0147852369','source':'delhi','destination':'pune','bill-amt':'2500'},
#     {'name':'Anita','mobile':'3256417895','source':'pune','destination':'raipur','bill-amt':'2500'}
# ]

# if collection.insert_many(data):
#     print("Data inserted successfully")
# else:
#     print("something wrong")

# -------------------------------------------------------------------------------------------------------------------
# # delete data
# del_data={'name':'sumit'}
# if collection.delete_one(del_data):
#     print(f"{del_data} data deleted")
# else:
#     print("something wrong")

# -------------------------------------------------------------------------------------------------------------------

# # update data
# con = {'name':'Anita'}
# new_mobile={'$set':{'mobile':'9770337151'}}
# if collection.update_one(con,new_mobile):
#     print(f"Data updated successfully")
# else:
#     print("something wrong")


# -------------------------------------------------------------------------------------------------------------------
# # find information

# for i in collection.find({'destination':'pune'}):
#     print(i)

# -------------------------------------------------------------------------------------------------------------------

# # sort by name
# sorted_red = collection.find().sort('name',pymongo.ASCENDING)

# for i in sorted_red:
#     print(i)

# -------------------------------------------------------------------------------------------------------------------