import os, pickle
import nbimporter

SRC_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SRC_DIR, '..', 'data')
IMG_DIR = os.path.join(DATA_DIR,'DeepFashion', 'img')
IMG_HRES_DIR = os.path.join(DATA_DIR, 'DeepFashion', 'img-hres')
ANNOT_DIR = os.path.join(DATA_DIR, 'DeepFashion', 'annotations')
LINK_DIR = os.path.join(DATA_DIR, 'link')
DATASET_DIR = os.path.join(DATA_DIR, 'dataset')

INPUT_SHAPE = (299, 299, 3)


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