# 加载必要的库
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from warnings import filterwarnings
filterwarnings('ignore')
from sklearn.cluster import KMeans
from common import utils as u
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
import plotly.graph_objs as go

#%%
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\data.zip'
file_dict = u.unpack_file_to_df(file_path)
df = file_dict['data']
u.show_info(df)

# %%
# 检查重复记录数量,并去重
u.show_duplicated(df)

# %%
# 检查NA值
u.show_na(df)

# %%
# 处理异常,缺失值数据
print(df.describe())
print(len(df))
di = df[df['UnitPrice'] < 0].index
df.drop(index=[di[i] for i in range(len(di))], inplace=True)
print(len(df))

df = df[(df['UnitPrice'] >= 0) & (df['Quantity'] > 0)]

# %%
# 缺失值处理
df.isna().sum()

# 统计缺失值占比
df.isna().sum() / df.shape[0] * 100

# 删除CustomerID为空的数据
df = df[~df['CustomerID'].isnull()]

# %%
# 把InvoiceDate转换为datetime类型
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype('str')

# %%
# 查看数据日期区间（需要用到最后的交易时间统计客户最后一次交易的时间距离现在的天数)
print('最大日期是：', df['InvoiceDate'].max())
print('最小日期是：', df['InvoiceDate'].min())

# %%
# 数据分析
# 数据准备
df['sales'] = df['Quantity'] * df['UnitPrice']

# 减少重复数据
df_f = df
df_f.drop_duplicates(subset=['InvoiceNo', 'CustomerID'], keep='first', inplace=True)

# 计算购买频率
frequency_df = df_f.groupby('CustomerID', as_index=False)['InvoiceNo'].count()
frequency_df.rename(columns={'InvoiceNo': 'frequency'}, inplace=True)
frequency_df.set_index('CustomerID', drop=True, inplace=True)
df_rm = df.groupby('CustomerID').agg({'sales': np.sum, 'InvoiceDate': np.max})
'''
通过最后一次的交易日期计算出客户最近一次下单距离2012-01-01的天数（2012-01-01，一般会用当天的
日期但由于数据是12年以前的所以这里直接用2012-01-01减去最大日期得到想要距离天数）
'''
df_rm['Datediff'] = (pd.to_datetime('2012-01-01') - df_rm['InvoiceDate']).dt.days

# 删除InvoiceDate字段列
df_rm.drop(columns=['InvoiceDate'], inplace=True)
df_rm.head()

# %%
df_rfm = pd.merge(df_rm, frequency_df, on='CustomerID')
print(df_rfm.head())

# %%
# 3)数据可视化
u.fix_matplotlib_error()
sns.pairplot(df_rfm, diag_kind='hist')
plt.show()

# %%
# 2）单独拿出来看分布直方图
plt.figure(0, figsize=(12, 6))
i = 0
for c in df_rfm.columns:
    i += 1
    plt.subplot(1, 3, i)
    sns.distplot(df_rfm[c], bins=30)
    plt.title('{} 直方图'.format(c))
plt.show()

# %%

# 3.RFM模型
c = 8
clf = KMeans(n_clusters=c)
clf.fit(df_rfm)

rmd = df_rfm['Datediff'].mean()
df_rfm['Datediff'] = df_rfm['Datediff'].astype(float)
fmd = df_rfm['frequency'].mean()
df_rfm['frequency'] = df_rfm['frequency'].astype(float)
mmd = df_rfm['sales'].mean()
df_rfm['sales'] = df_rfm['sales'].astype(float)
print(rmd, fmd, mmd)


# %%
def customer_type(frame):
    _customer_type = []
    for i in range(len(frame)):
        if frame.iloc[i, 1] <= rmd and frame.iloc[i, 2] >= fmd and frame.iloc[i, 0] >= mmd:
            _customer_type.append('重要价值用户')
        elif frame.iloc[i, 1] > rmd and frame.iloc[i, 2] >= fmd and frame.iloc[i, 0] >= mmd:
            _customer_type.append('重要唤回用户')
        elif frame.iloc[i, 1] <= rmd and frame.iloc[i, 2] < fmd and frame.iloc[i, 0] >= mmd:
            _customer_type.append('重要深耕用户')
        elif frame.iloc[i, 1] > rmd and frame.iloc[i, 2] < fmd and frame.iloc[i, 0] >= mmd:
            _customer_type.append('重要挽留用户')
        elif frame.iloc[i, 1] <= rmd and frame.iloc[i, 2] >= fmd and frame.iloc[i, 0] < mmd:
            _customer_type.append('潜力用户')
        elif frame.iloc[i, 1] > rmd and frame.iloc[i, 2] >= fmd and frame.iloc[i, 0] < mmd:
            _customer_type.append('一般维持用户')
        elif frame.iloc[i, 1] <= rmd and frame.iloc[i, 2] < fmd and frame.iloc[i, 0] < mmd:
            _customer_type.append('新用户')
        elif frame.iloc[i, 1] > rmd and frame.iloc[i, 2] < fmd and frame.iloc[i, 0] < mmd:
            _customer_type.append('流失用户')
    frame['classification'] = _customer_type


customer_type(df_rfm)

# %%
print('不同类型的客户总数：')
print('--------------------')
df_rfm.groupby('classification').size().reset_index(name='客户数')

print('不同类型的客户消费总额：')
print('--------------------')
df_rfm.groupby('classification')['sales'].sum().reset_index(name='金额')

# %%
# 4)可视化不同类型客户数量
sns.countplot(y='classification', order=df_rfm['classification'].value_counts().index,
              data=df_rfm, palette='viridis')
plt.title('不同类型的客户总数')
plt.show()

# 5）不同类型的客户消费份额
plt.figure(1, figsize=(10, 10))
sales = df_rfm.groupby('classification')['sales'].sum()
labels = sales.index
plt.pie(x=sales, labels=labels, autopct='%1.1f%%',
        wedgeprops={'width': .35, 'edgecolor': 'w'},
        pctdistance=.85)
plt.title('不同类型的客户消费份额', fontsize=20)
plt.axis('off')
plt.show()

# %%
# 4）方法二：假设不规定8个分类利用模型来选择最优分类，利用最近交易间隔，交易金额进行细分
X = df_rfm[['sales', 'frequency', 'Datediff']].iloc[:, :].values
inertia = []
for n in range(1, 11):
    algorithm = (KMeans(n_clusters=n, max_iter=300, tol=0.0001, random_state=1, algorithm='elkan'))
    algorithm.fit(X)
    inertia.append(algorithm.inertia_)

algorithm = (KMeans(n_clusters=5, n_init=10, max_iter=300,
                    tol=0.0001, random_state=111, algorithm='elkan'))
algorithm.fit(X)
labels3 = algorithm.labels_
centroids3 = algorithm.cluster_centers_

df_rfm['label3'] = labels3
trace1 = go.Scatter3d(
    x=df_rfm['sales'],
    y=df_rfm['Datediff'],
    z=df_rfm['frequency'],
    mode='markers',
    marker=dict(
        color=df_rfm['label3'],
        size=10,
        line=dict(
            color=df_rfm['label3'],
            #             width= 10
        ),
        opacity=0.8
    )
)
data = [trace1]
layout = go.Layout(
    #     margin=dict(
    #         l=0,
    #         r=0,
    #         b=0,
    #         t=0
    #     )
    height=800,
    width=800,
    title='Sales  VS  DateDiff  VS  Frequency',
    scene=dict(
        xaxis=dict(title='Sales'),
        yaxis=dict(title='DateDiff'),
        zaxis=dict(title='Frequency')
    )
)
fig = go.Figure(data=data, layout=layout)
