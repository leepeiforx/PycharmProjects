from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from common.utils import plot_learning_curve
import matplotlib.pyplot as plt
import time

# %%

boston = load_boston()
X = boston.data
y = boston.target

# print(boston.feature_names)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)
start = time.perf_counter()
train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('elaspe:{0:.6f}; train_score: {1:.6f};cv_score:{2:.6f}'
      .format(time.perf_counter() - start, train_score, cv_score))

# %%
# 模型优化
# 归一化(提高收敛速度)
model = LinearRegression(normalize=True)
model.fit(X_train, y_train)
start = time.perf_counter()
train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('归一化')
print('elaspe:{0:.6f}; train_score: {1:.6f};cv_score:{2:.6f}'
      .format(time.perf_counter() - start, train_score, cv_score))


# %%

def polynoimal_model(degree=1):
    polynoimal_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipline = Pipeline([('polynoimal_features', polynoimal_features),
                        ('linear_regression', linear_regression)])
    return pipline


model = polynoimal_model(degree=2)  # 二项多阶式
start = time.perf_counter()
model.fit(X_train, y_train)
train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('elaspe:{0:.6f}, train_score:{1:.6f}, cv_score:{2:.6f}'
      .format(time.perf_counter() - start, train_score, cv_score))

# %%
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=.2, random_state=0)

title = 'Learning Curve (degree={})'
degrees = [1, 2, 3]

start = time.perf_counter()
plt.figure(figsize=(16, 12), dpi=200)
for i in range(len(degrees)):
    plt.subplot(3, 1, i + 1)
    plot_learning_curve(estimator=polynoimal_model(degree=degrees[i]), X=X, y=y, ylim=(0.01, 1.01), cv=cv,
                        title=title.format(degrees[i]))

plt.show()
print('elaspe:{0:.6f}'.format(time.perf_counter()-start))
