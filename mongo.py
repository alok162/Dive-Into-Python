from pymongo import MongoClient
try:
    conn = MongoClient()
    print 'connected successfully'
except:
    print 'could not connect to mongodb'

db = conn.demo_mongo
collection = db.employee
cursor = collection.find()
for i in cursor:
    print i