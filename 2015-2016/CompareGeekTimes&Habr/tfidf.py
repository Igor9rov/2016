from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
data_train = ['gju so i am confused to leave', 'I want to leave', 'kek']
X_train = vectorizer.fit_transform(data_train)
print(X_train.toarray())

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
data_train = ['зареду за дом', 'дом кеково зареду', 'kek']
X_train = vectorizer.fit_transform(data_train)
print(X_train.toarray())