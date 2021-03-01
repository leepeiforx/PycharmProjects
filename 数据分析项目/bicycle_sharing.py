import gc

import pandas as pd
import pyecharts.options as opts
import seaborn as sns
from matplotlib import pyplot as plt
from pyecharts.charts import *
from pyecharts.faker import Faker

from common import utils

# %%
# 导入数据
file_path = r'数据分析项目/database/bicycle_sharing.csv'
df = pd.read_csv(file_path)
df.head()

# 数据清洗,异常值处理
print(utils.show_na(df))  # 各字段不存在NA值
print(utils.show_info(df))  # 不存在异常值,但需要修改datetime字段数据类型
print(utils.show_duplicated(df))  # 不存在重复记录
"""源数据经查不需要进行清洗"""

# 提取数据特征
df['datetime'] = pd.to_datetime(df['datetime'])
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['hour'] = df['datetime'].dt.hour
df['minute'] = df['datetime'].dt.minute

sns.set_style('ticks')
plt.figure(figsize=(12, 6))
# 利用kdeplot查看数据的分布特征
sns.kdeplot(df['count'])
sns.despine(left=True)
plt.grid(linestyle='--', alpha=0.5, axis='y')
plt.title('Demand Distribution')
plt.legend()
plt.xlabel('Demand')
plt.ylabel('Frequency')
plt.show()
'''count数据字段呈现明显的右偏,取值主要集中在0~400这个区间段'''
# 从时间维度看需求趋势

df_by_year = pd.pivot_table(data=df, index='month', columns='year', values=['casual', 'registered', 'count'],
                            aggfunc='sum')

"""
pandas.melt 使用参数：

pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
参数解释：
frame:要处理的数据集。
id_vars:不需要被转换的列名。
value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了。
var_name和value_name是自定义设置对应的列名。
col_level :如果列是MultiIndex，则使用此级别。
"""
df_stack = df_by_year.stack().reset_index()
df_melt = pd.melt(df_stack, id_vars=['month', 'year'])

plt.figure(figsize=(16, 6))
plt.subplot(211)
sns.lineplot(data=df_melt[df_melt['year'] == 2011], x='month', y='value', hue='variable', linestyle='--')
plt.ylabel('Count')
plt.xlabel('')
plt.title('2011 Demand Tendency')
plt.legend(loc='upper right')
plt.grid()
plt.subplot(212)
sns.lineplot(data=df_melt[df_melt['year'] == 2012], x='month', y='value', hue='variable', linestyle='--')
plt.ylabel('Count')
plt.xlabel('')
plt.grid()
plt.legend(loc='upper right')
plt.title('2012 Demand Tendency')
plt.show()

"""
上图为可视化结果，整体上可见2012年相较于2011年，骑行的需求有了大幅的增长。总需求和注册用户需求的变化最为明显，
而非注册用户提升效果一般，这说明：经过一年的运营，越来越多的使用者在平台上注册了，注册用户提升显著。
8从月份角度，我们能看到的是：6月~9月是骑行旺季，12月~2月是骑行淡季
"""

# 从小时维度
df_by_hour = df.groupby('hour')[['casual', 'registered', 'count']].sum().reset_index()
df_by_hour = pd.melt(df_by_hour, id_vars=['hour'])  # 将以上的二维表转化为一维表,方便绘图
plt.figure(figsize=(12, 9))
plt.xticks(range(0, 24))
sns.lineplot(data=df_by_hour, x='hour', y='value', hue='variable', linestyle='-.')
plt.show()
"""
从24小时观察骑行需求：存在6~7AM以及5~6PM两个峰值，
中午12AM有一个小峰值，符合通勤规律，注册用户特征更为明显，而非注册用户则变化平缓。
"""
# （工作日和非工作日小时维度）
df_by_workandhour = pd.pivot_table(data=df, index='hour', columns='workingday',
                                   values=['casual', 'registered', 'count'],
                                   aggfunc='sum', fill_value=0)

df_by_workandhour = df_by_workandhour.stack().reset_index()
df_by_workandhour = pd.melt(df_by_workandhour, id_vars=['hour', 'workingday'])

df_ct = df_by_workandhour[df_by_workandhour['variable'] == 'count']
plt.figure(figsize=(12, 9))
plt.xticks(range(0, 24))
sns.lineplot(data=df_ct, x='hour', y='value', hue='workingday', linestyle='-.')
plt.show()

"""
可见工作日与非工作日的骑行需求规律反差巨大，非工作日的共享单车苏醒慢，
骑行需求高峰出现在12AM~3PM的这段时间内，另外凌晨0AM~4AM的骑行需求大于工作日，周末使劲造！
"""


# 不同季节的小时维度
def set_season(val):
    if val == 1:
        return '春'
    elif val == 2:
        return '夏'
    elif val == 3:
        return '秋'
    elif val == 4:
        return '冬'
    else:
        return None


df_by_seasons = pd.pivot_table(data=df, index='hour', columns='season',
                               values=['casual', 'registered', 'count'],
                               aggfunc='sum', fill_value=0)

