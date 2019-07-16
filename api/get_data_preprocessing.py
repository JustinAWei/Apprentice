from make_preprocessing import make_preprocessing
from sklearn.pipeline import Pipeline

def get_data_preprocessing(*args):
    print(args)
    pipe_items = []
    for preprocessing_fn in args:
        preprocessing_name = preprocessing_fn[0]
        pipe_items.append((preprocessing_name, make_preprocessing(*preprocessing_fn)))
    print(pipe_items)
    return Pipeline(pipe_items)
