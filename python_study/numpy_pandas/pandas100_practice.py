# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %%

import numpy as np
import pandas as pd

# %%

# 查看 Pandas 版本信息
print(pd.__version__)

# %%

# 从列表创建 Series
s1 = pd.Series([1, 2, 3, 4])

# %%

# 从 Ndarray 创建 Series
s1 = pd.Series(np.arange(5))
s1.index = list('ABCDE')

# %%

# 从字典创建 Series
s3 = pd.Series({'A': 1,
                'B': 2,
                'C': 3,
                'D': 4})
print(s3)

# %%

# Series 基本操作
# 修改 Series 索引
s1.index = list('ABCDE')
print(s1)

# %%

# Series 纵向拼接
s2 = s1.append(s3)
s2

# %%

# Series 按指定索引删除元素
print(s2)
s2.drop(labels='A', axis=0)

# %%

# Series 修改指定索引元素
s2['B'] = 0
s2

# %%

# Series 按指定索引查找元素
s2['C']

# %%

# Series 切片操作
s2[:3]

# %%

# Series 运算
# Series 加法运算
# Series 的加法运算是按照索引计算，
# 如果索引不同则填充为 NaN（空值）。
print(s1, s3)
# print(s1.add(s3))
# print(s1+s3)

# %%

# Series 减法运算
# Series的减法运算是按照索引对应计算，
# 如果不同则填充为 NaN（空值）
# print(s1.sub(s3))
# print(s1-s3)

# %%

# Series 乘法运算
# s1*s3
s1.mul(s3)

# %%

# Series 除法运算
# s1/s3
s1.divide(s3)

# %%

# Series 求中位数
s1.median()

# %%

# Series 求和
s1.sum()

# %%

# Series 求最大值
s1.max()

# %%

# Series 求最小值
s1.min()

# %%

# 创建 DataFrame 数据类型
# 通过 NumPy 数组创建 DataFrame
# 定义时间序列作为 index
dates = pd.date_range('2019/09/02', periods=6, freq='D', )
num_arr = np.random.randn(6, 4)
columns = list('ABCD')
df = pd.DataFrame(num_arr, index=dates, columns=columns)
df

# %%

# 通过字典数组创建 DataFrame
data = dict(zip(('animal', 'age', 'visits', 'priority'),
                (['cat', 'cat', 'snake', 'dog',
                  'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                 [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                 [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 ['yes', 'yes', 'no', 'yes',
                  'no', 'no', 'no', 'yes', 'no', 'no'])))
labels = list('abcdefghij')
df = pd.DataFrame(data, index=labels)
df

# %%

# 查看 DataFrame 的数据类型
df.dtypes

# %%

# DataFrame 基本操作
# 23. 预览 DataFrame 的前 5 行数据
df.head()

# %%

# 查看 DataFrame 的后 3 行数据
df.tail(3)

# %%

# 查看 DataFrame 的索引
df.index

# %%

# 查看 DataFrame 的列名
df.columns

# %%

# 查看 DataFrame 的数值
print(df.values)

# %%

# 查看 DataFrame 的统计数据
print(df.describe())

# %%

# DataFrame 转置操作
print(df.T)

# %%

# 对 DataFrame 进行按列排序
df.sort_values(by='age', ascending=False)

# %%

# 对 DataFrame 数据切片
df.iloc[0:4]

# %%

# 对 DataFrame 通过标签查询（单列）
# df['age']
# df.loc[:,['age']]
df.age

# %%

# 对 DataFrame 通过标签查询（多列）
# df.loc[:,['age','visits']]
df[['age', 'visits']]

# %%

# 对 DataFrame 通过位置查询
df.iloc[1:3]

# %%

# DataFrame 副本拷贝
df2 = df.copy()
df2

# %%

# 判断 DataFrame 元素是否为空
df.isnull()

# %%

# 添加列数据
num = pd.Series([i for i in range(10)], index=df.index)
df['No.'] = num
df

# %%

# 根据 DataFrame 的下标值进行更改。
df2
# df.iat ?
df2.iat[1, 1] = 0
# df2.iloc[[1],[1]] = 1
print(df2)

# %%

# 根据 DataFrame 的标签对数据进行修改
df2.loc['f', ['age', 'visits']] = 1

# %%

# DataFrame 求平均值操作
df2.mean()

# %%

# 对 DataFrame 中任意列做求和操作
df2.age.mean()
df2['age'].mean()

# %%

# 字符串操作
# 42. 将字符串转化为小写字母
string = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca',
                    np.nan, 'CABA', 'dog', 'cat'])
print(string)
print(string.str.lower())

# %%

# 将字符串转化为大写字母
string.str.upper()
string

# %%

# DataFrame 缺失值操作
# 对缺失值进行填充
df2 = df.copy()
print(df2)
# df3 = df2.fillna(value=2)
# df3
# 删除存在缺失值的行
print(df2.dropna(how='any'))

# %%

