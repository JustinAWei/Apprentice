from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, accuracy_score
import ast

from get_config import get_config
from get_predict_data import get_predict_data
from make_learner import make_learner
import pickle


def predict(json):
    with open('model_{id}.pickle'.format(id=json['id']), 'rb') as f:
        model = pickle.load(f)

    X = ast.literal_eval(json['X'])
    print(X)
    y_pred = model.predict(X)

    return (y_pred[0])
