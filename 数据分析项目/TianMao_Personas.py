from common import utils as u
import pandas as pd
import gc

# %%
file_path = r'D:\file\DataAnalysis\mydata9388.zip'
df_orginal = pd.read_csv(file_path)

# %%
# 数据量过大,为了提高运行效率,所以随机抽取2%的数据作为处理的样本(pass)
df_sample = df_orginal.sample(frac=.02, random_state=0)

# %%
# 回收内存
# del df_orginal
# gc.collect()

# %%
# 检查数据的字段特征,描述性统计,
print(u.show_info(df_sample))
# 将time字段属性更改为日期类型
df_orginal['time'] = pd.to_datetime(df_orginal['time'], format='%Y-%m-%d %H')

# %%
# 缺省值情况
print(u.show_na(df_sample))
# user_geohash字段缺省值比例过高,考虑删除该字段
df_orginal.drop(columns=['user_geohash'], inplace=True)

# %%
# 日期值处理
# 插入一个字段,将时间分割为凌晨,上午,中午,下午,晚上
df_orginal['hour'] = pd.cut(df_orginal['time'].dt.hour, bins=[-1, 5, 10, 13, 18, 24],
                            labels=['凌晨', '上午', '中午', '下午', '晚上'])

# %%
# 生成用户标签表，制作好的标签都加入这个表中
users = df_orginal['user_id'].unique()
labels = pd.DataFrame(users, columns=['user_id'])

# %%
# 用户行为标签
# 用户浏览活跃时间段(按每个用户id,每个时间段 分组计数统计item_id)
time_browse = df_orginal[df_orginal['behavior_type'] == 1] \
    .groupby(['user_id', 'hour'])['item_id'].count().reset_index()

time_browse.rename(columns={'item_id': 'hour_counts'}, inplace=True)

# %%
# 统计每个用户浏览次数最多的时段
time_browse_max = time_browse.groupby('user_id')['hour_counts'].max().reset_index()
time_browse_max.rename(columns={'hour_counts': 'read_counts_max'}, inplace=True)
time_browse = pd.merge(time_browse, time_browse_max, how='left', on='user_id')

