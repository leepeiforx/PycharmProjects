import datetime
import math
import pyecharts.options as opts
import random
from pyecharts.charts import *
from pyecharts.components import Table
# %%
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

# %%
# 直角坐标系图表
# 直方图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [123, 312, 89, 107, 82, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data))

bar.render()
# %%
# 折线图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [123, 312, 89, 107, 82, 23]

bar = (Line()
       .add_xaxis(x_data)
       .add_yaxis('', y_data))

bar.render()

# %%
# 折线图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [[random.randint(100, 200) for i in range(10)] for item in x_data]

Box = Boxplot()
Box.add_xaxis(x_data)
Box.add_yaxis('', Box.prepare_data(y_data))
bar.render()

# %%
# 散点图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [123, 312, 89, 107, 82, 23]

scatter = (Scatter()
           .add_xaxis(x_data)
           .add_yaxis('', y_data)
           )

scatter.render()

# %%
# 带涟漪效果的散点图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [123, 312, 89, 107, 82, 23]

escatter = (EffectScatter()
            .add_xaxis(x_data)
            .add_yaxis('', y_data)
            )
escatter.render()

# %%
# k线图
# x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
x_data = ['2020/4/{}'.format(i + 1) for i in range(30)]
y_data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
    [2416.62, 2432.4, 2414.4, 2443.03],
    [2441.91, 2421.56, 2418.43, 2444.8],
    [2420.26, 2382.91, 2373.53, 2427.07],
    [2383.49, 2397.18, 2370.61, 2397.94],
    [2378.82, 2325.95, 2309.17, 2378.82],
    [2322.94, 2314.16, 2308.76, 2330.88],
    [2320.62, 2325.82, 2315.01, 2338.78],
    [2313.74, 2293.34, 2289.89, 2340.71],
    [2297.77, 2313.22, 2292.03, 2324.63],
    [2322.32, 2365.59, 2308.92, 2366.16],
    [2364.54, 2359.51, 2330.86, 2369.65],
    [2332.08, 2273.4, 2259.25, 2333.54],
    [2274.81, 2326.31, 2270.1, 2328.14],
    [2333.61, 2347.18, 2321.6, 2351.44],
    [2340.44, 2324.29, 2304.27, 2352.02],
    [2326.42, 2318.61, 2314.59, 2333.67],
    [2314.68, 2310.59, 2296.58, 2320.96],
    [2309.16, 2286.6, 2264.83, 2333.29],
    [2282.17, 2263.97, 2253.25, 2286.33],
]

kline = (Kline()
         .add_xaxis(x_data)
         .add_yaxis('', y_data))

kline.render()

# %%
# 热力图
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(100)]

hours_list = ''
weeks_list = '周一,周二,周三,周四,周五,周末'

heat = (HeatMap()
        .add_xaxis(hours_list)
        .add_yaxis('', weeks_list, data))

heat.render()

# %%
# 象型图

x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data = [123, 312, 89, 107, 82, 23]

pictorialBar = (PictorialBar()
                .add_xaxis(x_data)
                .add_yaxis('', y_data))
pictorialBar.render()

# %%
# 层叠图
x_data = ['apple', 'huawei', 'xiaomi', 'oppo', 'vivo', 'meizu']
y_data_bar = [123, 312, 89, 107, 82, 23]
y_data_line = [153, 107, 23, 89, 123, 107]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data_bar))

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_line))

overlap = bar.overlap(line)
overlap.render()

# %%
# 地理图表
# GEO-地理坐标系

province = ['广东', '湖北', '湖南', '四川', '重庆',
            '黑龙江', '浙江', '山西', '河北', '安徽',
            '河南', '山东', '西藏']

data = [(item, random.randint(50, 150)) for item in province]

geo = (Geo()
       .add_schema(maptype='china')
       .add('', data)
       )
geo.render()

# %%
# MAP-地图
province = ['广东', '湖北', '湖南', '四川', '重庆',
            '黑龙江', '浙江', '山西', '河北', '安徽',
            '河南', '山东', '西藏']

data = [(item, random.randint(50, 150)) for item in province]

map_ = (Map()
        .add('', data, 'china'))
map_.render()

# %%
# BMAP-百度地图
province = ['广东', '湖北', '湖南', '四川', '重庆',
            '黑龙江', '浙江', '山西', '河北', '安徽',
            '河南', '山东', '西藏']

data = [(item, random.randint(50, 150)) for item in province]

