import csv

from StringIO import StringIO
from fit_model import fit_model
from flask import Flask, request, jsonify
from make_data import make_data
from predict import predict
from pymongo import MongoClient

uri = 'mongodb://localhost:27017/apprentice'

client = MongoClient(uri)
db = client.apprentice

app = Flask(__name__)


@app.route("/fit", methods=["POST"])
def server_fit():
    return jsonify(fit_model(request.json))


@app.route("/predict", methods=["POST"])
def server_predict():
    result = predict(request.json)
    return jsonify({
        "y": result
    })


def load_file(content, id):
    f = StringIO(content)
    reader = csv.reader(f, delimiter=',')

    X = []
    y = []

    for row in reader:
        if row[0] == "Y":
            break
        X.append(map(int, row))

    for row in reader:
        y.append(map(int, row))

    db.data.update({"_id": id}, {"$set": {"X": X, "y": y}}, upsert=True)


UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        id = db.data.insert({})
        load_file(file.read(), id)
        return jsonify({"id": str(id)})
    return ''''
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
    X, y = make_data(request.json['example'])
    example_data = {
        "X": X.tolist(),
        "y": y.tolist()
    }

    id = db.data.insert(example_data)
    return jsonify({
        "id": str(id)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)