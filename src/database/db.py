from os import getenv
from pymongo import MongoClient

MONGO_URI = getenv('MONGO_URI', 'mongodb://localhost:27017')

DB_NAME = getenv('DB_NAME', 'test_db_traduzo')

client = MongoClient(MONGO_URI)

db = client[DB_NAME]
