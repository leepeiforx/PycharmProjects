from common import utils as u
from common.utils import fix_matplotlib_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# 读取数据
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\2019B1631.zip'
# %%
df_dict = u.unpack_file_to_df(file_path)
data1 = df_dict['data1']
data2 = df_dict['data2']
data3 = df_dict['data3']

# %%
# 数据基本检查
print(u.show_info(data1))
print(u.show_info(data2))
print(u.show_info(data3))

# %%
# 检查重复值,NA值
print(u.show_na(data1))
print(u.show_duplicated(data1))
print(u.show_na(data2))
print(u.show_duplicated(data2))
print(u.show_na(data3))
print(u.show_duplicated(data3))

# %%
# 列重命名
data1.columns = ['序号', '校园卡号', '性别', '专业名称', '门禁卡号']
print(data1.head())

# %%
# 处理data2的数据

# 列重命名
data2.columns = ['流水号', '校园卡号', '校园卡编号', '消费时间', '消费金额', '存储金额',
                 '余额', '消费次数', '消费类型', '消费项目编码', '消费项目序列号',
                 '消费操作编码', '操作编码', '消费地点']

data2.head()

# %%
# 对data2中消费时间数据进行时间格式转换，coerce表示将无效解析设置为NaT
data2.loc[:, '消费时间'] = pd.to_datetime(data2.loc[:, '消费时间'], format='%Y/%m/%d %H:%M', errors='coerce')
data2.head()

# %%
u.show_na(data2)
# %%
# 可发现消费项目序列号、消费操作编码的缺失值过多，所以不加入后续分析
data2_new = data2.drop(columns=['消费项目序列号', '消费操作编码'])
# %%
data2['消费地点'].value_counts(dropna=False)
# %%
# 描述性统计
print(data2[['消费金额', '存储金额', '余额', '消费次数']].describe().T)

# 结果保存
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis'
data2_new.to_csv(file_path + r'\data2_new.csv', index=False, encoding='gbk')

# %%
# data3的数据处理
print(data3.shape)

print(data3.head())

print(data3.dtypes)

# %%
data3.columns = ['序号', '门禁卡号', '进出时间', '进出地点', '是否通过', '描述']

data3.loc[:, '进出时间'] = pd.to_datetime(data3.loc[:, '进出时间'], format='%Y/%m/%d %H:%M', errors='coerce')

# %%
# data3的缺失值情况
print(u.show_na(data3))

# 各个地点进出情况
print(data3['进出地点'].value_counts())

# 单独一列的所有值出现的频次
print(data3['是否通过'].value_counts(dropna=False))
# 删除是否通过中值为0的数据
# 找出正常值，覆盖原表
print('删除异常值前的数据', data3.shape)
data3 = data3[data3.loc[:, '是否通过'] != 0]
print('删除异常值后的数据', data3.shape)

# %%
# 保存数据
data3.to_csv(file_path + '/task_1_3.csv', encoding='gbk')

# %%
"""
将 data1.csv中的学生个人信息与 data2.csv中的消费记录建立关联，
处理结果保存为“task1_2_1.csv”；将 data1.csv 中的学生个人信息与data3.csv 
中的门禁进出记录建立关联，处理结果保存为“task1_2_2.csv”。
"""
data1_merge_data2 = pd.merge(data1, data2_new, how='left', on='校园卡号')
# %%
print(data1_merge_data2.shape)
print(data1_merge_data2.tail())
print(u.show_na(data1_merge_data2))

# 删除缺失值
print('删除缺省值前的数据', data1_merge_data2.shape)
data1_merge_data2.dropna(subset=['消费地点'], how='any', inplace=True)
data1_merge_data2.to_csv(file_path + '/task_2_1.csv', encoding='gbk')

# %%
# data1连接data3
data1_merge_data3 = pd.merge(data1, data3, how='left', on='门禁卡号')

# %%
print(data1_merge_data3.tail())
print(u.show_na(data1_merge_data3))

print('删除缺省值前的数据', data1_merge_data3.shape)
data1_merge_data3.dropna(subset=['进出地点'], how='any', inplace=True)
print('删除缺省值后的数据', data1_merge_data3.shape)
data1_merge_data3.to_csv(file_path + '/task_3_1.csv', encoding='gbk')

# %%
# 食堂就餐行为分析
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis'
data = pd.read_csv(file_path + '/task_2_1.csv', encoding='gbk')
# %%
df_canteen = data['消费地点'][data['消费地点'].str.contains('食堂')].value_counts()

fix_matplotlib_error()
plt.figure(figsize=(10, 6), dpi=50)
plt.pie(x=df_canteen.values, labels=df_canteen.index, autopct='%1.2f%%', shadow=False,
        startangle=90)
