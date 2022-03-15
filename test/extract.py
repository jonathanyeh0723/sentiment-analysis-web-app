import os
import glob

def read_imdb(data_dir="aclImdb"):

    data = {} # dict
    labels = {}

    for data_type in ["train", "test"]:

        data[data_type] = {} # dict
        labels[data_type] = {}

        for sentiment in ['pos', 'neg']:

            data[data_type][sentiment] = [] # list
            labels[data_type][sentiment] = []

            path = os.path.join(data_dir, data_type, sentiment, "*.txt")
            files = glob.glob(path)

            for f in files:
                with open(f) as review:
                    data[data_type][sentiment].append(review.read())
                    labels[data_type][sentiment].append(1 if sentiment == 1 else 0)

    return data, labels
