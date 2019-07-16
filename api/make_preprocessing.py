from sklearn.preprocessing import Imputer
from sklearn.preprocessing import Normalizer

def make_preprocessing(l, argsdict):
    if l == 'normalizer':
        return Normalizer(**argsdict)
    elif l == 'imputer':
        return Imputer(**argsdict)
