import os, pickle

SRC_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SRC_DIR, '..', 'data')
IMG_DIR = os.path.join(DATA_DIR,'DeepFashion', 'img')
ANNOT_DIR = os.path.join(DATA_DIR, 'DeepFashion', 'annotations')
LINK_DIR = os.path.join(DATA_DIR, 'link')
DATASET_DIR = os.path.join(DATA_DIR, 'dataset')
MODEL_DIR = os.path.join(SRC_DIR, '..', 'model')
ACTIVATIONS_DIR = os.path.join(DATA_DIR, 'activations')


def load_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def save_pickle(a, filename):
    with open(filename, 'wb') as f:
        pickle.dump(a, f)
        
def make_autopct(values, threshold):
    def my_autopct(pct):
        total = sum(values)
        if pct > threshold:
            return '{:.2f}%-{:,}'.format(pct, int((pct * total)/100))
    return my_autopct

def make_labels(values, all_labels, threshold):
    total = sum(values)
    labels = []
    for i, val in enumerate(values):
        l = all_labels[i] if val/total > threshold/100 else ''
        labels.append(l)
    return labels