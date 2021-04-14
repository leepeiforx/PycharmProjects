# 第一节 分布数列
# 1.1 连续型变量分布数列的编制

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from common import utils as ut

# %%
file_path = r'数据分析项目/database/ad_performance.csv'
df = pd.read_csv(file_path)

print(df['日均UV'].max())

# 利用pandas的cut方法进行分组
ut.fix_matplotlib_error()
bins = range(0, 25501, 500)
uv_bins = pd.cut(df['日均UV'], bins, right=False)
uv_bins = uv_bins.value_counts().reset_index().sort_values(by='index')
uv_bins.rename(columns={'日均UV': 'ct'}, inplace=True)
sns.barplot(data=uv_bins, x='index', y='ct')
plt.show()
#
# 计算频率、向上累计及向下累计，看结果就很容易理解了。
uv_bins['percentage'] = uv_bins['ct'] / sum(uv_bins['ct'])
uv_bins['cumsum_up'] = uv_bins['ct'].cumsum()
uv_bins['cumsum_down'] = uv_bins['ct'][::-1].cumsum()

# %%
# 离散变量分布数列的编制
df['广告类型'].value_counts()

# 总结：其实就是 value_counts()这个函数的运用

# 第二节 统计图
# 参考matplotlib,seaborn,pyecharts

# %%
# 第三节 描述统计量
# 平均数
print('平均数', df['投放总时间'].mean())
# 中位数
print('中位数', df['投放总时间'].median())
# 众数
print('众数', df['投放总时间'].mode())
# 标准差
print('标准差', df['投放总时间'].std())
# 方差
print('方差', df['投放总时间'].var())
# 峰度
print('峰度', df['投放总时间'].kurt())
# 偏度
print('偏度', df['投放总时间'].skew())

df_adtime = df['投放总时间'].value_counts().reset_index()
sns.barplot(data=df_adtime, x='index', y='投放总时间')
plt.show()

# 最值(大/小)
print('最大值', df['投放总时间'].max())
print('最小值', df['投放总时间'].min())

# 区间
print('区间', df['投放总时间'].max() - df['投放总时间'].min())

# 求和
print('求和', df['投放总时间'].sum())

# 计数
print('计数', df['投放总时间'].count())

# 标准误差
se = np.sqrt(df['投放总时间'].var() / df['投放总时间'].count())
print('标准误差:', se)

# 置信度(95%)
score_confidence = 2.005745995 * se

# %%
# 使用分类汇总计算描述统计量
# 使用pandas的groupby进行分组聚类，并计算每组平均值
ad_type = df.groupby('合作方式')['广告类型'].count()
ad_type.mean()
# 还可以用sum、count等方法进行不同的分类汇总

# %%
# 使用数据透视表方法计算描述统计量
pivot_table = pd.pivot_table(data=df, index='合作方式', columns='广告卖点', values='渠道代号', aggfunc='count')

# %%
df.columns
