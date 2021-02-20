import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# %%
'第一期 Pandas基础'
# 1.将下面的字典创建为DataFrame

data = {"grammer": ["Python", "C", "Java", "GO", np.nan, "SQL", "PHP", "Python"],
        "score": [1, 2, np.nan, 4, 5, 6, 7, 10]}

df = pd.DataFrame(data)
print(df)

# %%
# 2.提取含有字符串"Python"的行
# 方法1
print(df[df['grammer'] == 'Python'])

# 方法2
res = df['grammer'].str.contains("Pyt")
res.fillna(value=False, inplace=True)
print(df[res])

# %%
# 3.输出df的所有列名
print(df.columns)

# %%
# 4.修改第二列列名为'popularity'
df.rename(columns={'score': 'popularity'}, inplace=True)
print(df)

# %%
# 5.统计grammer列中每种编程语言出现的次数¶
df['grammer'].value_counts()

# %%
# 6.将空值用上下值的平均值填充
val_mean = df['popularity'].mean()
df['popularity'].fillna(value=val_mean, inplace=True)
print(df)

# %%
# 7.提取popularity列中值大于3的行
print(df[df['popularity'] > 3])

# %%
# 8.按照grammer列进行去除重复值
df2 = df['grammer'].drop_duplicates()
print(df2)

# %%
# 9.计算popularity列平均值
print(df['popularity'].mean())

# %%
# 10.将grammer列转换为list
df_list = df['grammer'].to_list()
print(df_list)

# %%
# 11.将DataFrame保存为EXCEL
df.to_excel('temp.xlsx', )

# %%
# 12.查看数据行列数
print(df.shape)

# %%
# 13.提取popularity列值大于3小于7的行
print(df[(df['popularity'] > 3) & (df['popularity'] < 7)])

# %%
# 14.交换两列位置

# 方法1,删除再插入
temp = df['popularity']
df.drop(labels=['popularity'], axis=1, inplace=True)
df.insert(0, 'popularity', temp)
print(df)

# 方法2,
cols = df.columns[[1, 0]]
df = df[cols]
print(df)

# %%
# 15.提取popularity列最大值所在行
print(df[df['popularity'] == df['popularity'].max()])

# %%
# 16.查看最后5行数据
print(df.tail(5))

# %%
# 17.删除最后一行数据

df2 = df.drop(labels=len(df) - 1)
print(df2)

# %%
# 18.添加一行数据['Perl',6.6]
# append 不支持原地修改
row = {'grammer': 'Perl', 'popularity': 6.6}
df = df.append(row, ignore_index=True)
print(df)

# %%
# 19.对数据按照"popularity"列值的大小进行排序
df.sort_values(by='popularity', ascending=False, inplace=True)
print(df)

# %%
# 20.统计grammer列每个字符串的长度

# 注意NAN值
df['grammer'].fillna('R', inplace=True)
df['grammer'].apply(lambda x: len(x))


def lenstr(x):
    return len(x)


df['grammer'].map(lenstr)

# %%
'第二期 Pandas数据处理'
# 21.读取本地EXCEL数据
file_path = r'C:\Users\bolat\Desktop\file\pandas120.xlsx'
df = pd.read_excel(file_path)

# %%
# 22.查看df数据前5行
print(df.head(5))

# %%
# 23.将salary列数据转换为最大值与最小值的平均值

# 方法1,使用apply函数
# 注意,func内的方法和func外使用时存在差别.
df = pd.read_excel(file_path)


def func(t):
    t1 = t['salary'].split('-')
    left, right = [int(x.strip('k')) for x in t1]
    print(left, right)
    r = round((left + right) / 2 * 1000, 1)
    t['salary'] = r
    return t


df = df.apply(func, axis=1)
print(df)
# 方法2 iterrows + 正则
df = pd.read_excel(file_path)
for index, row in df.iterrows():
    nums = re.findall('\d+', row[2])
    df.iloc[index, 2] = (int(nums[0]) + int(nums[1])) / 2 * 1000
print(df)

# %%
# 24.将数据根据学历进行分组并计算平均薪资

