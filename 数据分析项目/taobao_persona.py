from datetime import datetime

import numpy as np
import pandas as pd

# %%
# 读取数据
file_path = r'D:\迅雷下载\python_database\taobao_persona.zip'
df_orginal = pd.read_csv(file_path)

# %%
# 数据预处理
# 数据抽样
# 数据集太大，为了提高运行效率，只随机抽取1%的数据作为代码运行数据,随后如果需要再替换为全量数据
df = df_orginal.sample(frac=0.01, random_state=1)

# %%
# df_sample = df.sample(frac=.1, random_state=0)

# %%
# 回收内存
del df_orginal
# del df

# %%
# 检查数据情况
# user_geohash字段缺失值过多,
# print(utils.show_na(df))
# print(utils.show_info(df))
# print(utils.show_duplicated(df))
df.drop(columns='user_geohash', inplace=True)
# %%
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
df.rename(columns={'user_id': 'u_id', 'behavior_type': 'b_type',
                   'item_category': 'item_cls'}, inplace=True)

# 制作用户标签表
users = df['u_id'].unique()
labels = pd.DataFrame(users, columns=['u_id'])

# %%
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


# %%
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


# %%
# 用户浏览/购买活跃时间段
most_view_by_hour = get_max_label(df, cls=1, col1='u_id', col2='hour', agg_col='item_id')
most_buy_by_hour = get_max_label(df, cls=4, col1='u_id', col2='hour', agg_col='item_id')

merge_label = labels.merge(most_view_by_hour, how='left', on='u_id')
merge_label = merge_label.merge(most_buy_by_hour, how='left', on='u_id')
merge_label.rename(columns={'hour_x': '浏览时间', 'hour_y': '购买时间'}, inplace=True)

# %%
# 查看每个用户浏览.收藏,加购物车,购买的各类目情况
most_view_by_item = get_max_label(df, cls=1, col1='u_id', col2='item_cls', agg_col='item_id')
most_view_by_item.rename(columns={'item_cls': '浏览'}, inplace=True)
most_collect_by_item = get_max_label(df, cls=2, col1='u_id', col2='item_cls', agg_col='item_id')
most_collect_by_item.rename(columns={'item_cls': '收藏'}, inplace=True)
most_chart_by_item = get_max_label(df, cls=3, col1='u_id', col2='item_cls', agg_col='item_id')
most_chart_by_item.rename(columns={'item_cls': '加购误差'}, inplace=True)
most_buy_by_item = get_max_label(df, cls=4, col1='u_id', col2='item_cls', agg_col='item_id')
most_buy_by_item.rename(columns={'item_cls': '购买'}, inplace=True)

merge_label = merge_label.merge(most_view_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_collect_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_chart_by_item, how='left', on='u_id')
merge_label = merge_label.merge(most_buy_by_item, how='left', on='u_id')

# %%
# 划分间隔时间
# 用户近30天行为
df['date_diff'] = (datetime(2014, 12, 18) - df['time']).dt.days + 1

df_view_30 = df[df['b_type'] == 1].groupby('u_id')['item_id'].count().reset_index()
df_view_30.rename(columns={'item_id': '近30天浏览数'})
df_collect_30 = df[df['b_type'] == 2].groupby('u_id')['item_id'].count().reset_index()
df_collect_30.rename(columns={'item_id': '近30天收藏数'})
df_cart_30 = df[df['b_type'] == 3].groupby('u_id')['item_id'].count().reset_index()
df_cart_30.rename(columns={'item_id': '近30天加入购物车数'})
df_buy_30 = df[df['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
df_buy_30.rename(columns={'item_id': '近30天购买数'})

# %%
# 近30天活跃情况(计算u_id)的date非重复计数
df_active_30 = df.groupby('u_id')['date'].nunique().reset_index()
df_active_30.rename(columns={'date': '活跃天数'}, inplace=True)

merge_label = merge_label.merge(df_view_30, how='left', on='u_id')
merge_label = merge_label.merge(df_collect_30, how='left', on='u_id')
merge_label = merge_label.merge(df_cart_30, how='left', on='u_id')
merge_label = merge_label.merge(df_buy_30, how='left', on='u_id')
merge_label = merge_label.merge(df_active_30, how='left', on='u_id')

# %%
# 用户最近7日指数
df_7days = df[df['date_diff'] <= 7]

df_view_7 = df_7days[df_7days['b_type'] == 1].groupby('u_id')['item_id'].count().reset_index()
df_view_7.rename(columns={'item_id': '近7天浏览数'})
df_collect_7 = df_7days[df_7days['b_type'] == 2].groupby('u_id')['item_id'].count().reset_index()
df_collect_7.rename(columns={'item_id': '近7天收藏数'})
df_cart_7 = df_7days[df_7days['b_type'] == 3].groupby('u_id')['item_id'].count().reset_index()
df_cart_7.rename(columns={'item_id': '近7天加入购物车数'})
df_buy_7 = df_7days[df_7days['b_type'] == 4].groupby('u_id')['item_id'].count().reset_index()
df_buy_7.rename(columns={'item_id': '近7天购买数'})

# 近30天活跃情况(计算u_id)的date非重复计数
df_active_7 = df_7days.groupby('u_id')['date'].nunique().reset_index()
df_active_7.rename(columns={'date': '活跃天数'}, inplace=True)

merge_label = merge_label.merge(df_view_7, how='left', on='u_id')
merge_label = merge_label.merge(df_collect_7, how='left', on='u_id')
merge_label = merge_label.merge(df_cart_7, how='left', on='u_id')
merge_label = merge_label.merge(df_buy_7, how='left', on='u_id')
merge_label = merge_label.merge(df_active_7, how='left', on='u_id')

# %%
# 最后一次行为距今天数

# 上次浏览
df_view_diff = df[df['b_type'] == 1].groupby('u_id')['date_diff'].min().reset_index()
df_view_diff.rename(columns={'date_diff': '上次行为据今天天数'}, inplace=True)
merge_label = merge_label.merge(df_view_diff, how='left', on='u_id')

# 上次收藏
df_collect_diff = df[df['b_type'] == 2].groupby('u_id')['date_diff'].min().reset_index()
df_collect_diff.rename(columns={'date_diff': '上次行为据今天天数'}, inplace=True)
merge_label = merge_label.merge(df_collect_diff, how='left', on='u_id')

# 上次加购物车
df_cart_diff = df[df['b_type'] == 1].groupby('u_id')['date_diff'].min().reset_index()
df_cart_diff.rename(columns={'date_diff': '上次行为据今天天数'}, inplace=True)
merge_label = merge_label.merge(df_cart_diff, how='left', on='u_id')

df_buy_diff = df[df['b_type'] == 1].groupby('u_id')['date_diff'].min().reset_index()
df_buy_diff.rename(columns={'date_diff': '上次行为据今天天数'}, inplace=True)
merge_label = merge_label.merge(df_buy_diff, how='left', on='u_id')

# 上次


# 最近两次购买间隔天数
# %%
second_max = df.sort_values('date_diff', ascending=False) \
    .groupby('u_id').nth(1)['date_diff'].reset_index()
date_max = df.groupby('u_id')['date_diff'].max().reset_index()
