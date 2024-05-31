from pymongo import MongoClient

client = MongoClient('mongodb://3.73.128.252:27017/')

print(client.list_database_names())