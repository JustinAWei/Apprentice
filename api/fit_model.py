import os
import pickle
import time

import numpy as np
from get_data import get_data
from make_learner import make_learner


def fit_model(config):
    X, y = get_data(config['id'])
    learner = make_learner(config['algorithm'], config['hyperparams'])

    start = time.clock()
    model = learner.fit(X, y)
    fit_time = time.clock() - start

    if not os.path.exists('models'):
        os.makedirs('models')

    with open('models/model_{id}.pickle'.format(id=config['id']), 'wb') as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

    return {
        "time": round(fit_time, 2),
        "rows": np.array(X).shape[0],
        "size": os.path.getsize('models/model_{id}.pickle'.format(id=config['id']))/1000
    }
