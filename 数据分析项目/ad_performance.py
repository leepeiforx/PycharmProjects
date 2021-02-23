import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pyecharts.charts import *
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score  # 导入轮廓系数指标
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

import common.utils as utils

file_path = r'数据分析项目/database/ad_performance.csv'
pd.set_option('display.max_columns', None)  # 设置显示所有字段
df = pd.read_csv(file_path)
df.drop(columns=['Unnamed: 0'], inplace=True)
utils.fix_matplotlib_error()  # 解决matplotlib中的中文乱码问题

# 检查数据的NA值,描述性统计,重复值情况
print(utils.show_na(df))
print(utils.show_info(df))  # 平均停留时间字段存在2个缺失值
print(utils.show_duplicated(df))

# %%
# 缺失值数据查看
df[df['平均停留时间'].isna()]

# 删除包含缺失值的记录
df = df[~df['平均停留时间'].isna()]
df.reset_index(inplace=True, drop=True)

# 各字段相关性展示
corr = df.corr().round(2)
sns.heatmap(corr, cmap='Blues', annot=True)
plt.show()

# %%
data = []
for x in range(corr.shape[0]):
    for y in range(corr.shape[1]):
        data.append([x, y, corr.iloc[x, y] * 100])
heatmap = (
    HeatMap()
        .add_xaxis(xaxis_data=corr.index.to_list())
        .add_yaxis('', yaxis_data=corr.index.to_list(), value=data)
)
heatmap.render()
"""
可以看到，“访问深度”和“平均停留时间”相关性比较高，相关性高说明两个变量在建
立模型的时候，作用是一样或者效果是一样的，可以考虑组合或者删除其一。
"""

# %%
# 数据处理
# 1.缺失值处理(前面已经做了,这里省略)

# 2.独热编码
cols = df.columns[-5:].to_list()

model_ohe = OneHotEncoder(sparse=False)  # 建立OneHotEncoder对象
ohe_matrix = model_ohe.fit_transform(df[cols])

# 3.数据标准化：
cols = df.columns[1:-5].to_list()
model_scaler = MinMaxScaler()
scaler_matrix = model_scaler.fit_transform(df[cols])

# 4.分类数据和数值数据合并
X = np.hstack((scaler_matrix, ohe_matrix))

# %%
# 建立模型
# 通过平均轮廓系数检验得到最佳Kmeans聚类模型
score_list = []  # 存储每个k下模型的平均轮廓系数
silhouette_int = -1  # 初始化的平均轮廓系数阀值
for n_cluster in range(2, 8):  # 遍历2~7几个有限组
    model_kmeans = KMeans(n_clusters=n_cluster)
    labels_temp = model_kmeans.fit_predict(X)  # 训练聚类模型
    silhouette_temp = silhouette_score(X, labels_temp)  # 得到每个k下面的平均轮廓系数
    if silhouette_temp > silhouette_int:
        best_k = n_cluster  # 保存最佳值k
        silhouette_int = silhouette_temp  # 保存平均轮廓系数得分
        best_kmeans = model_kmeans  # 保存模型实例对象
        cluster_labels_k = labels_temp  # 保存聚类标签
    score_list.append([n_cluster, silhouette_temp])  # 将每次k及得分追加到列表中
print('{}'.format('k值对应的轮廓系数'))
print(np.array(score_list))
print('最优的k值是{},\n对应轮廓系数是{}'.format(best_k, silhouette_int))

"""总体思想（评价指标）还是怎么聚才能使得簇内距离足够小，簇与簇之间平均距离足够大来评判。"""

# %%
# 聚类结果特征分析与展示
cluster_labels = pd.DataFrame(cluster_labels_k, columns=['clusters'])
merge_data = pd.concat((df, cluster_labels), axis=1)

cluster_count = pd.DataFrame(merge_data.groupby(merge_data['clusters'])['渠道代号']
                             .count()).T.rename(index={'渠道代号': 'count'})

cluster_ratio = (cluster_count / int(cluster_count.sum(axis=1))) \
    .round(2).rename(index={'count': 'percentage'})
# %%
# 计算各个聚类类别内部最显著特征值
cluster_features = []
for i in range(best_k):
    label_data = merge_data[merge_data['clusters'] == i]  # 获取特定分类的数据
    part1_data = label_data.iloc[:, 1:-6]  # 获取数据型数据特征
    part1_desc = part1_data.describe().round(3)  # 得到数据型数据的描述性统计

    merge_data1 = part1_desc.iloc[2, :]  # 得到数值型特征的均值

    part2_data = label_data.iloc[:, -6:-1]
    part2_desc = part2_data.describe(include='all')  # 获得字符串数据类型的描述性统计
    merge_data2 = part2_desc.iloc[2, :]  # 得到字符型特征的均值
    merge_line = pd.concat((merge_data1, merge_data2))  # 将数值型特征(均值)和字符型特征(均值)按行合并
    cluster_features.append(merge_line)
    print(part1_desc, part2_desc)

cluster_pd = pd.DataFrame(cluster_features).T  # 将列表转化为DataFrame
print('{}'.format('每个类别的主要特征'))
all_cluster_set = pd.concat((cluster_count, cluster_ratio, cluster_pd))

# %%
# 可视化输出
num_sets = cluster_pd.iloc[:7, :].T.astype(np.float64)  # 获取要可视化的数据
num_sets_scaler = model_scaler.fit_transform(num_sets)  # 获取标准化后的数据
num_sets_scaler = pd.DataFrame(num_sets_scaler)

c_schema = [{'name': '日均UV', 'max': 1, 'min': 0},
            {'name': '平均注册率', 'max': 1, 'min': 0},
            {'name': '平均搜索量', 'max': 1, 'min': 0},
            {'name': '访问深度', 'max': 1, 'min': 0},
            {'name': '平均停留时间', 'max': 1, 'min': 0},
            {'name': '订单转化率', 'max': 1, 'min': 0}]
# 画图
rader = (
    Radar()
        .add_schema(schema=c_schema, shape='polygon')
        .add('0分组', [num_sets_scaler.iloc[0, :].to_list()], color="#f9713c")
        .add('1分组', [num_sets_scaler.iloc[1, :].to_list()], color="#4169E1")
        .add('2分组', [num_sets_scaler.iloc[2, :].to_list()], color="#00BFFF")
        .add('3分组', [num_sets_scaler.iloc[3, :].to_list()], color="#b3e4a1")
)
rader.render()
