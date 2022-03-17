from sklearn.utils import shuffle


def prepare_imdb_data(data, labels):
    """Prepare train and test sets."""

    # Combine data
    train_data = data['train']['pos'] + data['train']['neg']
    test_data = data['test']['pos'] + data['test']['neg']

    train_labels = labels['train']['pos'] + labels['train']['neg']
    test_labels = labels['test']['pos'] + labels['test']['neg']

    # Shuffle reviews and corresponding labels
    train_data, train_labels = shuffle(train_data, train_labels)
    test_data, test_labels = shuffle(test_data, test_labels)

    return train_data, test_data, train_labels, test_labels
