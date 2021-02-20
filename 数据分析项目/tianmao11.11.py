import zipfile
import pandas as pd
import numpy as np

# %%

file_path = r'C:\Users\bolat\Desktop\file\DataAnalysis\beautymakeup3411.zip'
zip_file = zipfile.ZipFile(file_path)
# zip_file.filelist[0].filename
# 注:当压缩包里只有一个文件时,可以直接用pandas读取,如果存在多个文件的话,则要使用zip_file解压,取文件名然后再读取.
df = pd.read_csv(zip_file.open(zip_file.filelist[0].filename))
# %%
'''
可参考的探索方向：
购买化妆品的客户的关注度(评论数)是多少？各产品销量分布情况？
哪些产品的卖得最好，哪些牌子最受欢迎，哪些化妆品是大家最需要的？
不同商家之间的差异，及促销打折力度？
模拟定价系统及推荐系统？
'''
df.head()
# %%
df.shape
# %%
# 查看各字段信息
df.info()

# %%
# 数据清洗
# 1.检查NA数据
df.isna().sum()
# 有两列数据存在缺失值：sale_count, comment_count
# %%
# 查看数据的描述性统计
df.describe()
# %%
# 查看sales_count,comments_count列的众数
df['sale_count'].mode()
df['comment_count'].mode()
# 考虑用众数来替换na值
df_fillna = df.fillna(0)
# %%
# 检查数据是否存在重复行
print(len(df_fillna.drop_duplicates()))
df_fillna.drop_duplicates(inplace=True)
# %%
# 经过删除操作之后,但索引没变,因此应用reindex重置索引
df_fillna.reset_index(inplace=True, drop=True)

# %%
# 提取表格中有用信息并新增为列
# 对商品标签进行分词处理
import jieba

title_cut = []
for t in df_fillna['title']:
    t = jieba.lcut(t)
    title_cut.append(t)

df_fillna['item_name_cut'] = title_cut

# %%
df_fillna[['title', 'item_name_cut']].head()

# %%
# 给商品添加分类
basic_config_data = """
护肤品	套装	    套装							
护肤品	乳液类	乳液	美白乳	润肤乳	凝乳	柔肤液'	亮肤乳	菁华乳	修护乳
护肤品	眼部护理	眼霜	眼部精华	眼膜					
护肤品	面膜类	面膜													
护肤品	清洁类	洗面	洁面	清洁	卸妆	洁颜	洗颜	去角质	磨砂						
护肤品	化妆水	化妆水	爽肤水	柔肤水	补水露	凝露	柔肤液	精粹水	亮肤水	润肤水	保湿水	菁华水	保湿喷雾	舒缓喷雾
护肤品	面霜类	面霜	日霜	晚霜	柔肤霜	滋润霜	保湿霜	凝霜	日间霜	晚间霜	乳霜	修护霜	亮肤霜	底霜	菁华霜
护肤品	精华类	精华液	精华水	精华露	精华素										
护肤品	防晒类	防晒霜	防晒喷雾												
化妆品	口红类	唇釉	口红	唇彩											
化妆品	底妆类	散粉	蜜粉	粉底液	定妆粉 	气垫	粉饼	BB	CC	遮瑕	粉霜	粉底膏	粉底霜		
化妆品	眼部彩妆	眉粉	染眉膏	眼线	眼影	睫毛膏									
化妆品	修容类	鼻影	修容粉	高光	腮红	
"""

category_config_map = {}
print(basic_config_data.split('\n'))
for config_line in basic_config_data.split('\n'):
    basic_config_list = config_line.strip().strip('\n').strip('\t').split('\t')
    if len(basic_config_list) < 2:
        pass
    else:
        main_category = basic_config_list[0]
        sub_category = basic_config_list[1]
        unit_category_list = basic_config_list[2:]
        for unit_category in unit_category_list:
            if unit_category and unit_category.strip().strip('\t').strip('\n'):
                category_config_map[unit_category] = (main_category, sub_category)

# %%
sub_type = []  # 子类别
main_type = []  # 主类别
for i in range(len(df_fillna)):
    exist = False
    for temp in df_fillna['item_name_cut'][i]:
        if temp in category_config_map:
            sub_type.append(category_config_map.get(temp)[1])
            main_type.append(category_config_map.get(temp)[0])
            exist = True
            break
    if not exist:
        sub_type.append('其他')
        main_type.append('其他')

