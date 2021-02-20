import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture


def create_data(centers, num=100, std=0.7):
    X, labels_true = make_blobs(n_samples=num, centers=centers, cluster_std=std)
    return X, labels_true


def plot_data(*args):
    X, labels_true = args
    labels = np.unique(labels_true)
    fig = plt.figure()
    plt.subplot(1, 1, 1)
    colors = 'rgbyckm'
    for i, label in enumerate(labels):
        position = labels_true == label
        plt.scatter(X[position, 0], X[position, 1], label='Cluster {}'.format(label))
        color = colors[i % len(colors)]

    plt.legend(loc='best', framealpha=.5)
    plt.xlabel('X[0]')
    plt.ylabel('Y[1]')
    plt.title('data')

    plt.show()


X, labels_true = create_data([[1, 1], [2, 2], [1, 2], [10, 20]], 1000, 0.5)
plot_data(X, labels_true)

#%%
# K均值聚类
from sklearn.cluster import KMeans

kmeans = KMeans()
