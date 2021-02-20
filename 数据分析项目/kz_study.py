from common import utils as u
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
'''
event_time -购买时间
event_type -行为类别
product_id -产品编号
category_id -产品的类别ID
category_code -产品的类别分类法（代码名称）
brand -品牌名称
price -产品价格
user_id -用户ID
'''

# %%
# 1.读取文件,查看基本信息
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\archive.zip'

df = u.unpack_file_to_df(file_path)
df = df['kz']
u.show_info(df)
print(df.shape)
u.show_na(df)
u.show_duplicated(df)
print(df.describe())

# %%
# 修正各字段
# 1.删除重复记录
df.drop_duplicates(inplace=True, ignore_index=True)
# %%
# 2.修改event_time字段为日期属性,并添加月字段
df['event_time'] = pd.to_datetime(df['event_time'])
df['month'] = df['event_time'].dt.month

# %%
df.info()
print(df.head())

# %%
# 1、进行用户消费趋势分析（按月）
# 调用utils中的函数,修正plt中绘图的错误
u.fix_matplotlib_error()

# %%
df_month = df.groupby('month', as_index=False)
df_month_sum = df_month.sum()

# %%
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
sns.lineplot(x='month', y='price', data=df_month_sum)
plt.title('每月消费总金额')
plt.xticks([i for i in range(1, 13)])
plt.subplot(2, 1, 2)
df_month_count = df_month.count()
sns.lineplot(x='month', y='user_id', data=df_month_count)
plt.title('每月消费人数')
plt.xticks([i for i in range(1, 13)])
plt.show()

# %%
# 品牌消费情况
df1 = df.copy()
df1.set_index('event_time', inplace=True)
df1.drop(columns=['event_time'], inplace=True)
df1.sort_index(inplace=True)
df1.head()
# %%
# plt.text直接受数值型数据,要注意
df_brand = df1.groupby('brand', as_index=False).sum(). \
    sort_values('price', ascending=False)[['brand', 'price']].head(20)
df_brand.reset_index(inplace=True)
x = df_brand.index.to_list()
y = df_brand['price']
sns.barplot(x='brand', y='price', data=df_brand)
plt.xticks(rotation=90)
for a, b in zip(x, y):
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=5)
plt.show()

#%%
