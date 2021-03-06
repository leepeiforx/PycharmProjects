import os
from datetime import datetime

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import *

from common import utils

# %%
# 读取数距
file_path = r'D:\迅雷下载\python_database\taobao_persona.zip'
df = pd.read_csv(file_path)
# %%
# 数距预处理
# 数距抽样
# 数距集太大，为了提高运行效率，只随机抽取1%的数距作为代码运行数距,随后如果需要再替换为全量数据


# 检查数距情况
# user_geohash字段缺失值过多,
print(utils.show_na(df))
print(utils.show_info(df))
print(utils.show_duplicated(df))

# %%
pd.set_option('display.max_columns', None)  # 显示所有字段数据

df.drop(columns='user_geohash', inplace=True)
df.drop_duplicates(inplace=True)
# 日期及时间字段处理
# 修改time字段的属性
df['time'] = pd.to_datetime(df['time'])
df['date'] = df['time'].dt.date
df['time_hms'] = df['time'].dt.time
df['time_hms'] = df['time_hms'].apply(lambda x: x.hour)
# bins默认为左闭右开区间
# 将时间段分为'凌晨,上午,中午,下午,晚间'
df['hour'] = pd.cut(df['time_hms'], bins=[-1, 5, 10, 13, 18, 24],
                    labels=['凌晨', '上午', '中午', '下午', '晚间'])
# 字段重命名
df.rename(columns={'user_id':       'u_id', 'behavior_type': 'b_type',
                   'item_category': 'item_cls'}, inplace=True)

# 制作用户标签表
users = df['u_id'].unique()
labels = pd.DataFrame(users, columns=['u_id'])

# 用户行为标签
"""
针对dataframe中每行或每列的操作，并且将行或列当作Series，应用的是apply函数
    dataframe.apply(func,axis=0)
针对dataframe中每个元素的操作，应用的是applymap函数,
    dataframe.applymap(func)
针对dataframe中某行或某列的操作，应用的是map函数，
    实际上是series.map。series.map(arg,na_action=None)
针对dataframe中的行或列进行汇总，应用的是aggregate函数，
包括求和，平均，最大，最小
"""


def get_max_label(tab, **kwargs):
    col1 = kwargs['col1']
    col2 = kwargs['col2']
    agg_col = kwargs['agg_col']
    cls = kwargs['cls']

    _df = tab.loc[tab['b_type'] == cls]
    _df_group = _df.groupby([col1, col2])[agg_col].count().reset_index()
    # print(_df_group)
    _df_group_max = _df_group.groupby(col1)[agg_col].max().reset_index()
    _merge_data = pd.merge(_df_group, _df_group_max, on=col1, how='left')
    if isinstance(_merge_data.loc[0, col1], np.int64):
        _merge_data[col2] = _merge_data[col2].astype(str)
    _merge_data = _merge_data.loc[_merge_data.iloc[:, 2] == _merge_data.iloc[:, 3], col2] \
        .groupby(_merge_data[col1]).apply(lambda x: ','.join(x)).reset_index()
    return _merge_data


# 用户浏览/购买活跃时间段
most_view_by_hour = get_max_label(df, cls=1, col1='u_id', col2='hour', agg_col='item_id')
most_buy_by_hour = get_max_label(df, cls=4, col1='u_id', col2='hour', agg_col='item_id')

merge_label = labels.merge(most_view_by_hour, how='left', on='u_id')
merge_label = merge_label.merge(most_buy_by_hour, how='left', on='u_id')
merge_label.rename(columns={'hour_x': '浏览时间', 'hour_y': '购买时间'}, inplace=True)

# 查看每个用户浏览.收藏,加购物车,购买的各类目情况
most_view_by_item = get_max_label(df, cls=1, col1='u_id', col2='item_cls', agg_col='item_id')
most_view_by_item.rename(columns={'item_cls': '浏览类目'}, inplace=True)
most_collect_by_item = get_max_label(df, cls=2, col1='u_id', col2='item_cls', agg_col='item_id')
most_collect_by_item.rename(columns={'item_cls': '收藏类目'}, inplace=True)
most_chart_by_item = get_max_label(df, cls=3, col1='u_id', col2='item_cls', agg_col='item_id')
most_chart_by_item.rename(columns={'item_cls': '加购物车类目'}, inplace=True)
most_buy_by_item = get_max_label(df, cls=4, col1='u_id', col2='item_cls', agg_col='item_id')
most_buy_by_item.rename(columns={'item_cls': '购买类目'}, inplace=True)

