import pandas as pd
from matplotlib import pyplot as plt
from common import utils as u
import numpy as np

# %%
file_path = r'D:\file\DataAnalysis\douyin.zip'
df = pd.read_csv(file_path)
# %%
# print(df.head())
print(df.shape)
print(u.show_info(df))

# %%
print(u.show_na(df))

# %%
print(u.show_duplicated(df))

# %%
print(df.columns)
# %%
df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
df['real_time'] = pd.to_datetime(df['real_time'], format='%Y-%m-%d %H:%M:%S')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'] = df['date'].dt.date


# %%
# 日播放量，日用户量，日作者量，日作品量

def aggre_func(date, gby, col):
    return date.groupby(gby)[col]


data_id = aggre_func(df, gby='date', col='uid').count()
data_uid = aggre_func(df, gby='date', col=['uid']).nunique()
data_author = aggre_func(df, gby='date', col=['author_id']).nunique()
data_item = aggre_func(df, gby='date', col='item_id').nunique()

# %%
u.fix_matplotlib_error()
x = data_id.index
plt.figure(figsize=(12, 12))
ax1 = plt.subplot(411)
plt.plot(x, data_id)
plt.setp(ax1.get_xticklabels(), visible=False)
plt.title('日播放量,日用户量,日作者量,日作品量随时间变化趋势')
plt.ylabel('日播放量')

ax2 = plt.subplot(412, sharex=ax1)
plt.plot(x, data_uid)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.ylabel('日用户量')

ax3 = plt.subplot(413)
plt.plot(x, data_author)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.ylabel('日作者数量')

ax4 = plt.subplot(414, sharex=ax3)
plt.plot(x, data_item)
plt.setp(ax4.get_xticklabels(), visible=True)
plt.ylabel('日稿件数量')

plt.show()

"""
日播放量，日用户量，日作者量，日作品量随时间的变化趋势基本一致：平稳增长；
在2019-10-20到2019-10-29时间段内，各指标均先出现巨大增长，
后趋近平稳，再回落到正常水平值。猜测该时间点平台有进行活动推广，以至于吸引了大量用户。
"""

# %%
# 作者：作品数量，作品获赞率

# 作品数量top50
author_50 = aggre_func(df, gby='author_id', col='item_id').count()
author_50.sort_values(ascending=False, inplace=True)
author_50 = author_50[:50]

col_author = author_50.index
author_l_50 = aggre_func(df, gby='author_id', col='like').mean()[col_author]
# 计算作品数量top50在所有视频总量的占比
author_p_50 = author_50 / len(df['id'])

author_50_lst = [str(x) for x in author_50.keys()]
y1 = author_50
y2 = author_l_50
y3 = author_p_50

fig, ax1 = plt.subplots(figsize=(18, 6))
color = 'tab:blue'
ax1.set_xlabel('作者ID')
ax1.set_ylabel('作品数量', color=color)
ax1.bar(author_50_lst, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# instantiate a second axes that shares the same x-axis
color = 'tab:red'
ax2 = ax1.twinx()
ax2.set_ylabel('作品点赞率', color=color)
ax2.plot(author_50_lst, y2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

color = 'tab:green'
ax3 = ax1.twinx()
ax3.set_ylabel('作品播放率', color=color)
ax3.plot(author_50_lst, y3, color=color)
ax3.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

"""
作者作品数量与播放率成正比关系
作者作品数量和点赞率并没有太大的关系
"""

# %%
# 作者：播放量贡献
author_p = df['author_id'].value_counts().cumsum() / len(df['id'])
x = range(len(author_p))

plt.figure(figsize=(12, 6))
plt.title('平台作品播放量贡献')
plt.plot(x, author_p)
plt.xlabel('作者数量')
plt.ylabel('播放量占比')
plt.text(0, 0.6, '播放量占比')
plt.show()

# 约3500，18%左右作者贡献了平台80%的播放量，服从二八法则。
# %%
# 3.2 作品
# 作品来源
channel = df['channel'].value_counts()
labels = channel.index
plt.figure(figsize=(6, 6))
plt.pie(channel, labels, autopct='%.2f%%')
plt.show()

# %%
# 3.2.2 背景音乐
# 选用的歌曲 top10
music_10 = df['music_id'].value_counts().iloc[:10]
x = [str(x) for x in music_10.keys()]

plt.figure(figsize=(12, 4))
plt.bar(x, music_10)
plt.xlabel('歌曲ID')
plt.ylabel('播放量')
plt.show()

# %%
# 播放量top10的歌曲作品的播放量随时间变化趋势
music_date = df.groupby(['music_id', 'date']).count()['uid'].unstack().loc[music_10.index].T
plt.figure(figsize=(12, 6))
music_date.plot()
plt.show()

'''
上面所说的2019-10-21到2019-10-29时间段内，各歌曲作品的播放量都有增高，
其中ID为 22，220， 68，25 的歌曲有暴涨趋势。'''

# %%
# 歌曲与点赞率，完播率
music_aa = df.groupby('music_id')[['finish', 'like']].mean()[:1000]
music_aa.plot(figsize=(18, 6))
plt.show()
# 不同背景音乐作品的点赞率和完播率差距不大，即产生播放量后的点赞和完整播放结果差别不大

# %%
music_aa = df.groupby('music_id')['id'].count() / len(df['id'])
music_aa[:1000].plot(figsize=(18, 6))
plt.show()
# 不同背景音乐作品的播放量差异巨大，个别歌曲播放量表现突出

# %%
music_100 = df['music_id'].value_counts().cumsum() / len(df['id'])
x = range(len(music_100))
plt.plot(x, music_100)
plt.text(0, 0.8, '歌曲数量同播放占比')
plt.show()

# %%
# top10歌曲点赞率随时间的变化趋势
music_like_date = df.groupby(['music_id', 'date'])['like'].mean().unstack()
music_like_date = music_like_date.iloc[music_10.index].T
cols_str = [str(x) for x in music_like_date.index]
# %%
# 不同歌曲下完播率随时间的变化趋势
music_finish_date = df.groupby(['music_id', 'date'])['finish'].mean().unstack()
music_finish_date = music_finish_date.iloc[music_10.index].T

plt.figure(figsize=(12, 6))
ax1 = plt.subplot(211)
plt.plot(cols_str, music_like_date)
plt.setp(ax1.get_xticklabels(), visible=False)
plt.legend(loc='upper center', ncol=10, labels=cols_str)
plt.title('不同歌曲下播放量top10变量随时间的变化趋势')
plt.ylabel('点赞率')

ax2 = plt.subplot(212)
plt.plot(cols_str, music_finish_date)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.ylabel('完播率')
plt.show()
