from common import utils as u
import pandas as pd
from pyecharts import charts as c
from pyecharts import options as opts
import gc

# %%
file_path = r'D:\file\DataAnalysis\89031322.zip'
file_dict = u.unpack_file_to_df(file_path)
user = file_dict['tianchi_fresh_comp_train_user']

# user_geohash字段缺失值过多,同时因为不做地理坐标分析(数据脱敏之后也无法做),所以删除该列
user.drop(columns='user_geohash', inplace=True)
# 修改time字段属性
user['time'] = pd.to_datetime(user['time'], format='%Y-%m-%d %H:%M:%S')
user['date'] = user['time'].dt.date
user['month'] = user['time'].dt.month
user['hours'] = user['time'].dt.hour

# 修改其他字段属性
user['behavior_type'] = user['behavior_type'].astype('str')
user['user_id'] = user['user_id'].astype('str')
user['item_id'] = user['item_id'].astype('str')

# 数据分析——可视化
user.info()

# 统计每日PV和UV数据
pv = user[user['behavior_type'] == '1'].groupby('date')['behavior_type'].count().reset_index()
uv = user[user['behavior_type'] == '1'].drop_duplicates(['user_id', 'date']) \
    .groupby('date')['user_id'].count().reset_index()

# 绘图准备数据
x_data = pv['date'].to_list()
pv = pv['behavior_type'].to_list()
pv = [round(i / 10000, 2) for i in pv]

uv = uv['user_id'].to_list()
uv = [round(i / 10000, 2) for i in uv]
# %%
line = (
    c.Line()
        .add_xaxis(x_data)
        .add_yaxis('pv', pv, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('uv', yaxis_index=1, y_axis=uv, label_opts=opts.LabelOpts(is_show=False))
        .extend_axis(yaxis=opts.AxisOpts(name='uv', type_='value', min_=0, max_=1.6, interval=.4,
                                         axislabel_opts=opts.LabelOpts(formatter='{value}万人')))
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="pv",
            type_="value",
            min_=0,
            max_=100,
            interval=20,
            axislabel_opts=opts.LabelOpts(formatter="{value} 万次"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="pv与uv趋势图"),
    )
)
line.render()

# %%
# pv、uv差异分析（by day）
pv = user[user['behavior_type'] == '1'].groupby('date')['behavior_type'].count().reset_index()
uv = user[user['behavior_type'] == '1'].drop_duplicates(['user_id', 'date']) \
    .groupby('date')['user_id'].count().reset_index()
pv_uv = pd.merge(pv, uv, 'outer', on='date')
pv_uv.set_index('date', inplace=True)
new_day = pv_uv.diff()
new_day.columns = ['new_pv', 'new_uv']

x_data = list(new_day.index)
new_pv = new_day['new_pv'].to_list()
new_uv = new_day['new_uv'].to_list()
line = (
    c.Line()
        .add_xaxis(x_data)
        .add_yaxis('新增pv', new_pv, label_opts=opts.LabelOpts(is_show=False))
        # .add_yaxis('新增uv', new_uv, label_opts=opts.LabelOpts(is_show=False))
        .extend_axis(yaxis=opts.AxisOpts(name='新增uv', type_='value', min_=-2000, max_=1600,
                                         interval=400, axislabel_opts=opts.LabelOpts(formatter='{value}'), ))
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="新增pv",
            type_="value",
            min_=-350000,
            max_=250000,
            interval=100000,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="pv、uv差异分析"),
    )
)
il = (
    c.Line()
        .add_xaxis(x_data)
        .add_yaxis('新增uv', new_uv, yaxis_index='1', label_opts=opts.LabelOpts(is_show=False))
)
s = line.overlap(il)
s.render()

# %%
# 4） 不同时期用户行为分析
shopping_cart = user[user['behavior_type'] == '3'].groupby('date')['behavior_type'].count().reset_index()
collect = user[user['behavior_type'] == '2'].groupby('date')['behavior_type'].count().reset_index()
buy = user[user['behavior_type'] == '4'].groupby('date')['behavior_type'].count().reset_index()

# %%
x_data = shopping_cart['date'].to_list()
v1 = shopping_cart['behavior_type'].to_list()
v2 = collect['behavior_type'].to_list()
v3 = buy['behavior_type'].to_list()

line = (c.Line()
        .add_xaxis(x_data)
        .add_yaxis('加购人数', v1, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('收藏人数', v2, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('购买人数', v3, label_opts=opts.LabelOpts(is_show=False)))

line.render()
#%%
# 清理一波内存
del file_dict
del line
del il
del x_data
del buy
del collect
del new_day
del new_pv
del new_uv
del pv
del pv_uv
del s
del shopping_cart
del uv
gc.collect()


# %%
"""
4、把数据拆分为活动数据和日常数据做不同时段的分析
——由于数据里面包含双十二大促的数据，
因此整理分析用户的不同时段行为可能会导致分析结果与实际差异较大，因此拆分开来做不同的对比分析"""

# 日期类的数据需要注意数据类型,否则下面的操作就无法实现
active = user[user['date'].isin(['2014-12-11', '2014-12-12', '2014-12-13'])]
daily = user[~user['date'].isin(['2014-12-11', '2014-12-12', '2014-12-13'])]

# %%
# 3）活动期间不同时段的用户行为分析
x_data = shopping_cart['date'].to_list()
v1 = shopping_cart['behavior_type'].to_list()
v2 = collect['behavior_type'].to_list()
v3 = buy['behavior_type'].to_list()

line = (c.Line()
        .add_xaxis(x_data)
        .add_yaxis('加购人数', v1, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('收藏人数', v2, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('购买人数', v3, label_opts=opts.LabelOpts(is_show=False)))

line.render()

# %%