# %%
# 选取各用户浏览次数最多的时段，如有并列最多的时段，用逗号连接
time_browse_hour = time_browse[time_browse['hour_counts'] == time_browse['read_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x))['hour']
time_browse_hour.head()

# 将用户浏览活跃时间段加入到用户标签表中
labels = pd.merge(labels, time_browse_hour, on='user_id', how='left')
labels.rename(columns={'hour': 'time_browse'}, inplace=True)

# %%
# 用户购买活跃时间段
time_buy = df_orginal[df_orginal['behavior_type'] == 4].groupby(['user_id', 'hour'])['item_id'].count().reset_index()
time_buy.rename(columns={'item_id': 'hour_counts'}, inplace=True)
time_buy_max = time_buy.groupby('user_id').max()['hour_counts'].reset_index()
time_buy_max.rename(columns={'hour_counts': 'hour_counts_max'}, inplace=True)
time_buy = pd.merge(time_buy, time_buy_max, how='left', on='user_id')
time_buy_hour = time_buy[time_buy['hour_counts'] == time_buy['hour_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x))['hour']

# %%
labels = pd.merge(labels, time_buy_hour, how='left', on='user_id')
labels.rename(columns={'hour': 'time_buy'}, inplace=True)

# %%
# 回收变量及内存
del time_browse
del time_buy
del time_browse_hour
del time_browse_max
del time_buy_hour
del time_buy_max
gc.collect()

# %%
# 关于类目的用户行为
# 浏览
df_orginal_browse = df_orginal.loc[df_orginal['behavior_type'] == 1,
                                   ['user_id', 'item_id', 'item_category']].reset_index()
# 收藏
df_orginal_collect = df_orginal.loc[df_orginal['behavior_type'] == 2,
                                    ['user_id', 'item_id', 'item_category']].reset_index()
# 加购物车
df_orginal_cart = df_orginal.loc[df_orginal['behavior_type'] == 3,
                                 ['user_id', 'item_id', 'item_category']].reset_index()
# 购买
df_orginal_buy = df_orginal.loc[df_orginal['behavior_type'] == 4,
                                ['user_id', 'item_id', 'item_category']].reset_index()

# %%
# 浏览最多的类目(计算每个用户在每个分类下的浏览数量)
df_cate_most_browse = df_orginal_browse. \
    groupby(['user_id', 'item_category'])['item_id'].count().reset_index()
df_cate_most_browse.rename(columns={'item_id': 'item_category_counts'}, inplace=True)

# 过滤数据,浏览的数量至少为2次才计入
df_cate_most_browse = df_cate_most_browse[df_cate_most_browse['item_category_counts'] > 1]

df_cate_most_browse_max = df_cate_most_browse.groupby('user_id')['item_category_counts'].max().reset_index()
df_cate_most_browse_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_browse = pd.merge(df_cate_most_browse, df_cate_most_browse_max, how='left', on='user_id')
df_cate_most_browse['item_category'] = df_cate_most_browse['item_category'].astype('str')

# 选取各用户浏览最多的类目,如有并列最多的类目,则用逗号分隔开,
df_cate_most_browse = df_cate_most_browse[df_cate_most_browse['item_category_counts'] ==
                                          df_cate_most_browse['item_category_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x)).reset_index()

labels = labels.merge(df_cate_most_browse, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_browse'}, inplace=True)

# %%
# 收藏最多的类目
# 逻辑同访问最多一样
df_cate_most_collect = df_orginal_collect. \
    groupby(['user_id', 'item_category'])['item_id'].count().reset_index()
df_cate_most_collect.rename(columns={'item_id': 'item_category_counts'}, inplace=True)

# 过滤数据,浏览的数量至少为2次才计入
df_cate_most_collect = df_cate_most_collect[df_cate_most_collect['item_category_counts'] > 1]

df_cate_most_collect_max = df_cate_most_collect.groupby('user_id')['item_category_counts'].max().reset_index()
df_cate_most_collect_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_collect = pd.merge(df_cate_most_collect, df_cate_most_collect_max, how='left', on='user_id')
df_cate_most_collect['item_category'] = df_cate_most_collect['item_category'].astype('str')

# 选取各用户收藏最多的类目,如有并列最多的类目,则用逗号分隔开,
df_cate_most_collect = df_cate_most_collect[df_cate_most_collect['item_category_counts'] ==
                                            df_cate_most_collect['item_category_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x)).reset_index()

labels = labels.merge(df_cate_most_collect, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_collect'}, inplace=True)

# %%
# 加购物车最多的类目
# 逻辑同访问最多一样
df_cate_most_cart = df_orginal_cart. \
    groupby(['user_id', 'item_category'])['item_id'].count().reset_index()
df_cate_most_cart.rename(columns={'item_id': 'item_category_counts'}, inplace=True)

# 过滤数据,浏览的数量至少为2次才计入
df_cate_most_cart = df_cate_most_cart[df_cate_most_cart['item_category_counts'] > 1]

df_cate_most_cart_max = df_cate_most_cart.groupby('user_id')['item_category_counts'].max().reset_index()
df_cate_most_cart_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_cart = pd.merge(df_cate_most_cart, df_cate_most_cart_max, how='left', on='user_id')
df_cate_most_cart['item_category'] = df_cate_most_cart['item_category'].astype('str')

# 选取各用户收藏最多的类目,如有并列最多的类目,则用逗号分隔开,
df_cate_most_cart = df_cate_most_cart[df_cate_most_cart['item_category_counts'] ==
                                      df_cate_most_cart['item_category_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x)).reset_index()

labels = labels.merge(df_cate_most_cart, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_cart'}, inplace=True)

# %%
# 加购物车最多的类目
# 逻辑同访问最多一样
df_cate_most_buy = df_orginal_buy. \
    groupby(['user_id', 'item_category'])['item_id'].count().reset_index()
df_cate_most_buy.rename(columns={'item_id': 'item_category_counts'}, inplace=True)

# 过滤数据,浏览的数量至少为2次才计入
df_cate_most_buy = df_cate_most_buy[df_cate_most_buy['item_category_counts'] > 1]

df_cate_most_buy_max = df_cate_most_buy.groupby('user_id')['item_category_counts'].max().reset_index()
df_cate_most_buy_max.rename(columns={'item_category_counts': 'item_category_counts_max'}, inplace=True)
df_cate_most_buy = pd.merge(df_cate_most_buy, df_cate_most_buy_max, how='left', on='user_id')
df_cate_most_buy['item_category'] = df_cate_most_buy['item_category'].astype('str')

# 选取各用户收藏最多的类目,如有并列最多的类目,则用逗号分隔开,
df_cate_most_buy = df_cate_most_buy[df_cate_most_buy['item_category_counts'] ==
                                    df_cate_most_buy['item_category_counts_max']]. \
    groupby('user_id').aggregate(lambda x: ','.join(x)).reset_index()

labels = labels.merge(df_cate_most_buy, how='left', on='user_id')
labels.rename(columns={'item_category': 'cate_most_buy'}, inplace=True)

# %%
del df_orginal_buy
del df_orginal_cart
del df_orginal_collect
del df_orginal_browse
del df_cate_most_browse
del df_cate_most_collect
del df_cate_most_buy
del df_cate_most_cart
del df_cate_most_browse_max
del df_cate_most_collect_max
del df_cate_most_cart_max
del df_cate_most_buy_max
del df_cate_most_browse
gc.collect(0)

# %%
'''
30天用户行为
数据集中的数据正好是一个月，30天的数据即整个数据集的数'''
df_count_30_buy = df_orginal[df_orginal['behavior_type'] == 4]. \
    groupby('user_id')['item_id'].count().reset_index()

labels = pd.merge(labels, df_count_30_buy, how='left', on='user_id')
labels.rename(columns={'item_id': 'counts_30_buy'}, inplace=True)

# %%
# 近30天加购次数
df_count_30_cart = df_orginal[df_orginal['behavior_type'] == 3]. \
    groupby('user_id')['item_id'].count().reset_index()

labels = pd.merge(labels, df_count_30_buy, how='left', on='user_id')
labels.rename(columns={'item_id': 'counts_30_cart'}, inplace=True)

# %%
# 近30天活跃天数
# 对用户进行分组，统计活跃的天数，包括浏览、收藏、加购、购买
df_orginal['date'] = df_orginal['time'].dt.date
count_30_active = df_orginal.groupby('user_id')['date'].nunique().reset_index()
# %%
labels = pd.merge(labels, count_30_active, how='left', on='user_id')
labels.rename(columns={'date': 'counts_30_active'}, inplace=True)

# %%清空内存
del df_count_30_cart
del df_count_30_buy
del count_30_active
del users
gc.collect()

# %%
# 7天用户行为
# 7日内购买
df_near_7 = df_orginal[df_orginal['time'] > '2014-12-11']

count_7_buy = df_near_7[df_near_7['behavior_type'] == 4]. \
    groupby('user_id')['item_id'].count().reset_index()

count_7_buy.rename(columns={'item_id': 'count_7_buy'}, inplace=True)
labels = pd.merge(labels, count_7_buy, how='left', on='user_id')

# %%
# 7日内加购
count_7_cart = df_near_7[df_near_7['behavior_type'] == 3]. \
    groupby('user_id')['item_id'].count().reset_index()

count_7_cart.rename(columns={'item_id': 'count_7_cart'}, inplace=True)
labels = pd.merge(labels, count_7_cart, how='left', on='user_id')

# %%
# 近7天活跃天数
count_7_active = df_near_7.groupby('user_id')['time'].nunique().reset_index()

count_7_active.rename(columns={'time': 'count_7_active'}, inplace=True)
labels = pd.merge(labels, count_7_active, how='left', on='user_id')

# %%
# 回收内存
del count_30_active
del count_7_active
del count_7_cart
del count_7_buy
del df_count_30_buy
del df_count_30_cart
gc.collect()

# %%
df_orginal['date'] = pd.to_datetime(df_orginal['date'], format='%Y-%m-%d')
df_orginal['date'] = df_orginal['date'].dt.date
days_browse = df_orginal[df_orginal['behavior_type'] == 1].groupby('user_id')['date'].max().reset_index()
from common.time import datediff

days_browse['date'] = days_browse['date'].apply(lambda x: datediff(x, '2014-12-19'))
labels = labels.merge(days_browse, how='left', on='user_id')
labels.rename(columns={'date': 'days_browse'}, inplace=True)

# %%
# 上次加购距今天数
days_cart = df_orginal[df_orginal['behavior_type'] == 3] \
    .groupby('user_id')['date'].max().reset_index()
days_cart['date'] = days_cart['date'].apply(lambda x: datediff(x, '2014-12-19'))

days_cart.rename(columns={'date': 'days_cart'}, inplace=True)

labels = labels.merge(days_cart, how='left', on='user_id')

# %%
# 上次购买距今天数
days_buy = df_orginal[df_orginal['behavior_type'] == 4] \
    .groupby('user_id')['date'].max().reset_index()
days_buy['date'] = days_buy['date'].apply(lambda x: datediff(x, '2014-12-19'))

days_buy.rename(columns={'date': 'days_buy'}, inplace=True)

labels = labels.merge(days_buy, how='left', on='user_id')

# %% 回收内存
del days_browse
del days_buy
del days_cart
del count_7_active
del count_7_cart
del count_7_buy
del days_buy
del df_near_7
gc.collect()

# %%
# 最近两次购买间隔天数
df_interval_buy = df_orginal[df_orginal['behavior_type'] == 4] \
    .groupby(['user_id', 'date'])['item_id'].count().reset_index()
interval_buy = df_interval_buy.groupby('user_id')['date'] \
    .apply(lambda x: x.sort_values().diff(1).dropna().head(1)).reset_index()
interval_buy['date'] = interval_buy['date'].dt.days
interval_buy.drop(columns=['level_1'], inplace=True)
interval_buy.rename(columns={'date': 'interval_buy'}, inplace=True)

labels = labels.merge(interval_buy, how='left', on='user_id')

# %%
# 是否浏览未下单
df_browse_buy = df_orginal.loc[(df_orginal['behavior_type'] == 1) | (df_orginal['behavior_type'] == 4),
                               ['user_id', 'item_id', 'behavior_type', 'time']]
browse_not_buy = pd.pivot_table(df_browse_buy, index=['user_id', 'item_id'], columns='behavior_type',
                                values='time', aggfunc='count')

browse_not_buy.columns = ['browse', 'buy']
browse_not_buy.fillna(0, inplace=True)

browse_not_buy['browse_not_buy'] = 0

browse_not_buy.loc[(browse_not_buy['browse'] > 0) & (browse_not_buy['buy'] == 0), 'browse_not_buy'] = 1
browse_not_buy = browse_not_buy.groupby('user_id')['browse_not_buy'].sum().reset_index()

labels = labels.merge(browse_not_buy, how='left', on='user_id')
labels['browse_not_buy'] = labels['browse_not_buy'].apply(lambda x: '是' if x > 0 else '否')

# %%
# 是否加购未下单
df_cart_buy = df_orginal.loc[(df_orginal['behavior_type'] == 3) | (df_orginal['behavior_type'] == 4),
                             ['user_id', 'item_id', 'behavior_type', 'time']]

cart_not_buy = pd.pivot_table(df_cart_buy, index=['user_id', 'item_id'], columns='behavior_type',
                              values='time', aggfunc='count')

cart_not_buy.columns = ['cart', 'buy']
cart_not_buy.fillna(0, inplace=True)

cart_not_buy['cart_not_buy'] = 0

cart_not_buy.loc[(cart_not_buy['cart'] > 0) & (cart_not_buy['buy'] == 0), 'cart_not_buy'] = 1
cart_not_buy = cart_not_buy.groupby('user_id')['cart_not_buy'].sum().reset_index()

labels = labels.merge(cart_not_buy, how='left', on='user_id')
labels['cart_not_buy'] = labels['cart_not_buy'].apply(lambda x: '是' if x > 0 else '否')

# %%
# 用户属性标签
# 是否复购用户
buy_again = df_orginal[df_orginal['behavior_type'] == 4].groupby('user_id')['item_id'].count().reset_index()
buy_again.rename(columns={'item_id': 'buy_again'}, inplace=True)
labels = labels.merge(buy_again, how='left', on='user_id')
labels['buy_again'] = labels['buy_again'].apply(lambda x: '是' if x > 1 else '否' if x == 1 else '未购买')

# %%
# 访问活跃度
from matplotlib import pyplot as plt

u.fix_matplotlib_error()
user_active_level = labels['counts_30_active'].value_counts().sort_index(ascending=False)
plt.figure(figsize=(10, 9))
user_active_level.plot(kind='line', title='30天内访问次数与访问人数的关系', fontsize=10)
plt.xlabel('访问次数', fontsize=14)
plt.ylabel('访问人数', fontsize=14)
plt.show()

labels['user_active_level'] = '高'
labels.loc[labels['counts_30_active'] <= 16, 'user_active_level'] = '低'
# %%
# 购买活跃度
buy_active_level = labels['counts_30_buy'].value_counts().sort_index(ascending=False)
plt.figure(figsize=(10, 9))
buy_active_level.plot(kind='line', title='30天内购买次数与购买人数的关系', fontsize=10)
plt.xlabel('购买次数', fontsize=14)
plt.ylabel('购买人数', fontsize=14)
plt.show()

labels['buy_active_level'] = '高'
labels.loc[labels['counts_30_buy'] <= 14, 'buy_active_level'] = '低'

# %%
# 购买的品类是否单一
buy_single = df_orginal[df_orginal['behavior_type'] == 4].groupby('user_id')['item_category'].nunique().reset_index()
buy_single.rename(columns={'item_category': 'buy_single'}, inplace=True)
labels = labels.merge(buy_single, how='left', on='user_id')
#
labels['buy_single'].fillna(-1, inplace=True)
labels['buy_single'] = labels['buy_single'].apply(lambda x: '是' if x > 1 else '否' if x == 1 else '未购买')

# %%
# 用户价值分组（RFM）
last_buy_days = labels['days_buy'].value_counts().sort_index()

plt.figure(figsize=(16, 9))
last_buy_days.plot(title='最后一次购买距今天时间差与购买人数的关系', fontsize=18)
plt.xlabel('距离今天时间差(days)', fontsize=14)
plt.ylabel('购买人数', fontsize=14)
plt.show()

labels['buy_days_level'] = '高'
labels.loc[labels['days_buy'] > 8, 'buy_days_level'] = '低'

labels['rfm_values'] = labels['buy_active_level'].str.cat(labels['buy_days_level'])


def trans_value(x):
    if x == '高高':
        return '重要价值客户'
    elif x == '低高':
        return '重要深耕客户'
    elif x == '高低':
        return '重要唤回客户'
    else:
        return '即将流失客户'


labels['rfm'] = labels['rfm_values'].apply(trans_value)
labels.drop(columns=['rfm_values', 'buy_days_level'], inplace=True)

labels['rfm'].value_counts()

# %%
# 结果保存
file_path = r'D:\file\DataAnalysis'
labels.to_csv(file_path + r'\tiammao_personna.csv', encoding='GBK')
print('done')



