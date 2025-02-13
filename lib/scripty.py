import pickle
import random
import sklearn
import numpy as np
from googletrans import Translator
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier as DTC
import sys
import warnings
import asyncio


with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
stop_words = set(stopwords.words("english"))


def create_lexicon(pos, neg):
    lexicon = []
    for file_name in [pos, neg]:
        with open(file_name, 'r') as f:
            contents = f.read()
            for line in contents.split('\n'):
                data = line.strip('\n')
                if data:
                    all_words = word_tokenize(data)
                    lexicon += list(map((lambda x: x.lower()), all_words))
    lexicons = []
    for word in lexicon:
        if not word in stop_words:
            lexicons.append(word)
    word_counts = Counter(lexicons)  # it will return kind of dictionary
    l2 = []
    for word in word_counts:
        if 4000 > word_counts[word]:
            l2.append(word)
    return l2

def check_class(data):
    with open("decisiontree.pkl", "rb") as f:
        clf = pickle.load(f, fix_imports=True)
    prediction = clf.predict(data)
    return np.array(prediction)

line=sys.argv[1]
async def translate(line):
    translator=Translator()
    line=await translator.translate(line,dest='en')
    line = word_tokenize(line.text)

    words = list(set([w.lower() for w in line]))
    lexicons = create_lexicon('pos_english.txt', 'neg_english.txt')
    featureset = np.zeros(len(lexicons))
    for w in lexicons:
        if w in words:
            idx = lexicons.index(w.lower())
            featureset[idx] += 1
    featureset = list(featureset)
    featureset = np.array(featureset)
    y_pred = list(check_class([featureset[:-17]]))
    print(y_pred)

result = asyncio.run(translate(line=line))
sys.stdout.flush()