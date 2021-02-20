import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile as zp

# %%
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\didi4010.zip'
file = zp.ZipFile(file_path)
temp_list = []
for f in file.filelist:
    temp_list.append((f.filename.split('.')[0], f.filename))
temp_dict = {}
for f in temp_list:
    filename = f[0]
    file_values = pd.read_excel(file.open(f[1]))
    temp_dict[filename] = file_values

# %%
print(temp_dict.keys())
city = temp_dict['city']
test = temp_dict['test']
print(test.head())

# %%
# 计算ROI
test['ROI'] = test['gmv'] / (test['coupon per trip'] * test['trips'])
test.head()

# %%
# requests检验
'''
记两组requests方差分别为c1,c2
零假设H0：c1=c2；备选假设H1：c1≠c2
显著性水平取0.05
'''
requests_A = test[test['group'] == 'control']['requests']
requests_B = test[test['group'] == 'experiment']['requests']

import scipy.stats as st

print(st.levene(requests_A, requests_B).pvalue)

# p值大于0.05，不拒绝原假设，因此可认为两组实验requests齐方差。

# %%
# 3.2 requests均值检验
'''
该数据为同一样本实验前后的不同水平，因此选用配对样本t检验。
记两组requests均值分别为u1,u2
零假设H0：u1=u2；备选假设H1：u1≠u2
显著性水平取0.05
'''
test['group'].value_counts()

# #配对样本t检验（两独立样本t检验之前需检验是否齐方差，此处不需要）
print(st.ttest_rel(requests_A, requests_B).pvalue)
# p值大于0.05，不拒绝原假设，因此可认为实验条件对requests影响不显著。

# %%
# 4 gmv检验
'同理对gmv进行方差和均值检验。'

# gmv方差检验
gmv_A = test[test['group'] == 'control']['gmv']
gmv_B = test[test['group'] == 'experiment']['gmv']
print(st.levene(gmv_A, gmv_B).pvalue)
# p值大于0.05，不拒绝原假设，因此可认为两组实验gmv齐方差。

# gmv均值检验
print(st.ttest_rel(gmv_A, gmv_B).pvalue)
# p值小于0.05，拒绝原假设，因此可认为实验条件对gmv有显著影响。

# %%
# ROI检验
# 同理对ROI进行j方差和均值检验。
# ROI方差检验
roi_A = test[test['group'] == 'control']['ROI']
roi_B = test[test['group'] == 'experiment']['ROI']
print(st.levene(roi_A, roi_B).pvalue)
# p值大于0.05，不拒绝原假设，因此可认为两组实验ROI齐方差。

# ROI均值检验
print(st.ttest_rel(roi_A, roi_B).pvalue)
# p值小于0.05，拒绝原假设，因此可认为实验条件对ROI有显著影响。

# %%
# 城市运营分析
# 1.常规查看(NA值,重复值,字段属性,描述性统计等)
print(city.head())
print(city.info())
print(city.isna().sum())
print('重复记录数: ', len(city[city.duplicated().values == True]))

# %%
# 2 数据探索
req_hour = city.groupby('hour').sum()[['requests']]
# req_hour = city.groupby('hour').agg({'requests': sum})
print(req_hour)

# %%
# 绘制各时点订单请求柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

req_hour.plot(kind='bar')
plt.xticks(rotation=0)
plt.title('各时点订单请求对比')
plt.show()

'''
可见，在11、12、13这三个时间点内，12点用户发起订单的需求是最大的，其次是13点，11点。
司机运营平台应考虑加大该时点车辆供应。
'''
# %%
# 2.2 单量最多的日期
req_date = city.groupby(by=city['date'].dt.weekday)['requests'].sum()
req_date.plot(kind='line')
plt.title('各天订单情况')
plt.show()

'''
单月订单请求数随日期的变化呈周期性变化，我们猜测4个峰值分别对应4个周末，
周末用户出行需求较大。
经验证发现猜想与数据吻合，因此司机运营平台应考虑加大周末、节假日的车辆供给
'''
# %%
com_hour = pd.pivot_table(data=city, index='hour',
                          values=['requests', 'trips'],
                          aggfunc={'requests': np.sum, 'trips': np.sum})
com_hour['rate'] = com_hour['trips']/com_hour['requests']

com_hour

#%%
# 2.4 单月每日订单完成率
com_date = pd.pivot_table(data=city, index=city['date'].dt.day,
                          values=['requests', 'trips'],
                          aggfunc={'requests': np.sum, 'trips': np.sum})
com_date['rate'] = com_date['trips']/com_date['requests']

#绘制订单完成率随日期变化的折线图
com_date['rate'].plot(kind='line')
plt.title('每日订单完成率情况')
plt.show()

'单月每日订单完成率规律不太明显，但几个谷值基本都出现在周末附近，' \
'说明客户出行需求的提升可能导致响应率的降低。'

#%%
# 2.5 顾客等待时间
eta_hour = city.groupby('hour')[['pETA', 'aETA']].mean()


#绘制顾客等待时长复合柱状图
eta_hour.plot(kind='bar')
plt.title('顾客等待时长')
plt.xticks(rotation=0)
plt.show()

'''
以上可见，无论哪个时点，用户实际等待时长均明显大于用户预计等待时长。
各时点用户等待时长差异不明显，但13点最高。
客运部一方面应提升用户预计等待时长的准确性，另一方面优化平台派单逻辑等。
'''

#%%
# 2.6 司机在忙率
city['busy'] = city['supply hours'] * city['utiliz']
busy_hour = city.groupby('hour')[['supply hours', 'busy']].sum()
busy_hour['utiliz'] = busy_hour['busy'] / busy_hour['supply hours']

'12点司机在忙总时长最长，在忙率也最高，用户订单请求也最多，说明车辆总数偏少。'

#%%
# 2.7 订单时长

trip_min = city.groupby('hour')['average minutes of trips'].mean()
trip_min

'12点用户订单需求较多，同时订单时长最长，说明这个时间点是一个非常重要的时间点。'
supply_hours = city.groupby('hour')['supply hours'].mean()
supply_hours

'''
13点订单量也较大，此时点司机服务时长较短。
为优化用户出行体验，司机运营平台可联合客运部可考虑此时段尽量分配
总服务时长较长的司机来接单（经验较为丰富）。
'''

'''
3 后续思考方向
提升顾客预计等待时长预测准确度（需要历史数据进行预测）
加大车辆投入（分车辆不同等级来看，因此可能需要车辆相关信息表）
优化用户体验（需要客诉相关数据）
优化平台派单逻辑（需要订单的位置相关数据）
个性化需求（需要用户属性、及其他行为数据）
'''