merge_label = merge_label.merge(most_view_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_collect_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_chart_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_buy_by_item, how='left', on='u_id')

# 划分间隔时间
# 用户近30天行为
df['date_diff'] = (datetime(2014, 12, 18) - df['time']).dt.days + 1

df_view_30 = df[df['b_type'] == 1].groupby('u_id')['item_id'].count().reset_index()
df_view_30.rename(columns={'item_id': '近30天浏览数'}, inplace=True)
df_collect_30 = df[df['b_type'] == 2].groupby('u_id')['item_id'].count().reset_index()
df_collect_30.rename(columns={'item_id': '近30天收藏数'}, inplace=True)
df_cart_30 = df[df['b_type'] == 3].groupby('u_id')['item_id'].count().reset_index()
df_cart_30.rename(columns={'item_id': '近30天加入购物车数'}, inplace=True)
df_buy_30 = df[df['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
df_buy_30.rename(columns={'item_id': '近30天购买数'}, inplace=True)

# 近30天活跃情况(计算u_id)的date非重复计数
df_active_30 = df.groupby('u_id')['date'].nunique().reset_index()
df_active_30.rename(columns={'date': '活跃天数'}, inplace=True)

merge_label = merge_label.merge(df_view_30, how='left', on='u_id')
merge_label = merge_label.merge(df_collect_30, how='left', on='u_id')
merge_label = merge_label.merge(df_cart_30, how='left', on='u_id')
merge_label = merge_label.merge(df_buy_30, how='left', on='u_id')
merge_label = merge_label.merge(df_active_30, how='left', on='u_id')

# 用户最近7日指数
df_7days = df[df['date_diff'] <= 7]

df_view_7 = df_7days[df_7days['b_type'] == 1].groupby('u_id')['item_id'].count().reset_index()
df_view_7.rename(columns={'item_id': '近7天浏览数'}, inplace=True)
df_collect_7 = df_7days[df_7days['b_type'] == 2].groupby('u_id')['item_id'].count().reset_index()
df_collect_7.rename(columns={'item_id': '近7天收藏数'}, inplace=True)
df_cart_7 = df_7days[df_7days['b_type'] == 3].groupby('u_id')['item_id'].count().reset_index()
df_cart_7.rename(columns={'item_id': '近7天加入购物车数'}, inplace=True)
df_buy_7 = df_7days[df_7days['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
df_buy_7.rename(columns={'item_id': '近7天购买数'}, inplace=True)

# 近30天活跃情况(计算u_id)的date非重复计数
df_active_7 = df_7days.groupby('u_id')['date'].nunique().reset_index()
df_active_7.rename(columns={'date': '7日内活跃天数'}, inplace=True)

merge_label = merge_label.merge(df_view_7, how='left', on='u_id')
merge_label = merge_label.merge(df_collect_7, how='left', on='u_id')
merge_label = merge_label.merge(df_cart_7, how='left', on='u_id')
merge_label = merge_label.merge(df_buy_7, how='left', on='u_id')
merge_label = merge_label.merge(df_active_7, how='left', on='u_id')

# 最后一次行为距今天数
# 上次浏览
df_view_diff = df[df['b_type'] == 1].groupby('u_id')['date_diff'].max().reset_index()
df_view_diff.rename(columns={'date_diff': '上次浏览距今天天数'}, inplace=True)
merge_label = merge_label.merge(df_view_diff, how='left', on='u_id')

# 上次收藏
df_collect_diff = df[df['b_type'] == 2].groupby('u_id')['date_diff'].max().reset_index()
df_collect_diff.rename(columns={'date_diff': '上次收藏距今天天数'}, inplace=True)
merge_label = merge_label.merge(df_collect_diff, how='left', on='u_id')

# 上次加购物车
df_cart_diff = df[df['b_type'] == 3].groupby('u_id')['date_diff'].max().reset_index()
df_cart_diff.rename(columns={'date_diff': '上次加购物车今天天数'}, inplace=True)
merge_label = merge_label.merge(df_cart_diff, how='left', on='u_id')

# 上次购买
df_buy_diff = df[df['b_type'] == 4].groupby('u_id')['date_diff'].max().reset_index()
df_buy_diff.rename(columns={'date_diff': '上次购买距今天天数'}, inplace=True)
merge_label = merge_label.merge(df_buy_diff, how='left', on='u_id')

df['time'] = pd.to_datetime(df['time'])
# 最近两次购买间隔天数
df_interval_buy = df[df['b_type'] == 4].groupby(['u_id', 'date'])['item_id'].count().reset_index()
interval_buy = df_interval_buy.groupby('u_id')['date'].apply(lambda x: x.sort_values().diff(1).dropna().head(1)).reset_index()
interval_buy['date'] = interval_buy['date'].apply(lambda x: x.days)
interval_buy.drop(columns='level_1', inplace=True)
interval_buy.rename(columns={'date': '最近两次购买间隔天数'}, inplace=True)
merge_label = merge_label.merge(interval_buy, how='left', on='u_id')

# 是否浏览未下单
df_b_type = pd.pivot_table(data=df, index=['u_id'], columns=['b_type'],
                           values=['time'], aggfunc='count', fill_value=0)

df_b_type.columns = ['view', 'collect', 'cart', 'buy']
df_b_type['view_not_buy'] = df_b_type['view'] - df_b_type['buy']
df_b_type['cart_not_buy'] = df_b_type['cart'] - df_b_type['buy']
df_b_type.drop(columns=['view', 'collect', 'cart', 'buy'], inplace=True)
df_b_type.reset_index(inplace=True)

merge_label = merge_label.merge(df_b_type, on='u_id', how='left')

# 用户属性标签
# 是否复购用户
df_buy = df[df['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
df_buy.rename(columns={'item_id': '是否复购'}, inplace=True)
merge_label = merge_label.merge(df_buy, how='left', on='u_id')
merge_label['是否复购'].fillna(-1, inplace=True)
merge_label['是否复购'] = merge_label['是否复购'].apply(lambda x: '是' if x > 1 else '否' if x >= 0 else '未购买')

# 30天内购买次数与购买人数关系
buy_active_level = merge_label['近30天购买数'].value_counts().reset_index()
buy_active_level.rename(columns={'近30天购买数': '购买人数'}, inplace=True)
utils.fix_matplotlib_error()
plt.figure(figsize=(16, 12))
sns.lineplot(data=buy_active_level, x='index', y='购买人数', linestyle='--')
plt.title('30天内购买次数与购买人数关系')
plt.show()

# 购买的品类是否单一
buy_single = df[df['b_type'] == 4].groupby('u_id')['item_cls'].nunique().reset_index()
buy_single.rename(columns={'item_cls': '购买品类是否单一'}, inplace=True)
merge_label = merge_label.merge(buy_single, how='left', on='u_id')
merge_label['购买品类是否单一'].fillna(-1, inplace=True)
merge_label['购买品类是否单一'] = merge_label['购买品类是否单一'] \
    .apply(lambda x: '是' if x > 1 else '否' if x > 0 else '未购买')

# 用户价值分组(RFM)
last_buy_days = merge_label['上次购买距今天天数'].value_counts().reset_index()
plt.figure(figsize=(16, 12))
sns.lineplot(data=last_buy_days, x='index', y='上次购买距今天天数', linestyle='-.')
plt.xlabel('距离天数')
plt.ylabel('购买人数')
plt.title('')
plt.show()
# 注：访问异常的那天为双12


# 为RFM设置指标level
merge_label['购买活跃度'] = merge_label['近30天购买数'] \
    .apply(lambda x: '高' if x > 14 else '低' if x >= 0 else '未购买')

merge_label['购买天数分层'] = merge_label['上次购买距今天天数'] \
    .apply(lambda x: '高' if x < 8 else '低' if x <= 31 else '未购买')

merge_label['rfm_values'] = merge_label['购买活跃度'].str.cat(merge_label['购买天数分层'])


def get_rfm(val):
    if val == '高高':
        return '重要价值客户'
    elif val == '低高':
        return '重要深耕客户'
    elif val == '高低':
        return '重要唤回客户'
    else:
        return '即将流失客户'


merge_label['rfm_values'] = merge_label['rfm_values'].apply(get_rfm)

merge_label.drop(columns=['购买活跃度', '购买天数分层'], inplace=True)

merge_label['rfm_values'].value_counts()

# 保存一下merge_data 和 df文档,方便断点从这里开始继续调用
# file_path = ['\\'.join(item) for item in file_path.split('\\')[:-1]]

file_path = r'D:\迅雷下载\python_database\taobao_persona.zip'
file_path = os.path.splitext(file_path)[0]
file_name = ['taobao_persona_label.csv', 'taobao_persona_sample_df.csv']

if not os.path.exists(file_path):
    os.makedirs(file_path)  # 创建保存路径
    fp1 = file_path + r'\\' + file_name[0]
    open(fp1, 'w+')
    fp2 = file_path + r"\\" + file_name[1]
    open(fp2, 'w+')

fp1 = file_path + r'\\' + file_name[0]
fp2 = file_path + r"\\" + file_name[1]
merge_label.to_csv(fp1)
df.to_csv(fp2)
merge_label = pd.read_csv(fp1)
df = pd.read_csv(fp2)

# %%
df_plot1 = df[df['b_type'] == 1].groupby(df['time'].dt.date)['u_id'].count()
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.lineplot(data=df_plot1, x=df_plot1.index, y=df_plot1.values)
ax.set_title('用户浏览情况', fontsize=15)
ax.set_xlabel('浏览时间', fontsize=15)
ax.set_ylabel('浏览次数', fontsize=15)
ax.set_xticklabels(list(df_plot1.index)[0:-1:3])
fig.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 1], index=df['date'].str[-5:], columns='hour', values='u_id', aggfunc='count').reset_index()
df_temp = pd.melt(df_temp, id_vars='date')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='hour')
ax.set_title('用户浏览时间', fontsize=15)
ax.set_xlabel('访问日期', fontsize=15)
ax.set_ylabel('浏览量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 2], index=df['date'].str[-5:], columns='hour', values='u_id', aggfunc='count').reset_index()
df_temp = pd.melt(df_temp, id_vars='date')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='hour')
ax.set_title('用户收藏时间', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 3], index=df['date'].str[-5:], columns='hour', values='u_id', aggfunc='count').reset_index()
df_temp = pd.melt(df_temp, id_vars='date')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='hour')
ax.set_title('用户+购物车时间', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 4], index=df['date'].str[-5:], columns='hour', values='u_id', aggfunc='count').reset_index()
df_temp = pd.melt(df_temp, id_vars='date')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='hour')
ax.set_title('用户购买时间', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
# 各类行为排名top5类目
df_temp = pd.pivot_table(data=df[df['b_type'] == 1], columns=df['date'].str[-5:],
                         index='item_cls', values='u_id', aggfunc='count', fill_value=0).reset_index()
df_temp['total'] = df_temp.sum(axis=1)
df_temp.sort_values(by='total', ascending=False, inplace=True)
df_temp.drop(columns='total', inplace=True)
df_temp = df_temp[:5]
df_temp = pd.melt(df_temp, id_vars='item_cls')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='item_cls')
ax.set_title('用户浏览类目', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 2], columns=df['date'].str[-5:],
                         index='item_cls', values='u_id', aggfunc='count', fill_value=0).reset_index()
