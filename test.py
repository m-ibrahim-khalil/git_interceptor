import pymongo
import pickle


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tasks_db"]
mycol = mydb["tasks"]

record = mycol.find_one({})
objects = record['objects']
# print(objects)
commit = pickle.loads(objects["commit"])
print(commit)