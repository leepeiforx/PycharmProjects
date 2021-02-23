import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

import common.time as t
import common.utils as ut

# %%

# 读取数据
file_path = r'数据分析项目/database/uk_sales.zip'
df = pd.read_csv(file_path)

# 数据预处理
# print(ut.show_na(df))
# print(ut.show_info(df))
# print(ut.show_duplicated(df))
'''
经查,
    数据Description,CustomerID字段存在缺失值,其中CustomerID字段缺失值超过20%,考虑到需要使用RFM模型,涉及到UID,
    所以UID缺失的记录予以删除;Description字段因为与该项目目的无关,考虑将缺省的记录不作处理
    UnitPrice,Quantity字段存在异常值,删除相关异常记录
'''
df = df[~df['CustomerID'].isna()]  # 剔除ID为NA的数据
df = df[(df['Quantity'] >= 0) & (df['UnitPrice'] >= 0)]  # 剔除UnitPrice,Quantity<0的数据
df = df[~df.duplicated()]  # 剔除重复值
# 修改部分字段属性
df['date_time'] = pd.to_datetime(df['InvoiceDate']).dt.date  # 只保留年月日

frequency = df.groupby('CustomerID')['CustomerID'].count()
recent = df.groupby('CustomerID')['date_time'].max().reset_index()
money = df.groupby('CustomerID')['UnitPrice'].sum()
recent['recent'] = recent['date_time'].apply(t.datediff, endDate='2021-2-23')

recent.index = recent['CustomerID']
recent.drop(columns=['CustomerID', 'date_time'], inplace=True)

df_rfm = pd.merge(recent, frequency, how='outer', left_index=True, right_index=True)
df_rfm = df_rfm.merge(money, left_index=True, right_index=True)
df_rfm.rename(columns={'CustomerID': 'frequency',
                       'UnitPrice': 'money'}, inplace=True)

# %%
ut.fix_matplotlib_error()
sns.pairplot(df_rfm)
plt.show()

plt.figure(1, figsize=(12, 6))
n = 0
for x in ['frequency', 'recent', 'money']:
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    sns.distplot(df_rfm[x], bins=30)
    plt.title('{} 直方图'.format(x))
plt.show()

# %%
# RFM模型
model_min_max = MinMaxScaler()
scaler_min_max = model_min_max.fit_transform(df_rfm)
scaler_min_max = pd.DataFrame(scaler_min_max)
model = KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
               n_clusters=8, n_init=10, n_jobs=None, precompute_distances='auto',
               random_state=None, tol=0.0001, verbose=0)

# %%
predicted_label = model.fit_predict(scaler_min_max)
predicted_label = pd.DataFrame(predicted_label)

# %%
df_rfm_rindex = df_rfm.reset_index(drop=True)
df_rfm_with_label = pd.concat((df_rfm_rindex, predicted_label), axis=1)
df_rfm_with_label.rename(columns={0: 'customer_type'}, inplace=True)

df_rfm_with_label['customer_type'].value_counts()
