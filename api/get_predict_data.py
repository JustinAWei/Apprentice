from bson.objectid import ObjectId
from pymongo import MongoClient
uri = 'mongodb://localhost:27017/apprentice'

def get_predict_data(id):
    client = MongoClient(uri)
    db = client.apprentice

    data = db.data.find_one({'predict':id}, {"X": 1, "y": 1})

    X = data['X']

    if 'y' in data.keys():
        y = data['y']
    else:
        y = False
    return (X, y)