df_temp['total'] = df_temp.sum(axis=1)
df_temp.sort_values(by='total', ascending=False, inplace=True)
df_temp.drop(columns='total', inplace=True)
df_temp = df_temp[:5]
df_temp = pd.melt(df_temp, id_vars='item_cls')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='item_cls')
ax.set_title('用户收藏类目', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()
# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 3], columns=df['date'].str[-5:],
                         index='item_cls', values='u_id', aggfunc='count', fill_value=0).reset_index()
df_temp['total'] = df_temp.sum(axis=1)
df_temp.sort_values(by='total', ascending=False, inplace=True)
df_temp.drop(columns='total', inplace=True)
df_temp = df_temp[:5]
df_temp = pd.melt(df_temp, id_vars='item_cls')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='item_cls')
ax.set_title('用户+购物车', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
df_temp = pd.pivot_table(data=df[df['b_type'] == 4], columns=df['date'].str[-5:],
                         index='item_cls', values='u_id', aggfunc='count', fill_value=0).reset_index()
df_temp['total'] = df_temp.sum(axis=1)
df_temp.sort_values(by='total', ascending=False, inplace=True)
df_temp.drop(columns='total', inplace=True)
df_temp = df_temp[:5]
df_temp = pd.melt(df_temp, id_vars='item_cls')
plt.figure(figsize=(16, 16))
fig, ax = plt.subplots()
sns.lineplot(data=df_temp, x='date', y='value', hue='item_cls')
ax.set_title('用户购买类目', fontsize=15)
ax.set_xlabel('日期', fontsize=15)
ax.set_ylabel('数量', fontsize=15)
ax.set_xticks(df_temp['date'].unique()[::3])
plt.show()

# %%
len(df['item_id'].unique())

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近7天浏览数'], bins=[1, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('7日内用户浏览情况', fontsize=15)
ax.set_xlabel('浏览频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

merge_label['collects_rate'].value_counts()

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近7天收藏数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('7日内用户收藏情况', fontsize=15)
ax.set_xlabel('收藏频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()
# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近7天加入购物车数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('7日内+购物车情况', fontsize=15)
ax.set_xlabel('+购物车频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近7天购买数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('7日内用户购买情况', fontsize=15)
ax.set_xlabel('购买频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近30天浏览数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('30日内用户浏览情况', fontsize=15)
ax.set_xlabel('浏览频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
fig.show()

# merge_label['collects_rate'].value_counts()

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近30天收藏数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('30日内用户收藏情况', fontsize=15)
ax.set_xlabel('收藏频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
fig.show()
# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近30天加入购物车数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('30日内+购物车情况', fontsize=15)
ax.set_xlabel('收藏频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
fig.show()

# %%
merge_label['collects_rate'] = pd.cut(x=merge_label['近30天购买数'], bins=[1, 2, 5, 10, 20, 50, 100, 1000, 10000, ],
                                      right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='collects_rate', palette='Oranges_r')
ax.set_title('30日内用户购买情况', fontsize=15)
ax.set_xlabel('收藏频次', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
fig.show()

# %%
"""
最近用户行为
"""
df_latest = merge_label[['u_id', '上次浏览距今天天数', '上次收藏距今天天数', '上次加购物车今天天数',
                         '上次购买距今天天数', '最近两次购物间隔时间']]

# %%
merge_label['temp_rate'] = pd.cut(x=merge_label['上次浏览距今天天数'], bins=[1, 4, 8, 15, 31, ],
                                  right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='temp_rate', palette='Oranges_r')
ax.set_title('上次浏览距今天天数', fontsize=15)
ax.set_xlabel('间隔天数', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['temp_rate'] = pd.cut(x=merge_label['上次收藏距今天天数'], bins=[1, 4, 8, 15, 31, ],
                                  right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='temp_rate', palette='Oranges_r')
ax.set_title('上次收藏距今天天数', fontsize=15)
ax.set_xlabel('间隔天数', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['temp_rate'] = pd.cut(x=merge_label['上次加购物车今天天数'], bins=[1, 4, 8, 15, 31, ],
                                  right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='temp_rate', palette='Oranges_r')
ax.set_title('上次+购物车今天天数', fontsize=15)
ax.set_xlabel('间隔天数', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['temp_rate'] = pd.cut(x=merge_label['上次购买距今天天数'], bins=[1, 4, 8, 15, 31, ],
                                  right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='temp_rate', palette='Oranges_r')
ax.set_title('上次购买距今天天数', fontsize=15)
ax.set_xlabel('间隔天数', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
merge_label['temp_rate'] = pd.cut(x=merge_label['最近两次购买间隔天数'], bins=[1, 4, 8, 15, 31, ],
                                  right=False)
plt.figure(figsize=(16, 12))
fig, ax = plt.subplots()
sns.countplot(data=merge_label, x='temp_rate', palette='Oranges_r')
ax.set_title('最近两次购买间隔天数', fontsize=15)
ax.set_xlabel('间隔天数', fontsize=15)
ax.set_ylabel('用户数', fontsize=15)
plt.show()

# %%
bug_again = df[df['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
bug_again['cls'] = pd.cut(bug_again['item_id'], bins=[1, 2, 5, 10, 15, 20, 30, 50, 100], right=False)

plt.figure(figsize=(12, 12))
fig, ax = plt.subplots()
sns.lineplot(y=bug_again['cls'], palette='Oranges_r')
ax.set_title('用户购买频率')
ax.set_ylabel('用户复购频率')
ax.set_xlabel('用户数')
fig.show()

# %%
buy_active_level = merge_label['近30天购买数'].value_counts(dropna=True).reset_index()
buy_active_level.sort_values(by='index', ascending=False, inplace=True)

plt.figure(figsize=(12, 12))
fig, ax = plt.subplots()
sns.lineplot(data=buy_active_level, x='index', y='近30天购买数', markers='*', linestyle='--', color='orange')
ax.set_title('30天内购买次数与购买人数情况')
ax.set_ylabel('购买人数')
ax.set_xlabel('购买次数')
fig.show()

# %%

counts_30_active = merge_label['活跃天数'].value_counts().sort_index(ascending=False)
plt.figure(figsize=(12, 12))
fig, ax = plt.subplots()
sns.lineplot(data=counts_30_active, x=counts_30_active.index, y=counts_30_active.values, markers='^', linestyle='--', color='orange')
ax.set_title('30天内与活跃人数情况')
ax.set_xlabel('活跃天数')
ax.set_ylabel('活跃人数')
fig.show()
merge_label.columns

# %%

view = len(df[df['b_type'] == 1])
collect = len(df[df['b_type'] == 2])
cart = len(df[df['b_type'] == 3])
buy = len(df[df['b_type'] == 4])
# %%
label = ['浏览', '收藏+加购物车', '购买']
val = [view, collect + cart, buy]

funnel = (
    Funnel()
        .add('', [list(z) for z in zip(label, val)], )
        .set_global_opts(title_opts=opts.TitleOpts(title='淘宝行为转化漏斗'),
                         legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
                         tooltip_opts=opts.TooltipOpts(is_show=True))

)
funnel.render()

# %%
df['b_type'].unique()

# %%
merge_label['购买品类是否单一'].value_counts()

# %%
merge_label['最近两次购买间隔天数'].fillna(-1, inplace=True)

# merge_label['最近两次购买间隔天数']


print(merge_label['temp_rate'].value_counts())
print(7756 / (20000 - 4638))

# %%
buy_again = df[df['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
buy_again

# %%
# merge_label['是否复购'].value_counts()

merge_label['购买品类是否单一'].value_counts()

# %%
df[df['b_type'] == 4]['u_id'].nunique()

# %%
daily = df[~df['date'].isin(["2014-12-11", "2014-12-12", "2014-12-13"])]
# %%
active = df[df['date'].isin(["2014-12-11", "2014-12-12", "2014-12-13"])]

# %%
# 日常转化
l_pv = daily[daily.b_type == 1]["u_id"].count()
l_cart = daily[daily.b_type == 3]["u_id"].count()
l_collect = daily[daily.b_type == 2]["u_id"].count()
l_buy = daily[daily.b_type == 4]["u_id"].count()

l_attr = ["点击", "加入购物车", "收藏", "购买"]
valuel = [np.around((l_pv / l_pv * 100), 2),
          np.around((l_cart / l_pv * 100), 2),
          np.around((l_collect / l_pv * 100), 2),
          np.around((l_buy / l_pv * 100), 2),
          ]

datal = [[l_attr[i], valuel[i]] for i in range(len(l_attr))]

dy = (
    Funnel()
        .add(
        series_name="用户行为",
        data_pair=datal,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%", is_show=True),
        label_opts=opts.LabelOpts(is_show=True, position="ourside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="流量转化漏斗", subtitle="日常"))
)
dy.render()

# %%
a_pv = active[active.b_type == 1]["u_id"].count()
a_cart = active[active.b_type == 3]["u_id"].count()
a_collect = active[active.b_type == 2]["u_id"].count()
a_buy = active[active.b_type == 4]["u_id"].count()

a_attr = ["点击", "加入购物车", "收藏", "购买"]
valuel = [np.around((a_pv / a_pv * 100), 2),
          np.around((a_cart / a_pv * 100), 2),
          np.around((a_collect / a_pv * 100), 2),
          np.around((a_buy / a_pv * 100), 2),
          ]

datal = [[l_attr[i], valuel[i]] for i in range(len(l_attr))]

dy = (
    Funnel()
        .add(
        series_name="用户行为",
        data_pair=datal,
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%", is_show=True),
        label_opts=opts.LabelOpts(is_show=True, position="ourside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="流量转化漏斗", subtitle="双12.12活动期间"))
)
dy.render()