bmap = (BMap()
        .add_schema(baidu_ak='jhFnHPYyR6ddq7lioDHay0kYRUsDgl8x', center=[120.13066322374, 30.240018034923])
        .add('', data))
bmap.render()

# %%
# 基本图表
# 饼图

cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 53, 89, 107, 98, 23]
pie = (Pie()
       .add('', [list(z) for z in zip(cate, data)]))
pie.render()

# %%
# 漏斗图
cate = ['访问', '注册', '加入购物车', '提交订单', '付款成功']
data = [30398, 15230, 10045, 3100, 1696]
funnel = (Funnel()
          .add('', [list(z) for z in zip(cate, data)]))

funnel.render()

# %%
# 转化率
gauge = (Gauge()
         .add('', [('转化率', 34)]))

gauge.render()

# %%
# 水球图
liquid = (Liquid()
          .add('', [0.52, 0.44]))

liquid.render()

# %%
# 日历图
begin = datetime.date(2019, 1, 1)
end = datetime.date(2019, 12, 31)
data = [[str(begin + datetime.timedelta(days=i)), abs(math.cos(i / 100)) * random.randint(1000, 1200)]
        for i in range((end - begin).days + 1)]

calendar = (Calendar()
            .add('', data, calendar_opts=opts.CalendarOpts(range_='2019')))

calendar.render()

# %%
# 关系图


keys = ['name', 'symbolSize']
nodes = []
for i in range(1, 9):
    l1 = ['节点' + str(i), i]
    d1 = dict(zip(keys, l1))
    nodes.append(d1)

links = [{'source': '节点1', 'target': '节点2'},
         {'source': '节点1', 'target': '节点3'},
         {'source': '节点1', 'target': '节点4'},
         {'source': '节点2', 'target': '节点1'},
         {'source': '节点3', 'target': '节点4'},
         {'source': '节点3', 'target': '节点5'},
         {'source': '节点3', 'target': '节点6'},
         {'source': '节点4', 'target': '节点1'},
         {'source': '节点4', 'target': '节点2'},
         {'source': '节点4', 'target': '节点7'},
         {'source': '节点4', 'target': '节点8'},
         {'source': '节点5', 'target': '节点1'},
         {'source': '节点5', 'target': '节点4'},
         {'source': '节点5', 'target': '节点6'},
         {'source': '节点5', 'target': '节点7'},
         {'source': '节点5', 'target': '节点8'},
         {'source': '节点6', 'target': '节点1'},
         {'source': '节点6', 'target': '节点7'},
         {'source': '节点6', 'target': '节点8'},
         {'source': '节点7', 'target': '节点1'},
         {'source': '节点7', 'target': '节点2'},
         {'source': '节点7', 'target': '节点8'},
         {'source': '节点8', 'target': '节点1'},
         {'source': '节点8', 'target': '节点2'},
         {'source': '节点8', 'target': '节点3'},
         ]

graph = (Graph()
         .add('', nodes=nodes, links=links)
         )
graph.render()

# %%
# 平行坐标系
data = [
    ['一班', 78, 91, 123, 78, 82, 67, "优秀"],
    ['二班', 89, 101, 127, 88, 86, 75, "良好"],
    ['三班', 86, 93, 101, 84, 90, 73, "合格"],
]

parallel = (Parallel()
            .add_schema([opts.ParallelAxisOpts(dim=0, name='班级', type_='category', data=['一班', '二班', '三班']),
                         opts.ParallelAxisOpts(dim=1, name='英语'),
                         opts.ParallelAxisOpts(dim=2, name='数学'),
                         opts.ParallelAxisOpts(dim=3, name='语文'),
                         opts.ParallelAxisOpts(dim=4, name='物理'),
                         opts.ParallelAxisOpts(dim=5, name='生物'),
                         opts.ParallelAxisOpts(dim=6, name='化学'),
                         opts.ParallelAxisOpts(dim=7, name='评级', type_='category', data=['优秀', '良好', '合格'])
                         ])
            .add('', data))

parallel.render()

# %%
# 极坐标系
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 153, 89, 107, 98, 23]

polar = (Polar()
         .add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=cate, type_='category'))
         .add('', data, type_='bar')
         )

polar.render()

# %%
data = [
    [78, 91, 123, 78, 82, 67],
    [89, 101, 127, 88, 86, 75],
    [86, 93, 101, 84, 90, 73],
]