# 46. DataFrame 按指定列合并
left = pd.DataFrame({'key': ['fool1', 'fool2'],
                     'one': [1, 2]})
right = pd.DataFrame({'key': ['fool2', 'fool4'],
                      'two': [4, 5]})
print(left, '\n', right)
print(pd.merge(left, right, how='left', on='key'))

# %%

# DataFrame 文件操作
# CSV文件写入
df.to_csv('animal.csv')
print('done')
# csv文件读取
df_animal = pd.read_csv('animal.csv')
df_animal

# %%

# Excel 写入操作
df.to_excel('animal.xlsx')
print('done')
# Excel 读取操作
df_from_excel = pd.read_excel('animal.xlsx')
df_from_excel

# %%

# 进阶部分
# 时间序列索引?
# 建立一个以 2018 年每一天为索引，值为随机数的 Series
index = pd.date_range(start='2018/01/01', end='2018/12/31', freq='D')
s = pd.Series(np.random.rand(len(index)), index=index)
s

# %%

# 统计s 中每一个周三对应值的和?
s[s.index.weekday == 2].sum()
# s[(s.index.weekday== 2)|(s.index.weekday== 3)]

# %%

# 统计s中每个月值的平均值?
s.resample('M').mean()

# %%

# 将 Series 中的时间进行转换（秒转分钟）
index = pd.date_range('today', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(index)), index=index)
ts
ts.resample('Min').sum()

# %%

# UTC 世界时间标准?
index = pd.date_range('today', periods=1, freq='D')
ts = pd.Series(np.random.rand(len(index)), index=index)
ts_utc = ts.tz_localize('UTC')
ts_utc

# %%

# 转换为上海所在时区
ts_utc.tz_convert('Asia/Shanghai')

# %%