print(len(sub_type), len(main_type), len(df_fillna))
# %%
# 将主类,子类分别构造一列加入数据中
df_fillna['sub_type'] = sub_type
df_fillna['main_type'] = main_type
print(df_fillna['sub_type'].value_counts())
print(df_fillna['main_type'].value_counts())

# %%
# 将'是否适用于男士'新增为一列
gender = []
for i in range(len(df_fillna)):
    if '男' in df_fillna['item_name_cut'][i]:
        gender.append('yes')
    elif '男士' in df_fillna['item_name_cut'][i]:
        gender.append('yes')
    elif '男生' in df_fillna['item_name_cut'][i]:
        gender.append('yes')
    else:
        gender.append('no')

df_fillna['whether for male'] = gender

df_fillna['whether for male'].value_counts()

# %%
# （5）新增销售额、购买日期（天）为一列
df_fillna['sales amount'] = df_fillna['sale_count'] * df_fillna['price']

# %%
# 新增购买日期为一列(将update_time列转换为日期格式)
df_fillna['update_time'] = pd.to_datetime(df_fillna['update_time'])

# %%
# 设置'update_time'为index
df_fillna = df_fillna.set_index(df_fillna['update_time'])

# 新增时间'天'为一列
df_fillna['day'] = df_fillna.index.day

# 删除中文分词一列
df_fillna.drop(columns='item_name_cut', inplace=True)

print(df_fillna.head())
# %%
print(df_fillna.info())

# 保存备份
df_fillna.to_excel('clean_beautymakup.xlsx', sheet_name='clean_date')

# %%
# 数据探索
import matplotlib.pyplot as plt
import seaborn as sns
import pyecharts as py

# %%
# 各品牌SKU
file_path = r'C:\Users\my_c\PycharmProjects\pythonProject\clean_beautymakup.xlsx'
df_plot = pd.read_excel(file_path)
# 将列'店名'改为'品牌名'

df_plot.rename(columns={'店名': '品牌名'}, inplace=True)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

plt.figure(figsize=(8, 6))
brand_num \
    = df_plot['品牌名'].value_counts(ascending=False). \
    plot(kind='bar', alpha=.4, width=.8, color='b')
plt.show()

# %%
# 计算各品牌总销量和总销售额
sales_by_brand = df_plot['sale_count'].groupby(by=df_plot['品牌名']).sum() / 10000  # 为了绘图和统计方便,所以单位改为万
sales_by_brand.sort_values(ascending=True, inplace=True)
df_plot.rename(columns={'sales amount': 'turnover'}, inplace=True)
turnover_by_brand = df_plot['turnover'].groupby(by=df_plot['品牌名']).sum() / 10000  # 为了绘图和统计方便,所以单位改为万
turnover_by_brand.sort_values(ascending=True, inplace=True)
plt.figure(figsize=(12, 16))
plt.subplot(1, 2, 1)
sales_by_brand.plot(kind='barh', title='销量')
plt.subplot(1, 2, 2)
turnover_by_brand.plot(kind='barh', title='销售额')
plt.subplots_adjust(wspace=.4)
plt.show()

'''
相宜本草的销售量和销售额都是最高的。销量第二至第五，分别为美宝莲、悦诗风吟、妮维雅、欧莱雅；
销售额第二至第五，分别为欧莱雅、佰草集、美宝莲、悦诗风吟。 宝莲、悦诗风吟、欧莱雅都在销量、销售额前五中。
'''

# %%
# 3.3 各类别的销售量、销售额情况
main_type = df_plot['sale_count'].groupby(by=df_plot['main_type']).sum() / 10000
sub_type = df_plot['sale_count'].groupby(by=df_plot['sub_type']).sum() / 10000

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title('主类别占比')
plt.pie(main_type,
        explode=None,
        pctdistance=.7,  # 设置百分比标签与圆心的距离
        autopct='%.1f',  # 设置百分比的格式，这里保留一位小数
        labels=main_type.index,
        labeldistance=1.05,  # 设置标签与圆心的距离
        startangle=60,  # 设置饼图的初始角度
        radius=1.1,  # 设置饼图的半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针方向
        wedgeprops={'linewidth': 1.2, 'edgecolor': 'k'},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 10, 'color': 'k'})  # 设置文本标签的属性值
plt.subplot(1, 2, 2)
plt.title('二级分类占比')
plt.pie(sub_type,
        labels=sub_type.index,
        autopct='%.1f%%',
        pctdistance=0.8,
        labeldistance=1.05,
        startangle=230,
        radius=1.1,
        counterclock=False,
        wedgeprops={'linewidth': 1.2, 'edgecolor': 'k'},
        textprops={'fontsize': 10, 'color': 'k'}, )
