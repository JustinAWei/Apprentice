import ast

import pickle


def predict(json):
    with open('models/model_{id}.pickle'.format(id=json['id']), 'rb') as f:
        model = pickle.load(f)

    X = ast.literal_eval(json['X'])
    print(X)
    y_pred = model.predict(X)

    return (y_pred[0])
