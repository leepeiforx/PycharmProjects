from sklearn.svm import SVC
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np


def plot_hyperplane(clf, X, y,
                    h=0.02,
                    draw_sv=True,
                    title='hyperplan'):
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap='hot', alpha=0.5)

    markers = ['o', 's', '^']
    colors = ['b', 'r', 'c']
    labels = np.unique(y)
    for label in labels:
        plt.scatter(X[y == label][:, 0],
                    X[y == label][:, 1],
                    c=colors[label],
                    marker=markers[label])
    if draw_sv:
        sv = clf.support_vectors_
        plt.scatter(sv[:, 0], sv[:, 1], c='y', marker='x')


# %%
# 2个特征的,2个类别的数据集
X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=.3)

clf = SVC(C=1.0, kernel='linear')
clf.fit(X, y)

plt.figure(figsize=(12, 4), dpi=144)
plot_hyperplane(clf, X, y, h=0.01, title='Maximum Margin Hyperplan')
plt.show()

# %%
# 2个特征,3个类别的数据集
X, y = make_blobs(n_samples=100, centers=3, cluster_std=.8, random_state=1)
clf_linear = SVC(C=1.0, kernel='linear')
clf_poly = SVC(C=1.0, kernel='poly', degree=3)
clf_rbf = SVC(C=1.0, kernel='rbf', gamma=.5)
clf_rbf2 = SVC(C=1.0, kernel='rbf', gamma=.1)

plt.figure(figsize=(10, 10), dpi=144)
clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = ['Linear Kernal', 'Polynoimal Kernal with Degree = 3',
          'Gaussian Kernal with $\gamma=0.5$', 'Gaussian Kernal with $\gamma=0.1$']

for i, clf in enumerate(clfs):
    clf.fit(X, y)
    plt.subplot(2, 2, i + 1)
    plot_hyperplane(clf, X, y, title=titles[i])

plt.show()
