import pymorphy2
import pymorphy2_dicts
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
from sklearn import preprocessing

morph = pymorphy2.MorphAnalyzer()


def Jsonwriting(text):
    infile = open(text, 'r', encoding='utf-8')
    data = json.load(infile)
    infile.close()
    Traintext = []
    TestText = []
    stopwords = nltk.corpus.stopwords.words('russian')
    for i in range(0, len(data)):
        text = data[i]['text']
        text = re.sub(r'[^\w\s]', '', text)
        text = text.replace('\r', ' ')
        text = nltk.word_tokenize(text)
        text = [w for w in text if w.lower() not in stopwords]
        for j in range(len(text)):
            text[j] = morph.parse(text[j])[0].normal_form
        if i < 0.8 * len(data):
            Traintext.append(text)
        else:
            TestText.append(text)
    return Traintext, TestText


def writetothepickle(test, data):
    output = open(test, 'wb')
    pickle.dump(data, output, 2)
    output.close()


def readfrompickle(test):
    input = open(test, 'rb')
    data = pickle.load(input)
    input.close()
    return data


def buildimportantwords(text):
    PreAllwords = []
    Allwords = []
    for i in text:
        for j in i:
            Acces = j in PreAllwords
            if Acces == False:
                PreAllwords.append(j)
            else:
                Check = j in Allwords
                if Check == False:
                    Allwords.append(j)
    return Allwords

#http://nlpx.net/archives/57
def compute_tfidf(corpus):
    def compute_tf(text):
        tf_text = collections.Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/len(text)
        return tf_text
    i = 0
    def compute_idf(word, corpus):
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            Acces = word in Allwords
            if Acces == True:
                tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
        i = i + 1
        print(i)
    return documents_list


def buildsparsematrix(dictionary):
    k = 0
    indices = []
    data = []
    ind_ptr = []
    n_rows = len(dictionary)
    n_cols = len(Allwords)
    for i in dictionary:
        n = 0
        ind_ptr.append(k)
        for j in Allwords:
            Acces = j in i
            n = n + 1
            if Acces == True:
                indices.append(n)
                data.append(i[j])
                k = k + 1
    ind_ptr.append(k)
    Matrix = scipy.sparse.csr_matrix((data, indices, ind_ptr), shape=(n_rows, n_cols), dtype=np.float64)
    return Matrix
'''
Habr, TestHabr = Jsonwriting('habrahabr.json')
Geek, TestGeek = Jsonwriting('geektimes.json')

writetothepickle('TrainHabr.pkl', Habr)
writetothepickle('TrainGeek.pkl', Geek)
writetothepickle('TestHabr.pkl', TestHabr)
writetothepickle('TestGeek.pkl', TestGeek)
'''
TrainHabr = readfrompickle('TrainHabr.pkl')
TrainGeek = readfrompickle('TrainGeek.pkl')
TestHabr = readfrompickle('TestHabr.pkl')
TestGeek = readfrompickle('TestGeek.pkl')

AllTrainText = TrainHabr + TrainGeek
AllTestText = TestHabr + TestGeek
#Allwords = buildimportantwords(AllTrainText)
#writetothepickle('AllWords.pkl', Allwords)
Allwords = readfrompickle('AllWords.pkl')

#TFIDFTrainTextDictionary = compute_tfidf(AllTrainText)
#TFIDFTestTextDictionary = compute_tfidf(AllTestText)
#writetothepickle('TFIDFTrainTextDictionary.pkl', TFIDFTrainTextDictionary)
#writetothepickle('TFIDFTestTextDictionary.pkl', TFIDFTestTextDictionary)

TFIDFTrainTextDictionary = readfrompickle('TFIDFTrainTextDictionary.pkl')
TFIDFTestTextDictionary = readfrompickle('TFIDFTestTextDictionary.pkl')


TrainAccesory = [1 for i in range(len(TrainHabr))] + [2 for i in range(len(TrainGeek))]
TestAccesory = [1 for i in range(len(TestHabr))] + [2 for i in range(len(TestGeek))]

#SparseTrainMatrix = buildsparsematrix(TFIDFTrainTextDictionary)
#SparseTestMatrix = buildsparsematrix(TFIDFTestTextDictionary)

#writetothepickle('SparseTrainMatrix.pkl',SparseTrainMatrix)
#writetothepickle('SparseTestMatrix.pkl',SparseTestMatrix)

SparseTrainMatrix = readfrompickle('SparseTrainMatrix.pkl')
SparseTestMatrix = readfrompickle('SparseTestMatrix.pkl')

normalized_SparseTrainMatrix = preprocessing.normalize(SparseTrainMatrix)
normalized_SparseTestMatrix = preprocessing.normalize(SparseTestMatrix)

svc = svm.SVC(kernel='linear', degree = 1, gamma = 1e-7, C = 3).fit(normalized_SparseTrainMatrix, TrainAccesory)
Predict = svc.predict(normalized_SparseTestMatrix)
a = svc.score(normalized_SparseTestMatrix, TestAccesory)
print(a)
