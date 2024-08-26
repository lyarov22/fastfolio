import os
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(os.getenv('MONGO_URL'))
db = client['portfolio']
collection = db['sites']

site = collection.find_one({"_id": ObjectId("66c5992b8de7ddcf000f8a32")})
print(site)
