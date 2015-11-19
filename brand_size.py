from pymongo.mongo_client import MongoClient
client = MongoClient()
client.drop_database("foxtrot")
db = client.foxtrot


