import pymongo
import random

class MongoAlynisits(object):
    def __init__(self, host="localhost", port=27017, database_name="database_alynisits", collection_name="matlab"):
        try:
            self._connection = pymongo.MongoClient(host=host, port=port, username="TGR_GROUP3", password="ZK984B")
        except Exception as error:
            raise Exception(error)

        if not isinstance(host, str):
            raise ValueError("host must be a string")
        if not isinstance(port, int):
            raise ValueError("port must be an integer")
        if not isinstance(database_name, str) or not database_name:
            raise ValueError("database_name must be a non-empty string")
        if not isinstance(collection_name, str) or not collection_name:
            raise ValueError("collection_name must be a non-empty string")

        self._database = self._connection[database_name] if database_name else None
        self._collection = self._database[collection_name] if collection_name else None
    
    def insert(self, post):
        post_id = self._collection.insert_one(post).inserted_id
        return post_id

mongo_alynisits = MongoAlynisits()

data_list = list()
for data_fake in range(1,6):
    data_list.append({
        'Day': data_fake,
        'H': round(random.uniform(108, 119), 2),
        'Q': round(random.uniform(108, 119), 2)}
    )

for collection in data_list:
    print('[!] Inserting - ', collection)
    mongo_alynisits.insert(collection)