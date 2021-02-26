from datetime import datetime

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import *

from common import utils

file_path = r'数据分析项目/database/order2019.xlsx'
df = pd.read_excel(file_path)
df.head()
# %%
"""
字段说明:
id ： 序号
orderID ：订单id
userID ：用户id
goodsID ：商品id
orderAmount ：订单总额
payment ：买家实际支付金额
chanelID ：渠道id
platfromType ：购买渠道
orderTime ：订单产生时间
payTime ：订单支付时间，为2019-01-01至2020-05-28这个时间段的数据（主要以订单支付时间作为分析基础）
chargeback ：是否退款
"""

# %%
# print(utils.show_na(df))    # chanelID 存在8个缺失
# print(utils.show_info(df))
# print(utils.show_duplicated(df))    # 不存在重复值

# %%
"""
二、结论先行
1. 销量分析：用户的整体转换率高，双十一双十二活动效果明显
继续保持用户转化率，后续可以利用更多节假日所在月，复制双十一双十二的促销活动，增加销售额
针对性的对网页版和阿里平台进行店铺优化设计和渠道推广，同时借鉴WechatMP微信公众号平台和APP这
两个购买渠道之所以受到用户欢迎的要点——可针对性的对这几个购买渠道做埋点以及用户行为路径分析、页面评估

2.用户购买次数分析：复购率和人均购买次数极低，平台主要为“一次性买卖”
提高品牌影响力，培养用户忠实度，同时进一步挖掘已有客户的购买力

3. 使用RFM模型进行用户价值分类：针对不同客户群体，分别针对性的采取运营措施
重要价值用户：对其投入耕作资源，提供vip服务、个性化服务，保持其黏性的同时又继续引导其消费
潜力客户：这类客户需要对其深入挖掘，对其销售一些价值更高的产品，并要求其评论，根据评论内容找出其诉求和痛点，吸引他们
重要深耕用户：给其不定时发送促销活动提醒和优惠券活动等
新用户：组织社群活动，在群内不定时提供小样免费试用或抽奖活动，以及拉新进群达到一定数量即可获取大额优惠券等，提高用户兴趣，创建品牌知名度
重要换回用户：精准营销，根据用户画像等为用户提供其可能会关注或感兴趣的商品，通过续关店铺或出产更新更吸引人的产品赢回他们
一般用户：可以采用每日店铺打卡获取积分，积分可兑换热门产品小样或店铺内抽奖，让其持续不断关注到店铺
重要挽回用户：重点回访，针对性提问用户不再购买的可能性原因，并在此基础上重新向客户营销，如回答服务态度方面，安抚；如回答产品质量方面，则回答已改进，请重新试用并寄去小样等
流失客户：尝试恢复其兴趣，如无果，则不再浪费时间
三、分析框架
1.销量分析：购买时间，商品类别，购买渠道，转化率 ：转化流程为订单创建 -> 订单付款 -> 订单成交（未被退款）
2.用户购买次数分析：用户购买次数分布 （频次图）、人均购买次数（支付并未退款）、复购率（复购率=购买次数在2次及以上的人数/有购买行为的人数）
3.使用RFM模型进行用户价值分类
"""

# %%
# platfromType 字段存在多余的空格,需要修正
df['platfromType'] = df['platfromType'].str.replace(' ', '')
# %%
# 数据分析
data_not_chargeback = df[df['chargeback'] == '否']
data_by_month = data_not_chargeback.resample('M', on='payTime')['payment'].sum()
data_by_month = data_by_month.round(2)

x = ['{}年{}月'.format(x, y) for x, y in
     zip(data_by_month.index.year, data_by_month.index.month)]

line = (
    Line()
        .add_xaxis(x)
        .add_yaxis('销售额', data_by_month.to_list())
        .set_global_opts(title_opts=opts.TitleOpts('销售额月走势情况'))
)

