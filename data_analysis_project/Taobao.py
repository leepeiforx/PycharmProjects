import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gc

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 读取数据
file_path = r'C:\Users\bolat\Desktop\taobao_persona.csv'
df_orginal = pd.read_csv(file_path)

# 数据预处理
# 数据抽样
# 数据集太大，为了提高运行效率，只随机抽取20%的数据
df = df_orginal.sample(frac=0.2, random_state=1)
df_head = df.head(5)

# 回收内存
del df_orginal
gc.collect

# 缺失值处理
df.info()
df.shape

# 查看各字段缺失值情况
df.isnull().sum()

# 'user_geohash'字段缺失值过多,故将其删除


# 日期及时间字段处理
df.drop(columns='user_geohash', inplace=True)
df.columns
df['date'] = df['time'].str[:10]
df['date'] = pd.to_datetime(df['time'], format='%Y-%m-%d')

df['time'] = df['time'].str[11:]
df['time'] = df['time'].astype('int')

# 将时间段分为'凌晨,上午,中午,下午,晚间'
df['hour'] = pd.cut(df['time'], bins=[-1, 5, 10, 13, 18, 24],
                    labels=['凌晨', '上午', '中午', '下午', '晚间'])

# 制作用户标签表
users = df['user_id'].unique()
labels = pd.DataFrame(users, columns=['user_id'])

# 用户行为标签
time_browse = df[
    df['behavior_type'] == 1].groupby(['user_id', 'hour'])['item_id'] \
    .count().reset_index()
time_browse.rename(columns={'item_id': 'hour_counts'}, inplace=True)

# 统计每个用户浏览次数最多的时段
time_browse_max = time_browse.groupby('user_id')['hour_counts'].max().reset_index()
time_browse_max.rename(columns={'hour_counts': 'read_counts_max'}, inplace=True)

time_browse = pd.merge(time_browse, time_browse_max, how='left', on='user_id')

# 选取各用户浏览次数最多的时段，如有并列最多的时段，用逗号连接
time_browse_hour = time_browse.loc[time_browse['hour_counts'] == time_browse['read_counts_max'], 'hour'] \
    .groupby(time_browse['user_id']).aggregate(lambda x: '.'.join(x)).reset_index()

time_browse_hour.head()

# 将用户浏览活跃时间加入到用户标签中
labels = pd.merge(labels, time_browse_hour, how='left', on='user_id')
labels.rename(columns={'hour': 'time_browers'}, inplace=True)

# 用户购买活跃时间段
time_buy = df[df['behavior_type'] == 4].groupby(['user_id', 'hour'])['item_id'].count().reset_index()
time_buy.rename(columns={'item_id': 'hour_counts'}, inplace=True)
time_buy_max = time_buy.groupby('user_id')['hour_counts'].max().reset_index()
time_buy_max.rename(columns={'hour_counts': 'buy_counts_max'}, inplace=True)
time_buy = pd.merge(time_buy, time_buy_max, how='left', on='user_id')
time_buy_hour = time_buy.loc[time_buy['hour_counts'] == time_buy['buy_counts_max'], 'hour']. \
    groupby(time_buy['user_id']).aggregate(lambda x: '.'.join(x)).reset_index()

# 将用户购买活跃时间段加入到用户标签表中
labels = pd.merge(labels, time_browse_hour, how='left', on='user_id')
labels.rename(columns={'hour': 'time_buy'}, inplace=True)

# 清空中间temp表
try:
    del time_browse
    del time_browse_hour
    del time_browse_max

    del time_buy
    del time_buy_hour
    del time_buy_max
    gc.collect()
except NameError:
    print('...')

# 关于类目的用户行为
df_browse = df.loc[df['behavior_type'] == 1, ['user_id', 'item_id', 'item_category']]
df_collect = df.loc[df['behavior_type'] == 2, ['user_id', 'item_id', 'item_category']]
df_cart = df.loc[df['behavior_type'] == 3, ['user_id', 'item_id', 'item_category']]
df_buy = df.loc[df['behavior_type'] == 4, ['user_id', 'item_id', 'item_category']]

# 浏览最多的类目
# 对用户与类目进行分组，统计浏览次数
df_cate_most_browse = df_browse.groupby(['user_id', 'item_category'])['item_id'].count().reset_index()

df_cate_most_browse.rename(columns={'item_id': 'item_category_count'}, inplace=True)

# 统计每个用户浏览次数最多的类目
df_cate_most_browse_max = df_cate_most_browse.groupby('user_id')['item_category_count'].max().reset_index()
df_cate_most_browse_max.rename(columns={'item_category_count': 'item_category_count_max'}, inplace=True)
df_cate_most_browse = pd.merge(df_cate_most_browse, df_cate_most_browse_max, how='left', on='user_id')

df_cate_most_browse['item_category'] = df_cate_most_browse['item_category'].astype('str')
# 选取各用户浏览次数最多的类目，如有并列最多的类目，用逗号连接
df_cart_browse = df_cate_most_browse.loc[
    df_cate_most_browse['item_category_count'] ==
    df_cate_most_browse['item_category_count_max'], 'item_category']. \
    groupby(df_cate_most_browse['user_id']).aggregate(lambda x: '.'.join(x)).reset_index()

df_cart_browse.rename(columns={'item_category': 'cast_most_browse'}, inplace=True)
df_cart_browse.head()

labels = pd.merge(labels, df_cart_browse, how='left', on='user_id')
labels

# 加购最多的类目
df_cate_most_cart = df_cart.groupby(['user_id', 'item_category']).item_id.count().reset_index()
df_cate_most_cart = df_cart.groupby(['user_id', 'item_category']).item_id.count().reset_index()
df_cate_most_cart.rename(columns={'item_id': 'item_category_counts'}, inplace=True)
df_cate_most_cart_max = df_cate_most_cart.groupby('user_id').item_category_counts.max().reset_index()
df_cate_most_cart_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_cart = pd.merge(df_cate_most_cart, df_cate_most_cart_max, how='left', on='user_id')
df_cate_most_cart['item_category'] = df_cate_most_cart['item_category'].astype(str)
df_cate_cart = df_cate_most_cart.loc[df_cate_most_cart['item_category_counts'] == df_cate_most_cart[
    'item_category_counts_max'], 'item_category'].groupby(df_cate_most_cart['user_id']).aggregate(
    lambda x: ','.join(x)).reset_index()
# %%
labels = pd.merge(labels, df_cate_cart, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_cart'}, inplace=True)

# %%
# 购买最多的类目
# 生成逻辑与浏览最多的类目相同
df_cate_most_buy = df_buy.groupby(['user_id', 'item_category']).item_id.count().reset_index()
df_cate_most_buy = df_buy.groupby(['user_id', 'item_category']).item_id.count().reset_index()
df_cate_most_buy.rename(columns={'item_id': 'item_category_counts'}, inplace=True)
df_cate_most_buy_max = df_cate_most_buy.groupby('user_id').item_category_counts.max().reset_index()
df_cate_most_buy_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_buy = pd.merge(df_cate_most_buy, df_cate_most_buy_max, how='left', on='user_id')
df_cate_most_buy['item_category'] = df_cate_most_buy['item_category'].astype(str)
df_cate_buy = df_cate_most_buy.loc[
    df_cate_most_buy['item_category_counts'] == df_cate_most_buy['item_category_counts_max'], 'item_category'].groupby(
    df_cate_most_buy['user_id']).aggregate(lambda x: ','.join(x)).reset_index()

# %%
labels = pd.merge(labels, df_cate_buy, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_buy'}, inplace=True)

#%%
del df_cart_browse
del df_cate_collect
gc.collect(0)