df['salary'] = df['salary'].astype(float)
print(df.groupby(by='education', ).mean())
# %%
# 25.将createTime列时间转换为月-日
for i in range(len(df)):
    df.iloc[i, 0] = df.iloc[i, 0].to_pydatetime().strftime('%m-%d')
print(df.head(5))

df.groupby('createTime').sum()

# %%
'''26.查看索引、数据类型和内存信息'''
df.info()

# %%
# 27.查看数值型列的汇总统计
df.describe()

# %%
'''28.新增一列根据salary将数据分为三组'''
bins = [0, 5000, 20000, 50000]
group_names = ['low', 'medium', 'high']
df['categories'] = pd.cut(df['salary'], bins=bins, labels=group_names)
print(df)

# %%
# 26.查看索引、数据类型和内存信息
df.sort_values(by='salary', inplace=True, ascending=False)
print(df)

# %%
# 30.取出第33行数据
print(df.loc[33])

# %%
# 31.计算salary列的中位数
df['salary'].median()
np.median(df['salary'])

# %%
# 32.绘制薪资水平频率分布直方图
df['salary'].plot(kind='hist')
plt.show()

# %%
# 33.绘制薪资水平密度曲线
df['salary'].plot(kind='kde', xlim=(df['salary'].min(), df['salary'].max()))
plt.show()

# %%
# 34.删除最后一列categories
# def df['categories']
# or
df.drop(columns='categories', inplace=True)

# %%
# 35.将df的第一列与第二列合并为新的一列¶
df['test'] = df.iloc[:, 0] + df.iloc[:, 1]
print(df)
# df.iloc[:, 0]

# %%
# 36.将education列与salary列合并为新的一列
'#备注：salary为int类型，操作与35题有所不同'

df['temp'] = df['education'] + df['salary'].map(str)
print(df)

# %%
# 37.计算salary最大值与最小值之差
'注意salary前的[]'
df[['salary']].apply(lambda x: x.max() - x.min())

# %%
# 38.将第一行与最后一行拼接
pd.concat([df[0:1], df[-2:-1]], axis=0)

# %%
# 39.将第8行数据添加至末尾
df.append(df.loc[7])

# %%
# 40.查看每列的数据类型
print(df.dtypes)

# %%
# 41.将createTime列设置为索引
df.set_index('createTime', inplace=True)
print(df)

# %%
# 42.生成一个和df长度相同的随机数dataframe
dfr = pd.DataFrame(np.random.randint(1, 10, len(df)))
print(dfr)

# %%
# 43.将上一题生成的dataframe与df合并
'注:如果按日期为索引的话则无法合并'
df2 = df
df2['date'] = df2.index
df2['temp'] = range(len(df2))
df2 = df2.set_index('temp')
df2 = pd.concat([df2, dfr], axis=1)
print(df2)

# %%
# 44.生成新的一列new为salary列减去之前生成随机数列

df2['new'] = df2['salary'] - df2[0]
print(df2)

# %%
# 45.检查数据中是否含有任何缺失值
df.isna().any()
# df.isna().all()

# %%
# 46.将salary列类型转换为浮点数
df['salary'] = df['salary'].astype(float)

# %%
# 47.计算salary大于10000的次数¶
print(len(df[df['salary'] > 10000]))

# %%
# 48.查看每种学历出现的次数
print(df['education'].value_counts())

# %%
# 49.查看education列共有几种学历
print(df['education'].drop_duplicates())
print(df['education'].unique())

# %%
# 50.提取salary与new列的和大于60000的最后3行
# 方案1
df_temp = df2[['salary', 'new']]
row_sums = df_temp.apply(np.sum, axis=1)
res = df2.iloc[np.where(row_sums > 60000)][-3:]
print(res)

# 方案2
df2['temp'] = df2['salary'] + df2['new']
print(df2[df2['temp'] > 60000][-3:])

# %%
# 第三期 金融数据处理
# 51.使用绝对路径读取本地Excel数据
file_path = r'C:\Users\bolat\Desktop\file\600000.SH.xls'
df_financial = pd.read_excel(file_path)

# %%
# 52.查看数据前三行
df_financial.head(3)

