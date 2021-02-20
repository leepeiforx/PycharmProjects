import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile as z

# %%
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\home8424.zip'
file_package = z.ZipFile(file_path)
temp_list = []
for i in range(len(file_package.filelist)):
    temp_list.append(pd.read_csv(file_package.open(file_package.filelist[i].filename)))
dftemp = pd.concat(temp_list)
print(dftemp.shape)

# %%
# print(dftemp.head())
print(dftemp.info())

# %%
# 2,对数据索引恢复，并对修改时间格式
# dftemp.reset_index()
for i in [dftemp]:
    i.index = range(dftemp.shape[0])

dftemp.info()

# %%2.1,修改时间格式
dftemp['Start date'] = pd.to_datetime(dftemp['Start date'])
dftemp['End date'] = pd.to_datetime(dftemp['End date'])

print(dftemp.info())

# %%
# 2.2,提取出2017年的月份，新建df列命名为month
dftemp['month'] = dftemp['Start date'].dt.month

# %%
print(dftemp.head())

# %%
# 2.3，Duration转换为分钟
dftemp['Duration (min)'] = dftemp['Duration (ms)'] / 1000 / 60

# %%
# 删除dftemp['Duration (ms)']
del dftemp['Duration (ms)']

# %%
print(dftemp.head())

# %%
# 2.4,先按照month分组，再按照Member typer分组
df_group = dftemp.groupby(['month', 'Member type']).count()
print(df_group)

# %%
# 恢复df_group索引
df_group = df_group.reset_index()

# %%
# 2.5，提取出“月份”，‘会员’，‘非会员’三列信息
# 方案1,数据透视表
df_pivot = pd.pivot_table(data=df_group, index='month', columns='Member type',
                          values='Duration (min)')

# 方案2,直接构造新表
df_result = pd.DataFrame({'Month': [x for x in range(1, 13)],
                          'Member': df_group[df_group['Member type'] == 'Member']['Duration (min)'].reset_index(
                              drop=True),
                          'Casual': df_group[df_group['Member type'] == 'Casual']['Duration (min)'].reset_index(
                              drop=True)})

# %%
# 3，绘制折线图，显示会员与非会员每个月的骑行时间

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

sns.lineplot(x=df_pivot.index, y='Member', data=df_pivot, label='会员骑行时间')
sns.lineplot(x=df_pivot.index, y='Casual', data=df_pivot, label='非会员骑行时间')
plt.title('2017年会员骑行时间和非会员骑行时间对比')
plt.xlabel('日期(月)')
plt.ylabel('时长(min)')
plt.legend()
plt.show()

# %%
# 4，绘制饼状图，显示会员与非会员的人数比例
df_member = dftemp['Member type'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(x=df_member.values, labels=df_member.index, explode=(0, 0.1),
        autopct='%1.1f%%', shadow=True)
plt.title('2017')
plt.show()

#%%
# 结果文件保存
dftemp.to_csv('ofo_temp')
df_group.to_excel('ofo_temp.xlsx', sheet_name='group')

