import json

from pymongo import MongoClient

from config import *

client = MongoClient(MONGODB_HOST, MONGODB_PORT)

db = client[MONGODB_DB_NAME]
collection = db[MONGODB_COLLECTION]


def save_user_data_by_id(user_id, data={}):
    data['id'] = user_id

    entry_id = collection.insert_one(data).inserted_id

    return entry_id


def get_user_data_by_id(user_id):
    doc = collection.find_one({"id": user_id})

    sanitized_doc = json.dumps(doc, default=str)

    return sanitized_doc