radar = (Radar()
         .add_schema(schema=[opts.RadarIndicatorItem(name='语文', max_=150),
                             opts.RadarIndicatorItem(name='数学', max_=150),
                             opts.RadarIndicatorItem(name='英语', max_=150),
                             opts.RadarIndicatorItem(name='物理', max_=100),
                             opts.RadarIndicatorItem(name='生物', max_=100),
                             opts.RadarIndicatorItem(name='化学', max_=100), ])
         .add('', data)
         )
radar.render()

# %%
# 旭日图
data = [
    {'name': '湖南',
     'children': [
         {'name': '长沙',
          'children:': [
              {'name': '雨花区', 'value': 55},
              {'name': '岳麓区', 'value': 34},
              {'name': '天心区', 'value': 144},
          ]},
         {'name': '常德',
          'children': [
              {'name': '武陵区', 'value': 156},
              {'name': '鼎城区', 'value': 134},
          ]},
         {'name': '湘潭', 'value': 87},
         {'name': '株洲', 'value': 23},
     ],
     },
    {"name": "湖北",
     "children": [
         {"name": "武汉",
          "children": [
              {"name": "洪山区", "value": 55},
              {"name": "东湖高新", "value": 78},
              {"name": "江夏区", "value": 34},
          ]},
         {"name": "鄂州", "value": 67},
         {"name": "襄阳", "value": 34},
     ],
     },
    {"name": "北京", "value": 235}
]

sunburst = (Sunburst()
            .add('', data)
            )
sunburst.render()

# %%
# 桑基图
nodes = [{'name': '访问'}, {'name': '注册'}, {'name': '付费'}]

links = [{'source': '访问', 'target': '注册', 'value': 50},
         {'source': '注册', 'target': '付费', 'value': 30}]

sankey = (Sankey()
          .add('', nodes, links))

sankey.render()

# %%
# 河流图
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
date_lst = ['2014/4/{}'.format(i + 1) for i in range(30)]

zdata = [[day, random.randint(10, 50), c] for day in date_lst for c in cate]
print(zdata)
river = (ThemeRiver()
         .add(series_name='cate',
              data=zdata,
              singleaxis_opts=opts.SingleAxisOpts(type_='time')))

river.render()

# %%
# 词云

words = [
    ("hey", 230),
    ("jude", 124),
    ("dont", 436),
    ("make", 255),
    ("it", 247),
    ("bad", 244),
    ("Take", 138),
    ("a sad song", 184),
    ("and", 12),
    ("make", 165),
    ("it", 247),
    ("better", 182),
    ("remember", 255),
    ("to", 150),
    ("let", 162),
    ("her", 266),
    ("into", 60),
    ("your", 82),
    ("heart", 173),
    ("then", 365),
    ("you", 360),
    ("can", 282),
    ("start", 273),
    ("make", 265),
]
wc = (WordCloud()
      .add('', words))
wc.render()

# %%
# 表格
table = Table()

headers = ['City Name', 'Area', 'Population', 'Annual Rainfall']

rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]

table.add(headers, rows)
table.render()

# %%
# 3D图
# 3D散点图

data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for i in range(100)]

scatter3D = (Scatter3D()
             .add('', data=data))

scatter3D.render()

# %%
# 3D折线图

data = []
for t in range(0, 1000):
    x = math.cos(t / 10)
    y = math.sin(t / 10)
    z = t / 10
    data.append([x, y, z])

line3D = (Line3D()
          .add('', data,
               xaxis3d_opts=opts.Axis3DOpts(type_='value'),
               yaxis3d_opts=opts.Axis3DOpts(type_='value')))

line3D.render()

# %%
# 3D直方图

data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hours_list = [str(i) for i in range(24)]
weeks_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

bar3D = (Bar3D()
         .add('', data,
              xaxis3d_opts=opts.Axis3DOpts(hours_list, type_='category'),
              yaxis3d_opts=opts.Axis3DOpts(weeks_list, type_='category'),
              zaxis3d_opts=opts.Axis3DOpts(type_='value')
              )
         )
bar3D.render()

# %%
# 3D地图(加载不出来)

province = ['广东', '湖北', '湖南', '四川', '重庆',
            '黑龙江', '浙江', '山西', '河北', '安徽',
            '河南', '山东', '西藏']

data = [(i, random.randint(50, 100)) for i in province]

map3D = (Map3D()
         .add('', data_pair=data, maptype='china')
         )

map3D.render()

