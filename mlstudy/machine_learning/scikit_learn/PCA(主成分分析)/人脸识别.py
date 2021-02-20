import time
import logging
from sklearn.datasets import fetch_olivetti_faces
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# %%

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

data_home = 'datasets/'
logging.info('Start to load dataset')
faces = fetch_olivetti_faces(data_home=data_home)
logging.info('Done with load dataset')

# %%
X = faces.data
y = faces.target

targets = np.unique(faces.target)
target_names = np.array(['c{}'.format(i) for i in targets])
n_targets = target_names.shape[0]
n_samples, h, w = faces.images.shape

print('Sample count: {}\nTarget count: {}'.format(n_samples, n_targets))
print('Image size: {} x {}\nDataset shape: {}\n'.format(w, h, X.shape))


def plot_gallery(images, titles, h, w, n_row=2, n_col=5):
    """显示图片阵列"""
    plt.figure(figsize=(2 * n_col, 2.2 * n_row), dpi=144)
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.9, hspace=.01)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.axis('off')


n_row = 2
n_col = 6
samples_images = None
samples_titles = []
for i in range(n_targets):
    people_image = X[y == i]
    people_sample_index = np.random.randint(0, people_image.shape[0], 1)
    people_sample_image = people_image[people_sample_index, :]
    if samples_images is not None:
        samples_images = np.concatenate((samples_images, people_sample_image), axis=0)
    else:
        samples_images = people_sample_image
    samples_titles.append(target_names[i])

plot_gallery(samples_images, samples_titles, h, w, n_row, n_col)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1)

# %%
from sklearn.svm import SVC

start = time.perf_counter()
print('fitting train datasets')
clf = SVC(class_weight='balanced')
clf.fit(X_train, y_train)
print('done in {0:.2f}'.format(time.perf_counter() - start))

# s使用confusion_matrix和classification_report查看模型分类的准确性

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print('confusion matrix')
np.set_printoptions(threshold=1600)
print(cm)

# %%
cr = classification_report(y_test, y_pred)
print(cr)

# %% 使用PCA来处理数据集

from sklearn.decomposition import PCA

print('Exploring explained variance ratio for dataset...')
candidate_components = range(10, 300, 30)
explained_ratios = []
start = time.perf_counter()
for c in candidate_components:
    pca = PCA(n_components=c)
    clf = pca.fit(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))
print('done in {0:.2f} seconds'.format(time.perf_counter() - start))

# 根据不同的k值,构造PCA模型
plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.plot(candidate_components, explained_ratios)
plt.xlabel('Number of PCA Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained variance for PCA')
plt.yticks(np.arange(0.5, 1.05, 0.05))
plt.xticks(np.arange(0, 300, 20))

plt.show()

# %%
# 选取5张照片画出不同数据还原率下的照片

n_row = 1
n_col = 5


def title_prefix(prefix, title):
    return '{}:{}'.format(prefix, title)


samples_images = samples_images[:5]
samples_titles = samples_titles[:5]

plotting_images = samples_images
plotting_titles = [title_prefix('orig', t) for t in samples_titles]
candidate_components = [140, 75, 37, 19, 8]
for c in candidate_components:
    print('Fitting and projecting on PCA(n_componts={}...)'.format(c))
    start = time.perf_counter()
    pca = PCA(n_components=c)
    pca.fit(X)
    X_sample_pca = pca.transform(samples_images)
    X_sample_inv = pca.inverse_transform(X_sample_pca)
    plotting_images = np.concatenate((plotting_images, X_sample_inv), axis=0)
    samples_titles_pca = [title_prefix('{}'.format(c), t) for t in samples_titles]
    plotting_titles = np.concatenate((plotting_titles, samples_titles_pca), axis=0)
    print('Done in {0:.2f}'.format(time.perf_counter() - start))

print('Plotting sample image with different number of PCA components...')
plot_gallery(plotting_images, plotting_titles, h, w, n_row * (len(candidate_components) + 1), n_col)
plt.show()

# %%
# 最终结果
n_components = 140
print('Fitting PCA by using traing data...')
start = time.perf_counter()
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True)
pca.fit(X_train)
print('Done in {0:.2f}'.format(time.perf_counter() - start))

print('Projecting input data for PCA')
start = time.perf_counter()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print('Done in {0:.2f}'.format(time.perf_counter() - start))

# %%
from sklearn.model_selection import GridSearchCV

# 使用GridSearchCV选择一个最佳的SVC模型参数,然后用最佳参数对模型进行训练
print('Searching the best parameters for SVC...')
param_grid = {'C': [1, 5, 10, 50, 100], 'gamma': [0.00001, 0.0005, 0.001, 0.005, 0.01]}
clf = GridSearchCV(estimator=SVC(kernel='rbf', class_weight='balanced'), param_grid=param_grid, verbose=2, n_jobs=4)
clf.fit(X_train_pca, y_train)
print('Best parameter found by grid search:')
print(clf.best_params_)

# %%
# 使用这一模型对测试样本进行预测,并且使用confusion_matrix输出准确性信息

start = time.perf_counter()
print('Predicting test dataset...')
y_pred = clf.best_estimator_.predict(X_test_pca)
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print('Done in {:.2f}'.format(time.perf_counter() - start))
print('confusion matrix:')
print(cm)
print('classification report')
print(classification_report(y_test, y_pred))
