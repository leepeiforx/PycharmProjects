import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import *
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

from common import utils

# %%
file_path = r'数据分析项目/database/bilibili2019-1_2020-3.csv'
df = pd.read_csv(file_path)

# %%
print(utils.show_na(df))
print(utils.show_info(df))
print(utils.show_duplicated(df))

# %%
"""
IFL模型
I(Interaction_rate)：
I值反映的是平均每个视频的互动率，互动率越高，表明其视频更能产生用户的共鸣，使其有话题感。
**I=(总弹幕数+总评论数)/总播放量/统计范围内视频数量
F(Frequence)：
F值表示的是每个视频的平均发布周期，每个视频之间的发布周期越短，说明内容生产者创作视频的时间也就越短，创作时间太长，
不是忠实粉丝的用户可能将其遗忘。
**F=(统计范围内最晚发布视频时间-最早发布视频时间)/发布视频的数量
L(Like_rate)：
L值表示的是统计时间内发布视频的平均点赞率，越大表示视频质量越稳定，用户对up主的认可度也就越高。
**L=(点赞数X1+投币数X2+收藏数X3+分享数X4)/播放量X发布视频数
"""

# %%
df.drop_duplicates(inplace=True)  # 去重
df.dropna(inplace=True)  # 删除缺失值记录
df.reset_index(drop=True, inplace=True)  # 重置index
df.sort_values('view', ascending=False, inplace=True)  # 按播放量由高到低排序
df.reset_index(drop=True, inplace=True)  # 重置index
df['date'] = pd.to_datetime(df['date'])
# %%
# B站播放量top10视频
video_top10 = df.groupby(['title', 'bv'])['view'].sum().reset_index()
video_top10.sort_values('view', ascending=False, inplace=True)
video_top10 = video_top10.iloc[:10, :]
video_top10.sort_values('view', ascending=True, inplace=True)
# %%
bar = (
    Bar()
        .add_xaxis(video_top10['title'].to_list())
        .add_yaxis('播放量', video_top10['view'].to_list())
        .set_global_opts(title_opts=opts.TitleOpts('B站播放前10视频'))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .reversal_axis()
)
bar.render()

# %%
# B站硬笔数量top10 up主
coins_top10 = df.groupby(['author'])['coins'].sum().reset_index()
coins_top10.sort_values('coins', ascending=False, inplace=True)
coins_top10 = coins_top10.iloc[:10, :]
coins_top10.sort_values('coins', ascending=True, inplace=True)
bar = (
    Bar()
        .add_xaxis(coins_top10['author'].to_list())
        .add_yaxis('硬币数', coins_top10['coins'].to_list())
        .set_global_opts(title_opts=opts.TitleOpts('B站硬币数量top10 up'))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .reversal_axis()
)
bar.render()

# %%
# 四、构建特征值
# I:
# 视频数
video_count = df.groupby('author')['bv'].count()
# 过滤掉视频数不足5个的记录
data = df[~df['author'].isin(video_count[video_count.values < 5].index)].reset_index(drop=True)
# 弹幕数
bullet_screen_sum = data.groupby('author')['danmu'].sum()
# 转发数
comments = data.groupby('author')['replay'].sum()
# 观看数
view = data.groupby('author')['view'].sum()
# 视频数(<5个的)
video_count = data.groupby('author')['bv'].count()
I = round(((bullet_screen_sum + comments) / view / video_count * 100), 2).reset_index(name='I')

# 4.2 构造F值
latest_date = data.groupby('author')['date'].max().dt.date
earliest_date = data.groupby('author')['date'].min().dt.date
diff = (latest_date - earliest_date).dt.days
F = (diff / video_count).reset_index(name='F')

# 构造L值

data['L'] = (data['likes'] * 1 + data['coins'] * 2 + data['favorite'] * 3 + data['share'] * 4) / data['view']
L = (data.groupby('author')['L'].sum() / video_count).reset_index(name='L')

# 合并I,F,L指标
IFL = pd.merge(I, F, how='outer', left_index=True, right_index=True)
IFL = IFL.merge(L, how='outer', left_index=True, right_index=True)
IFL.drop(columns=['author_x', 'author_y'], inplace=True)
IFL = IFL.iloc[:, [2, 0, 1, 3]]
IFL.set_index('author', inplace=True)
model_scaler = MinMaxScaler()
date_scaler = model_scaler.fit_transform(IFL.iloc[:, 1:4])

# 使用K-Means聚类方法
score_list = []
silhouette_init = -1
for n_cluster in range(2, 10):
    model_kmeans = KMeans(n_clusters=n_cluster)  # 建立聚类模型对象
    label_temp = model_kmeans.fit_predict(date_scaler)
    silhouette_temp = silhouette_score(date_scaler, label_temp)  # 得到每个k下的平均轮廓系数
    if silhouette_temp > silhouette_init:  # 如果平均轮廓系数更高
        best_k = n_cluster  # 保存最佳k值
        silhouette_init = silhouette_temp  # 替换为下一轮的对照平均轮廓系数
        best_model = model_kmeans  # 保存模型示例对象
        cluster_labels_k = label_temp  # 保存聚类标签
    score_list.append([n_cluster, silhouette_temp])  # 将每次k值以及平均轮廓系数记录保存

print(score_list)
print('最优的k值是:{0}\n对应的轮廓系数是{1}'.format(best_k, silhouette_init))

cluster_labels = pd.DataFrame(cluster_labels_k, columns=['clusters'])
IFL.reset_index(inplace=True)
merge_data = pd.concat((IFL, cluster_labels), axis=1)

# %%
# #计算各个聚类类别内部最显著的特征值
cluster_features = []
for i in range(best_k):
    label_data = merge_data[merge_data['clusters'] == i].iloc[:, 1:4]
    desc_data = label_data.describe().round(3)
    mean_data = desc_data.iloc[1, :]
    mean_data.name = i
    cluster_features.append(mean_data)

cluster_pd = pd.DataFrame(cluster_features)
cluster_ct = pd.DataFrame(merge_data['clusters'].value_counts())
cluster_ct.rename(columns={'clusters': 'count'}, inplace=True)
cluster_ct['ratio'] = cluster_ct / sum(cluster_ct['count'])
all_cluster_set = pd.concat((cluster_pd, cluster_ct), axis=1)

c_schema = [
    {'name': 'I', 'max': 1, 'min': 0},
    {'name': 'F', 'max': 1, 'min': 0},
    {'name': 'L', 'max': 1, 'min': 0},
]

# radar = (
#     Radar()
#         .add_schema(schema=c_schema)
#         .add('0分组', [all_cluster.iloc[0, :].to_list()])
#         .add('1分组', [all_cluster.iloc[1, :].to_list()])
#         .add('2分组', [all_cluster.iloc[2, :].to_list()])
# )
# radar.render()\

all_cluster_set.iloc[:, :3].mean()
