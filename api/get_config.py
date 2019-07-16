def get_config():
    return {
        'data': {
                    'id': '59bc3043734d1d5739a8f43e',
                    'uri':'mongodb://localhost:27017/apprentice',
                    'predict': True
                },

        'learner':['svm', {}],
        #'preprocessing':[['normalizer', {}],['imputer', {'verbose':10}]],
        #'feature_selection':[['variancethreshold', {}]],
    }
