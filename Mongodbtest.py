import pymongo
client = pymongo.MongoClient("mongodb+srv://ketan:ketan123@cluster0.ej0xeh7.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name": "ketan",
    "Email": "ketan.singh@gmail.com",
    "surname": "Chauhan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )