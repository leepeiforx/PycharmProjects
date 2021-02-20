from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
from common.load_poly import plot_learning_curve
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt
import time

# %%

caner = load_breast_cancer()
X = caner.data
y = caner.target

print('data shape:{0}; no.positive:{1}; no.negetive:{2}'
      .format(X.shape, y[y == 1].shape[0], y[y == 0].shape[0]))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1)
clf = SVC(C=1.0, kernel='rbf', gamma=.1)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score:{}; test score:{}'.format(train_score, test_score))

gammas = np.linspace(0, 0.0003, 30)
param_grid = {'gamma': gammas}
clf_cv = GridSearchCV(SVC(), param_grid=param_grid, cv=5)
clf_cv.fit(X_train, y_train)
cv = ShuffleSplit(n_splits=10, test_size=.2, random_state=0)
title = 'learning curve for Gaussian Kernal{}'
print('best param:{0} \nbest score:{1}'.format(clf_cv.best_score_, clf_cv.best_params_))

plt.figure(figsize=(16, 12), dpi=144)
plot_learning_curve(estimator=clf_cv, X=X, y=y, ylim=(0.5, 1.01), cv=cv,
                    title=title.format(clf_cv.best_params_))

plt.figure(figsize=(16, 12), dpi=144)
plot_learning_curve(estimator=clf, X=X, y=y, ylim=(0.5, 1.01), cv=cv,
                    title='learning curve for Gaussian Kernal with $\gamma=0.1$')

plt.show()

# %%
# 以上模型过拟合,使用二阶多项式核函数来拟合模型

clf = SVC(kernel='poly', degree=2)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score:{0}; test score:{1}'.format(train_score, test_score))

# %%
degrees = [1, 2]
cv = ShuffleSplit(n_splits=5, test_size=.2, random_state=1)
title = 'Learning Curve with degree:{0}'

start = time.perf_counter()

plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(SVC(kernel='poly', degree=degrees[i], C=1.0), X=X, y=y,
                        title=title.format(degrees[i]), ylim=(0.8, 1.01), cv=cv, n_jobs=4)

print('elaspe:{0:.6f}'.format(time.perf_counter() - start))
plt.show()
