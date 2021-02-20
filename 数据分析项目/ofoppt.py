import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\ofoppt.zip'
df = pd.read_csv(file_path)
print(df.head())
print(df.info())
print(df.dtypes)

# %%
# 检查NA值及统计性描述
print(df.isna().sum())
print(df.describe())

# %%
# 检查重复值
print(df[df.duplicated().values == True].count())

# %%
# datetime转换为日期格式
week_dict = {
    1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周末'
}

# %%
df['datetime'] = pd.to_datetime(df['datetime'])
df['week'] = df['datetime'].dt.dayofweek + 1
df['week'] = df['week'].map(week_dict)
df['quarter'] = df['datetime'].dt.quarter
print(df['quarter'])
# %%
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# %%
# 可视化

# 组成人数
df_group = df.groupby(by=df['datetime'].dt.year)['count'].sum()
sns.barplot(x=df_group.index, y=df_group.values)
for i in range(len(df_group)):
    plt.text(x=i - 0.1, y=df_group.values[i], va='bottom',
             s=df_group.values[i])
plt.title('2011-2012年统计人数')
plt.show()

'总体来看，租车人数还是较多的，共享单车时长势头较好'

# %%

# 租车人数在各条件下的箱线图
plt.figure(figsize=(20, 10))
plt.subplot(2, 2, 1)
sns.boxplot(y=df['count'])
plt.title('租车人数全时间箱线图')

plt.subplot(2, 2, 2)
sns.boxplot(y=df['count'], x=df['datetime'].dt.hour)
plt.title('租车人数-小时箱线图')

plt.subplot(2, 2, 3)
sns.boxplot(y=df['count'], x=df['week'])
plt.title('租车人数-星期箱线图')

plt.subplot(2, 2, 4)
sns.boxplot(y=df['count'], x=df['season'], hue=df['datetime'].dt.month)
plt.title('租车人数-季度箱线图')
plt.legend(loc='upper right')

plt.show()

'''
根据以上箱线图，我们得出以下结论：

每小时的租车平均人数大约在150人左右
一天中有两个租车高峰，分别是早上8时左右和下午17时，18时左右，
原因是上下班高峰期用车人数增加
一星期中，工作日和非工作日用车数量没有明显差异
一年中夏天和秋天用车数量较高，春天租车数量较少
'''

# %%
# 租车人数在各条件下的核密度曲线图
plt.subplot(2, 2, 1)
sns.distplot(x=df['temp'])
plt.subplot(2, 2, 2)
sns.distplot(x=df['atemp'])
plt.subplot(2, 2, 3)
sns.distplot(x=df['humidity'])
plt.subplot(2, 2, 4)
sns.distplot(x=df['windspeed'])

plt.show()

'''
根据以上核密度图，得出结论：

实际温度在15-25度范围内租车人数较多
体感温度在15-30度范围内租车人数较多
湿度在50-80范围内租车人数较多
风速在8-20范围内租车人数较多
'''
# %%
# 小时-租车人数关系
df_hour = round(df.groupby(df['datetime'].dt.hour)['count'].mean(), 1)
sns.lineplot(x=df_hour.index, y=df_hour.values, marker='^', linestyle='--')
plt.xticks([x for x in range(24)])
plt.xlabel('小时')
plt.ylabel('平均租车人数')
for i in range(len(df_hour)):
    plt.text(x=df_hour.index[i], y=df_hour.values[i], va='top', ha='center',
             s=df_hour.values[i])
plt.show()

'''
每天上下班时间（8,17时）是两个用车高峰期
除此之外在12-13时是小高峰期，猜测可能是租车出门吃午餐的人
'''
# %%
# 月份-租车人数关系
df_month = round(df.groupby(df['datetime'].dt.month)['count'].mean(), 1)
sns.lineplot(x=df_month.index, y=df_month.values, marker='^', linestyle='--', palette='bright')
plt.xticks([x for x in range(1, 13)])
plt.xlabel('月份')
plt.ylabel('平均租车人数')
for i in range(len(df_month)):
    plt.text(x=df_month.index[i], y=df_month.values[i], va='top', ha='center',
             s=df_month.values[i])
plt.show()
'1-5月租车人数增加，6月达到最高值并趋于稳定，10月租车人数开始下降'

# %%
# 天气-租车人数关系
df_weather = round(df.groupby(df['weather'])['count'].mean(), 1)
edict = {1: '晴天', 2: '阴天', 3: '小雨小雪', 4: '恶劣天气'}
df_weather.rename(index=edict, inplace=True)

