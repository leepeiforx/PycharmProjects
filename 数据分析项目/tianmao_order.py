import pandas as pd
import common.utils as u
from pyecharts.charts import *
from pyecharts import options as opts

# %%
file_path = r'D:\file\DataAnalysis\tmall6650.zip'
df = pd.read_csv(file_path)

# %%
print(u.show_info(df))
print(u.show_na(df))
print(u.show_duplicated(df))

# %%
df.rename(columns={'订单付款时间 ': '订单付款时间', '收货地址 ': '收货地址'}, inplace=True)

# %%
df['订单创建时间'] = pd.to_datetime(df['订单创建时间'], format='%Y-%m-%d %H:%M:%S')
df['订单付款时间'] = pd.to_datetime(df['订单付款时间'], format='%Y-%m-%d %H:%M:%S')

# %%
order_ct = len(df['订单编号'])
payed_order = df[~df['订单付款时间'].isna()]
df_trans = df[df['买家实际支付金额'] != 0]
full_payed = df[(df['总金额'] == df['买家实际支付金额'])]

dict_convs = {'总订单数': order_ct, '付款订单数': len(payed_order),
              '到款订单数': len(df_trans), '全额付款订单数': len(full_payed)}

df_convs = pd.Series(dict_convs, name='订单数').to_frame()

# 添加总体转化率,每个环节除以总订单数
df_convs['convs_perc'] = round(df_convs['订单数'] / df_convs.iloc[0, 0] * 100, 2)

# %%
# 总体转化率
data_pair = list(z for z in zip(df_convs.index, df_convs['convs_perc']))
funnel = (
    Funnel()
        .add('总体转化率', data_pair=data_pair,
             is_selected=True, label_opts=opts.LabelOpts(position='inside'))
        .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter='{a}<br/>{b}:{c}%'))
        .set_global_opts(title_opts=opts.TitleOpts(title='总体转化率'),
                         tooltip_opts=opts.TooltipOpts(formatter='{a}<br/>{b}:{c}%'))
)
funnel.render()

# %%
# 单一环节转化率
name = r'单一环节转化率'
df_convs['shift'] = df_convs['订单数'].shift()
df_convs['shift'].fillna(df_convs.iloc[0, 0], inplace=True)
df_convs['single_convas'] = round(df_convs['订单数'] / df_convs['shift'] * 100, 2)
df_convs.drop(columns='shift', inplace=True)

data_pair = list(z for z in zip(df_convs.index, df_convs['single_convas']))
funnel = (
    Funnel()
        .add(name, data_pair=data_pair,
             is_selected=True, label_opts=opts.LabelOpts(position='inside'))
        .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter='{a}<br/>{b}:{c}%'))
        .set_global_opts(title_opts=opts.TitleOpts(title=name),
                         tooltip_opts=opts.TooltipOpts(formatter='{a}<br/>{b}:{c}%'))
)
funnel.render()

# %%
# 整体订单数趋势
df_time = df.set_index('订单创建时间')
df_time = df_time.resample('D')['订单编号'].count().reset_index()
line = (Line()
        .add_xaxis(df_time['订单创建时间'].dt.date.to_list())
        .add_yaxis('订单数量', df_time['订单编号'].to_list())
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(xaxis_opts=opts.AxisOpts(name='订单创建时间', name_location='center'))
        )
line.render()

# %%
# 销量区域分布-地理图
se_trans_map = df.groupby('收货地址')['订单编号'].count().reset_index()

#%%
# 处理收货地址中的"自治区","省"字符,strip掉
def strip_region(tab):
    tab['收货地址'] = tab['收货地址'].str.replace('省', '')
    for row in range(len(tab)):
        if tab.iloc[row, 0].endswith('自治区'):
            if tab.iloc[row, 0] == '内蒙古自治区':
                tab.iloc[row, 0] = tab.iloc[row, 0][:3]
            else:
                tab.iloc[row, 0] = tab.iloc[row, 0][:2]


strip_region(se_trans_map)
data_pair = list(z for z in zip(se_trans_map['收货地址'], se_trans_map['订单编号']))
map = (Map()
       .add('', data_pair=data_pair)
       .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=se_trans_map['订单编号'].max()*0.6))
       )

map.render()
