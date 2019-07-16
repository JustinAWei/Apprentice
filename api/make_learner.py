from sklearn import svm
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB


def make_learner(l, argsdict):
    if l == 'svm':
        return svm.SVC(**argsdict)
    elif l == 'gnb':
        return GaussianNB(**argsdict)
    elif l == 'mnb':
        return MultinomialNB(**argsdict)
    elif l == 'tree':
        return tree.DecisionTreeClassifier(**argsdict)
    elif l == 'gtree':
        return GradientBoostingClassifier(**argsdict)
