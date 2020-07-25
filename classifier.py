from textblob.classifiers import NaiveBayesClassifier

import pickle

pkldump = open("listdump.pkl", "rb")
phraselist = pickle.load(pkldump)
pkldump.close()

train = []

for phrase in phraselist:
    train.append([phrase])

