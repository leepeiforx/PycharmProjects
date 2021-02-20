import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.model_selection import ShuffleSplit
from mlstudy.machine_learning.scikit_learn.basic_theory import plot_learning_curve
import matplotlib.pyplot as plt

# from sklearn.

file_path = r'C:\Users\bolat\PycharmProjects\PyProjects\mlstudy\machine_learning\scikit_learn\data_bases\diabetes.csv'

df = pd.read_csv(file_path)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

models = [('KNN', KNeighborsClassifier(n_neighbors=2)),
          ('KNN with weights', KNeighborsClassifier(n_neighbors=2, weights='distance')),
          ('Radius KNN', RadiusNeighborsClassifier(n_neighbors=2, radius=500.0))]

# 分别训练3个模型,并计算评分
results = []
for name, model in models:
    model.fit(X_train, y_train)
    results.append((name, model.score(X_test, y_test)))

for i in range(len(results)):
    print('name:{}; score:{}'.format(results[i][0], results[i][1]))

# %%
# 使用普通k-均值算法预测糖尿病人
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)
train_score = knn.score(X_train, y_train)
test_score = knn.score(X_test, y_test)
print('train score:{}; test score:{}'.format(train_score, test_score))

# 画出学习曲线
knn = KNeighborsClassifier(n_neighbors=2)
cv = ShuffleSplit(n_splits=10, test_size=.2, random_state=0)
plt.figure(figsize=(16, 10), dpi=200)
plot_learning_curve(knn, 'Learning Curve for KNN Diabetes', X, y, ylim=(0.0, 1.01), cv=cv)
plt.show()


#%%
from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=2)
X_new = selector.fit_transform(X, y)
print(X_new[:5])





