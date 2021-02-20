from time import time
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt

# %%
print('loading train dataset...')
t = time()
f_path = r'C:\Users\bolat\PycharmProjects\PyProjects\mlstudy\machine_learning' \
         r'\scikit_learn\data_bases\file_classification\train'
new_train = load_files(f_path)
print('summary: {0} documents in {1} categories.'
      .format(len(new_train.data), len(new_train.target_names)))

print('vectorizing train dataset...')
t = time()
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in new_train.data))
print('n_sampels: {}; n_features: {}'.format(X_train.shape[0], X_train.shape[1]))
print('number of non-zero features in sample [{0}]: {1}'
      .format(new_train.filenames[0], X_train[0].getnnz()))
print('done in {0} seconds'.format(time() - t))

# %%
# 训练模型
print('predicting test dataset...')
t0 = time()
y_train = new_train.target
clf = MultinomialNB(alpha=0.0001)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
print('train score: {}'.format(train_score))
print('done in {0} seconds'.format(time() - t0))

# %%
print('loading test dataset')
t = time()
f_path = r'C:\Users\bolat\PycharmProjects\PyProjects\mlstudy\machine_learning' \
         r'\scikit_learn\data_bases\file_classification\test'
new_test = load_files(f_path)
print('summary {0} documents in {1} categories'.format(len(new_test.data), len(new_test.target_names)))

print('vetorizing test dataset...')
t = time()
X_test = vectorizer.transform((d for d in new_test.data))
y_test = new_test.target
print('n_samples: {}; n_features: {}'.format(X_test.shape[0], X_test.shape[1]))
print('number of non-zero features in sample[{0}]: {1}'.format(new_test.filenames[0], X_test[0].getnnz()))
print('elaspe: {} seconds'.format(time() - t))

print(X_test.shape)

# %%
print(X_test.shape)
# 初步验证一下
# pred = clf.predict(X_test[0])
# print('predict: {0} is in category {1}'
#       .format(new_test.filenames[0], new_test.target_names[pred[0]]))
print('actually: {0} is in category {1}'
      .format(new_test.filenames[0], new_test.target_names[new_test.target[0]]))

# %%
# 模型评价
print('predicting test dataset...')
t0 = time()
pred = clf.predict(X_test)
print('done in {0} seconds'.format(time() - t0))

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# 查看针对每个类别的预测准确性
print('classification report on test set for classifier:')
print(clf)
print(classification_report(y_test, pred, target_names=new_test.target_names))

# %%
# confusion_matrix 生成混淆矩阵观察每种类别被错误分类的情况
cm = confusion_matrix(y_test, pred)
print('confusion metrix:')
print(cm)

# show cunfusion matrix
plt.figure(figsize=(8, 8), dpi=144)
plt.title('confusion matrix of the classifier')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.matshow(cm, fignum=1, cmap='gray')
plt.colorbar()
plt.show()
