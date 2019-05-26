import pymongo
import json

class MongoDB:
    def __init__(self, uri):
        self._client = pymongo.MongoClient(uri)
        self._db = self._client["hack-roles"] 
    
    def __getitem__ (self, c_name):
        return self._db[c_name]

    


class DBProxy: 
    def __init__(self, json_file):
        self._json_file = json_file
        self._data = json.load(open(json_file))

    def items(self):
        return self._data

    def create(self, data):
        self._data.append(data)
        with open(self._json_file, "w") as file:
            json.dump(self._data, file)
            
    def update(self, query, change):
        pass
    
    def delete(self, query):
        pass