plt.show()

'''
从主类别销售量占比情况来看，
    护肤品的销量远大于化妆品；
从子类别销售量占比情况来看，
    底妆类、口红类在化妆品中销量最多，清洁类、化妆水、面霜类在护肤品中销量最多。
'''
# %%
plt.figure(figsize=(16, 10))
sns.barplot(data=df_plot, x='品牌名', y='sale_count',
            hue='main_type', saturation=.75, ci=0)

plt.title('各品牌各分类的总销量')
plt.ylabel('总销量')
plt.text(0, 78000, '注:此处也可以用堆叠图,对比效果更直接',
         verticalalignment='top', horizontalalignment='left', color='gray',
         fontsize=10)
plt.show()

plt.figure(figsize=(16, 10))
sns.barplot(data=df_plot, x='品牌名', y='turnover',
            hue='main_type', saturation=.75, ci=0)
plt.title('各品牌各分类的总销售额')
plt.ylabel('总销量')
plt.text(0, 78000, '注:此处也可以用堆叠图,对比效果更直接',
         verticalalignment='top', horizontalalignment='left', color='gray',
         fontsize=10)
plt.show()
'''
各品牌的化妆品、护肤品销量、销售情况均不一样，这与品牌的定位有关， 
有的品牌主打化妆品，化妆品会表现好很多，
如蜜丝佛陀等。主打护肤品的品牌，护肤品的销量销售额会表现好很多，
如欧莱雅、佰草集等。 有的品牌如美宝莲、兰蔻、悦诗风吟，化妆品和护肤品的销售、
销售额都还不错。
'''

# %%
plt.figure(figsize=(16, 10))
sns.barplot(data=df_plot, x='品牌名', y='sale_count',
            hue='sub_type', saturation=.75, ci=0)

plt.title('各品牌二级分类的总销量')
plt.ylabel('总销量')
plt.legend(loc='right')
plt.show()

plt.figure(figsize=(16, 10))
sns.barplot(data=df_plot, x='品牌名', y='turnover',
            hue='sub_type', saturation=.75, ci=0)
plt.title('各品牌各二级分类的总销售额')
plt.ylabel('总销量')
plt.legend(loc='right')
plt.show()

# %%
# 各品牌热度
plt.figure(figsize=(12, 16))
df_comment = df_plot['comment_count'].groupby(by=df_plot['品牌名']).mean()
df_comment.sort_values(ascending=False, inplace=True)
sns.barplot(x=df_comment.values, y=df_comment.index)
plt.xlabel('评论数')
plt.title('各品牌商品平均评论数')
plt.show()

# %%
# 销量与热度分布关系
plt.figure(figsize=(12, 10))
x = df_plot['sale_count'].groupby(by=df_plot['品牌名']).mean()
y = df_plot['comment_count'].groupby(by=df_plot['品牌名']).mean()
s = df_plot['price'].groupby(by=df_plot['品牌名']).mean()
txt = df_plot['id'].groupby(by=df_plot['品牌名']).count().index

sns.scatterplot(x=x, y=y, hue=s, size=s, sizes=(100, 1500), data=df_plot)
for i in range(len(txt)):
    plt.annotate(txt[i], xy=(x[i], y[i]))
plt.show()
'''
由上图所示：越靠上的品牌热度越高，越靠右的品牌销量越高，颜色越深圈越大价格越高
热度与销量呈现一定的正相关；
美宝莲热度第一，销量第二，妮维雅热度第二，销量第四，两者价格均相对较低；
价格低的品牌热度和销量相对较高，价格高的品牌热度和销量相对较低，
说明价格在热度和销量中有一定影响；
'''

# %%
# 3.5 各品牌价格分布
plt.figure(figsize=(12, 10))
sns.boxplot(x='品牌名', y='price', data=df_plot)
plt.ylim([0, 3000])
plt.show()

# %%
avg_price = df_plot['price'].groupby(by=df_plot['品牌名']).mean()
y = df['price'].mean()
avg_price.sort_values(ascending=False, inplace=True)
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price.index, y=avg_price.values, color='skyblue')
plt.axhline(y=y, color='r', label='total avg')
plt.show()

