from fit import fit
from predict import predict
from  make_example import make_example_data

from pymongo import MongoClient
import numpy as np

import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from StringIO import StringIO
import csv

uri = 'mongodb://localhost:27017/apprentice'

client = MongoClient(uri)
db = client.apprentice

app = Flask(__name__)

@app.route("/fit", methods=["POST"])
def server_fit():
    config = request.json
    print(config)
    return jsonify(fit(config))

@app.route("/predict", methods=["POST"])
def server_predict():
    config = request.json
    print(config)
    result = predict(config)
    return jsonify({
        "y": result
    })

def load_file(content, id):
    scsv = content
    f = StringIO(scsv)
    reader = csv.reader(f, delimiter=',')

    X = []
    y = []

    for row in reader:
        if(row[0] == "Y"):
            break
        X.append(map(int,row))

    for row in reader:
        y.append(map(int,row))

    print(
        {
            "X": X,
            "y": y
        }
    )
    db.data.update({"_id": id}, {"$set": {"X": X, "y": y}}, upsert = True)

UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        file = request.files['file']

        id = db.data.insert({})
        load_file(file.read(), id)
        return jsonify({
            "id": str(id)
        })
    return '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
  <p><input type=file name=file>
     <input type=submit value=Upload>
</form>
'''

@app.route('/example', methods=['POST'])
def load_example():
    print(request.headers)
    print(request.json['example'])

    X,y = make_example_data(request.json['example'])
    example_data = {
        "X":X.tolist(),
        "y":y.tolist()
    }

    print(example_data)
    id = db.data.insert(example_data)
    return jsonify({
        "id": str(id)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