sns.lineplot(x=df_weather.index, y=df_weather.values,
             marker='^', linestyle='--', palette='bright')
plt.xlabel('天气')
plt.ylabel('平均租车人数')
for i in range(len(df_weather)):
    plt.text(x=df_weather.index[i], y=df_weather.values[i], va='top', ha='center',
             s=df_weather.values[i])
plt.show()

'''
租车人数受天气好坏程度影响很大
晴天租车人数最高，小雨/小雪天气租车人数反而是最低的'''

#%%
# 风速-租车人数关系

df_windspeed= round(df.groupby(df['windspeed'])['count'].mean(), 1)
sns.lineplot(x=df_windspeed.index, y=df_windspeed.values,
             marker='^', linestyle='--', palette='bright')
plt.xlabel('风速')
plt.ylabel('平均租车人数')
# for i in range(len(df_windspeed)):
#     plt.text(x=df_windspeed.index[i], y=df_windspeed.values[i], va='top', ha='center',
#              s=df_windspeed.values[i])
plt.show()

'''
当风速高于20时，租车数量开始降低
当风速低于20时，租车数量一致较高
'''
#%%

df_humidity = round(df.groupby(df['humidity'])['count'].mean(), 1)
sns.lineplot(x=df_humidity.index, y=df_humidity.values,
             marker='^', linestyle='--', palette='bright')
plt.xlabel('湿度')
plt.ylabel('平均租车人数')
# for i in range(len(df_windspeed)):
#     plt.text(x=df_windspeed.index[i], y=df_windspeed.values[i], va='top', ha='center',
#              s=df_windspeed.values[i])
plt.show()

'''
当湿度在20时，租车人数达到最高值
在20之后，租车人数开始逐渐降低
'''

#%%
# 温度-租车人数关系
df_temp= round(df.groupby(df['temp'])['count'].mean(), 1)
sns.lineplot(x=df_temp.index, y=df_temp.values,
             marker='^', linestyle='--', palette='bright')
plt.xlabel('温度')
plt.ylabel('平均租车人数')
# for i in range(len(df_windspeed)):
#     plt.text(x=df_windspeed.index[i], y=df_windspeed.values[i], va='top', ha='center',
#              s=df_windspeed.values[i])
plt.show()
'''
当温度在36度之前，租车人数随着温度升高而增高
当温度大于36度之后，温度越高，租车人数越少
'''

#%%
# 体感温度-租车人数关系

df_atemp= round(df.groupby(df['atemp'])['count'].mean(), 1)
sns.lineplot(x=df_atemp.index, y=df_atemp.values,
             marker='^', linestyle='--', palette='bright')
plt.xlabel('温度')
plt.ylabel('平均租车人数')
# for i in range(len(df_windspeed)):
#     plt.text(x=df_windspeed.index[i], y=df_windspeed.values[i], va='top', ha='center',
#              s=df_windspeed.values[i])
plt.show()

'''
当体感温度在40度之前，租车人数随着体感温度升高而增高
当体感温度大于40度之后，体感温度越高，租车人数越少
'''


"""
四、总结与建议
时间hour：一天中有两个租车高峰，分别是早上8时左右和下午17时，18时左右，原因是上下班高峰期用车人数增加
时间year：租车数量逐年上升
月份month：一年中夏天和秋天用车数量较高，春天租车数量较少
天气weather：晴天租车人数最高，小雨/小雪天气租车人数反而是最低的
风速speed：当风速高于20时，租车数量开始降低；当风速低于20时，租车数量一致较高
湿度humidity：当湿度在20时，租车人数达到最高值；在20之后，租车人数开始逐渐降低
温度temp：当温度在36度之前，租车人数随着温度升高而增高；当温度大于36度之后，温度越高，租车人数越少
体感温度atemp：当体感温度在40度之前，租车人数随着体感温度升高而增高；当体感温度大于40度之后，体感温度越高，租车人数越少
对于租车公司，最应该：
春冬季节的晴天时刺激用户增长
每个月份之间最大的差异在于晴天时刻租车用户的人数
当晴天时刺激租车用户数量增长，带来的收益很高
对于租车公司应该重点运营：

1. 上下班高峰期，包括12.13时的小高峰期  
2. 重点季节是夏季和秋季，大约在5-10月份  
3. 在天气较好的时期  
对于租车公司的淡季：

1. 改进共享单车，提高在小雨/小雪天气的用户使用率  
2. 推行月卡等措施，提高用户在淡季月份的共享单车使用率  
3. 做好单车的保养工作  
"""