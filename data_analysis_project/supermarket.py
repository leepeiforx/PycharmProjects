import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts.charts import *
import pyecharts.options as opts

# %%
file_path = r'C:\Users\bolat\Desktop\supermarket.xls'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

df1 = pd.read_excel(file_path, sheet_name='订单')
df2 = pd.read_excel(file_path, sheet_name='销售人员')

# %%
# 对订单数据进行处理，删掉不需要的指标
df3 = df1.drop(['行 ID', '订单 ID', '客户 ID', '产品名称'], axis=1)
# df3.shape

# %%
# 合并表
df = pd.merge(df3, df2, how='left', on='地区')

# df.shape

df.sample(10)

# %%
# 数据缺失情况
df.isnull().sum()

# %%
# 查看数据的描述统计
df.describe()
# 查看各个字段属性
df.info()


# %%
# 销售额分析

def sum_by_group(df, data, kind, calu='sum()'):
    print(df[data].groupby(df[kind]).calu)
    return df[data].groupby(df[kind]).calu


# seals_year = df['销售额'].groupby([df['订单日期'].dt.year, df['订单日期'].dt.month]).sum()
seals_by_year = df['销售额'].groupby(df['订单日期'].dt.year).sum()

# bar = (Bar()
#        .add_xaxis(date)
#        .add_yaxis('', data, label_opts=opts.LabelOpts(is_show=False))
#        )
# bar.render()

plt.figure(figsize=(16, 12))
sns.barplot(x=seals_by_year.index, y=seals_by_year.values)
plt.show()

plt.figure(figsize=(16, 12))
plt.bar(x=seals_by_year.index, height=seals_by_year.values)
plt.xticks(seals_by_year.index, labels=['2015年', '2016年', '2017年', '2018年'])
plt.ylabel('销售额(元)')
for x, y in zip(seals_by_year.index, seals_by_year.values):
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom', fontsize=10)
plt.show()

# %%
# 各省份销售贡献情况
# 山东、广东、黑龙江是销售额前三省份，处于第一梯队；辽宁、河南和河北处于第二梯队
seals_by_pro = sum_by_group(df, '销售额', '地区').sort_values()
plt.figure(figsize=(16, 12))
plt.barh(y=seals_by_pro.index, width=seals_by_pro.values, height=.5, alpha=.5, color='b')
plt.ylabel('省份')
plt.xlabel('销售额(元)')
for y, x in enumerate(seals_by_pro.values):
    plt.text(x + 500, y - 0.2, '%0.2f' % x)
plt.show()

# %%
# 不同业务员销售情况
plt.figure()
seals_by_pe = sum_by_group(df, '销售额', '地区经理').sort_values()
plt.bar(x=seals_by_pe.index, height=seals_by_pe.values, width=.8, alpha=.5, color='r')
plt.ylabel('销售额(元')
for x, y in zip(seals_by_pe.index, seals_by_pe.values):
    plt.text(x, y + .05, '%0.2f' % y, ha='center', va='bottom', fontsize='10')
plt.show()

# %%
# 不同类别销售额贡献情况
seals_by_kind = sum_by_group(df, '销售额', '类别').sort_values()
plt.bar(x=seals_by_kind.index, height=seals_by_kind.values, width=.8, alpha=.5, color='g')
plt.ylabel('销售额(元')
for x, y in zip(seals_by_kind.index, seals_by_kind.values):
    plt.text(x, y + .05, '%0.2f' % y, ha='center', va='bottom', fontsize='10')
plt.show()

# %%
# 不同邮寄方式销售额贡献情况
seals_by_sendway = sum_by_group(df, '销售额', '邮寄方式').sort_values()
plt.bar(x=seals_by_sendway.index, height=seals_by_sendway.values,
        width=.8, alpha=.5, color='g')
plt.ylabel('销售额(元')
for x, y in zip(seals_by_sendway.index, seals_by_sendway.values):
    plt.text(x, y + .05, '%0.2f' % y, ha='center', va='bottom', fontsize='10')
plt.show()

# %%
# 利润额分析

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='利润', y='销售额', alpha=.5, color='g')
plt.xlabel('利润')
plt.ylabel('销售额(元)')
plt.show()

# %%
# 利润额随时间变化
plt.figure(figsize=(10, 5))
prf_by_time = df['利润'].groupby(df['订单日期'].dt.year).sum()
plt.bar(x=prf_by_time.index, height=prf_by_time.values, width=.8, alpha=.5, color='b')
plt.ylabel('利润')
plt.xticks(prf_by_time.index, labels=['2015年', '2016年', '2017年', '2018年'])
for x, y in zip(prf_by_time.index, prf_by_time.values):
    plt.text(x, y + 0.05, '%0.2f' % y, ha='center', va='bottom', fontsize=10)

