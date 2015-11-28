from pymongo import MongoClient
client = MongoClient()
db = client.foxtrot

collection = db.foxtrot_collection

from csv_reader import convertDict
category = convertDict("data/category.csv", 'Category ID', 'Category Description')
# Insert document into the collection.
categories = db.categories
category_id = categories.insert_one(category).inserted_id
print category_id
print db.collection_names(include_system_collections=False)
print categories.find_one()
