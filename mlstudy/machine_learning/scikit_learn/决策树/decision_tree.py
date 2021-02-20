import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt

# %%

f_path = r'C:\Users\bolat\PycharmProjects\PyProjects\mlstudy\machine_learning\scikit_learn\data_bases\titanic_train.csv'
data = pd.read_csv(f_path)


def read_data(fp):
    # 删除Cabin,Name,Ticket这些无用特征
    data.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)

    # 处理Sex字段,令male=1,female=0
    data['Sex'] = data['Sex'].map({'male': 1, 'female': 0})

    # 处理登船港口数据,(转化为int数值)
    embarked_lst = data['Embarked'].unique().tolist()
    data['Embarked'] = data['Embarked'].apply(lambda n: embarked_lst.index(n))

    #   处理缺失数据
    data.fillna(0, inplace=True)
    return data


train = read_data(f_path)
train.isna().sum()
# %%
X = train.drop(['Survived'], axis=1).values
y = train['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
print('train dataset: {0}; test dataset: {1}'.format(X_train.shape, X_test.shape))

# %%
# 训练模型
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print('train score:{}; test score:{}'.format(train_score, test_score))


# %%
# 优化模型参数
# scikit-learn不支持后剪枝
# 模型参数工具选择包
# from sklearn.model_selection import GridSearchCV

def plot_curve(train_sizes, cv_results, xlabel):
    train_sizes_mean = cv_results['mean_train_score']
    train_sizes_std = cv_results['std_train_score']
    test_sizes_mean = cv_results['mean_test_score']
    test_sizes_std = cv_results['std_test_score']

    plt.figure(figsize=(6, 4), dpi=144)
    plt.title('parameters turning')
    plt.xlabel(xlabel)
    plt.ylabel('score')

    plt.fill_between(train_sizes,
                     train_sizes_mean - train_sizes_std, train_sizes_mean + train_sizes_std,
                     alpha=.1, color='r')

    plt.fill_between(train_sizes,
                     test_sizes_mean - test_sizes_std, test_sizes_mean + test_sizes_std,
                     alpha=.1, color='r')

    plt.plot(train_sizes, train_sizes_mean, '.--', color='r', label='Training Scores')
    plt.plot(train_sizes, test_sizes_mean, '.-', color='g', label='Cross-validation Scores')
    plt.legend(loc='best')


threholds = np.linspace(0, 0.5, 10)

# 设置参数
param_grid = {'min_impurity_split': threholds}
clf = GridSearchCV(DecisionTreeClassifier(), param_grid=param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print('best param: {0}\n best score:{1}'.format(clf.best_params_, clf.best_score_))
plot_curve(threholds, clf.cv_results_, xlabel='gini threholds')
plt.show()

# %%
# 多组参数之间选择最优参数

entropy_threholds = np.linspace(0, 1, 50)
gini_threholds = np.linspace(0, 0.5, 50)
param_grid = [{'criterion': ['entory'], 'min_impurity_split': entropy_threholds},
              {'criterion': ['gini'], 'min_impurity_split': gini_threholds},
              {'max_depth': range(2, 20)},
              {'min_samples_split': range(2, 30, 2)}]

clf = GridSearchCV(DecisionTreeClassifier(), param_grid=param_grid, cv=5)
clf.fit(X, y)
print('best param: {0}\n best score:{1}'.format(clf.best_params_, clf.best_score_))