plt.show()

# %%
# 各大区利润贡献情况
plt.figure(figsize=(10, 5))
prf_by_area = sum_by_group(df, '利润', '地区').sort_values(ascending=False)
sns.barplot(y=prf_by_area.index, x=prf_by_area.values, color='g')
plt.xlabel('利润')
# for y,x in enumerate(prf_by_pro.values):
#     plt.text(y,x,'%.2f'%x)
plt.show()

# %%
# 各省利润贡献情况
plt.figure(figsize=(10, 5))
prf_by_pro = sum_by_group(df, '利润', '省/自治区').sort_values(ascending=False)
sns.barplot(y=prf_by_pro.index, x=prf_by_pro.values, color='g')
plt.xlabel('利润')
# for y,x in enumerate(prf_by_pro.values):
#     plt.text(y,x,'%.2f'%x)
plt.show()

# %%
# 各业务员利润贡献情况
prf_by_peo = sum_by_group(df, '利润', '地区经理')

x_data = list(prf_by_peo.index)
y_data = [round(item, 2) for item in prf_by_peo.values]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data, label_opts=opts.LabelOpts(formatter='{c}'))
       )
bar.render()

# %%
# 不同类别利润贡献情况
plt.figure(figsize=(10, 5))
prf_by_kind = df['利润'].groupby(by=[df['类别'], df['子类别']]).sum()
item = [item[0] + '/' + item[1] for item in prf_by_kind.index]
plt.bar(x=item, height=prf_by_kind.values)
for x, y in zip(item, prf_by_kind.values):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.title('sum_group')
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='子类别', y='利润', hue='子类别', ci=None, estimator=np.sum)
plt.title('sum')
plt.show()

plt.figure(figsize=(10, 5))
prf_by_kind = df['利润'].groupby(by=[df['类别'], df['子类别']]).sum()
sns.barplot(data=df, x='子类别', y='利润', hue='类别', ci=None, estimator=np.mean)
plt.title('mean')
plt.show()

bar = (Bar()
       .add_xaxis(list(prf_by_kind.index))
       .add_yaxis('', list(prf_by_kind.values))
       )
bar.render()

# %%
# 不同邮寄方式对利润贡献情况
prf_by_peo = sum_by_group(df, '利润', '地区经理')

plt.bar(x=prf_by_peo.index, height=prf_by_peo.values, width=.5, alpha=.5)
plt.bar('利润(元)')

plt.show()

# %%
# 交叉分析
# 各省各分类产品销售额情况

pivot_table = pd.pivot_table(data=df, values='销售额', index='省/自治区',
                             columns='类别', aggfunc=np.sum)
pivot_table

plt.figure(figsize=(10, 10), dpi=80)

sns.heatmap(data=pivot_table, annot=True,
            annot_kws={'size': 9, 'weight': 'bold', 'color': 'black'}, cmap='rainbow')
plt.show()

# %%
# 各省各分类产品利润情况
pivot_pro = pd.pivot_table(data=df, values='利润', index='省/自治区',
                           columns='类别', aggfunc=np.sum)

plt.figure(figsize=(10, 10), dpi=80)

sns.heatmap(data=pivot_pro, annot=True,
            annot_kws={'size': 9, 'weight': 'bold', 'color': 'black'}, cmap='rainbow')
plt.show()

# %%
# 销售额、利润额、销售经理交叉

pivot_table = pd.pivot_table(data=df, values=['利润', '销售额'],
                             index=['类别', '地区经理'], aggfunc=np.sum)

plt.figure(figsize=(10, 5), dpi=80)
sns.barplot(x='地区经理', y='利润', hue='类别', data=df, estimator=np.sum)
sns.lineplot(x='地区经理', y='销售额', hue='类别', data=df,
             estimator=np.sum, ci=0)
plt.show()

# %%
# 地区、分类、销售额、利润交叉表
pivot_table = pd.pivot_table(df, values=['销售额', '利润'],
                             index=['地区', '类别'], aggfunc=np.sum)

profit = [round(item[1], 2) for item in pivot_table.values]
sales = [round(item[0], 2) for item in pivot_table.values]

bar = (Bar()
       .add_xaxis(list(pivot_table.index))
       .add_yaxis('profit', profit)
       .add_yaxis('sales', sales)
       .set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False)))

bar.render()
