from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import VarianceThreshold


def make_feature_selection(l, argsdict):
    if l == 'variancethreshold':
        return VarianceThreshold(**argsdict)
    elif l == 'selectkbest':
        return SelectKBest(**argsdict)
