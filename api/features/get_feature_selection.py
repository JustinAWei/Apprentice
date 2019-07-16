from make_feature_selection import make_feature_selection
from sklearn.pipeline import Pipeline


def get_feature_selection(*args):
    print(args)
    pipe_items = []
    for feature_selection_fn in args:
        feature_selection_name = feature_selection_fn[0]
        pipe_items.append((feature_selection_name, make_feature_selection(*feature_selection_fn)))
    print(pipe_items)
    return Pipeline(pipe_items)