line.render()
utils.fix_matplotlib_error()
sns.lineplot(data=data_by_month, x=x, y=data_by_month,
             linestyle='--', markers='^')
plt.xticks(rotation=90)
plt.show()

"""
在2019-01-01至2020-05-28这段时间，销售最高额出现在“双十一”活动所在月——11月，
销售额达1064万，占2019年度销售总额的10.08%
19年1月至2月出现大幅度下降，到了3月开始迅速上升，5月冲上小高峰，随后一直处于高峰时期，到10月份有一定回落，
随后双11双12所在月迎来全年高峰时刻，进入2020年后则由于疫情影响，迅速跌入谷底并持续低迷，直至5月份仅434元销售额
"""

# %%
# 按商品类别进行统计

df_pt = pd.pivot_table(data=df, index='goodsID', values=['id', 'payment'],
                       aggfunc={'id': 'count', 'payment': 'sum'})

dnc_pt = pd.pivot_table(data=data_not_chargeback, index='goodsID', values=['id', 'payment'],
                        aggfunc={'id': 'count', 'payment': 'sum'})

top_10 = pd.merge(df_pt, dnc_pt, left_index=True, right_index=True)
top_10.rename(columns={'id_x': '销售数量', 'id_y': '实际销售数量',
                       'payment_x': '销售金额', 'payment_y': '实际销售金额'}, inplace=True)

top_10 = top_10.iloc[:, [2, 0, 1, 3]]
top_10['总销量占比'] = top_10['实际销售数量'] / top_10['销售数量']
top_10['销售额占比'] = top_10['实际销售金额'] / top_10['销售金额']

# %%
# 根据购买渠道进行销量统计
platfromType = data_not_chargeback.groupby('platfromType')['payment'].sum().reset_index()
platfromType.sort_values('payment', ascending=False, inplace=True)
plt.figure(figsize=(16, 12))
sns.barplot(data=platfromType, x='platfromType', y='payment', palette='Blues_r')
plt.xlabel('渠道平台', fontdict={'fontsize': 25})
plt.ylabel('销售金额', fontdict={'fontsize': 25})
plt.show()
"""
从上图可以看出：用户主要是通过WechatMP微信公众号平台和APP进行购买的，其次是网页版，
再次是阿里平台，微信商店和wap是最低
"""

# %%
print(df['chargeback'].value_counts())

sns.countplot(data=df, x='chargeback')
plt.show()

# %%
# 因为数据集里面的记录全部为已付款的,所以这里用订购时间模拟出一个创建订单的数据
rates = pd.Series({'创建': df['orderTime'].count() * 1.2,
                   '付款': df['payTime'].count(),
                   '实际付款': df[df['chargeback'] == '否'].shape[0]}, name='订购量').to_frame()
rates['整体转化率'] = rates['订购量'].apply(lambda x: round((x * 100 / rates.iloc[0, 0]), 2))
funnel = (
    Funnel()
        .add('转化率', [list(z) for z in zip(rates.index, rates['整体转化率'])])
        .set_series_opts(label_opts=opts.LabelOpts(position='inside', formatter='{b}:{c}'))
        .set_global_opts(title_opts=opts.TitleOpts('整体转化率(%)'))
)
funnel.render()

"""
从“整体转换率”可以看出：用户的整体转换率还是较高的，实际成交转化率达86.82%，需要继续保持
小结：双十一双十二的活动非常有效，后续可以利用更多节假日所在月，复制双十一双十二的促销活动，
增加销售额；再针对性的对网页版和阿里平台进行店铺优化设计和渠道推广，同时借鉴WechatMP微信公众号
平台和APP这两个购买渠道之所以受到用户欢迎的要点——可针对性的对这几个购买渠道做埋点以及用户行为路径分析、页面评估
"""

# %%
# 用户购买次数分析
uer_buy_time = data_not_chargeback.groupby('userID')['goodsID'].count()
sns.histplot(data=uer_buy_time, x=uer_buy_time)
plt.xlabel('购买频数')
plt.ylabel('用户数量')
plt.show()

