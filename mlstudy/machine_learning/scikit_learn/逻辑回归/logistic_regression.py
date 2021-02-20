from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression
import numpy as np
import time
import matplotlib.pyplot as plt

# %%
cancer = load_breast_cancer()

X = cancer.data

y = cancer.target
y = y.reshape(-1, 1)
print('data shape:{0}; no. positiion :{1}; no.negetitive:{2};'
      .format(X.shape, y[y == 1].shape[0], y[y == 0].shape[0]))

print(cancer.data[0])
print(X.shape, y.shape)

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1)
model = LogisticRegression()
model.fit(X_train, y_train)
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print('Train score:{tr_s:.6f}; Test_score:{tt_s:.6f}'.format(tr_s=train_score, tt_s=test_score))

# %%
# 样本预测
y_pred = model.predict(X_test)
print('matchs:{0}/{1}'.format(np.equal(y_pred, y_test).shape[0], y_test.shape[0]))

# 预测概率:找出概率低于90%的样本
y_pred_proba = model.predict_proba(X_test)  # 计算每个测试样本的预测概率

# 找出第一列,即预测为阴性的概率大于0.1的样本,保存在result里
y_pred_proba_0 = y_pred_proba[:, 0] > 0.1
result = y_pred_proba[y_pred_proba_0]

# 在result结果集里找出预测为阳性的概率大于0.1的样本
y_pred_proba_1 = result[:, 1] > 0.1
result = result[y_pred_proba_1]
result

# %%
# 模型优化
from common.load_poly import PolynomialModel

model = PolynomialModel(degree=2, estimator=LogisticRegression, penalty='l1')
start = time.perf_counter()
model.fit(X_train, y_train)
train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('elaspe:{0:.6f}; train_score:{1:.6f}; cv_score={2:.6f}'
      .format(time.perf_counter() - start, train_score, cv_score))

logistic_regression = model.named_steps['model']
# ** 这里统计有点问题**
print('model parameters shape:{0}; count of non-zero element: {1}'
      .format(logistic_regression.coef_.shape, np.count_nonzero(logistic_regression.coef_)))

# %%
from sklearn.model_selection import ShuffleSplit
from common.load_poly import plot_learning_curve

#
cv = ShuffleSplit(n_splits=10, test_size=.2, random_state=0)
titles = 'Learning Curve (degree={}, penalty={})'
degrees = [1, 2]
penalty = 'l2'
n_jobs = 5
for i in range(len(degrees)):
    print(i, degrees[i])
    plt.subplot(len(degrees), 1, i + 1)
    model = PolynomialModel(degree=degrees[i], estimator=LogisticRegression, penalty=penalty)
    title = titles.format(degrees[i], penalty)
    print(title)
    plot_learning_curve(model, title, X, y, ylim=(0.5, 1.1), cv=None, n_jobs=n_jobs,
                        train_sizes=np.linspace(0.1, 1.0, 5))
plt.show()
