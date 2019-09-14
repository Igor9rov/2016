from sklearn import svm

X = [{1: 2, 2: 3}, {4: 5, 5: -1}]
y = [1, 2]

lin_svc = svm.LinearSVC(C=1).fit(X, y)