# 不同时间表示方式的转换
rng = pd.date_range('1/1/2018', periods=5, freq='M')
ts = pd.Series(np.random.rand(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
ps.to_timestamp()

# %%

# Series 多重索引
# 创建多重索引 Series
# 构建一个 letters = ['A', 'B', 'C']
# 和 numbers = list(range(10))为索引，值为随机数的多重索引 Series。
letters = ['A', 'B', 'C']
numbers = list(range(10))
# 设置多重索引
mul_index = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mul_index)
s

# %%

# 多重索引 Series 查询
# s.index
s.loc[:, [1, 4, 5]]

# %%

# 多重索引 Series 切片?
s.loc[pd.IndexSlice['A':'C', 4:]]
# s.loc[pd.IndexSlice['B':'C',5:]]

# %%

# 根据多重索引创建 DataFrame
# 创建一个以 letters = ['A', 'B'] 和
# numbers = list(range(6))为索引，值为随机数据的多重索引 DataFrame。
letters = ['index1', 'index2']
numbers = list(range(1, 4))
mul_index = pd.MultiIndex.from_product([letters, numbers])
# df = pd.DataFrame(np.arange(12).reshape((6,2)),index=[list('AAABBB'),list('123123')],columns=['A','B'])
df = pd.DataFrame(np.arange(12).reshape((6, 2)), index=mul_index, columns=['A', 'B'])
df

# %%

# 多重索引设置列名称
df.index.names = ['first', 'second']

# %%

# DataFrame 多重索引分组求和
df.groupby(by='second').sum()
# df.groupby(by=['first']).sum()

# %%

# DataFrame 行列名称转换(二维表->一维表)
print(df)
print(df.stack())

# %%

# DataFrame 索引转换
print(df)
print(df.unstack())

# %%

# DataFrame 条件查找
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
df[df['age'] > 3]
df[df.visits >= 2]

# %%

# 根据行列索引切片
df.iloc[:3, :]

# %%

# DataFrame 多重条件查询
df[(df.animal == 'cat') & (df.age >= 3)]

# %%

# DataFrame 按关键字查询
df[df.animal.isin(['cat', 'snake'])]

# %%

# 70. DataFrame 按标签及列名查询
df.loc[:, ['animal', 'visits']][:4]

# %%

# DataFrame 多条件排序
print(df)
df.sort_values(by=['age', 'visits'], ascending=[True, False])

# %%

# 72.DataFrame 多值替换?
df['priority'].map({'yes': True,
                    'no': False})
df
# df['priority'].replace()

# %%

# DataFrame 分组求和
df.groupby(by='age').sum()

# %%

# 使用列表拼接多个 DataFrame
temp_df1 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 1
temp_df2 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 2
temp_df3 = pd.DataFrame(np.random.randn(5, 4))  # 生成由随机数组成的 DataFrame 3
concat_df = pd.concat([temp_df1, temp_df2, temp_df3], axis=1)
print(concat_df.shape)

# %%

# 找出 DataFrame 表中和最小的列
# idxmax(), idxmin() 为 Series 函数返回最大最小值的索引值
df = pd.DataFrame(np.random.randint(1, 10, size=(5, 10)), columns=list('abcdefghij'))
print(df)
print(df.sum(axis=1))
print(df.sum(axis=0))
df.sum().idxmin()

# %%

# DataFrame 中每个元素减去每一行的平均值
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
print(df.mean(axis=1))
df - df.mean(axis=1)

# %%

# DataFrame 分组，并得到每一组中最大三个数之和?
df = pd.DataFrame({'A': list('aaabbcaabcccbbc'),
                   'B': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
# print(df)
df.groupby(by='A')['B'].nlargest(3).sum()
# df.groupby(by='A')['B'].nlargest(3).sum(level=0)

# %%

# 78. 透视表的创建
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
pd.pivot_table(df, index=['A', 'B'])

# %%

# 透视表按指定行进行聚合
# 将该 DataFrame 的 D 列聚合，
# 按照 A,B 列为索引进行聚合，聚合的方式为默认求均值。
pd.pivot_table(df, values='D', index=['A', 'B'])

# %%

# 透视表聚合方式定义
pd.pivot_table(df, values='D', index=['A', 'B'], aggfunc=[np.sum, len])

# %%

# 透视表利用额外列进行辅助分割
pd.pivot_table(df, values='D', index=['A', 'B'], columns='C', aggfunc=np.sum)

# %%

# 透视表的缺省值处理
pd.pivot_table(df, values='D', index=['A', 'B'], columns='C', aggfunc=np.sum, fill_value=0)

# %%

# 绝对类型???
# 在数据的形式上主要包括数量型和性质型，数量型表示着数据可数范围可变，
# 而性质型表示范围已经确定不可改变，绝对型数据就是性质型数据的一种。
# 83. 绝对型数据定义
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df['raw_grade'] = df['raw_grade'].astype('category')

# 对绝对型数据重命名
df['raw_grade'].cat.categories = ['Very Good', 'Good', 'Very Bad']

# 重新排列绝对型数据并补充相应的缺省值
df['raw_grade'].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df

# %%

# 对绝对型数据进行排序
df.sort_values(by='raw_grade')

# %%

# 对绝对型数据进行分组
df.groupby(by='raw_grade').size()

# %%

# 数据清洗
# 在FilghtNumber中有数值缺失，其中数值为按 10 增长，
# 补充相应的缺省值使得数据完整，并让数据为 int 类型。
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df

# %%

# 数据列拆分
# 其中From_to应该为两独立的两列From和To，
# 将From_to依照_拆分为独立两列建立为一个新表。
temp = df['From_To'].str.split('_', expand=True)
temp.columns = ['From', 'To']
temp

# %%

# 字符标准化
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
temp

# %%

# 删除坏数据加入整理好的数据
df = df.drop(columns='From_To')
df = df.join(temp)
df

# %%

# 去除多余字符
print(df['Airline'])
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=True)
df['Airline'] = df['Airline'].str.strip()
df['Airline']

# %%

# 字符标准化
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
temp

# %%

# 格式规范
delays = df['RecentDelays'].apply(pd.Series)
delays.columns = ['delay_{}'.format(n)
                  for n in range(1, len(delays.columns) + 1)]
df = df.drop(columns='RecentDelays').join(delays)
df

# %%

# 数据预处理
# 信息区间划分
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Candy', 'Dany', 'Ella', 'Frank', 'Grace', 'Jenny'],
                   'grades': [58, 83, 79, 65, 93, 45, 61, 88]})


def choice(x):
    if x > 60:
        return 1
    else:
        return 0


df.grades = pd.Serise(map(lambda x: choice(x), df.grades))
df

# %%

# 95. 数据去重
# 一个列为A的 DataFrame 数据，如下图所示
# 尝试将 A 列中连续重复的数据清除。
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 3, 7]})
df.loc[df['A'].shift() != df['A']]


# %%

# 数据归一化

def z_score(df):
    y = df.sub(df.min()) / (df.max() - df.min())
    return y


df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
z_score(df)

# %%

# Pandas 绘图操作
# Series 可视化
ts = pd.Series(np.random.randn(100), index=pd.date_range('today', periods=100, freq='D'))
ts = ts.cumsum()
ts.plot()

# %%

# 折线图
df = pd.DataFrame(np.random.randn(100, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()

# %%

# 散点图
df = pd.DataFrame({'xs': [1, 5, 2, 8, 1],
                   'ys': [4, 2, 1, 9, 6]})
df = df.cumsum()
df.plot.scatter('xs', 'ys', color='red', marker='*')

# %%

# DataFrame 柱形图
df = pd.DataFrame({"revenue": [57, 68, 63, 71, 72, 90, 80, 62, 59, 51, 47, 52],
                   "advertising": [2.1, 1.9, 2.7, 3.0, 3.6, 3.2, 2.7, 2.4, 1.8, 1.6, 1.3, 1.9],
                   "month": range(12)})
ax = df.plot.bar('month', 'revenue', color='yellow')
df.plot('month', 'advertising', secondary_y=True, ax=ax)
