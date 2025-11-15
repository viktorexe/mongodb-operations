import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_mongo_client():
    uri = os.getenv('MONGO_URI')
    if not uri:
        raise ValueError("MONGO_URI not found in .env file")
    return MongoClient(uri)

def get_database(client, db_name):
    return client[db_name]

def get_collection(client, db_name, collection_name):
    return client[db_name][collection_name]