# %%
# 53.查看每列数据缺失值情况
df_financial.isnull().sum()

# %%
# 54.提取日期列含有空值的行¶
print(df_financial[df_financial['日期'].isnull()].index)

# %%
# 55.输出每列缺失值具体行数
for colname in df_financial.columns:
    idx = df_financial[colname][df_financial[colname].isnull() == True].index.to_list()
    print('col: {}, 第{}行位置存在缺失值'.format(colname, idx))

# %%
# 56.删除所有存在缺失值的行
'''
备注
axis：0-行操作（默认），1-列操作
how：any-只要有空值就删除（默认），all-全部为空值才删除
inplace：False-返回新的数据集（默认），True-在原数据集上操作
'''
df_financial.dropna(axis=0, how='any', inplace=True)

# %%
# 57.绘制收盘价的折线图

plt.style.use('seaborn-darkgrid')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.rc('font', size=6)  # 设置图中字体和大小
# plt.rc('figure', figsize=(4, 3), dpi=144)  # 设置图的大小

df_financial['收盘价(元)'].plot()
plt.show()

# %%
# 58.同时绘制开盘价与收盘价
df_financial[['开盘价(元)', '收盘价(元)']].plot()
plt.show()

# %%
# 59.绘制涨跌幅的直方图

# df_financial['涨跌幅(%)'].plot(kind='hist')
# or
df_financial['涨跌幅(%)'].hist()
plt.show()

# %%
# 60.让直方图更细致
df_financial['涨跌幅(%)'].hist(bins=30)
plt.show()

# %%
# 61.以data的列名创建一个dataframe
temp = pd.DataFrame(columns=df_financial.columns)
print(temp)

# %%
# 62.打印所有换手率不是数字的行
for row in range(len(df_financial['换手率(%)'])):
    if type(df_financial.loc[row, '换手率(%)']) != float:
        temp.append(df_financial.loc[row])
print(temp)

# %%
# 63.打印所有换手率为--的行
print(df_financial[df_financial['换手率(%)'].isin(['--'])])

# %%
# 64.重置data的行号
df_financial.reset_index(inplace=True)

# %%
# 65.删除所有换手率为非数字的行
temp_list = []
for i in range(len(df_financial['换手率(%)'])):
    if type(df_financial.loc[i, '换手率(%)']) != float:
        temp_list.append(i)
df_financial.drop(labels=temp_list, inplace=True)
print(df_financial)

# %%
# 66.绘制换手率的密度曲线
df_financial['换手率(%)'].plot(kind='kde')
plt.show()

# %%
'67.计算前一天与后一天收盘价的差值'
df_financial['收盘价(元)'].diff()

# %%
# 68.计算前一天与后一天收盘价变化率
df_financial['收盘价(元)'].pct_change()

# %%
# 69.设置日期为索引
df_financial.set_index('日期', inplace=True)

# %%
'70.以5个数据作为一个数据滑动窗口，在这个5个数据上取均值(收盘价)'
print(df_financial['收盘价(元)'].rolling(5).mean())

# %%
# 71.以5个数据作为一个数据滑动窗口，计算这五个数据总和(收盘价)
print(df_financial['收盘价(元)'].rolling(5).sum())

# %%
# 72.将收盘价5日均线、20日均线与原始数据绘制在同一个图上
df_financial['收盘价(元)'].plot()
df_financial['收盘价(元)'].rolling(5).mean().plot()
df_financial['收盘价(元)'].rolling(20).mean().plot()
plt.legend()
plt.show()

# %%
# 73.按周为采样规则，取一周收盘价最大值
df_financial['收盘价(元)'].resample('w').max()

# %%
# 74.绘制重采样数据与原始数据
df_financial['收盘价(元)'].plot()
df_financial['收盘价(元)'].resample('w').max().plot()
plt.legend()
plt.show()

# %%
# 75.将数据往后移动5天
df_financial.shift(5)

# %%
# 76.将数据向前移动5天¶
df_financial.shift(-5)