df_by_seasons = df_by_seasons.stack().reset_index()
df_by_seasons = pd.melt(df_by_seasons, id_vars=['hour', 'season'])

df_by_seasons = df_by_seasons[df_by_seasons['variable'] == 'count']
df_by_seasons['season'] = df_by_seasons['season'].apply(set_season)
utils.fix_matplotlib_error()
plt.figure(figsize=(12, 9))
plt.xticks(range(0, 24))
plt.title('Demand Tendency by season')
plt.grid()
sns.lineplot(data=df_by_seasons, x='hour', y='value', hue='season',
             linestyle='-.', markers=True, palette='Blues'
             )
plt.show()

# 一周不同时间段的骑行需求
# 从日期中提取出该日属于星期几
df['weekday'] = pd.to_datetime(df['datetime']).apply(lambda d: d.weekday())

weekday_demand = df.groupby(['weekday', 'hour'])['count'].mean().reset_index()
weekday_demand['count'] = round(weekday_demand['count'], 0)
weekday_demand.stack()
weekday_demand.sort_values(['weekday', 'hour'], ascending=True, inplace=True)
weekday_demand = weekday_demand.iloc[:, [1, 0, 2]]
data = [list(weekday_demand.iloc[i, :].values) for i in range(len(weekday_demand))]

x_axis = [
    "12am", "1am", "2am", "3am", "4am", "5am", "6am", "7am", "8am", "9am", "10am", "11am",
    "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm"
]
y_axis = [
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
]

bar3d = (Bar3D()
         .add('', data=data, shading='realistic',
              xaxis3d_opts=opts.Axis3DOpts(x_axis, type_='category'),
              yaxis3d_opts=opts.Axis3DOpts(y_axis, type_='category'),
              zaxis3d_opts=opts.Axis3DOpts(type_='value'),
              grid3d_opts=opts.Grid3DOpts(width=140, depth=84, is_rotate=True))
         .set_global_opts(title_opts=opts.TitleOpts('一周不同时间段的骑行需求'),
                          visualmap_opts=opts.VisualMapOpts(is_show=True, max_=600,
                                                            is_piecewise=False,
                                                            range_color=Faker.visual_color))
         )
bar3d.render()


# 天气维度(不同天气状况)
def set_weather(val):
    if val == 1:
        return 'Good'
    elif val == 2:
        return 'Normal'
    elif val == 3:
        return 'Bad'
    else:
        return 'Very Bad'


weather_demand = df.groupby(['weather', 'day'])['count'].sum().reset_index()
weather_demand['weather'] = weather_demand['weather'].apply(set_weather)

plt.figure(figsize=(16, 12))
sns.stripplot(data=weather_demand, x='weather', y='count', palette='Set2')
sns.despine(left=True)
plt.title('Demand Distribution by Weather')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

# 不同天气的骑行需求
df_sh = df.groupby(['weather', 'hour'])['count'].mean().reset_index()
df_sh['weather'] = df_sh['weather'].apply(set_weather)
plt.figure(figsize=(16, 12))
sns.lineplot(data=df_sh, x='hour', y='count', hue='weather', palette='Set1', linestyle=':')
plt.show()

"""
可见，天气越不好，骑行数量需求越少，极端天气未形成趋势线，极端天气还是占少数的（这个维度分析有必要吗，这不是常识吗）
"""

# 气温与体表温度
plt.figure(figsize=(10, 10))

sns.kdeplot(data=df, x='temp', y='atemp', shade=True, cut=10,
            cmap='YlGnBu', cbar=True)
sns.despine(left=True)
plt.grid(linestyle='--', alpha=.4)
plt.ylim(0, 50)
plt.xlim(0, 50)
plt.xlabel('Temperature')
plt.ylabel('Atemp')
plt.title('correlation of temp and atemp')
plt.show()

"""
从两者的关系度量图中我们能看出呈现正相关分布，另外能获取到的信息是：
颜色最深的分布最为集中，最适宜的气温27℃~28℃、体表温度31℃左右的骑行需求是最密集的。
"""

# 气温与风速
plt.figure(figsize=(10, 10))

sns.kdeplot(data=df, x='temp', y='windspeed', shade=True, cut=10,
            cmap='YlGnBu', cbar=True)
sns.despine(left=True)
plt.grid(linestyle='--', alpha=.4)
plt.ylim(0, 50)
plt.xlim(0, 50)
plt.xlabel('Temperature')
plt.ylabel('windspeed')
plt.title('correlation of temp and windspeed')
plt.show()

'''风速的分布存在断层，初步推断可能是异常数据，这里先不做处理；可见气温27℃~28℃，风速8~9骑行需求是最密集的。'''

# 天气因素与骑行需求
"""
将气温和风速作为天气因素分析骑行需求（忽略体表温度，气温即代表了体表温度），
使用散点图绘制，散点的大小和颜色代表了骑行量，每个散点代表一天。
"""
plt.figure(figsize=(12, 12))
plt.scatter(x='temp', y='windspeed',
            s=df['count'] / 2,
            c='count', cmap='RdBu_r',
            edgecolors='black', linestyle='--', linewidth=0.2, alpha=0.6,
            data=df)
