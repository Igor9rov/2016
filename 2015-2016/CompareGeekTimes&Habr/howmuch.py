# import pymorphy2
# import pymorphy2_dicts
import json
import codecs
import numpy as np
import nltk
import re
import pickle
import collections
import math
from scipy.sparse import csr_matrix
from sklearn import svm
import scipy
'''
morph = pymorphy2.MorphAnalyzer()
def Jsonwriting(text):
    infile = open(text, 'r', encoding='utf-8')
    data = json.load(infile)
    infile.close()
    Habr = []
    TestHabr = []
    stopwords = nltk.corpus.stopwords.words('russian')
    for i in range(0,997):
        text = data[i]['text']
        text = re.sub(r'[^\w\s]', '', text)
        text = text.replace('\r', ' ')
        text = nltk.word_tokenize(text)
        text = [w for w in text if w.lower() not in stopwords]
        for j in range(len(text)):
            text[j] = morph.parse(text[j])[0].normal_form
        if i< 800:
            Habr.append(text)
        else:
            TestHabr.append(text)
    return Habr, TestHabr
Habr, TestHabr = Jsonwriting('habrahabr.json')
'''
infile = open('habrahabr.json', 'r', encoding='utf-8')
data = json.load(infile)
print(len(data))
infile.close()