# %%
# 77.使用expending函数计算开盘价的移动窗口均值
'''
DataFrame.expanding(min_periods=1, center=False, axis=0)，
其中参数的意义和rolling一样，只是其不是固定窗口长度，其长度是不断的扩大的。
'''

df_financial['开盘价(元)'].expanding(min_periods=1).mean()

# %%
# 78.绘制上一题的移动均值与原始数据折线图
df_financial['expanding open mean'] = df_financial['开盘价(元)'].expanding(min_periods=1).mean()
df_financial[['expanding open mean', '开盘价(元)']].plot(figsize=(10, 6))
plt.show()

# %%
# 第四期 当Pandas遇上NumPy
# 81.导入并查看pandas与numpy版本
print(pd.__version__)
print(np.__version__)

# %%
# 82.从NumPy数组创建DataFrame
# 备注 使用numpy生成20个0-100随机数
array = np.random.randint(0, 101, 20)
df = pd.DataFrame(array)
print(df)

# %%
# 83.从NumPy数组创建DataFram
# 备注 使用numpy生成20个0-100固定步长的数
array = np.arange(0, 100, 5)
df2 = pd.DataFrame(array)
print(df2)

# %%
# 84.从NumPy数组创建DataFrame
# 备注 使用numpy生成20个指定分布(如标准正态分布)的数
array = np.random.normal(0, 1, 20)
df3 = pd.DataFrame(array)

# %%
# 85.将df1，df2，df3按照行合并为新DataFrame¶
df = pd.concat([df, df2, df3], axis=0)
print(df)

# %%
# 86.将df1，df2，df3按照列合并为新DataFrame
df = pd.concat([df, df2, df3], axis=1)
print(df)

# %%
# 87.查看df所有数据的最小值、25%分位数、中位数、75%分位数、最大值
df.describe()

np.percentile(df, q=[0, 25, 50, 75, 100])

# %%
# 88.修改列名为col1,col2,col3¶
df.columns = ['col1', 'col2', 'col3']

# 也可以用df.rename
# df.rename(columns={})

# %%
# 89.提取第一列中不在第二列出现的数字
print(df['col1'][~df['col1'].isin(df['col2'])])

# %%
# 90.提取第一列和第二列出现频率最高的三个数字

temp = pd.concat([df['col1'], df['col2']], axis=0)
print(temp.value_counts(ascending=False).index[:3])

# %%
# 91.提取第一列中可以整除5的数字位置
print(df['col1'][df['col1'] % 5 == 0].index)

# %%
# 92.计算第一列数字前一个与后一个的差值
print(df['col1'].diff().to_list())

# %%
# 93.将col1,col2,clo3三列顺序颠倒¶
print(df.iloc[:, ::-1])

# %%
# 94.提取第一列位置在1,10,15的数字
print(df.loc[[1, 10, 15], 'col1'])

print(df.iloc[[1, 10, 15], 0])

print(df['col1'].take([1, 10, 15]))

# %%
'95.查找第一列的局部最大值位置'
# 备注 即比它前一个与后一个数字的都大的数字

'满足以上条件的,即全部相减之后,对于任意一个数,如果其-左边>0,-右边>0,即它就是局部最大值'
temp_list = []
for i in range(1, len(df['col1'])-1):
    if df.loc[i, 'col1'] - df.loc[i - 1, 'col1'] > 0 and df.loc[i, 'col1'] - df.loc[i + 1, 'col1'] > 0:
        temp_list.append(i)
print(df['col1'])
print(df.loc[temp_list, 'col1'])

#%%
# 96.按行计算df的每一行均值

df[['col1','col2','col3']].mean(axis=1)

#%%
'97.对第二列计算移动平均值'
# 备注 每次移动三个位置，不可以使用自定义函数

# print(df['col2'])
df['col2'].rolling(3).mean()

#%%
# 98.将数据按照第三列值的大小升序排列¶
df.sort_values(by='col3',ascending=True,inplace=True)

#%%
# 99.将第一列大于50的数字修改为'高'
# df['col1'][df['col1']>50] = '高'
print(df['col1'])

#%%
# 100.计算第二列与第三列之间的欧式距离
np.linalg.norm(df['col2']-df['col3'])