# %%
# 3d地球
from pyecharts.faker import POPULATION

mapglobe = (MapGlobe()
            .add('', maptype='world', data_pair=POPULATION[1:])
)

mapglobe.render()

# %%
# 树型图表
# 树图
data = [
    {"name": "湖南",
     "children": [
         {"name": "长沙",
          "children": [
              {"name": "雨花区"},
              {"name": "岳麓区"},
              {"name": "天心区"},
          ]},
         {"name": "常德",
          "children": [
              {"name": "武陵区"},
              {"name": "鼎城区"},
          ]},
         {"name": "湘潭", "value": 87},
         {"name": "株洲", "value": 23},
     ],
     }
]

tree = (Tree()
        .add('', data))

tree.render()

# %%
# 矩形树图
data = [
    {"name": "湖南",
     "children": [
         {"name": "长沙",
          "children": [
              {"name": "雨花区", "value": 55},
              {"name": "岳麓区", "value": 34},
              {"name": "天心区", "value": 144},
          ]},
         {"name": "常德",
          "children": [
              {"name": "武陵区", "value": 156},
              {"name": "鼎城区", "value": 134},
          ]},
         {"name": "湘潭", "value": 87},
         {"name": "株洲", "value": 23},
     ],
     },
    {"name": "湖北",
     "children": [
         {"name": "武汉",
          "children": [
              {"name": "洪山区", "value": 55},
              {"name": "东湖高新", "value": 78},
              {"name": "江夏区", "value": 34},
          ]},
         {"name": "鄂州", "value": 67},
         {"name": "襄阳", "value": 34},
     ],
     },
    {"name": "北京", "value": 235}
]

treemap = (TreeMap()
           .add('', data))

treemap.render()

# %%
# 组合图表
# Timeline-时间轴

begin = datetime.date(2020, 9, 1)
end = datetime.date(2020, 9, 30)

cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']


def random_data(n):
    return [random.randint(100, 200) for _ in range(n)]


tl = Timeline()
tl.add_schema()

for i in range((end - begin).days + 1):
    day = begin + datetime.timedelta(days=i)

    bar = (Bar()
           .add_xaxis(cate)
           .add_yaxis('电商渠道', random_data(len(cate))))

    tl.add(bar, day)

tl.render()

# %%
# Tab-选项卡

begin = datetime.date(2020, 9, 1)
end = datetime.date(2020, 9, 30)

date_lst = [str(begin + datetime.timedelta(days=i)) for i in range((end - begin).days + 1)]

cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']


def random_data(n):
    return [random.randint(100, 200) for _ in range(n)]


tab = Tab()

for c in cate:
    line = (Line()
            .add_xaxis(date_lst)
            .add_yaxis('', random_data(len(date_lst))))
    tab.add(line, c)
tab.render()

# %%
# Page-顺序多图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data))

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data))

page = (Page()
        .add(bar, line))

page.render()

# %%
# Grid-并行多图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data))

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data))
grid = (Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_bottom='65%', pos_left='50%'))
        .add(line, grid_opts=opts.GridOpts(pos_left='15%')))

grid.render()

# %%
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]
theme_list = ['chalk', 'dark', 'essos', 'infographic', 'light'
                                                       'macarons', 'purple-passion', 'roma', 'romantic',
              'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland']

page = Page()
for item in theme_list:
    bar = (Bar(init_opts=opts.InitOpts(theme=item))
           .add_xaxis(x_data)
           .add_yaxis('', y_data_1)
           .add_yaxis('', y_data_2)
           .set_global_opts(title_opts=opts.TitleOpts('Theme={}'.format(item)))
           )
    page.add(bar)

page.render()

# %%
"""初始化配置
(opts.InitOpts)
"""
# InitOpts—初始化配置项
# 画布大小配置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar(init_opts=opts.InitOpts(width='600px', height='400px'))
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1)
       .add_yaxis('', y_data_2))
bar.render()

# %%
# opts.InitOpts—初始化配置项
# 主题配置

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]

bar = (Bar(init_opts=opts.InitOpts(theme='shine'))
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1))
bar.render()

# %%
# 网页标题(不是图表的标题，注意区分！！)
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]

bar = (Bar(init_opts=opts.InitOpts(page_title='AwesomeTang'))
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1))
bar.render()

# %%
# 背景颜色
""" 常见颜色可通过"white", "green"等来配置；
    支持rgb和rgba通道颜色配置，如：bg_color='rgb(1,3,4)；"""

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]

