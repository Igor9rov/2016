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

morph = pymorphy2.MorphAnalyzer()

def Habrahabrwriting():
    infile = open('habrahabr.json', 'r', encoding='utf-8')
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

def GeekTimeswriting():
    infile = open('geektimes.json', 'r', encoding='utf-8')
    data = json.load(infile)
    infile.close()
    Geek = []
    TestGeek = []
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
            Geek.append(text)
        else:
            TestGeek.append(text)
    return Geek, TestGeek

def writetothepickle(test, data):
    output = open(test, 'wb')
    pickle.dump(data, output, 2)
    output.close()

def readfrompickle(test):
    input = open(test, 'rb')
    data = pickle.load(input)
    input.close()
    return data
'''
Habr, TestHabr = Habrahabrwriting()
Geek, TestGeek = GeekTimeswriting()

writetothepickle('Habrtrain.pkl', Habr)
writetothepickle('Geektimetrain.pkl', Geek)
writetothepickle('Habrtest.pkl', TestHabr)
writetothepickle('Geektest.pkl', TestGeek)
'''
Habr = readfrompickle('Habrtrain.pkl')
Geek = readfrompickle('Geektimetrain.pkl')
TestHabr = readfrompickle('Habrtest.pkl')
TestGeek = readfrompickle('Geektest.pkl')

def compute_tfidf(corpus):
    def compute_tf(text):
        tf_text = collections.Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/float(len(text))
        return tf_text

    def compute_idf(word, corpus):
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
    return documents_list

#writetothepickle('TestHabrTFIDF.pkl', compute_tfidf(TestHabr))
#writetothepickle('HabrTFIDF.pkl', compute_tfidf(Habr))
#writetothepickle('TestGeekTFIDF.pkl', compute_tfidf(TestGeek))
#writetothepickle('GeekTFIDF.pkl', compute_tfidf(Geek))

Habr = readfrompickle('HabrTFIDF.pkl')
Geek = readfrompickle('GeekTFIDF.pkl')
TestHabr = readfrompickle('TestHabrTFIDF.pkl')
TestGeek = readfrompickle('TestGeekTFIDF.pkl')

TFIDFDictionary = Habr + Geek
TFIDFTestDictionary = TestHabr + TestGeek
AllDictionary = Habr + TestHabr + Geek + TestGeek
TrainAccesory = [1 for i in range(len(Habr))] + [2 for i in range(len(Geek))]
TestAccesory = [1 for i in range(len(TestHabr))] + [2 for i in range(len(TestGeek))]
'''
Allwords = []
for i in AllDictionary:
    for j in i:
        Acces = j in Allwords
        if Acces == False:
            Allwords.append(j)
writetothepickle('Allwords.pkl', Allwords)
'''
Allwords = readfrompickle('Allwords.pkl')
print(len(Allwords))
'''
k = 0
Usualmatrix = []
for i in TFIDFDictionary:
    for j in Allwords:
        Acces = j in i
        if Acces == False:
            Usualmatrix.append(0)
        else:
            Usualmatrix.append(i[j])
    k = k + 1
    print(k)

NpUsualMatrix = np.array(Usualmatrix)
NpUsualMatrix = NpUsualMatrix.reshape(1600, len(Allwords))
writetothepickle('NpUsualMatrix.pkl', NpUsualMatrix)

NpUsualMatrix = readfrompickle('NpUsualMatrix.pkl')
SparseM = csr_matrix(NpUsualMatrix)
writetothepickle('SparseMatrix.pkl', SparseM)

SparseMatrix = readfrompickle('Sparsematrix.pkl')
svm = svm.SVC(kernel='poly', degree=2, C=1).fit(SparseMatrix, TrainAccesory)
writetothepickle('SVM.pkl', svm)
TestAssesory = [1 for i in range(len(TestHabr))] + [2 for i in range(len(TestGeek))]
'''
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

SparseTestMatrix = buildsparsematrix(TFIDFTestDictionary)
SVM = readfrompickle('SVM.pkl')
HY = SVM.predict(np.c_[SparseTestMatrix])
np.testing.assert_array_almost_equal(HY, TestAccesory)