plt.legend(loc='best')
plt.title('食堂就餐人次占比饼图')
# 饼图保持圆形
plt.axis('equal')
plt.show()

# %%
# 通过食堂刷卡记录，分别绘制工作日和非工作日食堂就餐时间曲线图，
# 分析食堂早中晚餐的就餐峰值，并在报告中进行描述。
data.loc[:, '消费时间'] = pd.to_datetime(data.loc[:, '消费时间'],
                                     format='%Y-%m-%d %H:%M', errors='coerce')
# 创建一个消费星期列，根据消费时间计算出消费时间是星期几，Monday=1, Sunday=7
data['消费星期'] = data['消费时间'].dt.dayofweek + 1


# %%
# 以周一至周五作为工作日，周六日作为非工作日，拆分为两组数据
def work_or_relax(tab):
    if tab <= 5:
        return 'work'
    else:
        return 'relax'


# 注:
'''
map() 是一个Series的函数，DataFrame结构中没有map()。
map()将一个自定义函数应用于Series结构中的每个元素(elements)。
apply()将一个函数作用于DataFrame中的每个行或者列
applymap（）
将函数做用于DataFrame中的所有元素(elements)
'''
data['work_or_relax'] = data['消费星期'].map(work_or_relax)
# %%
# 计算周内&周末对应24小时区间内的消费次数
df_workday = pd.pivot_table(data=data[data['work_or_relax'] == 'work'],
                            index=data['消费时间'].dt.hour, aggfunc='count'
                            )['校园卡号']
# 周末
df_dayoff = pd.pivot_table(data=data[data['work_or_relax'] == 'relax'],
                           index=data['消费时间'].dt.hour, aggfunc='count'
                           )['校园卡号']
x = []
for i in range(24):
    x.append('{:02d}:00'.format(i))
plt.figure(figsize=(12, 6))
plt.plot(x, df_workday, label='周内')
plt.plot(df_dayoff, label='周末')
plt.xlabel('时间')
plt.xticks(rotation=60)
plt.ylabel('次数')
plt.legend(loc='best')
plt.show()

# %%
# 任务 3 学生消费行为分析
file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis'
data = pd.read_csv(file_path + '/task_2_1.csv', encoding='gbk')

# %%
# 计算人均刷卡频次(总刷卡次数/学生总人数)
cost_count = data['消费金额'].count()
student_count = data['校园卡号'].value_counts(dropna=False).count()
average_cost_count = round(cost_count / student_count)
print(average_cost_count)

average_cost_money = round(data['消费金额'].sum() / student_count)

# %%
# 选择消费次数最多的3个专业进行分析
df_cost = data['专业名称'].value_counts(dropna=False, ascending=False)[:3]
df = pd.DataFrame(columns=data.columns)
df_cost = data[data['专业名称'].isin([i for i in df_cost.index])]

# %%
# 分析 每个专业，不同性别 的学生消费特点
df_pivot = pd.pivot_table(data=data, index=['校园卡号', '性别'],
                          values=['消费金额', '消费次数'], aggfunc={'消费金额': np.sum,
                                                            '消费次数': 'count'})
df_pivot.reset_index(inplace=True)
df_pivot['性别'].replace({'男': 1, '女': 0}, inplace=True)

# %%
# 构建聚类模型
from sklearn.cluster import KMeans

# k为聚类类别，iteration为聚类最大循环次数，data_zs为标准化后的数据
k = 3  # 分成几类可以在此处调整
iteration = 500
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration, random_state=0)
model.fit(df_pivot)

# r1统计各个类别的数目，r2找出聚类中心
r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r2, r1], axis=1)
r.columns = list(df_pivot.columns) + ['类别数目']
print(r)

# %%
# 分析每一类学生群体的消费特点
# 可以根据 聚类类别 分表画图进行分析
# 通过对低消费学生群体的行为进行分析，探讨是否存在某些特征，能为学校助学金评定提供参考
data_500 = data.groupby('校园卡号').sum()[['消费金额']]
data_500.sort_values(by='消费金额', ascending=True, inplace=True)
data_500 = data_500.head(500)
data_500_index = data_500.index.values
data_500 = data[data['校园卡号'].isin(data_500_index)]

# %%
# 取出最低消费500人的最频繁的消费地点，并添加一列
# data_500.drop(columns=['Unnamed: 0'],inplace=True)
# data_500 = data_500['消费地点'].value_counts()[:10]

# 创建画布
u.fix_matplotlib_error()
plt.figure(figsize=(10, 6), dpi=50)
# 绘制饼图
plt.pie(data_500, labels=data_500.index, autopct='%1.2f%%', shadow=False, startangle=90)
# 显示图例
plt.legend(loc='best')
# 添加标题
plt.title("低消费学生常消费地点占比饼图")
# 饼图保持圆形
plt.axis('equal')
# 显示图像
plt.show()