bar = (Bar(init_opts=opts.InitOpts(bg_color='rgba(123,200,88,0.4)'))
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1))
bar.render()

# %%
# 全局配置
# opts.global_options
# TitleOpts-标题配置项
# 添加主/副标题

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1)
       .add_yaxis('', y_data_2)
       .set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题'))
       )

bar.render()

# %%
# 标题位置
# pos_top， pos_bottom，pos_left， pos_right分别对应 上/下/左/右。
# 可以接受像 20 这样的具体像素值；
# 可以接受像 '20%' 这样相对于容器高宽的百分比；
# 可以接受 'left', 'center', 'right'。

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1)
       .add_yaxis('', y_data_2)
       .set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题',
                                                  pos_left='center', pos_top='10%'))
       )

bar.render()

# %%
# 标题字体样式配置
# 更多的字体样式配置请参考「系列配置项——TextStyleOpts-文字样式配置项」

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]
bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data_1)
       .add_yaxis('', y_data_2)
       .set_global_opts(title_opts=opts.TitleOpts(title='主标题', subtitle='副标题',
                                                  pos_left='center', pos_top='10%',
                                                  title_textstyle_opts=opts.TextStyleOpts(color='red'),
                                                  subtitle_textstyle_opts=opts.TextStyleOpts(font_size=25)))
       )
bar.render()

# %%
# LegendOpts-图例配置项
# 关闭/显示图例
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True))
       )

bar.render()

# %%
# 图例显示位置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_left='20%', pos_bottom='90%'))
       )

bar.render()

# %%
# 图例水平/垂直布局
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       # 可选"vertical","horizontal"
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, orient='vertical'))
       )

bar.render()

# %%
# 图例间隔
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       # 默认间隔为10
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, item_gap=100))
       )

bar.render()

# %%
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       # 文本样式配置
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, textstyle_opts=opts.TextStyleOpts(color='red')))
       )

bar.render()

# %%
# 图例形状
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       # 可选'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
       .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, legend_icon='circle'))
       )

bar.render()

# %%
# 全局配置项
# (Charts.set_global_opts)
# TooltipOpts-提示框配置项
# 触发设置


# 虚假数据
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 提示框配置
bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       .set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on='mousemove|click'))
)

bar.render()

# %%
# 提示框背景颜色

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 提示框配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=True, background_color='blue'))
)

bar.render()

# %%
# 内容格式
# 模版变量如下：
#
# {a}: 系列名称
# {b}：数据名
# {c}：数值
# {d}：百分比，只在特定图表中生效，如饼图，漏斗图

cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 153, 89, 107, 98, 23]

pie = (Pie()
       .add('', [list(z) for z in zip(cate, data)])
       .set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=True, formatter='{b}:{d}%')))

pie.render()

# %%
# 提示文本样式
# 更多的字体样式配置请参考「系列配置项——TextStyleOpts-文字样式配置项」

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 提示框配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(tooltip_opts=opts.TooltipOpts(is_show=True, textstyle_opts=opts.TextStyleOpts(color='red')))
)

bar.render()

# %%
# AxisOpts-坐标轴配置项
# 坐标轴类型

x_data = [random.randint(0, 100) for _ in range(20)]
y_data = [random.randint(0, 100) for _ in range(20)]

# 将x轴设置为数值类型
scatter = (Scatter()
           .add_xaxis(x_data)
           .add_yaxis('', y_data)
           .set_global_opts(xaxis_opts=opts.AxisOpts(type_='value'))
           )

scatter.render()

# %%
# 添加坐标轴名称

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

scatter = (Bar()
           .add_xaxis(x_data)
           .add_yaxis('', y_data_1)
           .add_yaxis('', y_data_2)
           .set_global_opts(yaxis_opts=opts.AxisOpts(name='销售额/万元'))
           )

scatter.render()

# %%
# 坐标轴名称文本样式
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 将x轴设置为数值类型
scatter = (Bar()
    .add_xaxis(x_data)
    .add_yaxis('', y_data_1)
    .add_yaxis('', y_data_2)
    .set_global_opts(
    yaxis_opts=opts.AxisOpts(name='销售额/万元', name_textstyle_opts=opts.TextStyleOpts(color='green')))
)

scatter.render()

# %%
# 刻度最大/最小值
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 坐标轴最大/最小值
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(min_=0, max_=500))
)

bar.render()

