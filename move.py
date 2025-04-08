import pandas as pd
import pprint
from pymongo import MongoClient

pp = pprint.PrettyPrinter()
client = MongoClient(host="localhost", port=27017)
print(client.list_database_names())

db = client["air-quality"]
print(pp.pprint(list(db.list_collections())))

collection = db["india"]
pp.pprint(collection.find_one())