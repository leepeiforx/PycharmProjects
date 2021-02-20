from pyecharts.charts import *
from pyecharts import options as opt
from common import utils as u
import pandas as pd

# %%
file_path = r'D:\file\DataAnalysis\GENDER8810.zip'
file_dict = u.unpack_file_to_df(file_path, encoding='utf-8')

# 为了方便后面统计,所以更新了key键值
file_name = list(file_dict.keys())
file_name_new = ['town', 'country', 'city', 'area', 'all']
for i in range(len(file_name_new)):
    file_dict[file_name_new[i]] = file_dict.pop(file_name[i])


# # 处理表头
def rename(tab):
    for t in range(tab.shape[1]):
        if tab.iloc[1, t] == '小计':
            tab.iloc[1, t] = '小计' + '_' + str(tab.iloc[0, t])
        elif tab.iloc[1, t] == '男':
            tab.iloc[1, t] = '男' + '_' + str(tab.iloc[0, t - 1])
        elif tab.iloc[1, t] == '女':
            tab.iloc[1, t] = '女' + '_' + str(tab.iloc[0, t - 2])
    tab.iloc[1, 0] = '地 区'
    tab.columns = tab.iloc[1,]
    tab.drop(index=[0, 1], inplace=True)
    tab.reset_index(drop=True, inplace=True)


# 1.1 删除多余的列,以及第一行全是nan
for fd in file_dict:
    file_dict[fd].dropna(axis=1, how='all', inplace=True)
    file_dict[fd].drop(index=[0, 1], inplace=True)
    file_dict[fd].reset_index(inplace=True)
    file_dict[fd].drop(columns='index', inplace=True)
    rename(file_dict[fd])
    file_dict[fd] = file_dict[fd].set_index('地 区').stack().reset_index()
    file_dict[fd].columns = ['地区', '分类', '统计人数']
    file_dict[fd]['地区'] = file_dict[fd]['地区'].str.replace(' ', '')
    file_dict[fd]['性别'] = file_dict[fd]['分类'].str.split('_').str[0]
    file_dict[fd]['年龄段'] = file_dict[fd]['分类'].str.split('_').str[-1]
    file_dict[fd]['年龄段'] = file_dict[fd]['年龄段'].str.replace(' ', '')
    file_dict[fd]['rank'] = file_dict[fd]['年龄段'].str.split('-').str[-1].str.replace(pat=r'\D+', repl='')
    file_dict[fd]['统计人数'] = file_dict[fd]['统计人数'].astype('float')
    file_dict[fd].drop(columns='分类', inplace=True)
# %%
df_city = file_dict['city']
df_town = file_dict['town']
df_country = file_dict['country']
df_area = file_dict['area']
df_all = file_dict['all']

# %%

data = df_all[(df_all['年龄段'] == '合计') & (df_all['地区'] == '全国')]

bar = (Bar()
       .add_xaxis(data['性别'].to_list())
       .add_yaxis('', data['统计人数'].to_list())
       .set_global_opts(title_opts=opt.TitleOpts(title='2010年度全国人口情况')))
bar.render()

# %%
# # 性别
x_data = data[data['性别'] != '合计']['性别'].to_list()
y_data = data[data['性别'] != '合计']['统计人数'].to_list()
data_pair = [list(z) for z in zip(x_data, y_data)]
pie = (
    Pie()
        .add('性别', data_pair=data_pair, rosetype="radius")
        .set_series_opts(tooltip_opts=opt.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
    ),
        # 设置标签颜色
        label_opts=opt.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
        .set_global_opts(
        # 设置标题
        title_opts=opt.TitleOpts(
            # 名字
            title="人口性别分布",
            # 组件距离容器左侧的位置
            # 设置标题颜色
            title_textstyle_opts=opt.TextStyleOpts(color="#fff"),
        ),
    ))
pie.render()

# %%
# 年龄组

df_age = df_all[(df_all['年龄段'] != '合计') & (df_all['性别'] == '小计') & (df_all['地区'] == '全国')]
df_age['rank'] = df_age['rank'].astype('int')
df_age['cut'] = pd.cut(df_age['rank'], bins=[-1, 55, 64, 200],
                       labels=['55岁以下', '55-64岁', '64岁以上'])