# %%
# 坐标轴标签
# 更多的标签配置请参考「系列配置项——LabelOpts-标签配置项」
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 坐标轴最大/最小值
bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('图例1', y_data_1)
       .add_yaxis('图例2', y_data_2)
       .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color='red', font_size=10)))
       )

bar.render()

# %%

# 虚假数据
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 关闭坐标轴线
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=False)))
)

bar.render()

# %%坐标轴线-线样式配置
# 更多的线样式配置请参考「系列配置项——LineStyleOpts-线样式配置项」
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 坐标轴线样式配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(
        axisline_opts=opts.AxisLineOpts(
            is_show=True, linestyle_opts=opts.LineStyleOpts(color='red', width=2))))
)

bar.render()

# %%
# 坐标轴线—显示箭头
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 显示箭头
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(axisline_opts=opts.AxisLineOpts(is_show=True, symbol='arrow')))
)

bar.render()

# %%
# 坐标轴刻度配置
# (AxisPointerOpts)
# 坐标轴刻度-是否显示

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 坐标轴刻度朝向
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_show=False)))
)

bar.render()

# %%
# 坐标轴刻度-朝向
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 坐标轴刻度朝向
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(yaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_inside=True)))
)

bar.render()

# %%
# VisualMapOpts-视觉映射配置项
# 关闭/显示视觉组件

data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=False))
        )

heat.render()

# %%
# 指定组件最大/最小值
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, min_=20, max_=100))
        )

heat.render()

# %%
# 颜色配置
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, range_color=('green', 'yellow', 'red'))))

heat.render()

# %%
# 组件水平/垂直布局

data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        # 可选 水平（'horizontal'）或者竖直（'vertical'）
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, orient='horizontal'))
        )

heat.render()

# %%
# 组件位置
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, pos_top='center'))
        )

heat.render()

# %%
# 颜色分段显示
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, is_piecewise=True))
        )

heat.render()

# %%
# 自定义分段
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

# 添加一个特殊值作为示例
data[-1] = [23, 6, 100]

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        .set_global_opts(visualmap_opts=
                         opts.VisualMapOpts(is_show=True,
                                            # is_piecewise需设置为True
                                            is_piecewise=True,
                                            pieces=[{'max': 20}, {'min': 20, 'max': 50},
                                                    # 设置特殊值，等于100的时候显示黑色
                                                    {'min': 50, 'max': 99}, {'value': 100, 'color': 'black'}]))
        )

heat.render()

# %%
# DataZoomOpts
# 区域缩放配置项
# 缩放比例

x_data = list(range(1990, 2020))
y_data_1 = [random.randint(0, 100) for _ in x_data]
y_data_2 = [random.randint(0, 100) for _ in x_data]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=80))
)

bar.render()

# %%
# 缩放Y轴

x_data = list(range(1990, 2020))
y_data_1 = [random.randint(0, 100) for _ in x_data]
y_data_2 = [random.randint(0, 100) for _ in x_data]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .add_yaxis('图例2', y_data_2)
        .set_global_opts(datazoom_opts=opts.DataZoomOpts(orient='vertical'))
)

bar.render()

# %%
# 系统配置项
# 1.通过.set_series_opts进行配置
# 2.添加系列数据的时候设置

# 颜色配置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

# bar = (
#     Bar()
#         .add_xaxis(x_data,itemstyle_opts=opts.ItemStyleOpts(color='red'))
#         .add_yaxis('图例1', y_data)
#         .set_series_opts(itemstyle_opts=opts.ItemStyleOpts(color='green'))
# )
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('系列1', y_data, itemstyle_opts=opts.ItemStyleOpts(color='green'))
)

bar.render()

# %%
# 透明度设置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1)
        .set_series_opts(itemstyle_opts=opts.ItemStyleOpts(opacity=.5))
)

bar.render()

# %%
# 描边颜色
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('图例1', y_data_1, itemstyle_opts=opts.ItemStyleOpts(border_color='black'))
)

bar.render()

# %%
# 颜色设置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 标题样式配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题',
                                                   subtitle='副标题',
                                                   title_textstyle_opts=opts.TextStyleOpts(color='red'),
                                                   subtitle_textstyle_opts=opts.TextStyleOpts(color='blue')))
)
bar.render()

# %%
# 字体风格
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_global_opts(title_opts=
                         opts.TitleOpts(title='主标题',
                                        # 可选：'normal'，'italic'，'oblique'
                                        title_textstyle_opts=opts.TextStyleOpts(font_style='italic')))
)

