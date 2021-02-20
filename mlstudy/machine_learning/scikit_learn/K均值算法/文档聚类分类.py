from sklearn.cluster import KMeans
from sklearn.datasets import load_files
import time

# %%

print('loading documents ...')
t = time.perf_counter()
file_path = r'C:\Users\bolat\PycharmProjects\PyProjects\mlstudy' \
            r'\machine_learning\scikit_learn\data_bases\class_file'
doc = load_files(file_path)
print('summary: {0} documents in {1} categories.'.format(len(doc.data), len(doc.target_names)))
print('Done in {0:.2f} secondes'.format(time.perf_counter() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print('Vectorizing documents...')
t = time.perf_counter()
vectorizer = TfidfVectorizer(max_df=.4, min_df=2, max_features=max_features, encoding='latin-1')
X = vectorizer.fit_transform((d for d in doc.data))

print('n_samples :{}; n_features:{}'.format(X.shape[0], X.shape[1]))
print('number of non-zero features in sample[{0}]:{1}'.format(doc.filenames[0], X[0].getnnz()))
print('Done in {0:.2f} seconds'.format(time.perf_counter() - t))

# %%
# 文本聚类分析
print('clustering documents')
t = time.perf_counter()
n_clusters = 4
kmean = KMeans(n_clusters=n_clusters, max_iter=100, tol=0.01, verbose=1, n_init=3)
kmean.fit(X)
print('kmean :k={0}; cost={1:.2f}'.format(n_clusters, int(kmean.inertia_)))
print('Done in {:.2f}'.format(time.perf_counter() - t))

# %%
print(kmean.labels_[1000:1010])
print(doc.filenames[1000:1010])

# %%
from __future__ import print_function

print('Top terms per cluster:')

order_centroids = kmean.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(n_clusters):
    print('Cluster{}'.format(i))
    for ind in order_centroids[i, :10]:
        print('{}'.format(terms[ind]), end=' ')
    print()

# %%
# 聚类算法性能评估
# Adjust Rand Index

import numpy as np
from sklearn import metrics

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)

print('Adjust Rand Index for random sample:{:.2f}'.format(metrics.adjusted_rand_score(label_true, label_pred)))
label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]
print('Adjust Rand Index for same structure sample:{}'.format(metrics.adjusted_rand_score(label_true, label_pred)))

# %%
# 齐次性&完整性
# 齐次性
label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print('Homogeneity score for same structure sample:{:.3f}'
      .format(metrics.homogeneity_score(label_true, label_pred)))

label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]
print('Homogeneity score for each cluster come from only one class:{:.3f}'
      .format(metrics.homogeneity_score(label_true, label_pred)))

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print('Homogeneity score for each cluster come from two class:{:.3f}'
      .format(metrics.homogeneity_score(label_true, label_pred)))

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print('Homogeneity score for each cluster come from random sample:{:.3f}'
      .format(metrics.homogeneity_score(label_true, label_pred)))

# 完整性
label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print('Completeness score for same structure sample:{:.3f}'
      .format(metrics.completeness_score(label_true, label_pred)))

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print('Completeness score for each cluster come from only one class:{:.3f}'
      .format(metrics.completeness_score(label_true, label_pred)))

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print('Completeness score for each cluster come from two class:{:.3f}'
      .format(metrics.completeness_score(label_true, label_pred)))

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print('Completeness score for each cluster come from random sample:{:.3f}'
      .format(metrics.completeness_score(label_true, label_pred)))

#%%
# V-measure
label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print('V-measure for same structure sample:{:.3f}'
      .format(metrics.v_measure_score(label_true, label_pred)))

label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print('V-measure for each cluster come from only one class:{:.3f}'
      .format(metrics.v_measure_score(label_true, label_pred)))

label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print('V-measure for each cluster come from two class:{:.3f}'
      .format(metrics.v_measure_score(label_true, label_pred)))

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print('V-measure for each cluster come from random sample:{:.3f}'
      .format(metrics.v_measure_score(label_true, label_pred)))

#%%
labels = doc.target
print('adjusted rand index:{:.3f}'.format(metrics.adjusted_rand_score(labels, kmean.labels_)))
print('Homogeneity:{:.3f}'.format(metrics.homogeneity_score(labels, kmean.labels_)))
print('Completeness:{:.3f}'.format(metrics.completeness_score(labels, kmean.labels_)))
print('V-measure:{:.3f}'.format(metrics.v_measure_score(labels, kmean.labels_)))
print('Silhouette Coefficient:{:.3f}'.format(metrics.silhouette_score(X, kmean.labels_, sample_size=1000)))
