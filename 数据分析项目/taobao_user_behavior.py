import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'H:\下载\dataset1855.zip'
df = pd.read_csv(file_path)
print(df.head())

# 检查重复值
print(len(df[df.duplicated().values == True]))
print(len(df))

# 删除重复值
df.drop_duplicates(inplace=True)
print(len(df))

# 检查缺失值
df.isna().sum()
# 缺失值集中在用户地理信息列，故删去
del df['user_geohash']

# 将item_category拆分成time和hour
df['date'] = df['time'].str.split(' ').str[0]
df['hour'] = df['time'].str.split(' ').str[1]
#
df['date'] = pd.to_datetime(df['date'])

# reset index
print(df.info())
df.reset_index(drop=True, inplace=True)

# %%,抽检部分数据实验代码，后续再使用全部数据(随机抽取1000个）
df_random = df.loc[np.random.randint(0, len(df), 1000), :]
df_random.reset_index(drop=True, inplace=True)
# %%
# 五、分析过程
# 1.流量指标特征(uv,pv)
pv_daily = df[df['behavior_type'] == 1].groupby('date'). \
    count()['user_id']. \
    reset_index().rename(
    columns={'user_id': 'pv'})
uv_daily = df.groupby('date'). \
    nunique()['user_id'].reset_index(). \
    rename(columns={'user_id': 'uv'})

# %%
# 绘图

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

plt.figure(figsize=(10, 6))
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
pv_daily.plot(x='date', y='pv', ax=axes[0])
uv_daily.plot(x='date', y='uv', ax=axes[1])
plt.show()

'观察结果：在该月内，访问量和用户量整体缓慢攀升，并在双十二期间达到峰值，可见双十二的活动效果明显。'

# %%
# 1.2 时段流量指标
pv_hour = df[df['behavior_type'] == 1].groupby('hour'). \
    count()['user_id']. \
    reset_index().rename(
    columns={'user_id': 'pv'})
uv_hour = df.groupby('hour'). \
    nunique()['user_id'].reset_index(). \
    rename(columns={'user_id': 'uv'})

plt.figure(figsize=(10, 6))
_, axes = plt.subplots(2, 1, figsize=(12, 8))
pv_hour.plot(x='hour', y='pv', ax=axes[0])
uv_hour.plot(x='hour', y='uv', ax=axes[1])
plt.show()

'''
观察结果：23点到次日5点的访问量和用户量都在下降，5点到18点回升到相对稳定的水平；
18点到22点访问量有比较明显的提升，并在21点和22点达到峰值，而用户量的趋势类似，
但相对不那么明显。
小结：18-22点为用户活跃时段，5-18点为用户一般活跃时段，23-5点为用户非活跃时段。
'''

# %%
# 2. 用户购买情况分析
buy_daily = df[df['behavior_type'] == 4].groupby('date').count()['behavior_type']

# 付费率= 付费人数/活跃人数
paying_user = df[df['behavior_type'] == 4].groupby('date').nunique()['user_id']
active_user = df.groupby('date')['user_id'].nunique()

paying_rate = paying_user / active_user

paying_rate.fillna(value=0, inplace=True)

# 绘图
plt.figure(figsize=(40, 10))
_, axes = plt.subplots(2, 1)
axes[0].plot(buy_daily)
axes[0].set_ylabel('buy')
axes[0].set_title('buy_daily')

axes[1].plot(paying_rate)
axes[1].set_ylabel('paying_rate')
axes[1].set_title('paying_rate_daily')
plt.show()

'''
观察结果：成交量和付费率总体上维持在一个稳定的水平，在双十二当天均达到峰值。
小结：成交量的走势与pv/uv走势基本一致，印证了用户流量与成交量的正向关系，
而付费率在双十二当天骤升近50%则说明了双十二活动对提升用户付费率的效果明显。
'''

# %%
# 2.2 用户购买次数分析
# 用户购买次数分布
user_buy_time = df[df['behavior_type'] == 4]. \
    groupby('user_id').count()['item_id']

plt.hist(user_buy_time, bins=10, range=[0, 100])
plt.xlabel('buy_time')
plt.ylabel('num_of_user')
plt.title('user_buy_time')
plt.show()

# %%
# 复购率
# 复购率=购买次数在2次及以上的人数/有购买行为的人数

user_buy_time = user_buy_time.reset_index()
user_mulbuy = user_buy_time[user_buy_time['item_id'] > 2].count()['item_id']
user_buy = df[df['behavior_type'] == 4].nunique()['user_id']
rebuy_rate = user_mulbuy / user_buy
print(rebuy_rate)

# %%
# 用户行为漏斗分析
conversion_funnal = df['behavior_type'].value_counts()
# 点击转化率
pv_favor = conversion_funnal[2] / conversion_funnal[1] * 100
pv_cart = conversion_funnal[3] / conversion_funnal[1] * 100
pv_buy = conversion_funnal[4] / conversion_funnal[1] * 100
print('点击——收藏转化率:', '%.2f' % pv_favor, '%')
print('点击——购物车转化率：', '%.2f' % pv_cart, '%')
print('点击——支付转化率：', '%.2f' % pv_buy, '%')

# 3.2收藏/购物车转化率
favor_cart_buy = conversion_funnal[4] / (conversion_funnal[2] + conversion_funnal[3]) * 100
print('收藏——支付转化率：', '%.2f' % favor_cart_buy, '%')

# %%
# 4.使用RFM模型进行用户价值分类
# 由于本数据集没有消费金额数据，故只针对RF维度进行分析
# 构造R值
latest_time = df[df['behavior_type'] == 4].groupby('user_id').max()['date']
# 这里创建副本是为了防止下面用索引设置R值的时候出现链式赋值警告.

recency = (pd.to_datetime('2014-12-18') - latest_time).dt.days.copy()
recency_avg = recency.mean()
recency[recency < recency_avg] = 0
recency[recency > recency_avg] = 1

# 构建F值
frequency = df[df.behavior_type == 4].groupby('user_id').count()['item_id'].copy()
frq_avg = frequency.mean()
frequency[frequency < frq_avg] = 0
frequency[frequency > frq_avg] = 1

rfm = pd.merge(recency, frequency, on='user_id', how='inner')
rfm = rfm.reset_index().rename(columns={'date': 'r', 'item_id': 'f'})
rfm = rfm[['r', 'f']].astype('str')
rfm['user_type'] = rfm['r'] + rfm['f']
rfmg = rfm.groupby('user_type').count()['r'].sort_index(ascending=False).rename(
    index={'11': '重要价值用户：', '10': '重要发展用户：', '01': '重要保持用户：', '00': '重要挽留用户：'})
print(rfmg)
"""
重点价值用户是最重要的用户群体，但数量较少，只有464人，而其余类型的用户群体数量相当，均有2000人以上的规模，
需针对用户群体特点针对性采取运营措施。
结论：
1）重要价值用户是最优质的用户群体，应重点关注，既要保持其粘性，又要继续引导消费，可为这类用户提供vip服务；
2）重要发展用户的特点是近期有消费但频次不高，策略是提高其消费次数，具体措施有促销活动提醒和优惠卷活动等；
3）重要保持用户的特点是消费频次高但有一段时间没有消费，策略是重新唤醒，通过app消息推送，以及站外广告营销吸引其注意力，促进复购；
4）重要挽留用户近期没有消费且频次不高，若不加以挽留，会有流失的可能，对于这类用户一方面需要保持曝光量，
持续推送活动和优惠信息，另一方面需要进一步研究其兴趣和需求，才能采取有效的运营策略。
"""