bar.render()

# %%
# 字体粗细
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_global_opts(title_opts=
                         opts.TitleOpts(title='主标题',
                                        # 'normal'，'bold'，'bolder'，'lighter'
                                        title_textstyle_opts=opts.TextStyleOpts(font_weight='lighter')))
)
bar.render()

# %%
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题', title_textstyle_opts=opts.TextStyleOpts(font_size=20)))
)

bar.render()

# %%
# 文本字体
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 标题样式配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_global_opts(
        title_opts=opts.TitleOpts(title='主标题', title_textstyle_opts=opts.TextStyleOpts(font_family='Arial')))
)

bar.render()

# %%
# 富文本(暂略)

# %%
# LabelOpts-标签配置项
# 显示/关闭标签

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 标题样式配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

bar.render()

# %%
# 标签位置
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

# 标题样式配置
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .add_yaxis('', y_data_2)
        # .set_series_opts(label_opts=opts.LabelOpts(is_show=True,
        #                                            # 标签的位置。可选
        # 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'
        # 'insideTop'，'insideBottom'， 'insideTopLeft'，'insideBottomLeft'
        # 'insideTopRight'，'insideBottomRight'
        #                                            position='inside'))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside'))
)

bar.render()

# %%
# LineStyleOpts：线样式配置项
# 线宽

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('线宽5', y_data_1, linestyle_opts=opts.LineStyleOpts(width=5))
        .add_yaxis('线宽1', y_data_2, linestyle_opts=opts.LineStyleOpts(width=1))
        )

line.render()

# %%
# 线型
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]
y_data_3 = [223, 453, 189, 207, 221, 123]

# 'solid', 'dashed', 'dotted'
line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('solid', y_data_1, linestyle_opts=opts.LineStyleOpts(type_='solid'))
        .add_yaxis('dashed', y_data_2, linestyle_opts=opts.LineStyleOpts(type_='dashed'))
        .add_yaxis('dotted', y_data_3, linestyle_opts=opts.LineStyleOpts(type_='dotted'))
        )

line.render()

# %%
# 颜色
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]
y_data_3 = [223, 453, 189, 207, 221, 123]

# 注意区分线和图元
line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('1', y_data_1, color='green')
        .add_yaxis('2', y_data_2, color='green', linestyle_opts=opts.LineStyleOpts(color='black'))
        .add_yaxis('3', y_data_3, linestyle_opts=opts.LineStyleOpts(color='black'))
        )

line.render()

# %%
# SplitLineOpts-分割线配置项
# 显示分割线
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]

# 分割线
line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_1)
        .set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
                         yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)))
        )

line.render()

# %%
# SplitAreaOpts：分隔区域配置项
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

# 分割线
line = (Line()
    .add_xaxis(x_data)
    .add_yaxis('', y_data)
    .set_global_opts(
    # 显示Y轴分割区域
    yaxis_opts=opts.AxisOpts(splitarea_opts=
                             opts.SplitAreaOpts(is_show=True,
                                                areastyle_opts=opts.AreaStyleOpts(opacity=1))))
)

line.render()

# %%
# AreaStyleOpts：区域填充样式配置项
"""
显示填充区域
默认opacity=0,即不限时，如需显示设置opacity大于0，opacity介于0到1之间。
"""

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

line = (Line()
    .add_xaxis(x_data)
    .add_yaxis('', y_data)
    .set_global_opts(
    yaxis_opts=opts.AxisOpts(splitarea_opts=
                             opts.SplitAreaOpts(is_show=True,
                                                areastyle_opts=opts.AreaStyleOpts(opacity=.6))))
)

line.render()

# %%
# 颜色

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

line = (Line()
    .add_xaxis(x_data)
    .add_yaxis('', y_data)
    .set_global_opts(
    xaxis_opts=opts.AxisOpts(splitarea_opts=
                             opts.SplitAreaOpts(is_show=True,
                                                areastyle_opts=opts.AreaStyleOpts(opacity=.6, color='grey'))))
)

line.render()

# %%
# EffectOpts-涟漪特效配置项
# 特效类型
# 可选 'stroke' 和 'fill'
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

effectscatter = (EffectScatter()
                 .add_xaxis(x_data)
                 .add_yaxis('stoke', y_data_1, effect_opts=opts.EffectOpts(brush_type='stroke'))
                 .add_yaxis('fill', y_data_2, effect_opts=opts.EffectOpts(brush_type='fill'))
                 )

