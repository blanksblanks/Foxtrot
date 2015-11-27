from pymongo import MongoClient
client = MongoClient()
db = client.foxtrot

collection = db.foxtrot_collection

# Insert document into the collection.
from csv_reader import convertDict
category = convertDict("data/category.csv", 'Category ID', 'Category Description')
categories = db.categories
category_id = categories.insert_one(category).inserted_id
print category_id
