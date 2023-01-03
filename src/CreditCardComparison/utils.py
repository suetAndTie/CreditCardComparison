from datetime import datetime


def listify(x):
    return x if isinstance(x, (list, tuple)) else [x]


def string_to_datetime(string):
    return datetime.strptime(string, '%m/%d/%Y')
