# 画出学习曲线
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# %%
n_dots = 200

X = np.linspace(0, 1, n_dots)
y = np.sqrt(X) + 0.2 * np.random.rand(n_dots) - 0.1

# 因为在scikit-learn中需要使用到n_sample * n_feature的矩阵
# 所以需要转化为200*1的矩阵
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)
print(X.shape, y.shape)


# %%
def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()

    #     这是一个流水线,先增加多项式阶数,然后再用线性回归算法来拟合数据
    pipline = Pipeline([('polynomial_features', polynomial_features),
                        ('linear_regression', linear_regression)])
    return pipline


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1,
                        train_sizes=np.linspace(0.1, 1.0, 5)):
    plt.title(title)
    if ylim is not None:
        plt.ylim(ylim)
    plt.xlabel('Training Examples')
    plt.ylabel('Score')
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                                                            train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.grid()
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=1, color='r')
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=.1, color='g')
    plt.plot(train_sizes, train_scores_mean, 'o--', color='b', label='Training score')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Test score')
    plt.legend(loc='best')
    return plt


# 为了让学习曲线更顺滑,计算10次交叉验证数据集的分数
# cv = ShuffleSplit(n_splits=10, test_size=.2, random_state=0)
# titles = ['Learning Curves(Under Fitting)', 'Learning Curves', 'Learning Curves(Over Fitting)']
degrees = [1, 3, 10]
#
# plt.figure(figsize=(18, 4), dpi=200)
# for i in range(len(degrees)):
#     plt.subplot(1, 3, i + 1)
#     plot_learning_curve(polynomial_model(degrees[i]), titles[i], X, y, ylim=(0.75, 1.01), cv=cv)
#
# plt.show()