# %%
# 人均购买次数
total_buy_time = data_not_chargeback['userID'].count()
total_paying_user_num = data_not_chargeback['userID'].nunique()
user_avg_buy_time = total_buy_time / total_paying_user_num

# 复购率 购买2次及以上
user_mul_buy_num = uer_buy_time[uer_buy_time.values >= 2].count()
rebuy_rate = user_mul_buy_num / total_paying_user_num

"""
观察结果：从用户购买次数分布频次图可看出，凡是成功完成本次交易（支付成功且未退款）的用户，均存在10次以内的交易频率；
而用户人均购买次数为1次，复购率22.8%
小结：综合以上结果来看，该电商平台基本上都为一次性交易的买卖，付费用户的复购率偏低，
需要想办法培养一批忠实用户；结合用户购买次数频次图来看，该平台所有付费用户都只存在10次以内的交易频率，
需要大力挖掘这批客户的购买力，针对性的推出营销挽回方案
"""

# %%
# 3. 使用RFM模型进行用户价值分类
# 1） 计算RFM三个指标
df_rfm = pd.pivot_table(data=data_not_chargeback, index='userID', values=['goodsID', 'payment', 'payTime'],
                        aggfunc={'goodsID': 'count', 'payment': 'sum',
                                 'payTime': 'max'})
df_rfm.rename(columns={"goodsID": 'F', 'payment': 'M', 'payTime': 'R'}, inplace=True)

df_rfm['R'] = df_rfm['R'].apply(lambda x: (datetime(2021, 2, 26) - x))
df_rfm['R'] = df_rfm['R'].dt.days

# %%
# 给RFM三个指标分别打分
avg_r = df_rfm['R'].mean()
avg_f = df_rfm['F'].mean()
avg_m = df_rfm['M'].mean()

df_rfm['R_Score'] = df_rfm['R'].apply(lambda x: 1 if x > avg_r else 0)
df_rfm['F_Score'] = df_rfm['F'].apply(lambda x: 1 if x > avg_f else 0)
df_rfm['M_Score'] = df_rfm['M'].apply(lambda x: 1 if x > avg_m else 0)


def set_users_label(x):
    if x.iloc[0] == 1 and x.iloc[1] == 1 and x.iloc[2] == 1:
        return '重要价值客户'
    elif x.iloc[0] == 1 and x.iloc[1] == 1 and x.iloc[2] == 0:
        return '潜力客户'
    elif x.iloc[0] == 1 and x.iloc[1] == 0 and x.iloc[2] == 1:
        return '重要深耕客户'
    elif x.iloc[0] == 1 and x.iloc[1] == 0 and x.iloc[2] == 0:
        return '新客户'
    elif x.iloc[0] == 0 and x.iloc[1] == 1 and x.iloc[2] == 1:
        return '重要唤回客户'
    elif x.iloc[0] == 0 and x.iloc[1] == 1 and x.iloc[2] == 0:
        return '一般客户'
    elif x.iloc[0] == 0 and x.iloc[1] == 0 and x.iloc[2] == 1:
        return '重要挽回客户'
    elif x.iloc[0] == 0 and x.iloc[1] == 0 and x.iloc[2] == 0:
        return '流失客户'


df_rfm['label'] = df_rfm[['R_Score', 'F_Score', 'M_Score']].apply(set_users_label, axis=1)  #
user_type = df_rfm['label'].value_counts().reset_index()
user_costs = df_rfm.groupby('label')['M'].sum().reset_index()
# %%
user_costs.sort_values('M', inplace=True)
# %%
plt.figure(figsize=(16, 24))
plt.subplot(211)
sns.barplot(data=user_type, x='index', y='label', palette='Blues_r')
plt.title('不同类型用户数量')
plt.subplot(212)
sns.barplot(data=user_costs, x='label', y='M', palette='Reds')
plt.title('不同类型用户数量')
plt.show()
