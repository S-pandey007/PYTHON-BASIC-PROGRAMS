import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Qemp"]
collection = db["Chess_Competition"]

# data = [
#     {'player_id':'01','player_name':'shubham pandey','player_age':22,'player_phone':9770337151},
#     {'player_id':'02','player_name':'rajkumar','player_age':23,'player_phone':1236547896},
#     {'player_id':'03','player_name':'dipak','player_age':24,'player_phone':3216549874}
# ]

# if(collection.insert_many(data)):
#     print("Data inserted !")
# else:
#     print("something wrong")

print(collection.find_one({"player_id":"01"}))
print(collection.find_one({"player_id":"02"}))
print(collection.find_one({"player_id":"03"}))