df_age = df_age.groupby('cut')['统计人数'].sum().reset_index()
x_data = df_age['cut'].to_list()
y_data = df_age['统计人数'].to_list()
data_pair = [list(z) for z in zip(x_data, y_data)]
pie = (
    Pie()
        .add('', data_pair=data_pair)
        .set_series_opts(tooltip_opts=opt.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b}: {c} ({d}%")))
pie.render()

# %%
# 细分各年龄层
df_age = df_all[(df_all['年龄段'] != '合计') & (df_all['性别'] == '小计') & (df_all['地区'] == '全国')]
x_data = df_age['年龄段'].to_list()
y_data = df_age['统计人数'].to_list()
data_pair = [list(z) for z in zip(x_data, y_data)]
pie = (
    Pie()
        .add('', data_pair=data_pair)
        .set_series_opts(tooltip_opts=opt.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b}: {c} ({d}%")))
pie.render()

# %%
# 按户籍划分
city = df_city[(df_city['地区'] == '全国') & (df_city['性别'] == '合计')]['统计人数'].reset_index()
city['类型'] = '城市'
country = df_country[(df_country['地区'] == '全国') & (df_city['性别'] == '合计')]['统计人数'].reset_index()
country['类型'] = '农村'
town = df_town[(df_town['地区'] == '全国') & (df_city['性别'] == '合计')]['统计人数'].reset_index()
town['类型'] = '城镇'

df_con = pd.concat([city, country, town], axis=0)
x_data = df_con['类型'].to_list()
y_data = df_con['统计人数'].to_list()
data_pair = [list(z) for z in zip(x_data, y_data)]
pie = (
    Pie()
        .add('', data_pair=data_pair)
        .set_series_opts(tooltip_opts=opt.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b}: {c} ({d}%")))
pie.render()


# %%
# 2.5 全国人口结构金字塔

def draw_population(tab):
    df_temp = tab[(tab['地区'] == '全国') & (tab['性别'].isin(['男', '女'])) & (tab['年龄段'] != '合计')]
    age = list(df_temp['年龄段'].unique())
    male = df_temp[df_temp['性别'] == '男']['统计人数'].to_list()
    female = list(-df_temp[df_temp['性别'] == '女']['统计人数'].values)
    bar = (Bar()
           .add_xaxis(age)
           .add_yaxis('男', male, stack='stack1')
           .add_yaxis('女', female, stack='stack1')
           .set_series_opts(label_opts=opt.LabelOpts(is_show=False))
           .reversal_axis()
           )
    bar.render()


draw_population(df_all)

# %%
# 城市人口金字塔结构
draw_population(df_city)

# %%
# 镇人口金字塔分布
draw_population(df_town)

# %%
# 农村人口金字塔分布
draw_population(df_country)

# %%
# 全国各地-外出半年以上人口比重
area = df_area[df_area['年龄段'] == '外出半年以上人口占总人口比重']
city = list(area['地区'].unique())
male = area[area['性别'] == '男']['统计人数'].to_list()
female = area[area['性别'] == '女']['统计人数'].to_list()
scatter = (Scatter()
           .add_xaxis(city)
           .add_yaxis('男', male)
           .add_yaxis('女', female)
           .set_global_opts(title_opts=opt.TitleOpts(title='全国各地-外出半年以上人口比重'))
           )
scatter.render()

# %%
#  全国各地人口分布地图

population_all = df_all[(df_all['地区'] != '全国') & (df_all['性别'] == '合计')][['地区', '统计人数']]
x_data = population_all['地区'].to_list()
y_data = population_all['统计人数'].to_list()
data_pair = list(z for z in zip(x_data, y_data))

population_map = (Map()
                  .add('', data_pair=data_pair, maptype='china')
                  .set_global_opts(title_opts=opt.TitleOpts(title='全国各地区人口分布'),
                                   visualmap_opts=opt.VisualMapOpts(max_=population_all['统计人数'].max(),
                                                                    min_=population_all['统计人数'].min()))
                  .set_series_opts(label_opts=opt.LabelOpts(is_show=False)))
population_map.render()