effectscatter.render()

# %%
# 范围&周期
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_1 = [123, 153, 89, 107, 98, 23]
y_data_2 = [231, 321, 135, 341, 245, 167]

effectscatter = (EffectScatter()
                 .add_xaxis(x_data)
                 .add_yaxis('stoke', y_data_1, effect_opts=opts.EffectOpts(scale=10, period=5))
                 .add_yaxis('fill', y_data_2, effect_opts=opts.EffectOpts(scale=5, period=10))
                 )

effectscatter.render()

# %%
# 形状
# ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',
# 'diamond', 'pin', 'arrow', 'none'
# 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。

data = [['北京', '上海'], ['武汉', '深圳'], ['拉萨', '北京'], ['深圳', '上海']]

geo = (Geo()
       .add_schema(maptype='china')
       .add('', data, type_='lines',
            effect_opts=opts.EffectOpts(symbol=r'image://C:\Users\bolat\Desktop\2.jpg', symbol_size=10))
       )

geo.render()

# %%
# 标记大小

data = [['北京', '上海'], ['武汉', '深圳'], ['拉萨', '北京'], ['深圳', '上海']]

geo = (Geo()
       .add_schema(maptype='china')
       .add('', data, type_='lines', effect_opts=opts.EffectOpts(symbol='circle', symbol_size=10))
       )

geo.render()

# %%
# 标记点
# 特殊值标点
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

# 特殊值标记
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                         markpoint_opts=opts.MarkPointOpts(
                             data=[opts.MarkPointItem(type_='max', name='最大值'),
                                   opts.MarkPointItem(type_='average', name='平均值'),
                                   opts.MarkPointItem(type_='min', name='最小值'), ]))
)

# bar = (
#     Bar()
#         .add_xaxis(x_data)
#         .add_yaxis('', y_data)
#         .set_series_opts(
#         # 为了不影响标记点，这里把标签关掉
#         label_opts=opts.LabelOpts(is_show=False),
#         markpoint_opts=opts.MarkPointOpts(
#             data=[
#                 opts.MarkPointItem(type_="max", name="最大值"),
#                 opts.MarkPointItem(type_="min", name="最小值"),
#                 opts.MarkPointItem(type_="average", name="平均值"),
#             ]))
# )

bar.render()

# %%
# 自定义标记
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

# 三种定位方式如下

data = [
    # 根据坐标定位
    opts.MarkPointItem(coord=['Xiaomi', 90], name="坐标", value='coord'),
    # 根据像素值定位
    opts.MarkPointItem(x=200, y=160, name="像素值", value='px'),
    # 设置显示的value
    opts.MarkPointItem(coord=[5, 150], name="设置value", value='hi'),
]
bar = (
    Bar()
        .add_xaxis(x_data)
        .add_yaxis('', y_data)
        .set_series_opts(
        # 为了不影响标记点，这里把标签关掉
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=data))
)
bar.render()

# %%
# 指定维度
# 在设置type_时，我们可以指定是按照X or Y轴进行标记。
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(
                            data=[opts.MarkPointItem(type_='max', name='y轴最大', value_index=1),
                                  opts.MarkPointItem(type_='max', name='x轴最大', value_index=0)]))
       )

bar.render()

# %%
# 标记线
# 特殊值标记

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       .set_global_opts(yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)))
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markline_opts=opts.MarkLineOpts(
                            data=[opts.MarkLineItem(type_='max', name='max'),
                                  opts.MarkLineItem(type_='min', name='min'),
                                  opts.MarkLineItem(type_='average', name='average')]))
       )

bar.render()

# %%
# 自定义标记线

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markline_opts=opts.MarkLineOpts(
                            data=[opts.MarkLineItem(x='Xiaomi', name='x=Xiaomi'),
                                  opts.MarkLineItem(y=100, name='y=100')]))
       )

bar.render()

# %%
# 标记区域
date_list = ['10月{}日'.format(i) for i in range(1, 32)]
data = [random.randint(10, 100) for _ in date_list]

line = (Line()
    .add_xaxis(date_list)
    .add_yaxis('', data)
    .set_series_opts(markarea_opts=opts.MarkAreaOpts(
    data=[opts.MarkAreaItem(name="十一黄金周", x=("10月1日", "10月7日"),
                            itemstyle_opts=opts.ItemStyleOpts(color='gray', opacity=.1)),
          ])
)
)

line.render()