'''
娇兰、SKII、雪花秀、雅诗兰黛、兰蔻、资生堂这几个国际大牌的产品价格很高，
产品平均价格都在500以上，都是一线大牌；
兰芝、倩碧、玉兰油、植村秀、佰草集、薇姿、雅漾的平均价格在300-400元左右，
其中佰草集是最贵的国货品牌；
美加净作为国货品牌，性价比高，平均价格最低，妮维雅的平均价格第二低，
在100元左右；全品牌平均价格低于400元，除了前五个国际大牌其余品牌的平均价格都低于全品牌平均价格
'''

# %%
# 销量&销售额

plt.figure(figsize=(12, 10))
x = df_plot['sale_count'].groupby(by=df_plot['品牌名']).mean()
y = round(df_plot['turnover'].groupby(by=df_plot['品牌名']).mean(), 1)
s = avg_price
txt = df_plot['id'].groupby(by=df_plot['品牌名']).count().index

sns.scatterplot(x=x, y=y, data=df_plot,
                hue=s, size=s, sizes=(100, 1500),
                marker='v', alpha=.5, color='b')
for i in range(len(txt)):
    plt.annotate(txt[i], xy=(x[i], y[i]), xytext=(x[i] + 0.2, y[i] + 0.2))
plt.ylabel('销售额')
plt.xlabel('销量')
# 取消科学计数法
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.legend(loc='upper right')
plt.show()

'''
由上图所示，越靠上代表销售额越高，越靠左代表销量越高，图形越大代表平均价格越高
销售量和销售额呈现正相关；
相宜本草、美宝莲、蜜丝佛陀销量和销售额位居前三，且平均价格居中；
说明销量销售额与价格有很重要的联系；
'''
# %%
# 3.6 男性护肤品销量情况
gender_data = df_plot[df_plot['whether for male'] == 'yes']
gender_data1 = gender_data[gender_data['main_type'] != '其他']
sns.barplot(y='品牌名', x='sale_count', data=gender_data1, hue='main_type', ci=0)
plt.show()

# %%
f, ax = plt.subplots(1, 2)
plt.title('男士护肤品销量排名情况')
gender_data['sale_count'].groupby(by=gender_data['品牌名']).sum(). \
    sort_values(ascending=True).plot(kind='barh', ax=ax[0])

gender_data['turnover'].groupby(by=gender_data['品牌名']).sum(). \
    sort_values(ascending=True).plot(kind='barh', ax=ax[1])
plt.title('男士护肤品销售额排名情况')
plt.show()
'''
男士购买的大多是护肤品；
妮维雅是男生护肤品中销量遥遥领先的品牌，第二第三分别为欧莱雅、相宜本草；
'''

#%%
# 3.7 分析时间与销量的关系，体现购买高峰期
from matplotlib.pyplot import MultipleLocator
plt.figure(figsize=(12, 6))
day_sale = df_plot['sale_count'].groupby(by=df_plot['day']).sum()
day_sale.plot()
plt.grid(linestyle='-.',axis='x',color='gray',alpha=.5)
x_major_locator = MultipleLocator(1)    #把x轴的刻度间隔设置为1，并存在变量里
ax = plt.gca()   #ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator) #把x轴的主刻度设置为1的倍数
plt.xlabel('日期（11月）')
plt.ylabel('销量')
plt.show()

'''
淘宝化妆品的购买高峰在11号前几天，可能是双十一之前商家提前预热，已经有很大的优惠了，消费者的购物欲望强烈；
双十一当天，销量最低，可能是消费者为了避免网络高峰，在双11号之前提前购买了；
双十一之后的3天，销量远不如双十一之前了，但也逐步增长了，可能是商家持续打折有优惠，以及消费者的购物余热起作用。
'''

'''
总结
美妆类别中护肤品销量远大于化妆品，其中清洁类、化妆水、面霜等基础护肤类销量最高；
男士购买美妆集中在护肤品类，其中妮维雅品牌是最受男士喜爱的品牌；
价格和热度对销售量有关联，平价基础产品是大多数消费者的选择；
由于商家在双十一提前预热，巨大的优惠力度和为了避免网络高峰，不少消费者选择提前消费，销量高峰出现在双十一前几天；
双十一后3天商家持续打折优惠，消费者还保有购物余热，但远不如双十一之前。

建议
消费者对产品价格和热度关注度较高，品牌可以适当调整产品价格并通过诸如网络社交平台的方式提高品牌热度；
对于男性消费者，品牌可以定向推荐平价基础护肤产品，在销量中可以看到也有一部分男性购买化妆品，品牌可以在护肤品中适当捆绑化妆品产品带动消费；
消费者购买欲望并不集中在双十一当天，商家可以提前预热加大优惠力度刺激消费者提前消费，避免网络高峰。
'''