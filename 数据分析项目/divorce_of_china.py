from common import utils as u
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts

# %%
file_path = r'D:\file\DataAnalysis\gov.zip'
df = pd.read_csv(file_path)
# %%
df.rename(columns={'Unnamed: 0': '地区'}, inplace=True)
df.drop(index=[0, 1], inplace=True)
df.set_index('地区', inplace=True)

# %%
# u.show_info(df)
# u.show_na(df)
# u.show_duplicated(df)

# %%
df = df.stack().reset_index()
df.columns = ['地区', '各年度登记状况', '配对数']

# %%
df['time'] = df['各年度登记状况'].str.slice(0, 9)
df['type'] = df['各年度登记状况'].str.slice(9, 13)
df['year'] = df['各年度登记状况'].str.slice(0, 4)
df['year'] = df['year'].astype('int')
# %%
df.drop(columns='各年度登记状况', inplace=True)

# %%
# 全国2007第一季度-2020第三季度离婚&结婚登记情况
#
nation = df[df['地区'] == '全国合计']
x_data = list(nation['time'].unique())
married = nation[nation['type'] == '结婚登记']['配对数'].to_list()
divorce = nation[nation['type'] == '离婚登记']['配对数'].to_list()
line = (
    Line()
        .add_xaxis(x_data)
        .add_yaxis('结婚', married)
        .add_yaxis('离婚', divorce)
        .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90)))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)
line.render()

# %%
bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('离婚', divorce, stack='stack1')
       .add_yaxis('结婚', married, stack='stack1')
       .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90))))
bar.render()

#%%