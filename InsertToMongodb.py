import json
from pymongo import MongoClient
from datetime import datetime

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

def main():
    client = MongoClient("mongodb+srv://ronsong:0809@cluster0.abzec.mongodb.net/")
    db = client["leetcode"]

    Insert(db, "algorithms", 'db/allQuestions.json')
    Insert(db, "companies", 'db/allCompanies.json')
    Insert(db, "topics", 'db/allTopics.json')
    InsertOne(db, "version", {"last_updated": datetime.utcnow()})

if __name__ == "__main__":
    main()
