import pandas as pd
import numpy as np
import os

# 设置默认文件路径在桌面
default_path = r'C:\Users\bolat\Desktop'


def load_data_package():
    print('加载数据处理包')

    print('完成加载pandas,numpy,matplotlib,seaborn包')


def data_info(df, head=5, tail=5):
    print('输出头前{}的data数据'.format(head))
    print(df.head(head))
    print('\n')

    print('输出末尾{}的data数据'.format(tail))
    print(df.tail(tail))
    print('\n')

    print('各字段数据类型')
    print(df.info)
    print('\n')

    print('部分字段描述性统计情况')
    print(df.describe())


def read_file_to_pandas(file_name, file_path=default_path):
    file_ab_path = file_path + file_name
    print(file_ab_path)
    fname, fattr = os.path.splitext(file_name)
    if fattr == '.csv':
        print('done')
        df = pd.read_csv(file_ab_path)
    elif fattr == 'xlsx' or fattr == 'xls':
        df = pd.read_excel(file_ab_path)

    print('已完成读入工作')
    return df

def check_na(df):
    print(df.isnull().sum())
