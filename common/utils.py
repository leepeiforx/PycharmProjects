import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve
import pandas as pd
import zipfile as zp


# %%

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


def unpack_file_to_df(zipfile, encoding='gbk'):
    """

    :param encoding: 解码方式
    :param zipfile: 文件的压缩路径
    :return: 返回压缩包内的{文件名:内容}字典
    """
    file = zp.ZipFile(zipfile)
    temp_list = []
    for f in file.filelist:
        fname = f.filename.split('.')[0]
        f_type = f.filename.split('.')[1]
        temp_list.append((f_type, fname, f.filename))
    temp_dict = {}
    for f in temp_list:
        f_type = f[0]
        fname = f[1]
        file_value = f[2]
        if f_type == 'csv':
            file_values = pd.read_csv(file.open(file_value), encoding=encoding)
        elif f_type == 'xlsx' or 'xls':
            file_values = pd.read_excel(file.open(file_value))
        temp_dict[fname] = file_values
    return temp_dict


def show_info(tab):
    print('显示各个字段的记录数,数据类型:')
    print(tab.info())
    print('显示各数值字段的描述性统计')
    print(tab.describe())
    print('该文档字段-记录数量')
    print(tab.shape)


def show_duplicated(tab):
    print('原始数据记录数:')
    print(len(tab))
    print('非重复数据记录数:')
    print(len(tab[~tab.duplicated().values == True]))
    print('重复数据记录数:')
    print(len(tab[tab.duplicated().values == True]))


def show_na(tab):
    print('各个字段缺省值数量')
    print(tab.isna().sum())
    print('各字段缺失值占比')
    print(tab.apply(lambda x: x.isna().sum() / len(x), axis=0))


def fix_matplotlib_error():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题