plt.show()
# %%
plt.figure(figsize=(12, 12))
sns.scatterplot(x='temp', y='windspeed',
                size=df['count'] / 2,
                cmap='RdBu_r', linewidth=0.2, alpha=0.6,
                data=df)
plt.show()
"""
可见骑行需求较多的分布范围：气温20℃~35℃，风速40以下；
人们更热衷于温暖天气骑行，炎热天气需求也大的原因可能是因为相对于公共交通，骑行更加灵活方便吧。
"""

# %%
# 考虑温度和湿度
plt.figure(figsize=(12, 12))
plt.scatter(x='temp', y='humidity',
            s=df['count'] / 2,
            c='count', cmap='RdBu_r',
            edgecolors='black', linestyle='--', linewidth=0.2, alpha=0.6,
            data=df)
plt.show()

# %%
# 清空缓存
del data
del df_by_workandhour
del df_by_seasons
del df_by_hour
del df_by_year
del df_sh
del df_stack
del df_ct
del df_melt
del weekday_demand
del weather_demand
del x_axis
del y_axis
gc.collect()

# %%

df['diff'] = df['registered'] - df['casual']  # 衍生特征注册用户与非注册用户的骑行需求差值

plt.figure(figsize=(20, 8))
plt.subplots_adjust(hspace=.3, wspace=.1)
# 绘制子图1：月度差异
plt.subplot(221)
month_diff = df.groupby('month')[['casual', 'registered']].mean().reset_index()
month_diff = pd.melt(month_diff, id_vars=['month'])
sns.lineplot(data=month_diff, x='month', y='value', hue='variable', linestyle='--')
plt.title('Workingday Month Demand Diff')
plt.grid(linestyle='--', alpha=.8)
plt.legend()
plt.xlabel('month')
plt.ylabel('Count')
sns.despine(left=True)
#
# 绘制子图2：小时差异
plt.subplot(222)
hour_diff = df.groupby('hour')[['casual', 'registered']].mean().reset_index()
hour_diff = pd.melt(hour_diff, id_vars=['hour'])
sns.lineplot(data=hour_diff, x='hour', y='value', hue='variable', linestyle='--')
plt.title('Workingday Hour Demand Diff')
plt.grid(linestyle='--', alpha=.8)
plt.legend()
plt.xlabel('hour')
plt.ylabel('Count')
sns.despine(left=True)

# 绘制子图3：工作日差异
plt.subplot(223)
df_day = df.groupby(['hour', 'workingday'])[['casual', 'registered']].mean().reset_index()
df_day = pd.melt(df_day, id_vars=['hour', 'workingday'])
sns.lineplot(data=df_day[df_day['workingday'] == 1], x='hour', y='value', hue='variable', linestyle='--')
plt.title('Workingday Hour Demand Diff')
plt.grid(linestyle='--', alpha=.8)
plt.legend()
plt.xlabel('hour')
plt.ylabel('Count')
sns.despine(left=True)

# 绘制子图4,休息日差异
plt.subplot(224)
sns.lineplot(data=df_day[df_day['workingday'] == 0], x='hour', y='value', hue='variable', linestyle='--')
plt.title('Holiday Hour Demand Diff')
plt.grid(linestyle='--', alpha=.8)
plt.legend()
plt.xlabel('hour')
plt.ylabel('Count')
sns.despine(left=True)

plt.show()

"""
上图为注册用户与非注册用户在各因素下的差异组合图：
第一幅为两者的月度差异图，可见整体趋势相同，注册用户远高于非注册用户；
第二幅为两者的小时差异图，可见注册用户的小时规律明显，非注册用户则只在12AM~5PM存在峰值，整体差异较大；
第三幅为两者的工作日差异图，可见注册用户工作日小时规律明显，二非注册用户趋势平缓；
第四幅为两者的非工作日差异图，可见非工作日两者差异相较于其他因素差异较小，且趋势相同，值得注意的是注册用户在凌晨更加活跃。
总的来说，注册用户需求远高于非注册用户，注册用户的使用规律明显，而非注册用户受其他因素的影响相对较弱。
"""

"""
1、共享单车由注册用户与非注册用户构成，而主要群体以注册用户为主。
2、共享单车的用户总数主要受摄氏度、体感温度、湿度、时刻影响比较明显。
3、根据数据分析提出几个建议
（1）用户总数随时间在持续上升，可以增加共享单车的投放数量以满足业务需求；
（2）用户总数在夏季、秋季、冬季较多，而在春季较少，可以选择在春季大批量回收车辆进行维修保养；
（3）用户总数在工作日的上下班时段达到高峰期，因此在此时间段前进行车辆调度集中投放在地铁口、
公交站台、小区出口等附近以供人们方便使用，提高用户量； 而在假期，则在白天时刻集中投放在各小区出口、地铁口、景点等附近以供人们方便使用，用以提供用户量；
（4）用户总数在温度达到20-25摄氏度之间达到高峰期，因为温度较舒服，人们喜欢骑单车出行，因此在这种天气时增大投放量。
"""
