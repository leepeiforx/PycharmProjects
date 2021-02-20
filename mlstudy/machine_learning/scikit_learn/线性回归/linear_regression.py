import numpy as np

# 多项式与线性回归
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


def polynomial_model(degree=1):
    polynomial_feature = PolynomialFeatures(degree=degree, include_bias=False)
    linear_gression = LinearRegression()
    pipeline = Pipeline([('polynomial_feature', polynomial_feature), ('linear_gression', linear_gression)])
    return pipeline


# %%
# 使用线性回归拟合正弦函数

n_dots = 200
X = np.linspace(-2 * np.pi, 2 * np.pi, n_dots)
y = np.sin(X) + 0.2 * np.random.rand(n_dots) - 1
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

from sklearn.metrics import mean_squared_error

degrees = [2, 3, 5, 10]
results = []
for degree in degrees:
    model = polynomial_model(degree)
    model.fit(X, y)
    train_score = model.score(X, y)
    mse = mean_squared_error(y, model.predict(X))
    results.append({'model': model, 'degree': degree, 'score': train_score, 'mse': mse})

for r in results:
    print('degree:{};train_score:{},mean squared error:{}'.format(r['degree'], r['score'], r['mse']))

# %%
# 画出拟合效果
import matplotlib.pyplot as plt
from matplotlib.figure import SubplotParams

plt.figure(figsize=(12, 6), dpi=200, subplotpars=SubplotParams(hspace=.3))
for i, r in enumerate(results):
    fig = plt.subplot(2, 2, i + 1)
    plt.xlim(-8, 8)
    plt.title('linearr regression degree={}'.format(r['degree']))
    plt.scatter(X, y, s=5, c='b', alpha=.5)
    plt.plot(X, r['model'].predict(X), 'r--')
plt.show()


#%%
from sklearn.linear_model import Lasso