from bson.objectid import ObjectId
from pymongo import MongoClient

uri = 'mongodb://localhost:27017/apprentice'


def get_data(id):
    client = MongoClient(uri)
    db = client.apprentice

    data = db.data.find_one({'_id': ObjectId(id)}, {"X": 1, "y": 1})

    X = data['X']
    y = data['y']
    return X, y
