import numpy as np
import os
from get_config import get_config
from get_data import get_data
from make_learner import make_learner
import pickle
import time

def fit(config):
    X, y = get_data(config['id'])
    learner = make_learner(config['algorithm'], config['hyperparams'])

    start = time.clock()
    model = learner.fit(X, y)
    fit_time = time.clock() - start

    with open('model_{id}.pickle'.format(id=config['id']), 'wb') as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

    return {
        "time":round(fit_time, 2),
        "rows": np.array(X).shape[0],
        "size": os.path.getsize('model_{id}.pickle'.format(id=config['id']))
    }


# s = pickle.dumps(make_learner(*config['learner']).fit(*get_data(**config['data'])))
