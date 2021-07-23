import json
from pymongo import MongoClient
from datetime import datetime
import os
from utils.runtime import runtime

def Insert(db, _collection, _file):
    collection = db[_collection]

    with open(_file) as file:
        file_data = json.load(file)

    collection.delete_many({})

    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)

def InsertOne(db, _collection, _data):
    collection = db[_collection]
    collection.delete_many({})
    collection.insert_one(_data)

@runtime
def run():
    client = MongoClient(os.environ.get("MONGODB_CLIENT"))
    db = client[os.environ.get("MONGODB_DB")]

    Insert(db, "algorithms", 'db/allQuestions.json')
    Insert(db, "companies", 'db/allCompanies.json')
    Insert(db, "topics", 'db/allTopics.json')
    InsertOne(db, "version", {"last_updated": datetime.utcnow()})

def main():
    run()

if __name__ == "__main__":
    main()
