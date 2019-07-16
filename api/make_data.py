from sklearn.datasets import load_boston
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import load_iris


def make_data(l):
    if l == 'boston':
        return load_boston(return_X_y=True)
    elif l == 'iris':
        return load_iris(return_X_y=True)
    elif l == 'diabetes':
        return load_diabetes(return_X_y=True)
    elif l == 'digits':
        return load_digits(return_X_y=True)
