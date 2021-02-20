from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# %%

X, y = make_blobs(n_samples=200, n_features=2, centers=4,
                  cluster_std=1, center_box=(-10, 100),
                  shuffle=True, random_state=1)
plt.figure(figsize=(6, 4), dpi=144)
plt.xticks([])
plt.yticks([])
plt.scatter(X[:, 0], X[:, 1], s=20, marker='o')
plt.show()

# %%
# 使用k-mean拟合
from sklearn.cluster import KMeans


def fit_plot_kmean_model(n_clusters, X):
    plt.xticks([])
    plt.yticks([])

    # 使用K-Mean算法拟合
    kmean = KMeans(n_clusters=n_clusters)
    kmean.fit_predict(X)

    labels = kmean.labels_
    centers = kmean.cluster_centers_

    markers = ['o', '^', '*', 's']
    colors = ['r', 'b', 'y', 'k']

    # 计算成本
    score = kmean.score(X)
    # print('k={}; score={}'.format(n_clusters, score))
    # 画样本
    for c in range(n_clusters):
        clusters = X[labels == c]
        plt.title('k={}; score={}'.format(n_clusters, round(score, 2)))
        plt.scatter(clusters[:, 0], clusters[:, 1], s=20, marker=markers[c], c=colors[c])

    # 画出中心点
    plt.scatter(centers[:, 0], centers[:, 1], s=300, marker='o', c='white', alpha=.9)

    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker='${}$'.format(i), s=50, c=colors[i])


n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)
kmean.fit(X)
print('kmean: k={}, cost={}'.format(n_clusters, int(kmean.score(X))))

# %%
# 画出分类后的样本和所属的聚类中心
labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ['o', '^', '*']
colors = ['r', 'b', 'y']

plt.figure(figsize=(6, 4), dpi=144)
plt.xticks([])
plt.yticks([])

# 画样本
for c in range(n_clusters):
    clusters = X[labels == c]
    plt.scatter(clusters[:, 0], clusters[:, 1], marker=markers[c], color=colors[c], s=20)

# 画中心点
plt.scatter(centers[:, 0], centers[:, 1], marker='o', color='white', alpha=.9, s=300)

for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker='${}$'.format(i), s=50, c=colors[i])

plt.show()

# %%
n_clusters = [2, 3, 4]
plt.figure(figsize=(10, 3), dpi=144)
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)
plt.show()
