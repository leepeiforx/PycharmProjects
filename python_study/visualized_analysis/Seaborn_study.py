# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#%%

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips)

#%%

''' 虽然这些点是以二维绘制的，但可以通过根据第三(个变量对点进行着色来将
 另一个维度添加到绘图中。在seaborn中，这被称为使用“色调语义”，
 因为该点的颜色获得了意义：(hue)'''
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)

#%%

'为了强调类别之间的差异并提高可访问性，可以为每个类别使用不同的标记样式：'
sns.relplot(x='total_bill',y='tip',hue='smoker',style='smoker',data=tips)

#%%

'''也可以通过单独改变每个点的色调和样式来表示四个变量。
但是这应该谨慎，因为眼睛对形状的敏感度远低于对颜色的敏感度:'''
sns.relplot(x='total_bill',y='tip',hue='smoker',style='time',data=tips)

#%%

# 在上面的例子中，色调语义表示类别，所以使用了默认的定性调色板。
# 如果色调语义表示数值(特别是，如果它可以转换为浮点数)，默认的颜色切换到顺序调色板:
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)

# 在这两种情况下，您都可以自定义调色板，有多种方式可以实现。
# 在这里，我们使用cubehelix_palette()的字符串接口自定义一个顺序调色板:
sns.relplot(x='total_bill',y='tip',hue='size',palette="ch:r=-.5,l=.75",data=tips)

#%%

# 第三个语义变量改变每个点的大小:
sns.relplot(x='total_bill',y='tip',size='size',data=tips)

# 与matplotlib.pyplot.scatter()不同，变量的值不用于直接决定点的面积。
# 数据单位中的值范围被规范化为面积单位的范围，这个范围可以自定义
sns.relplot(x='total_bill',y='tip',size='size',sizes=(15,200),data=tips)

#%%

# 强调线图的连续性
df = pd.DataFrame(dict(times=np.arange(500),
                       values=np.random.randn(500).cumsum()))
g = sns.relplot(x='times',y='values',kind='line',data=df)

# 改变x轴坐标的显示方法可以斜着表示,不用平着挤一堆
g.fig.autofmt_xdate()

#%%

# *注: 阴影部分是由于纵坐标上多个值导致的, 取值为均值, 阴影部分是置信区间.
# 此时, 可以通过ci (confidence interval)参数来控制阴影部分, ci=None
# 也可以关闭数据聚合功能(urn off aggregation altogether), 设置estimator=None即可.

fmri = sns.load_dataset('fmri')
fmri.head()
sns.relplot(x='timepoint',y='signal',kind='line',hue='subject',col='subject',
            row='event',ci='sd',style='event',palette="ch:r=-.5,l=.75",
            dashes=False,markers=True,
            height=3,aspect=.75,linewidth=2.5,
            data=fmri.query("region=='frontal'"))

#%%

# 由于lineplot()假设您想要将y绘制为x的函数，默认行为是在
# 绘制之前按数字x对数据进行排序。但是，这可以被禁用：
df = pd.DataFrame(np.random.randn(500,2).cumsum(axis=0),columns=['X','Y'])
sns.relplot(x='X',y='Y',sort=False,kind='line',data=df)

#%%

# 聚合和表示不确定性
# 更复杂的数据集将对x变量的相同值有多个观测值。seaborn的默认行为是通过
# 绘制平均值及95%的置信区间，在每个x周围聚合多个测量值:
fmri = sns.load_dataset('fmri')
sns.relplot(x='timepoint',y='signal',kind='line',data=fmri)

# 置信区间是使用bootstrapping计算的，对于较大的数据集，
# 它可能是时间密集型的。因此，可以禁用它们:
sns.relplot(x='timepoint',y='signal',kind='line',ci=None,data=fmri)

# 尤其是对于较大的数据，另一个不错的选择是通过绘制标准差，
# 而不是置信区间来表示分布在每个时间点的分布范围:
sns.relplot(x='timepoint',y='signal',kind='line',ci='sd',data=fmri)

# 可以通过设置estimator参数为None，来完全停用聚合。
# 当数据在每个点上有多个观察值时，这可能会产生奇怪的效果。
sns.relplot(x='timepoint',y='signal',kind='line',estimator=None,data=fmri)

#%%

# Plotting subsets of data with semantic mappings
# 函数lineplot()与scatterplot()具有相同的灵活性：它可以通过修改绘图元素的色调，
# 大小和样式来显示最多三个附加变量。它使用于scatterplot()相同的API，
# 这意味着我们不需要停下来考虑控制matplotlib中线条与点外观的参数。
#
# 在lineplot()中使用语义也将决定数据的聚合方式。
# 例如，添加具有两个级别的色调语义将绘图分成两行以及错误带，
# 每个都着色以指示它们对应于哪个数据集。

sns.relplot(x='timepoint',y='signal',hue='region',kind='line',data=fmri)

#%%

# 在线条图中添加样式语义默认情况下会改变线条中的破折号模式：
sns.relplot(x='timepoint',y='signal',hue='region',
            style='event',kind='line',data=fmri)

# 但您可以通过每次观察时使用的标记识别子集，或者使用短划线或代替它们
sns.relplot(x='timepoint',y='signal',hue='region',
            style='event',kind='line',
            dashes=False,markers=True,data=fmri)

# 与散点图一样，要谨慎使用多个语义制作线图。虽然有时提供信息，
# 但它们也很难解析和解释。但当您只检查一个附加变量的变化时，
# 更改线条的颜色和样式也很有用。当打印成黑白或有色盲的人观看时，
# 这可以使绘图更容易访问：
sns.relplot(x='timepoint',y='signal',hue='event',
            style='event',kind='line',data=fmri)
# 当您使用重复测量数据（即，您有多次采样的单位）时，您还可以单独绘制每个采样单位，
# 而无需通过语义区分它们。这样可以避免使图例混乱

# units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
sns.relplot(x='timepoint',y='signal',hue='region',
            units='subject',estimator=None,kind='line',
            data=fmri.query("event == 'stim'"))

#%%

# lineplot()中默认的色彩映射和图例的处理还取决于色调语义是类别还是数值
dots = sns.load_dataset('dots').query("align == 'dots'")
print(dots.head())
sns.relplot(x='time',y='firing_rate',hue='coherence',
            style='choice',kind='line',data=dots)

# 可能会发生这样的情况：即使hue变量是数值，它也很难用线性色标表示。
# 如下示例，其中hue变量的级别以对数方式缩放。
# 您可以通过传递列表或字典为每一行提供特定的颜色值：

palette = sns.cubehelix_palette(light=.8,n_colors=6)
sns.relplot(x='time',y='firing_rate',hue='coherence',
            style='choice',
            palette=palette,kind='line',data=dots)

# 或者您可以更改色彩映射的规范化方式：
from matplotlib.colors import LogNorm
palette = sns.cubehelix_palette(light=.7,n_colors=6)
sns.relplot(x='time',y='firing_rate',hue='coherence',
            style='choice',hue_norm=LogNorm(),
            kind='line',data=dots)

# 第三个语义，size改变线的宽度：
sns.relplot(x='time',y='firing_rate',
            size='coherence',style='choice',
            kind='line',data=dots)

# 虽然size变量通常是数值型的，但是也可以用线宽映射为类别变量。
# 在这样做的时候要小心，因为除了“粗”线和“细”线之外，
# 很难区分更多。然而，当线具有高频变异性时，
# 破折号很难被察觉，因此在这种情况下，使用不同的宽度可能更有效:
sns.relplot(x='time',y='firing_rate',hue='coherence',size='choice',
            palette=palette,kind='line',data=dots)



#%%

# 用日期数据绘图
# 线图通常用于可视化与实际日期和时间相关的数据。
# 这些函数以原始格式将数据传递给底层的matplotlib函数，
# 因此他们可以利用matplotlib在tick标签中设置日期格式的功能。
# 但是所有这些格式化都必须在matplotlib层进行，
# 您应该参考matplotlib文档来了解它是如何工作的：

df = pd.DataFrame(dict(time=pd.date_range('2019-1-1',periods=500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x='time',y='value',kind='line',data=df)

g.fig.autofmt_xdate()

#%%

# 显示与切面的多种关系
# 我们在本教程中强调，虽然这些函数可以同时显示几个语义变量，
# 但这样做并不总是有效的。但是，当你想要了解两个变量之间的关系
# 如何依赖于多个其他变量时呢？
#
# 最好的方法可能是多次绘制。因为relplot()基于FacetGrid，
# 所以这很容易做到。要显示附加变量的影响，
# 而不是将其分配给图中的一个语义角色，而
# 是使用它来“切面”可视化。
# 这意味着您可以创建多个轴并在每个轴上绘制数据的子集:

sns.relplot(x='total_bill',y='tip',col='time',
            hue='smoker',data=tips)

# 您还可以通过这种方式显示两个变量的影响：
# 一个是通过在列上切面而另一个是在行上切面。
# 当您开始向网格添加更多变量时，您可能希望减小图形大小。
# 请记住，大小FacetGrid由每个切面的高度和长宽比参数化的：

sns.relplot(x='timepoint',y='signal',hue='subject',
            col='region',row='event',height=3,
            kind='line',data=fmri)

# 当您想要检查一个变量的多个级别的效果时，
# 在列上对该变量进行切面处理，然后将切面“包装”到行中:


# col_wrap 每行的最高平铺数
# aspect 纵横比

sns.relplot(x='timepoint',y='signal',hue='event',style='event',
            col='subject',col_wrap=5,
            height=3,aspect=.75,linewidth=2.5,
            kind='line',data=fmri.query("region=='frontal'"))

# 这些可视化通常被称为格点图，它们非常有效，
# 因为它们以总体模式和与这些模式的偏差的数据格式来呈现数据，
# 便于眼睛观察。虽然你应该利用scatterplot()
# 和relplot()提供的灵活性，
# 但一定要记住，几个简单的图通常比一个复杂的图更有效

#%%

# Plotting with categorical data

# Categorical scatterplots:
#     stripplot() (with kind="strip"; the default)
#     swarmplot() (with kind="swarm")

# Categorical distribution plots:
#
#     boxplot() (with kind="box")
#     violinplot() (with kind="violin")
#     boxenplot() (with kind="boxen")

# Categorical estimate plots:
#
#     pointplot() (with kind="point")
#     barplot() (with kind="bar")
#     countplot() (with kind="count")
sns.set(style='ticks',color_codes=True)

#%%

# Categorical scatterplots
tips = sns.load_dataset('tips')
sns.catplot(x='day',y='total_bill',data=tips)

# The jitter parameter controls the
# magnitude of jitter or disables it altogether:
sns.catplot(x="day", y="total_bill", jitter=False, data=tips)

# The second approach adjusts the points along the categorical
# axis using an algorithm that prevents them from overlapping.
# It can give a better representation of the distribution of
# observations, although it only works well for relatively small datasets.
# This kind of plot is sometimes called a “beeswarm” and is drawn
# in seaborn by swarmplot(), which is activated by setting kind="swarm"
# in catplot():

sns.catplot(x='day',y='total_bill',kind='swarm',data=tips)

# Similar to the relational plots, it’s possible to add another
# dimension to a categorical plot by using a hue semantic.
# (The categorical plots do not currently support size or style semantics).
# Each different categorical plotting function handles the hue semantic
# differently. For the scatter plots, it is only necessary to change the
# color of the points:

sns.catplot(x='day',y='total_bill',hue='sex',kind='swarm',data=tips)

# Unlike with numerical data, it is not always obvious how to
# order the levels of the categorical variable along its axis.
# In general, the seaborn categorical plotting functions
# try to infer the order of categories from the data.
# If your data have a pandas Categorical datatype,
# then the default order of the categories can be set there.
# If the variable passed to the categorical axis looks numerical,
# the levels will be sorted. But the data are still treated as
# categorical and drawn at ordinal positions on the categorical
# axes (specifically, at 0, 1, …) even when numbers are used to label them:

sns.catplot(x='size',y='total_bill',kind='swarm',data=tips.query("size !=3"))

# The other option for chosing a default ordering is
# to take the levels of the category as they appear
# in the dataset. The ordering can also be
# controlled on a plot-specific basis using the order parameter.
# This can be important when drawing multiple categorical
# plots in the same figure, which we’ll see more of below:

sns.catplot(x='smoker',y='tip',kind='swarm',data=tips)
sns.catplot(x='smoker',y='tip',order=['No','Yes'],kind='swarm',data=tips)

# We’ve referred to the idea of “categorical axis”.
# In these examples, that’s always corresponded to
# the horizontal axis. But it’s often helpful to put the
# categorical variable on the vertical axis (particularly
# when the category names are relatively long or there are
# many categories). To do this, swap the assignment of variables to axes:

sns.catplot(x='tip',y='smoker',kind='swarm',data=tips)

#%%

# Distributions of observations within categories
#
# As the size of the dataset grows,, categorical scatter plots
# become limited in the information they can provide about the
# distribution of values within each category. When this happens,
# there are several approaches for summarizing the distributional
# information in ways that facilitate easy comparisons across the
# category levels.

# Boxplots
# The first is the familiar boxplot(). This kind of plot shows the
# three quartile values of the distribution along with extreme values.
# The “whiskers” extend to points that lie within 1.5 IQRs of the
# lower and upper quartile, and then observations that fall outside
# this range are displayed independently. This means that each value
# in the boxplot corresponds to an actual observation in the data.

sns.catplot(x='day',y='total_bill',kind='box',data=tips)

# When adding a hue semantic, the box for each level of the semantic
# variable is moved along the categorical axis so they don’t overlap:

sns.catplot(x='day',y='total_bill',hue='smoker',kind='box',data=tips)

# This behavior is called “dodging” and is turned on by default because
# it is assumed that the semantic variable is nested within the main
# categorical variable. If that’s not the case, you can disable the dodging:
tips['weekend'] = tips['day'].isin(['Sat','Sun'])
sns.catplot(x='day',y='total_bill',hue='weekend',kind='box',data=tips)

# A related function, boxenplot(), draws a plot that is
# similar to a box plot but optimized for showing
# more information about the shape of the distribution.
# It is best suited for larger datasets:

diamonds = sns.load_dataset('diamonds')
sns.catplot(x='color',y='price',kind='boxen',
            data=diamonds.sort_values('color'))

#%%

# Violinplots
# A different approach is a violinplot(), which combines a
# boxplot with the kernel density
# estimation procedure described in the distributions tutorial:
sns.catplot(x='total_bill',y='day',hue='time',
            kind='violin',data=tips)

#%%

#This approach uses the kernel density estimate to provide
#a richer description of the distribution of values.
#Additionally, the quartile and whikser values from the
#boxplot are shown inside the violin. The downside is that,
#because the violinplot uses a KDE, there are some other
#parameters that may need tweaking, adding some complexity
#relative to the straightforward boxplot:
sns.catplot(x='total_bill',y='day',hue='time',kind='violin',
            bw=.15,cut=0,data=tips)

sns.catplot(x='total_bill',y='day',hue='time',kind='violin',
            data=tips)

#It’s also possible to “split” the violins when
#the hue parameter has only
#two levels, which can allow for a more efficient use of space:

sns.catplot(y='total_bill',x='day',hue='sex',kind='violin',
            split=True,data=tips)

#Finally, there are several options for the plot that
#is drawn on the interior of the violins, including ways
#to show each individual observation instead of the summary
#boxplot values:

#inner：控制violinplot内部数据点的表示，
#有“box”, “quartile”, “point”, “stick”四种方式

sns.catplot(x='day',y='total_bill',hue='sex',kind='violin',
            inner='stick',split=True,palette='pastel',data=tips)


#It can also be useful to combine swarmplot() or striplot()
#with a box plot or violin
# plot to show each observation along
# with a summary of the distribution:

g = sns.catplot(x='day',y='total_bill',kind='violin',inner=None,data=tips)
sns.swarmplot(x='day',y='total_bill',color='k',size=3,data=tips,ax=g.ax)

#%%

#Statistical estimation within categories
#
#For other applications, rather than showing the distribution
#within each category, you might want to show an estimate of
#the central tendency of the values. Seaborn has two main ways
#to show this information. Importantly, the basic API for these functions
#is identical to that for the ones discussed above.

titanic = sns.load_dataset('titanic')
titanic.head()
sns.catplot(x='sex',y='survived',hue='class',kind='bar',data=titanic)

#For other applications, rather than showing the
#distribution within each category, you might want to
#show an estimate of the central tendency of the values.
#Seaborn has two main ways to show this information.
#Importantly, the basic API for these
#functions is identical to that for the ones discussed above.

sns.catplot(x='deck',kind='count',palette='ch:.25',data=titanic)

#Both barplot() and countplot() can be invoked with all
#of the options discussed above, along with others that are
#demonstrated in the detailed documentation for each function:

sns.catplot(y='deck',hue='class',kind='count',palette='pastel',
            edgecolor='.6',data=titanic)


#%%

#Point plots

#An alternative style for visualizing the same information
#is offered by the pointplot() function. This function also
#encodes the value of the estimate with height on the other
#axis, but rather than showing a full bar, it plots the point
#estimate and confidence interval. Additionally, pointplot()
#connects points from the same hue category. This makes it
#easy to see how the main relationship is changing as a
#function of the hue semantic, because your eyes are quite
#good at picking up on differences of slopes:

sns.catplot(x='sex',y='survived',hue='class',
            kind='point',data=titanic)

#When the categorical functions lack the style semantic
#of the relational functions, it can still be a good idea
#to vary the marker and/or linestyle along with the hue
#to make figures that are maximally accessible and reproduce
#well in black and white:

sns.catplot(x='class',y='survived',hue='sex',
            palette={'male':'r','female':'b'},
            markers=['^','o'],linestyles=['-','--'],
            kind='point',data=titanic)

#%%

#Plotting “wide-form” data
#
#While using “long-form” or “tidy” data is preferred,
#these functions can also by applied to “wide-form”
#data in a variety of formats, including pandas DataFrames
#or two-dimensional numpy arrays. These objects should be
#passed directly to the data parameter:

iris = sns.load_dataset('iris')
sns.catplot(data=iris,orient='h',kind='box')

#Additionally, the axes-level functions accept vectors
#of Pandas or numpy objects rather than variables in a
#DataFrame:

sns.catplot(x=iris.species, y=iris.sepal_length,kind='violin',data=iris)
#sns.violinplot(x=iris.species, y=iris.sepal_length)

#%%

#To control the size and shape of plots made by the functions
#discussed above, you must set up the figure yourself using
#matplotlib commands:
fig,ax = plt.subplots(2,1,figsize=(8,3))
sns.countplot(y=titanic.deck,color='c',ax=ax[0])
sns.countplot(y=titanic.deck,color='c',ax=ax[1])

#%%

#Showing multiple relationships with facets

#Just like relplot(), the fact that catplot() is built
#on a FacetGrid means that it is easy to add faceting
#variables to visualize higher-dimensional relationships:


sns.catplot(x='day',y='total_bill',hue='smoker',
            col='time',aspect=.6,kind='swarm',dodge=True,data=tips)

#For further customization of the plot, you can use the
#methods on the FacetGrid object that it returns:

g = sns.catplot(x='fare',y='survived',row='class',
                kind='box',orient='h',height=1.5,aspect=4,
                data=titanic.query("fare > 0"))

g.set(xscale='log')

#%%

#可视化数据集的分布

#在处理一组数据时，您通常想做的第一件事就是了解变量的分布情况。
#本教程的这一章将简要介绍seaborn中用于检查单变量和双变量分布
#的一些工具。 您可能还需要查看[categorical.html]（categorical.
#html #categical-tutorial）章节中的函数示例，这些函数可以轻松
#地比较变量在其他变量级别上的分布。

sns.set(color_codes=True)

#对于直方图我们可能很熟悉，而且matplotlib中已经存在hist函数。
#直方图首先确定数据区间，然后观察数据落入这些区间中的数量来
#绘制柱形图以此来表征数据的分布情况。 为了说明这一点，让我们
#删除密度曲线并添加一个rug plot，它在每个观察值上画一个小的
#垂直刻度。您可以使用rugplot() 函数来创建rugplot本身，
#但是也可以在 distplot()中使用:
x = np.random.normal(size=100)

#在绘制柱状图时，您的主要选择是要使用的“桶”的数量和放置它们
#的位置。 distplot() 使用一个简单的规则来很好地猜测默认情况下
#正确的数字是多少，但是尝试更多或更少的“桶”可能会揭示数据中
#的其他特性:
sns.distplot(x,bins=10,kde=False, rug=True)

#%%

#核密度估计
#可能你对核密度估计不太熟悉，但它可以是绘制分布形状的有力工具。
#和直方图一样，KDE图沿另一个轴的高度，编码一个轴上的观测密度：
#sns.distplot(x,hist=False,rug=True)
from scipy import stats
from scipy.integrate import trapz
#sns.distplot(x, hist=False, rug=True);

#绘制KDE比绘制直方图更需要计算。每个观测值首先被一个
#以该值为中心的正态(高斯)曲线所取代:

x = np.random.normal(0,1,size=30)
bandwidth = 1.06*x.std()*x.size**(-1/5.)
support = np.linspace(-4,4,200)

kernels = []
for i in x:
    kernel = stats.norm(i,bandwidth).pdf(support)
    kernels.append(kernel)
    plt.plot(support,kernel,color='r')
sns.rugplot(x,color='.2',linewidth=3)

#%%

#接下来，对这些曲线求和，计算支持网格(support grid)中每
#个点的密度值。然后对得到的曲线进行归一化，使曲线下的面积等于1
density = np.sum(kernels,axis=0)
density /= trapz(density,support)
plt.plot(support,density)

#我们可以看到，如果在seaborn中使用kdeplot() 函数，
#我们可以得到相同的曲线。这个函数也被distplot()所使用,
#但是当您只想要密度估计时，它提供了一个更直接的接口，
#可以更容易地访问其他选项

sns.kdeplot(x,shade=True)

#KDE的带宽（bw）参数控制估计与数据的拟合程度，就像直方图中的
#bin大小一样。 它对应于我们在上面绘制的内核的宽度。 默认行为
#尝试使用常用参考规则猜测一个好的值，但尝试更大或更小的值可
#能会有所帮助：

sns.kdeplot(x)
sns.kdeplot(x,bw=.2,label='bw:0.2')
sns.kdeplot(x,bw=2,label='bw:2')
plt.legend()

#%%

#正如您在上面所看到的，高斯KDE过程的本质意味着估计超出了数据
#集中最大和最小的值。有可能控制超过极值多远的曲线是由'cut'
#参数绘制的;然而，这只影响曲线的绘制方式，而不影响曲线的拟合
#方式:
sns.kdeplot(x,shade=True,cut=0)
sns.rugplot(x)

#%%

#拟合参数分布
#您还可以使用 distplot()
#
#将参数分布拟合到数据集上，并直观地评估其与观测数据的对应程度:

x= np.random.gamma(6,size=200)
sns.distplot(x,kde=False,fit=stats.gamma)


#%%

#绘制二元分布
#它对于可视化两个变量的二元分布也很有用。在seaborn中，
#最简单的方法就是使用jointplot()函数，它创建了一个多面板图形，
#显示了两个变量之间的二元(或联合)关系，
#以及每个变量在单独轴上的一元(或边际)分布

mean,cov = [0,1],[(1,5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
df = pd.DataFrame(data,columns=['x','y'])

#散点图
#
#可视化二元分布最常见的方法是散点图，其中每个观察点都以
#_x_和_y_值表示。 这类似于二维rug plot。
#您可以使用matplotlib的plt.scatter 函数绘制散点图,
#它也是 jointplot()函数显示的默认类型的图:

sns.jointplot(x='x',y='y',data=df)

#%%

#六边形“桶”(Hexbin)图
#
#类似于单变量的直方图，用于描绘二元变量关系的图称为 “hexbin”
#图,因为它显示了落入六边形“桶”内的观察计数。
#此图对于相对较大的数据集最有效。它可以通过调用matplotlib中的
#plt.hexbin函数获得并且在jointplot()作为一种样式。
#当使用白色作为背景色时效果最佳。

#多元高斯分布
#sns也允许用with语句中套用axes_style()达
#到临时设置参数的效果（仅对with块内的绘图函数起作用）。
x,y = np.random.multivariate_normal(mean,cov,1000).T
with sns.axes_style('white'):
    sns.jointplot(x=x,y=y,kind='hex',color='k')

#%%

##核密度估计
#    也可以使用上面描述的核密度估计过程来可视化二元分布。
#    在seaborn中，这种图用等高线图表示， 在jointplot()中被当作一种样式:

sns.jointplot(x='x',y='y',data=df,kind='kde',color='k')


#您还可以使用kdeplot()函数绘制二维核密度图。这允许您在一个特定的(可能已经存在的)
#matplotlib轴上绘制这种图，而 jointplot() 函数能够管理它自己的图:

fig,ax = plt.subplots(figsize=(6,6))
sns.kdeplot(df.x,df.y,ax=ax)
sns.rugplot(df.x,color='g',ax=ax)
sns.rugplot(df.y,vertical=True,ax=ax)

#如果希望更连续地显示双变量密度，可以简单地增加轮廓层的数量:
fig,ax1 = plt.subplots()
cmap = sns.cubehelix_palette(as_cmap=True,dark=0,light=1,reverse=True)
sns.kdeplot(df.x,df.y,cmap=cmap,n_levels=50,shade=True,ax=ax1)

#jointplot()函数使用JointGrid来管理图形。为了获得更大的灵活性，
#您可能想直接使用JointGrid来绘制图形。jointplot()在绘图后返回JointGrid对象，
#您可以使用它添加更多图层或调整可视化的其他方面：`

g = sns.jointplot(x='x',y='y',data=df,kind='kde',color='m')
g.plot_joint(plt.scatter,c='w',s=30,linewidth=1,marker='+')
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels('$x$','$y$')

#%%

#可视化数据集中的成对关系

#要在数据集中绘制多个成对的双变量分布，您可以使用pairplot()函数。 这将创建一
#个轴矩阵并显示DataFrame中每对列的关系，默认情况下，它还绘制对角轴上每个
#变量的单变量分布：

iris = sns.load_dataset('iris')
sns.pairplot(iris)

#与jointplot()和JointGrid之间的关系非常类似， pairplot()函数构建在
#PairGrid对象之上, 可以直接使用它来获得更大的灵活性：

g = sns.pairplot(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot,n_levels=6)


#%%

#Visualizing linear relationships

#Many datasets contain multiple quantitative variables, and
#the goal of an analysis is often to relate those variables to
#each other. We previously discussed functions that can accomplish
#this by showing the joint distribution of two variables. It can be
#very helpful, though, to use statistical models to estimate a
#simple relationship between two noisy sets of observations.
#The functions discussed in this chapter will do so through
#the common framework of linear regression.
#
#In the spirit of Tukey, the regression plots in seaborn are
#primarily intended to add a visual guide that helps to emphasize
#patterns in a dataset during exploratory data analyses. That
#is to say that seaborn is not itself a package for statistical
#analysis. To obtain quantitative measures related to the fit of
#regression models, you should use statsmodels. The goal of seaborn,
# however, is to make exploring a dataset through visualization
# quick and easy, as doing so is just as (if not more) important
# than exploring a dataset through tables of statistics.
tips = sns.load_dataset('tips')

sns.regplot(x='total_bill',y='tip',data=tips)

sns.lmplot(x='total_bill',y='tip',data=tips)

#You should note that the resulting plots are identical, except
#that the figure shapes are different. We will explain why this
#is shortly. For now, the other main difference to know about is
#that regplot() accepts the x and y variables in a variety of
#formats including simple numpy arrays, pandas Series objects,
#or as references to variables in a pandas DataFrame object
#passed to data. In contrast, lmplot() has data as a required
#parameter and the x and y variables must be specified as strings.
#This data format is called “long-form” or “tidy” data. Other
#than this input flexibility, regplot() possesses a subset of
#lmplot()’s features, so we will demonstrate them using the latter.

#It’s possible to fit a linear regression when one of the
#variables takes discrete values, however, the simple scatterplot
#produced by this kind of dataset is often not optimal:

sns.lmplot(x='size',y='tip',data=tips)

#One option is to add some random noise (“jitter”) to
#the discrete values to make the distribution of those
#values more clear. Note that jitter is applied only to
#the scatterplot data and does not influence the regression
#line fit itself:

sns.lmplot(x='size',y='tip',data=tips,x_jitter=.05)

#A second option is to collapse over the observations in each discrete bin to
#plot an estimate of central tendency along with a confidence interval:
sns.lmplot(x='size',y='tip',data=tips,x_estimator=np.mean)


#%%

#Fitting different kinds of models
#
#The simple linear regression model used above is very simple to fit,
#however, it is not appropriate for some kinds of datasets. The Anscombe’s
#quartet dataset shows a few examples where simple linear regression provides
#an identical estimate of a relationship where simple visual inspection
#clearly shows differences. For example, in the first case, the linear
#regression is a good model:

anscombe = sns.load_dataset('anscombe')

sns.lmplot(x='x',y='y',data=anscombe.query("dataset=='I'"),
           ci=None,scatter_kws={'s':80})

#The linear relationship in the second dataset is the same, but the plot
#clearly shows that this is not a good model:
sns.lmplot(x='x',y='y',data=anscombe.query("dataset=='II'"),
           ci=None,scatter_kws={'s':80})

#In the presence of these kind of higher-order relationships,
#lmplot() and regplot() can fit a polynomial regression model
#to explore simple kinds of nonlinear trends in the dataset:

sns.lmplot(x='x',y='y',data=anscombe.query("dataset=='II'"),
           ci=None,scatter_kws={'s':80},order=2)

#In the presence of outliers, it can be useful to fit a robust regression,
#which uses a different loss function to downweight relatively large
#residuals:
sns.lmplot(x='x',y='y',data=anscombe.query("dataset=='III'"),
           ci=None,scatter_kws={'s':80},robust=True)

#When the y variable is binary, simple linear regression also “works”
#but provides implausible predictions:

tips['big_tip'] = (tips.tip/tips.total_bill) > .15
sns.lmplot(x='total_bill',y='big_tip',data=tips,y_jitter=.03)

#The solution in this case is to fit a logistic regression, such that the
#regression line shows the estimated probability of y = 1
#for a given value of x:

sns.lmplot(x='total_bill',y='big_tip',data=tips,y_jitter=.03,logistic=True)

#An altogether different approach is to fit a nonparametric regression
#using a lowess smoother. This approach has the fewest assumptions,
#although it is computationally intensive and so currently confidence
#intervals are not computed at all:

sns.lmplot(x='total_bill',y='tip',data=tips,lowess=True)

#%%

sns.lmplot(x='x',y='y',data=anscombe.query("dataset=='I'"),
           ci=None,scatter_kws={'s':80})

#The residplot() function can be a useful tool for checking whether the
#simple regression model is appropriate for a dataset. It fits and removes
#a simple linear regression and then plots the residual values for each
#observation. Ideally, these values should be randomly scattered around y = 0:

plt.subplots(1)
sns.residplot(x='x',y='y',data=anscombe.query("dataset=='I'"),
              scatter_kws={'s':80})

#If there is structure in the residuals,
#it suggests that simple linear regression is not appropriate:
plt.subplots(1)
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80})

#%%

#Conditioning on other variables
#
#The plots above show many ways to explore the relationship between a pair
#of variables. Often, however, a more interesting question is “how does
#the relationship between these two variables change as a function of a
#third variable?” This is where the difference between regplot() and
#lmplot() appears. While regplot() always shows a single relationship,
#lmplot() combines regplot() with FacetGrid to provide an easy interface
#to show a linear regression on “faceted” plots that allow you to explore
#interactions with up to three additional categorical variables.
#
#The best way to separate out a relationship is to plot both levels on the
#same axes and to use color to distinguish them:

sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips)

#In addition to color, it’s possible to use different scatterplot
#markers to make plots the reproduce to black and white better.
#You also have full control over the colors used:

sns.lmplot(x='total_bill',y='tip',hue='smoker',markers=['o','x'],
           palette='Set1',data=tips)

#To add another variable, you can draw multiple “facets” which each level of
#the variable appearing in the rows or columns of the grid:

sns.lmplot(x='total_bill',y='tip',hue='smoker',markers=['o','x'],
           palette='Set1',data=tips,col='time')

sns.lmplot(x='total_bill',y='tip',hue='smoker',markers=['o','x'],
           palette='Set1',data=tips,col='time',row='sex')

#%%

#Controlling the size and shape of the plot

#Before we noted that the default plots made by regplot()
#and lmplot() look the same but on axes that have a different size
#and shape. This is because regplot() is an “axes-level”
#function draws onto a specific axes. This means that you can make
#multi-panel figures yourself and control exactly where the regression
#plot goes. If no axes object is explicitly provided, it simply uses
#the “currently active” axes, which is why the default plot has the
#same size and shape as most other matplotlib functions. To control
#the size, you need to create a figure object yourself.

fig,ax = plt.subplots(figsize=(5,6))
sns.regplot(x='total_bill',y='tip',data=tips,ax=ax)

#In contrast, the size and shape of the lmplot() figure is controlled
#through the FacetGrid interface using the size and aspect parameters,
#which apply to each facet in the plot, not to the overall figure itself:
sns.lmplot(x='total_bill',y='tip',col='day',data=tips,col_wrap=2,height=3)

sns.lmplot(x='total_bill',y='tip',col='day',data=tips,aspect=.5)

#%%

#Plotting a regression in other contexts

#A few other seaborn functions use regplot() in the context of a larger,
#more complex plot. The first is the jointplot() function that we introduced
#in the distributions tutorial. In addition to the plot styles previously
#discussed, jointplot() can use regplot() to show the linear regression fit
#on the joint axes by passing kind="reg":

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

#between variables in a dataset. Take care to note how this is different
#from lmplot(). In the figure below, the two axes don’t show the same
#relationship conditioned on two levels of a third variable; rather,
#PairGrid() is used to show multiple relationships between different
#pairings of the variables in a dataset:

sns.pairplot(data=tips,x_vars=['total_bill','size'],y_vars=['tip'],
             height=5,aspect=.8,kind='reg')

#Like lmplot(), but unlike jointplot(), conditioning on an additional
#categorical variable is built into pairplot() using the hue parameter:

sns.pairplot(data=tips,x_vars=['total_bill','size'],y_vars=['tip'],
             hue='smoker',height=5,aspect=.8,kind='reg')


#%%

#构建结构化多图网格

#在探索中等维度数据时，经常需要在数据集的不同子集上绘制同一类型图的多个实例。
#这种技术有时被称为“网格”或“格子”绘图，它与“多重小图”的概念有关。这种技
#术使查看者从复杂数据中快速提取大量信息。 Matplotlib为绘制这种多轴图提供了很
#好的支持; seaborn构建于此之上，可直接将绘图结构和数据集结构关系起来。
#
#要使用网格图功能，数据必须在Pandas数据框中，并且必须采用 Hadley Whickam所谓的
#“整洁”数据的形式。简言之，用来画图的数据框应该构造成每列一个变量，每一行
#一个观察的形式。至于高级用法，可以直接使用本教程中讨论的对象，以提供最大的灵
#活性。一些seaborn函数（例如lmplot()，catplot()和pairplot()）也在后台使用它们。
#与其他在没有操纵图形的情况下绘制到特定的（可能已经存在的）
#matplotlib Axes上的“Axes-level” seaborn函数不同，
#这些更高级别的函数在调用时会创建一个图形，并且通常对图形的设置方式更加严格。
#在某些情况下，这些函数或它们所依赖的类构造函数的参数将提供不同的接口属性，
#如lmplot()中的图形大小，你可以设置每个子图的高和宽高比。但是，使用这些对象的
#函数在绘图后都会返回它，并且这些对象大多都有方便简单的方法来改变图的绘制方式。

#基于一定条件的多重小图
#
#当你想在数据集的不同子集中分别可视化变量分布或多个变量之间的关系时，
#FacetGrid类非常有用。 FacetGrid最多有三个维：row，col和hue。
#前两个与轴(axes)阵列有明显的对应关系;将色调变量hue视为沿深度轴的第三个维度，
#不同的级别用不同的颜色绘制。
#
#首先，使用数据框初始化FacetGrid对象并指定将形成网格的行，
#列或色调维度的变量名称。这些变量应是离散的，然后对应于变量的不同取值的数据
#将用于沿该轴的不同小平面的绘制。例如，假设我们想要在tips数据集中检查
#午餐和晚餐小费分布的差异。
#此外，relplot()，catplot()和lmplot()都在内部使用此对象，
#并且它们在完成时返回该对象，以便进一步调整。

g = sns.FacetGrid(tips,col='time')
#如上初始化网格会设置matplotlib图形和轴，但不会在其上绘制任何内容。
#在网格上可视化数据的主要方法是FacetGrid.map()。为此方法提供绘图函数以及要绘制
#的数据框变量名作为参数。我们使用直方图绘制每个子集中小费金额的分布。

g.map(plt.hist,'tip')
#map函数绘制图形并注释轴，生成图。要绘制关系图，只需传递多个变量名称。
#还可以提供关键字参数，这些参数将传递给绘图函数：


g = sns.FacetGrid(tips,col='sex',hue='smoker')
g.map(plt.scatter,'total_bill','tip',alpha=.7)
g.add_legend()

#有几个传递给类构造函数的选项可用于控制网格外观。
g = sns.FacetGrid(tips,row='smoker',col='time')
g.map(sns.regplot,'size','total_bill',color='.3',fit_reg=False,x_jitter=.01)
g.add_legend()
#注意，matplotlib API并未正式支持margin_titles，此选项在一些情况下可能无法
#正常工作。特别是，它目前不能与图之外的图例同时使用。


#通过提供每个面的高度以及纵横比来设置图形的大小：
g = sns.FacetGrid(tips,col='day',height=4,aspect=.5)
g.map(sns.barplot,'sex','total_bill')

#小图的默认排序由DataFrame中的信息确定的。如果用于定义小图的变量是类别变量，
#则使用类别的顺序。否则，小图将按照各类的出现顺序排列。但是，
#可以使用适当的* _order参数指定任意构面维度的顺序：
ordered_days = tips.day.value_counts().index
g = sns.FacetGrid(tips,row='day',row_order=ordered_days,
                  height=1.7,aspect=4)
g.map(sns.distplot,'total_bill',hist=False,rug=True)


#可以用seaborn调色板（即可以传递给color_palette()的东西。）
#还可以用字典将hue变量中的值映射到matplotlib颜色

pal = dict(Lunch='seagreen',Dinner='gray')
g = sns.FacetGrid(tips,hue='time',palette=pal,height=5)
g.map(plt.scatter,'total_bill','tip',
      s=50,alpha=.7,linewidth=.5,edgecolor='white')

g.add_legend()
#
#还可以让图的其他方面（如点的形状）在色调变量的各个级别之间变化，
#这在以黑白方式打印时使图易于理解。为此，只需将一个字典传递给hue_kws，
#其中键是绘图函数关键字参数的名称，值是关键字值列表，每个级别为一个色调变量

g = sns.FacetGrid(tips,hue='sex',palette='Set1',height=5,
                  hue_kws={'marker':['^','*']})
g.map(plt.scatter,'total_bill','tip',s=100,linewidth=.5,edgecolor='white')
g.add_legend()
#

#%%

#如果一个变量的水平数过多，除了可以沿着列绘制之外，也可以“包装”它们
#以便它们跨越多行。执行此wrap操作时，不能使用row变量。

attend = sns.load_dataset('attention').query("subject<=12")
attend.head()
g = sns.FacetGrid(attend,col='subject',col_wrap=4,
                  height=2,ylim=(0,10))
g.map(sns.pointplot,'solutions','score',color='.3',ci=None)

#使用FacetGrid.map() （可以多次调用）绘图后，你可以调整绘图的外观。
#FacetGrid对象有许多方法可以在更高的抽象层次上操作图形。
#最一般的是FacetGrid.set()，还有其他更专业的方法，
#如FacetGrid.set_axis_labels()，它们都遵循内部构面没有轴标
#签的约定。例如：

with sns.axes_style('white'):
    g = sns.FacetGrid(tips,row='sex',col='smoker',
                      margin_titles=True,height=2.5)

g.map(plt.scatter,'total_bill','tip',color='#334488',edgecolor='white',
      lw=.5)

g.set_axis_labels('Total bill(US Dollars)','Tip')
g.set(xticks=[10,30,50],yticks=[2,6,10])
g.fig.subplots_adjust(wspace=.02,hspace=.02)

#对于需要更多自定义的情形，你可以直接使用底层matplotlib图形Figure和
#轴Axes对象，它们分别作为成员属性存储在Figure和轴Axes（一个二维数组）中。
#在制作没有行或列刻面的图形时，你还可以使用ax属性直接访问单个轴。

g = sns.FacetGrid(tips,col='smoker',margin_titles=True,height=4)
g.map(plt.scatter,'total_bill','tip',color='#338844',
      edgecolor='white',s=50,lw=1)
for ax in g.axes.flat:
    ax.plot((0,50),(0,0.2*50),c='.2',ls='--')
g.set(xlim=(0,60),ylim=(0,14))

#%%

#使用自定义函数

#使用FacetGrid时，你除了可以使用现有的matplotlib和seaborn函数，
#还可以使用自定义函数。但是，这些函数必须遵循一些规则：
#
#    它必须绘制到“当前活动的”matplotlib轴Axes上。 matplotlib.pyplot
#    命名空间中的函数就是如此。如果要直接使用当前轴的方法，可以调用
#    plt.gca来获取对当前Axes的引用。
#    它必须接受它在位置参数中绘制的数据。在内部，FacetGrid将为传递给
#    FacetGrid.map()的每个命名位置参数传递一Series数据。
#    它必须能接受color和label关键字参数，理想情况下，它会用它们做一些有
#    用的事情。在大多数情况下，最简单的方法是捕获** kwargs的通用字典并
#    将其传递给底层绘图函数。
#
#让我们看一下自定义绘图函数的最小示例。这个函数在每个构面采用一个数据向量：
#
from scipy import stats
def quantile_plot(x,**kwargs):
    qntls,xr = stats.probplot(x,fit=False)
    plt.scatter(xr,qntls,**kwargs)

g = sns.FacetGrid(tips,col='sex',height=4)
g.map(quantile_plot,'total_bill')

def qqplot(x,y,**kwargs):
    _,xr = stats.probplot(x,fit=False)
    _,yr = stats.probplot(y,fit=False)
    plt.scatter(xr,yr,**kwargs)

g = sns.FacetGrid(tips,col='smoker',height=4)
g.map(qqplot,'total_bill','tip')

#因为plt.scatter接受颜色和标签关键字参数并做相应的处理，
#所以我们可以毫无困难地添加一个色调构面：
g = sns.FacetGrid(tips,col='sex',hue='smoker',height=4)
g.map(qqplot,'total_bill','tip')

#这种方法还允许我们使用额外的美学元素来区分色调变量的级别，
#以及不依赖于分面变量的关键字参数

g = sns.FacetGrid(tips,hue='time',col='sex',height=4,
                  hue_kws={'marker':['s','D']})
g.map(qqplot,'total_bill','tip')
#
#有时候，你需要使用color和label关键字参数映射不能按预期方式工作的函数。
#在这种情况下，你需要显式捕获它们并在自定义函数的逻辑中处理它们。
#例如，这种方法可用于映射plt.hexbin，使它与FacetGrid API匹配：
def hexbin(x,y,color,**kwargs):
    cmap = sns.light_palette(color,as_cmap=True)
    plt.hexbin(x,y,gridsize=15,cmap=cmap,**kwargs)

with sns.axes_style('dark'):
    g = sns.FacetGrid(tips,hue='time',col='time',height=4)

g.map(hexbin,'total_bill','tip',extent=[0,50,0,10])


#%%

#绘制成对数据关系
#
#PairGrid允许你使用相同的绘图类型快速绘制小子图的网格。在PairGrid中，
#每个行和列都分配给一个不同的变量，结果图显示数据集中的每个对变量的关系。
#这种图有时被称为“散点图矩阵”，这是显示成对关系的最常见方式，但是
#PairGrid不仅限于散点图。
#
#了解FacetGrid和PairGrid之间的差异非常重要。前者每个构面显示以不同级别的
#变量为条件的相同关系。后者显示不同的关系（尽管上三角和下三角组成镜像图）。
#使用PairGrid可为你提供数据集中有趣关系的快速，高级的摘要。
#
#该类的基本用法与FacetGrid非常相似。首先初始化网格，然后将绘图函数传递
#给map方法，并在每个子图上调用它。还有一个伴侣函数， pairplot() ，可以
#更快的绘图。

iris = sns.load_dataset('iris')
g = sns.PairGrid(iris)
g.map(plt.scatter)


#可以在对角线上绘制不同的函数，以显示每列中变量的单变量分布。但请注意，
#轴刻度与该绘图的计数或密度轴不对应。
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

#此图的一种常见用法是通过单独的分类变量对观察结果进行着色。例如，iris数据集三种
#不同种类的鸢尾花都有四种测量值，因此你可以看到不同花在这些取值上的差异。


g = sns.PairGrid(iris,hue='species')
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

#默认情况下，使用数据集中的每个数值列，但如果需要，你可以专注于特定列。

g = sns.PairGrid(iris,vars=['sepal_length','sepal_width'],hue='species')
g.map(plt.scatter)

#也可以在上三角和下三角中使用不同的函数来强调关系的不同方面。

g = sns.PairGrid(iris)
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot,lw=3,legend=False)
g.map_lower(sns.kdeplot)
#
#对角线上具有单位关系的方形网格实际上只是一种特殊情况，你也可以在行和列
#中使用不同的变量进行绘图

g = sns.PairGrid(tips,y_vars=['tip'],x_vars=['total_bill','size'],
                 height=4)

g.map(sns.regplot,color='.3')
g.set(ylim=(-1,11),yticks=[0,5,10])


#当然，美学属性是可配置的。例如，你可以使用不同的调色板（例如，显示色调变量
#的顺序）并将关键字参数传递到绘图函数中。

g = sns.PairGrid(tips,hue='size',palette='GnBu_d')
g.map(plt.scatter,s=50,edgecolor='white')
g.add_legend()
#
#PairGrid很灵活，但要快速查看数据集，使用pairplot()更容易。此函数默认使用散点图
#和直方图，但会添加一些其他类型（目前，你还可以绘制非对角线上的回归图和
#对角线上的KDE）。
sns.pairplot(iris,hue='species',height=2.5)

#还可以使用关键字参数控制绘图的美观，函数会返回PairGrid实例以便进一步调整。
g = sns.pairplot(iris,hue='species',palette='Set2',diag_kind='kde',height=2.5)

#%%

#Controlling figure aesthetics
#Drawing attractive figures is important. When making figures for yourself,
#as you explore a dataset, it’s nice to have plots that are pleasant to
#look at. Visualizations are also central to communicating quantitative
#insights to an audience, and in that setting it’s even more necessary
#to have figures that catch the attention and draw a viewer in.
#
#Matplotlib is highly customizable, but it can be hard to know what
#settings to tweak to achieve an attractive plot. Seaborn comes with
#a number of customized themes and a high-level interface for controlling
#the look of matplotlib figures.

#Let’s define a simple function to plot some offset sine waves, which will
#help us see the different stylistic parameters we can tweak.

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)
sinplot()

#To switch to seaborn defaults, simply call the set() function.
sns.set()
sinplot()

#(Note that in versions of seaborn prior to 0.8, set() was called on import.
# On later versions, it must be explicitly invoked).
#
#Seaborn splits matplotlib parameters into two independent groups.
#The first group sets the aesthetic style of the plot, and the second
#scales various elements of the figure so that it can be easily
#incorporated into different contexts.
#
#The interface for manipulating these parameters are two pairs of
#functions. To control the style, use the axes_style() and set_style()
#functions. To scale the plot, use the plotting_context() and
#set_context() functions. In both cases, the first function returns a
#dictionary of parameters and the second sets the matplotlib defaults.

#%%

#Seaborn figure styles
#There are five preset seaborn themes: darkgrid, whitegrid, dark, white,
#and ticks. They are each suited to different applications and personal
#preferences. The default theme is darkgrid. As mentioned above, the grid
#helps the plot serve as a lookup table for quantitative information, and
#the white-on grey helps to keep the grid from competing with lines that
#represent data. The whitegrid theme is similar, but it is better suited
#to plots with heavy data elements:

sns.set_style('whitegrid')
data = np.random.normal(size=(20,6))+np.arange(6)/2
sns.boxplot(data=data)

#%%

#For many plots, (especially for settings like talks, where you primarily
#want to use figures to provide impressions of patterns in the data),
#the grid is less necessary.
sns.set_style('dark')
sinplot()

#%%

sns.set_style('white')
sinplot()

#%%

#Sometimes you might want to give a little extra structure to the plots,
#which is where ticks come in handy:
sns.set_style('ticks')
sinplot()

#%%

#Removing axes spines
#
#Both the white and ticks styles can benefit from removing the top
#and right axes spines, which are not needed. The seaborn function
#despine() can be called to remove them:

sinplot()
sns.despine()

f,ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=10,trim=True)

#You can also control which spines are removed with additional
#arguments to despine():

f,ax = plt.subplots()
sns.set_style('whitegrid')
sns.boxplot(data=data,palette='deep')
sns.despine(left=True)

#%%

#Temporarily setting figure style

#Although it’s easy to switch back and forth, you can also use the
#axes_style() function in a with statement to temporarily set plot
#parameters. This also allows you to make figures with differently-styled
#axes:

f = plt.figure()
with sns.axes_style('darkgrid'):
    ax = f.add_subplot(1,2,1)
    sinplot()
ax = f.add_subplot(1,2,2)
sinplot(-1)

#%%

#Overriding elements of the seaborn styles
#If you want to customize the seaborn styles, you can pass a dictionary
#of parameters to the rc argument of axes_style() and set_style(). Note
#that you can only override the parameters that are part of the style
#definition through this method. (However, the higher-level set() function
#takes a dictionary of any matplotlib parameters).

#If you want to see what parameters are included, you can just call the
#function with no arguments, which will return the current settings:

sns.axes_style()

#%%

sns.set_style('darkgrid',{'axes,facecolor':'.9'})
sinplot()

#%%

#Scaling plot elements

#A separate set of parameters control the scale of plot elements,
#which should let you use the same code to make plots that are
#suited for use in settings where larger or smaller plots are appropriate.

#First let’s reset the default parameters by calling set():

sns.set()

#The four preset contexts, in order of relative size, are paper,
#notebook, talk, and poster. The notebook style is the default,
#and was used in the plots above.

sns.set_context('paper')
sinplot()

#%%

sns.set_context('talk')
sinplot()

#%%

sns.set_context('poster')
sinplot()

#%%

#Most of what you now know about the style functions should transfer to
#the context functions.
#
#You can call set_context() with one of these names to set the parameters,
#and you can override the parameters by providing a dictionary of parameter
#values.

#You can also independently scale the size of the font elements when
#changing the context. (This option is also available through the
#top-level set() function).

sns.set_context('notebook',font_scale=1.5,rc={'line.linewidth':2.5})
sinplot()

#Similarly, you can temporarily control the scale of figures nested under
#a with statement.
#
#Both the style and the context can be quickly configured with the set()
#function. This function also sets the default color palette, but that
#will be covered in more detail in the next section of the tutorial.

#%%

#选择调色板
#https://www.cntofu.com/book/172/docs/9.md

#颜色在图像风格中比起其他元素显得更为重要。当合理有效地使用颜色时，
#数据模式会被凸显出来；反之，则会被掩盖。这里有很多数据可视化中关于颜色使用的
#优秀资源，我推荐阅读这些 Rob Simmon 的博客文章以及这篇更加学术性的论文。
#此外，matplotlib 文档也提供了一篇很好的教程来说明一些内置Colormap的感知属性。

#seaborn让您在选择与您处理的数据类型和可视化过程中搭配的配色方案变得简单。

#%%

#创建调色板

#使用离散调色板过程中最重要函数是color_palette()。这个函数为许多(但不是全部)
#可以在seaborn中生成颜色的方式提供了一个接口，并且在任何具有palette参数的函
#数的内部都可以使用(以及某些需要多种颜色时具有color参数的情况)。

#color_palette() 会接受所有的seaborn调色板或者matplotlib Colormap
#(除了 jet, 您永远都不应该使用它). 它还可以获取以任何有效matplotlib
#格式(RGB元组、十六进制颜色代码或HTML颜色名字)指定的颜色列表。
#返回值始终是RGB元组的列表。

#最后，在没有参数的情况下调用color_palette()函数将会返回当前默认的颜色循环。

#函数set_palette()接受相同的参数，并将为所有图像设置默认的颜色循环。您也可以
#在with语句中调用color_palette()来临时改变调色板。(参见)

#在不了解数据特征的情况下，通常也不可能知道哪种调色板或Colormap最适合一组数据。
#接下来，我们将通过三种常见的调色板 定性调色板, 顺序调色板, 和 发散调色板 来
#拆分介绍color_palette()函数的使用方法以及其他seaborn函数。

#%%

#定性调色板
#当您想要区分不具有内在顺序的离散数据块时，定性(分类)调色板是最佳方案。

#导入seaborn的同时，会引入默认的颜色循环，由6种颜色构成。并将调用标准
#matplotlib颜色循环，看起来也更加赏心悦目。

current_palette = sns.color_palette()
sns.palplot(current_palette)

#默认主题有六种变体，分别为deep, muted, pastel, bright, dark, and colorblind。

#%%

#使用循环颜色系统

#当您要区分任意数量的类别而不强调任何类别时，最简单的方法是在循环颜色空间
#中绘制间距相等的颜色(在此颜色空间中，色调会发生变化，同时保持亮度和饱和度不变)。
#这是大多数seaborn函数在处理当需要区分的数据集超过颜色循环中的6种颜色时时所使
#用的默认方法。

#最为常用的方法是使用hls颜色空间——一种简单的RGB值变体。

sns.palplot(sns.color_palette('hls',8))

#hls_palette()函数允许您控制颜色的亮度(lightness)和饱和度(saturation)。

sns.palplot(sns.hls_palette(8,l=.3,s=.8))


#然而，由于人类视觉系统的工作方式，RGB强度很高的颜色也不一定看起来同样强烈。
#我们认为黄色和绿色是相对较亮的，蓝色是相对较暗的，当目标是与hls系统保持一
#致性时可能会带来一些问题。

#为了解决这一问题，seaborn提供了一个husl系统(后来更名为HSLuv)的接口，
#这也使选择间隔均匀的色调变得容易，同时使亮度和饱和度都更加均匀。

sns.palplot(sns.color_palette('husl',8))

#类似地，husl_palette()函数也为这个系统提供了一个更灵活的接口。


#%%

#使用Color Brewer调色板

#Color Brewer为定性调色板提供了另一种美观的配色方案(同样包含顺序调色板包括
#和发散调色板，详情见下文)。这些也作为matplotlib Colormap存在，但并没有得到
#很好的处理。在seaborn中，当您需要定性(qualitative)的Color Brewer方案时，
#你总是会得到离散的颜色，但这意味着在某些情况下颜色会循环重复。

#Color Brewer的一个很好的特点是它对色盲比较友好。色盲有很多种，最为常见的是
#红绿色盲。通常，对于需要根据颜色进行元素区分时，应该尽量避免使用这两种颜色。

sns.palplot(sns.color_palette('Paired'))

sns.palplot(sns.color_palette("Set2"))

#为了帮助您从Color Brewer库中选取配色方案，seaborn提供了
#choose_colorbrewer_palette()函数。这个函数能够启动交互式组件来帮助
#您浏览各种选项，修改不同的参数。但是只能在Jupyter notebook中使用。
#sns.palplot(sns.color_palette(sns.choose_colorbrewer_palette('qualitative')))

#当然，您可能只希望手动指定一组您喜欢的颜色。color_palette()
#函数会接受一个颜色列表，操作起来也很简单。

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(sns.color_palette(flatui))


#%%

#使用来自xkcd color survey的颜色名字

#不久前，xkcd开展了一项众包工作来为随机RGB颜色命名。产生了954个颜色名字，
#您现在可以在seaborn中使用xkcd_rgb字典来引用它们：
plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw=3)
plt.plot([0,1],[0,2],sns.xkcd_rgb['medium green'],lw=3)
plt.plot([0,1],[0,3],sns.xkcd_rgb['denim blue'],lw=3)

#除了从xkcd_rgb字典中提取单一颜色外，
#您也可以向xkcd_palette()函数传递一个颜色名字列表。

colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
sns.palplot(sns.xkcd_palette(colors))

#%%

#顺序调色板
#第二类主要的调色板被称为“顺序调色板”(sequential)，当数据集的范围从相对
#低值(不感兴趣)到相对高值(很感兴趣)时，最好使用顺序调色板，尽管在某些情况
#下您可能需要顺序调色板中的离散颜色。在kdeplot()和heatmap()函数中使用它们
#来作为Colormap则更为常见(以及类似的matplotlib函数)。

#在这种情况下使用jet（或其他彩虹调色板）等Colormap是很常见的，因为色调范围
#给人的印象是提供有关数据的额外信息。然而，具有较大色调变化的Colormap往往
#会引入数据中不存在的不连续性，并且我们的视觉系统无法自然地将彩虹光谱映射
#到诸如“高”或“低”的定量区分。导致来这些可视化的结果更加令人困惑，因为
#它们掩盖了数据中的模式，而不是揭示它们。jet 调色板使用了最亮的颜色
#(黄色和青色)的中间数据值，导致效果是强调无趣的(和任意的)值，而不是强调极
#端的值。

#对于连续性的数据，最好使用色调变化幅度较小，而亮度和饱和度变化幅度较大的
#配色方案。这种方法会很自然地吸引人们注意数据中相对重要的部分。
#

#%%

#Color Brewer库有大量这样的配色方案，它们以调色板中主要的一种或多种颜色命名。
sns.palplot(sns.color_palette('BuGn_r'))

#seaborn同样添加了一个小窍门来帮助您创建“深色”调色板，它没有一个很宽的动态
#范围。在当您需要按顺序映射直线或点时这可能会很有用，因为颜色较亮的线条会比
#较难以区分。

sns.palplot(sns.color_palette('GnBu_r'))

sns.palplot(sns.color_palette('GnBu_d'))

#您可能想要使用choose_colorbrewer_palette()函数来尝试多种选项，当您希望传递
#给seaborn或者matplotlib的返回值为Colormap对象时，您可以将as_cmap对象设置为
#True

#%%

#顺序 “cubehelix” 调色板

#cubehelix调色板系统使顺序调色板的亮度产生线性变化，色调也会产生一些变化。这意
#味着您的Colormap在转换为黑白模式时(用于打印)的信息将得到保留，且对色盲友好

#Matplotlib内置了默认的cubehelix版本：
sns.palplot(sns.color_palette('cubehelix',8))

#Seborn为cubehelix系统提供了一个接口，以便您可以制作各种调色板，这些调色板都具
#有良好的线性亮度渐变。

#由seborn cubehelix_palette() 函数返回的默认调色板与matplotlib的默认值稍有不同
#，因为它不会围绕色轮旋转很远，也不会覆盖很宽的强度范围。它还反转顺序，以便让
#更重要的值的颜色更暗

sns.palplot(sns.cubehelix_palette(8))

#cubehelix_palette() 函数的其他参数控制调色板的外观。您将更改的两个主要参数为
#start (介于0到3之间的值)和 rot —— 旋转次数(任意值，但可能在-1和1之间)。

sns.palplot(sns.cubehelix_palette(8,start=.6,rot=-.75))

#您还可以控制端点的亮度，甚至反转渐变：
sns.palplot(sns.cubehelix_palette(8,start=2,rot=0,dark=0,
                                  light=.85,reverse=True))

#如同其他seaborn函数，您将默认得到一个颜色列表。但您也可以通过
#修改 as_cmap=True 将调色板作为Colormap对象的返回值来传递给seaborn
#或matplotlib函数。

fig,ax = plt.subplots()
x,y = np.random.multivariate_normal([0,0],[[1,-.5],[-.5,1]],size=300).T

cmap = sns.cubehelix_palette(light=1,as_cmap=True)

sns.kdeplot(x,y,cmap=cmap,shade=True)

#为了帮助您选择更好的调色板或者Colormap，您可以在Jupyter notebook中使用
# choose_cubehelix_palette() 函数来启动互动界面帮助您测试、修改不同的参数。
# 如果您希望函数返回一个Colormap(而不是列表)，则在例如像 hexbin 这样的函数
# 中设置 as_Cmap=True。

sns.palplot(sns.color_palette(sns.choose_colorbrewer_palette('sequential')))

#%%

#自定义调色板

'''#为了更简单地生成自定义顺序调色板，您可以使用 light_palette() 
#或 dark_palette() 函数。它们都是以某个颜色为种子，从明向暗或
#从暗向明渐变，产生顺序调色板。与这些函数相搭配的还有 
#choose_light_palette() 和 choose_dark_palette() 来提供交互式
#组件便于创建调色板。
'''
sns.palplot(sns.light_palette('blue'))

sns.palplot(sns.dark_palette('purple'))

#这些调色板同样可以被反转。

sns.palplot(sns.light_palette('blue',reverse=True))

#这些调色板同样可以被用来创建Colormap对象而不是颜色列表。
pal = sns.light_palette('palegreen',as_cmap=True)
fig.ax =plt.subplots()
sns.kdeplot(x,y,cmap=pal)

'''默认情况下，输入可以是任何有效的matplotlib颜色。替代解释由 input 参数控制
。现在，您可以在 hls 或 husl 空间中提供元组以及默认的 rgb，您也可以使用任何
有效的 xkcd 颜色来生成调色板。'''

sns.palplot(sns.light_palette((210,90,60),input='husl'))

'''注意，交互式调色板小部件的默认输入空间是 husl，
它不同于函数本身的默认设置，但是在这种情况下更有用。'''

#%%

#发散调色板
'''第三类调色板称为“发散调色板”(diverging)。当数据集的低值和高值都很重要，
且数据集中有明确定义的中点时，这会是您的最佳选择。例如，绘制温度相对于基准
时间点的变化图时，最好使用发散Colormap来同时显示温度相对于基准值的上升和下降
选择良好分散调色板的规则类似于良好的顺序调色板。不过在这种情况时需要注意两端
颜色向中间颜色渐变时中间点的颜色不应该喧宾夺主，两端的颜色也应该具有相似的亮
度和饱和度。
这里还需要强调的是，应该避免使用红色和绿色，因为需要考虑到红绿色盲患者的观感。
不出所料，Color Brewer库也同样提供了一些精心挑选的发散调色板。'''

sns.palplot(sns.color_palette('BrBG',7))

sns.palplot(sns.color_palette("RdBu_r", 7))

'''matplotlib库中内置的 coolwarm 调色板也是一个很好的选择。请注意，
这个Colormap的中间值和极值之间的对比度较小。'''

sns.palplot(sns.color_palette('coolwarm',7))

#%%

#自定义发散调色板
'''您可以使用seaborn的diverging_palette()函数来创建自定义colormap来描述发散
数据(搭配有交互式组件choose_diverging_palette())。此函数使用 husl 颜色系统
来创建发散调色板，您需要在函数中设置两个色调参数(用度表示)，也可以选择设置两
端颜色的亮度和饱和度。 使用 husl 意味着两端到中间点的色调变化将是平衡的。'''

sns.palplot(sns.diverging_palette(220,20,n=7))

sns.palplot(sns.diverging_palette(145,280,s=85,l=25,n=7))

#sep 参数控制两端到中间点色调变化的间隔。
sns.palplot(sns.diverging_palette(10,220,sep=50))
#也可以将中间点的颜色设置成暗色而非亮色。
sns.palplot(sns.diverging_palette(255,133,l=60,n=7,center='dark'))

#%%

#设置默认调色板
'''与color_palette()函数相伴随的有set_palette()。 两者之间的关系与美学教程中介
绍的set_palette()函数和color_palette()函数接受相同参数的关系相类似。但它会更改
默认的matplotlib参数，以便调色板应用于所有图像。'''

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x + i * .5)*(7 - i)*flip)

#sns.set_palette('husl')
#sinplot()

#您可以在 with 语句中通过 color_palette() 函数来临时改变调色板。

with sns.color_palette('PuBuGn_d'):
    sinplot()


#%%

#sns.relplot()
'''seaborn.relplot(x=None, y=None, hue=None, size=None, style=None, 
data=None, row=None, col=None, col_wrap=None, row_order=None, 
col_order=None, palette=None, hue_order=None, hue_norm=None, 
sizes=None, size_order=None, size_norm=None, markers=None, 
dashes=None, style_order=None, legend='brief', kind='scatter', 
height=5, aspect=1, facet_kws=None, **kwargs)'''


'''Figure-level interface for drawing relational plots onto a FacetGrid.

This function provides access to several different axes-level functions 
that show the relationship between two variables with semantic mappings 
of subsets. The kind parameter selects the underlying axes-level function 
to use:

    scatterplot() (with kind="scatter"; the default)
    lineplot() (with kind="line")

Extra keyword arguments are passed to the underlying function, so you should 
refer to the documentation for each to see kind-specific options.

The relationship between x and y can be shown for different subsets of the 
data using the hue, size, and style parameters. These parameters control 
what visual semantics are used to identify the different subsets. It is 
possible to show up to three dimensions independently by using all three 
semantic types, but this style of plot can be hard to interpret and is 
often ineffective. Using redundant semantics (i.e. both hue and style 
for the same variable) can be helpful for making graphics more accessible.

See the tutorial for more information.

After plotting, the FacetGrid with the plot is returned and can be used 
directly to tweak supporting plot details or add other layers.

Note that, unlike when using the underlying plotting functions directly, 
data must be passed in a long-form DataFrame with variables specified by 
passing strings to x, y, and other parameters.'''


'''参数：x, y：names of variables in data

    Input data variables; must be numeric.

hue：name in data, optional

    Grouping variable that will produce elements with different colors. 
    Can be either categorical or numeric, although color mapping will 
    behave differently in latter case.

size：name in data, optional

    Grouping variable that will produce elements with different sizes. 
    Can be either categorical or numeric, although size mapping will 
    behave differently in latter case.

style：name in data, optional

    Grouping variable that will produce elements with different styles. 
    Can have a numeric dtype but will always be treated as categorical.

data：DataFrame

    Tidy (“long-form”) dataframe where each column is a variable and 
    each row is an observation.

row, col：names of variables in data, optional

    Categorical variables that will determine the faceting of the grid.

col_wrap：int, optional

    “Wrap” the column variable at this width, so that the column facets 
    span multiple rows. Incompatible with a row facet.

row_order, col_order：lists of strings, optional

    Order to organize the rows and/or columns of the grid in, otherwise 
    the orders are inferred from the data objects.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should 
    be something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

hue_order：list, optional

    Specified order for the appearance of the hue variable levels, otherwise 
    they are determined from the data. Not relevant when the hue variable is 
    numeric.

hue_norm：tuple or Normalize object, optional

    Normalization in data units for colormap applied to the hue variable 
    when it is numeric. Not relevant if it is categorical.

sizes：list, dict, or tuple, optional

    An object that determines how sizes are chosen when size is used. It 
    can always be a list of size values or a dict mapping levels of the 
    size variable to sizes. When size is numeric, it can also be a tuple 
    specifying the minimum and maximum size to use such that other values 
    are normalized within this range.

size_order：list, optional

    Specified order for appearance of the size variable levels, otherwise 
    they are determined from the data. Not relevant when the size variable 
    is numeric.

size_norm：tuple or Normalize object, optional

    Normalization in data units for scaling plot objects when the size 
    variable is numeric.

legend：“brief”, “full”, or False, optional

    How to draw the legend. If “brief”, numeric hue and size variables 
    will be represented with a sample of evenly spaced values. If “full”,
    every group will get an entry in the legend. If False, no legend data is 
    added and no legend is drawn.

kind：string, optional

    Kind of plot to draw, corresponding to a seaborn relational plot. 
    Options are {scatter and line}.

height：scalar, optional

    Height (in inches) of each facet. See also: aspect.

aspect：scalar, optional

    Aspect ratio of each facet, so that aspect * height gives the width of 
    each facet in inches.

facet_kws：dict, optional

    Dictionary of other keyword arguments to pass to FacetGrid.

kwargs：key, value pairings

    Other keyword arguments are passed through to the underlying plotting 
    function.

返回值：g：FacetGrid

    Returns the FacetGrid object with the plot on it for further tweaking.
'''

#%%

#Examples

#Draw a single facet to use the FacetGrid legend placement:
sns.set(style='ticks')
#tips = sns.load_dataset('tips')
g = sns.relplot(x='total_bill',y='tip',hue='day',data=tips)

#Facet on the columns with another variable:
g = sns.relplot(x='total_bill',y='tip',hue='day',col='time',data=tips)

#Facet on the columns and rows:
g = sns.relplot(x='total_bill',y='tip',hue='day',
                col='time',row='sex',data=tips)

#“Wrap” many column facets into multiple rows:
g = sns.relplot(x='total_bill',y='tip',hue='time',
                col='day',col_wrap=2,data=tips)

#Use multiple semantic variables on each facet with specified attributes:
g = sns.relplot(x='total_bill',y='tip',hue='time',size='size',
                palette=['b','r'],sizes=(10,100),col='time',data=tips)

#%%

#Use a different kind of plot:
fmri = sns.load_dataset('fmri')
g = sns.relplot(x='timepoint',y='signal',hue='event',style='event',
                col='region',kind='line',data=fmri)

#Change the size of each facet:
g = sns.relplot(x='timepoint',y='signal',hue='event',col='region',
                height=5,aspect=.7,kind='line',data=fmri)

#%%

#seaborn.scatterplot
'''seaborn.scatterplot(x=None, y=None, hue=None, style=None, size=None, 
data=None, palette=None, hue_order=None, hue_norm=None, sizes=None, 
size_order=None, size_norm=None, markers=True, style_order=None, 
x_bins=None, y_bins=None, units=None, estimator=None, ci=95, 
n_boot=1000, alpha='auto', x_jitter=None, y_jitter=None, 
legend='brief', ax=None, **kwargs)'''


'''Draw a scatter plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data
using the hue, size, and style parameters. These parameters control what visual
semantics are used to identify the different subsets. It is possible to show 
up to three dimensions independently by using all three semantic types, but 
this style of plot can be hard to interpret and is often ineffective. Using 
redundant semantics (i.e. both hue and style for the same variable) can be 
helpful for making graphics more accessible.'''

#%%

'''See the tutorial for more information.

参数：x, y：names of variables in data or vector data, optional

    Input data variables; must be numeric. Can pass data directly or reference 
    columns in data.

hue：name of variables in data or vector data, optional

    Grouping variable that will produce points with different colors. Can be 
    either categorical or numeric, although color mapping will behave 
    differently in latter case.

size：name of variables in data or vector data, optional

    Grouping variable that will produce points with different sizes. Can be 
    either categorical or numeric, although size mapping will behave 
    differently in latter case.

style：name of variables in data or vector data, optional

    Grouping variable that will produce points with different markers. 
    Can have a numeric dtype but will always be treated as categorical.

data：DataFrame

    Tidy (“long-form”) dataframe where each column is a variable and each 
    row is an observation.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

hue_order：list, optional

    Specified order for the appearance of the hue variable levels, otherwise 
    they are determined from the data. Not relevant when the hue variable is 
    numeric.

hue_norm：tuple or Normalize object, optional

    Normalization in data units for colormap applied to the hue variable 
    when it is numeric. Not relevant if it is categorical.

sizes：list, dict, or tuple, optional

    An object that determines how sizes are chosen when size is used. It can 
    always be a list of size values or a dict mapping levels of the size 
    variable to sizes. When size is numeric, it can also be a tuple specifying 
    the minimum and maximum size to use such that other values are normalized 
    within this range.

size_order：list, optional

    Specified order for appearance of the size variable levels, otherwise they 
    are determined from the data. Not relevant when the size variable is 
    numeric.

size_norm：tuple or Normalize object, optional

    Normalization in data units for scaling plot objects when the size 
    variable is numeric.

markers：boolean, list, or dictionary, optional

    Object determining how to draw the markers for different levels of the 
    style variable. Setting to True will use default markers, or you can pass 
    a list of markers or a dictionary mapping levels of the style variable to 
    markers. Setting to False will draw marker-less lines. Markers are 
    specified as in matplotlib.

style_order：list, optional

    Specified order for appearance of the style variable levels otherwise 
    they are determined from the data. Not relevant when the style variable 
    is numeric.

{x,y}_bins：lists or arrays or functions

    Currently non-functional.

units：{long_form_var}

    Grouping variable identifying sampling units. When used, a separate line 
    will be drawn for each unit with appropriate semantics, but no legend 
    entry will be added. Useful for showing distribution of experimental 
    replicates when exact identities are not needed.

    Currently non-functional.

estimator：name of pandas method or callable or None, optional

    Method for aggregating across multiple observations of the y variable at 
    the same x level. If None, all observations will be drawn. Currently 
    non-functional.

ci：int or “sd” or None, optional

    Size of the confidence interval to draw when aggregating with an 
    estimator. “sd” means to draw the standard deviation of the data. 
    Setting to None will skip bootstrapping. Currently non-functional.

n_boot：int, optional

    Number of bootstraps to use for computing the confidence interval. 
    Currently non-functional.

alpha：float

    Proportional opacity of the points.

{x,y}_jitter：booleans or floats

    Currently non-functional.

legend：“brief”, “full”, or False, optional

    How to draw the legend. If “brief”, numeric hue and size variables will 
    be represented with a sample of evenly spaced values. If “full”, every 
    group will get an entry in the legend. If False, no legend data is added 
    and no legend is drawn.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

kwargs：key, value mappings

    Other keyword arguments are passed down to plt.scatter at draw time.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.

See also

Show the relationship between two variables connected with lines to emphasize 
continuity.Draw a scatter plot with one categorical variable, arranging the 
points to show the distribution of values.'''

#%%

#Examples

#Draw a simple scatter plot between two variables:
ax = sns.scatterplot(x='total_bill',y='tip',data=tips)

#Group by another variable and show the groups with different colors:
ax = sns.scatterplot(x='total_bill',y='tip',hue='time',data=tips)

#Show the grouping variable by varying both color and marker:
ax = sns.scatterplot(x='total_bill',y='tip',
                     hue='time',style='time',data=tips)

#Vary colors and markers to show two different grouping variables:
fig,ax = plt.subplots()
ax = sns.scatterplot(x='total_bill',y='tip',
                     hue='day',style='time',data=tips)

#Show a quantitative variable by varying the size of the points:
fig,ax = plt.subplots(1,2,figsize=(8,6))
sns.scatterplot(x='total_bill',y='tip',size='size',data=tips,ax=ax[0])

#Also show the quantitative variable by also using continuous colors:
#fig,ax = plt.subplots()
sns.scatterplot(x='total_bill',y='tip',size='size',
                hue='size',data=tips,ax=ax[1])

#Use a different continuous color map:
fig,ax = plt.subplots()
cmap = sns.cubehelix_palette(dark=.3,light=.8,as_cmap=True)
ax = sns.scatterplot(x='total_bill',y='tip',hue='size',size='size',
                     palette=cmap,data=tips)


#Change the minimum and maximum point size and show all sizes in legend:
fig,ax = plt.subplots()
ax = sns.scatterplot(x='total_bill',y='tip',hue='size',size='size',
                     sizes=(20,200),palette=cmap,legend='full',data=tips)

#Use a narrower range of color map intensities:
fig,ax = plt.subplots()
ax = sns.scatterplot(x='total_bill',y='tip',hue='size',size='size',
                     sizes=(20,200),hue_norm=(0,7),legend='full',data=tips)

#Vary the size with a categorical variable, and use a different palette:
fig,ax = plt.subplots()
ax = sns.scatterplot(x='total_bill',y='tip',hue='day',size='smoker',
                     palette='Set2',data=tips)

#Use a specific set of markers:
fig,ax = plt.subplots()
marker = {'Yes':'s','No':'X'}
ax = sns.scatterplot(x='total_bill',y='tip',hue='day',style='smoker',
                     markers=marker,
                     palette='Set2',data=tips)
#Control plot attributes using matplotlib parameters:
fig,ax = plt.subplots()
ax = sns.scatterplot(x='total_bill',y='tip',s=100,color='.2',marker='+',
                     data=tips)

#Pass data vectors instead of names in a data frame:
iris = sns.load_dataset('iris')
fig,ax = plt.subplots()
ax = sns.scatterplot(x=iris.sepal_length,y=iris.sepal_width,
                     hue=iris.species,style=iris.species)

#%%

#Pass a wide-form dataset and plot against its index:
index = pd.date_range('2010-1-1',periods=100,freq='m',name='date')
data = np.random.randn(100,4).cumsum(axis=0)
wide_df = pd.DataFrame(data,index,columns=list('ABCD'))
print(wide_df)
fig,ax = plt.subplots()
ax = sns.scatterplot(data = wide_df)
ax.set_xlim(['2010','2018'])

#%%

#seaborn.lineplot

'''seaborn.lineplot(x=None, y=None, hue=None, size=None, 
style=None, data=None, palette=None, hue_order=None, hue_norm=None, 
sizes=None, size_order=None, size_norm=None, dashes=True, 
markers=None, style_order=None, units=None, estimator='mean', 
ci=95, n_boot=1000, sort=True, err_style='band', err_kws=None, 
legend='brief', ax=None, **kwargs)'''

'''Draw a line plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of
 the data using the hue, size, and style parameters. These parameters 
 control what visual semantics are used to identify the different 
 subsets. It is possible to show up to three dimensions independently 
 by using all three semantic types, but this style of plot can be 
 hard to interpret and is often ineffective. Using redundant semantics
 (i.e. both hue and style for the same variable) can be helpful for 
 making graphics more accessible.

See the tutorial for more information.

By default, the plot aggregates over multiple y values at each value 
of x and shows an estimate of the central tendency and a confidence 
interval for that estimate.'''

#%%

'''参数：x, y：names of variables in data or vector data, optional

    Input data variables; must be numeric. Can pass data directly 
    or reference columns in data.

hue：name of variables in data or vector data, optional

    Grouping variable that will produce lines with different colors. 
    Can be either categorical or numeric, although color mapping will 
    behave differently in latter case.

size：name of variables in data or vector data, optional

    Grouping variable that will produce lines with different widths. 
    Can be either categorical or numeric, although size mapping will 
    behave differently in latter case.

style：name of variables in data or vector data, optional

    Grouping variable that will produce lines with different dashes 
    and/or markers. Can have a numeric dtype but will always be 
    treated as categorical.

data：DataFrame

    Tidy (“long-form”) dataframe where each column is a variable 
    and each row is an observation.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. 
    Should be something that can be interpreted by color_palette(), 
    or a dictionary mapping hue levels to matplotlib colors.

hue_order：list, optional

    Specified order for the appearance of the hue variable levels, 
    otherwise they are determined from the data. Not relevant when 
    the hue variable is numeric.

hue_norm：tuple or Normalize object, optional

    Normalization in data units for colormap applied to the hue 
    variable when it is numeric. Not relevant if it is categorical.

sizes：list, dict, or tuple, optional

    An object that determines how sizes are chosen when size is used. 
    It can always be a list of size values or a dict mapping levels 
    of the size variable to sizes. When size is numeric, it can also 
    be a tuple specifying the minimum and maximum size to use such 
    that other values are normalized within this range.

size_order：list, optional

    Specified order for appearance of the size variable levels, 
    otherwise they are determined from the data. Not relevant when 
    the size variable is numeric.

size_norm：tuple or Normalize object, optional

    Normalization in data units for scaling plot objects when the 
    size variable is numeric.

dashes：boolean, list, or dictionary, optional

    Object determining how to draw the lines for different levels of 
    the style variable. Setting to True will use default dash codes, 
    or you can pass a list of dash codes or a dictionary mapping 
    levels of the style variable to dash codes. Setting to False will 
    use solid lines for all subsets. Dashes are specified as in 
    matplotlib: a tuple of (segment, gap) lengths, or an empty 
    string to draw a solid line.

markers：boolean, list, or dictionary, optional

    Object determining how to draw the markers for different levels 
    of the style variable. Setting to True will use default markers, 
    or you can pass a list of markers or a dictionary mapping levels 
    of the style variable to markers. Setting to False will draw 
    marker-less lines. Markers are specified as in matplotlib.

style_order：list, optional

    Specified order for appearance of the style variable levels 
    otherwise they are determined from the data. Not relevant when 
    the style variable is numeric.

units：{long_form_var}

    Grouping variable identifying sampling units. When used, a 
    separate line will be drawn for each unit with appropriate 
    semantics, but no legend entry will be added. Useful for showing 
    distribution of experimental replicates when exact identities are 
    not needed.

estimator：name of pandas method or callable or None, optional

    Method for aggregating across multiple observations of the y 
    variable at the same x level. If None, all observations will be 
    drawn.

ci：int or “sd” or None, optional

    Size of the confidence interval to draw when aggregating with an 
    estimator. “sd” means to draw the standard deviation of the 
    data. Setting to None will skip bootstrapping.

n_boot：int, optional

    Number of bootstraps to use for computing the confidence interval.

sort：boolean, optional

    If True, the data will be sorted by the x and y variables, 
    otherwise lines will connect points in the order they appear 
    in the dataset.

err_style：“band” or “bars”, optional

    Whether to draw the confidence intervals with translucent error 
    bands or discrete error bars.

err_band：dict of keyword arguments

    Additional paramters to control the aesthetics of the error bars. 
    The kwargs are passed either to ax.fill_between or ax.errorbar, 
    depending on the err_style.

legend：“brief”, “full”, or False, optional

    How to draw the legend. If “brief”, numeric hue and size 
    variables will be represented with a sample of evenly spaced 
    values. If “full”, every group will get an entry in the legend. 
    If False, no legend data is added and no legend is drawn.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current 
    Axes.

kwargs：key, value mappings

    Other keyword arguments are passed down to plt.plot at draw time.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.

See also

Show the relationship between two variables without emphasizing 
continuity of the x variable.Show the relationship between two 
variables when one is categorical.'''

#%%

#Examples

#Draw a single line plot with error bands showing a confidence
#interval:

ax = sns.lineplot(x='timepoint',y='signal',data=fmri)

#Group by another variable and show the groups with different colors:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x="timepoint", y="signal", hue="event",data=fmri)

#Show the grouping variable with both color and line dashing:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x="timepoint", y="signal",
                  hue="event",style='event',data=fmri)

#Use color and line dashing to represent two different grouping variables:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x="timepoint", y="signal",
                  hue="region",style='event',data=fmri)

#Use markers instead of the dashes to identify groups:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x="timepoint", y="signal",hue='event',
                  style='event',markers=True,data=fmri)

#Show error bars instead of error bands and plot the standard error:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x="timepoint", y="signal",hue='event',
                  style='event',err_style='bars',ci=68,data=fmri)

#Show experimental replicates instead of aggregating:
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x='timepoint',y='signal',hue='event',
                  units='subject',estimator=None,lw=1,
                  data=fmri.query("region=='frontal'"))

#Use a quantitative color mapping:
dots = sns.load_dataset('dots').query("align == 'dots'")
fig = plt.figure()
plt.subplot()
ax = sns.lineplot(x='time',y='firing_rate',hue='coherence',
                  style='choice',data=dots)

#Use a different normalization for the colormap:

#%%

dots = sns.load_dataset('dots').query("align == 'dots'")

from matplotlib.colors import LogNorm
plt.figure()
plt.subplot()
ax = sns.lineplot(x='time',y='firing_rate',hue='coherence',
                  style='choice',hue_norm=LogNorm(),data=dots)
plt.legend(loc='best')

#Use a different color palette:

plt.figure()
plt.subplot()
ax = sns.lineplot(x='time',y='firing_rate',hue='coherence',
                  style='choice',palette='ch:2.5,.25',
                  data=dots)

#Use specific color values, treating the hue variable as categorical:
palette =sns.color_palette('mako_r',6)

plt.figure()
plt.subplot()
ax = sns.lineplot(x='time',y='firing_rate',hue='coherence',
                  style='choice',palette=palette,data=dots)

#Change the width of the lines with a quantitative variable:
plt.figure(figsize=(5,10))
plt.subplot(211)
ax = sns.lineplot(x='time',y='firing_rate',hue='choice',size='coherence',
                  legend='full',data=dots)
plt.subplot(212)
ax = sns.lineplot(x='time',y='firing_rate',hue='choice',size='coherence',
                  data=dots)

#Change the range of line widths used to normalize the size variable:
plt.figure()
plt.subplot()
ax = sns.lineplot(x='time',y='firing_rate',hue='choice',
                  size='coherence',sizes=(.25,2.5),
                  data=dots)

#Plot from a wide-form DataFrame:

index = pd.date_range('1-1-2000',periods=100,freq='m',name='date')
data = np.random.randn(100,4).cumsum(axis=0)
wide_df = pd.DataFrame(data,index,columns=list('abcd'))
plt.figure()
plt.subplot()
ax = sns.lineplot(data=wide_df)

#Plot from a list of Series:
plt.figure()
plt.subplot()
list_data = [wide_df.loc[:'2005','a'],wide_df.loc['2003':,'b']]
ax = sns.lineplot(data=list_data)

#Plot a single Series, pass kwargs to plt.plot:
plt.figure()
plt.subplot()
ax = sns.lineplot(data=wide_df['a'],color='coral',label='line')

#Draw lines at points as they appear in the dataset:
plt.figure()
plt.subplot()
x,y = np.random.randn(2,5000).cumsum(axis=1)
ax = sns.lineplot(x=x,y=y,sort=False,lw=1)

#%%

#seaborn.catplot

'''seaborn.catplot(x=None, y=None, hue=None, data=None, row=None, 
col=None, col_wrap=None, estimator=<function mean>, ci=95, 
n_boot=1000, units=None, order=None, hue_order=None, 
row_order=None, col_order=None, kind='strip', height=5, 
aspect=1, orient=None, color=None, palette=None, legend=True, 
legend_out=True, sharex=True, sharey=True, margin_titles=False, 
facet_kws=None, **kwargs)'''

'''seaborn.catplot 是一个将分类图绘制到FacetGrid上图级别接口。

这个函数可以访问多个轴级功能，这些轴级功能通过不同的可视化图表展示数字
和一个或多个分类变量的关系。kind 参数可以选择的轴级基础函数有：'''

'''分类散点图:

    stripplot() (with kind="strip"; the default)
    swarmplot() (with kind="swarm")

分类分布图:

    boxplot() (with kind="box")
    violinplot() (with kind="violin")
    boxenplot() (with kind="boxen")

分类估计图:

    pointplot() (with kind="point")
    barplot() (with kind="bar")
    countplot() (with kind="count")

额外的关键字参数将传递给基础函数，因此，您应参阅每个文档，以查看特定类型的选项.

请注意，与直接使用轴级函数不同, 数据必须在长格式DataFrame中传递，并通过将字符串
传递给 x, y, hue, 等指定的变量.

与基础绘图函数的情况一样, 如果变量有 categorical 数据类型, 则将从对象推断出分类
变量的级别及其顺序。否则，您可能必须使用更改 dataframe 排序或使用函数参数
(orient, order, hue_order, etc.) 来正确设置绘图。

此函数始终将其中一个变量视为分类，并在相关轴上的序数位置（0,1，... n）处绘制
数据，即使数据具有数字或日期类型。

有关更多信息，请参考 tutorial。

绘图后，返回带有绘图的 FacetGrid，可以直接用于调整绘图细节或添加其他图层。'''

#%%

'''参数：x, y, hue： data names 中的变量名称

    用于绘制长格式数据的输入。查看解释示例

data：DataFrame

    用于绘图的长形（整洁）数据集。每列应对应一个变量，每行应对应一个观察。

row, col：data 中的变量名称, 可选

    分类变量将决定网格的分面。

col_wrap：int, 可选

    以此宽度“包裹”列变量，以便列面跨越多行。 与行方面不兼容。

estimator：可调用的映射向量 -> 标量，可选

    在每个分类箱内估计的统计函数。

ci：float或“sd”或None，可选

    在估计值附近绘制置信区间的大小。如果是“sd”，则跳过自举(bootstrapping)
    并绘制观察的标准偏差。None,如果为None，则不执行自举，并且不会绘制错误条。

n_boot：int，可选

    计算置信区间时使用的引导程序迭代次数。

units：数据或矢量数据中变量的名称,可选

    采样单元的标识符，用于执行多级引导程序并考虑重复测量设计。

order, hue_order：字符串列表，可选

    命令绘制分类级别，否则从数据对象推断级别。

row_order, col_order：字符串列表，可选

    命令组织网格的行和/或列，否则从数据对象推断命令。

kind：字符串，可选

    要绘制的绘图类型（对应于分类绘图功能的名称。选项包括：“点”，“条形”，
    “条形”，“群”，“框”，“小提琴”或“盒子”。

height：标量，可选

    每个刻面的高度（以英寸为单位）。另见： aspect。

aspect：标量，可选

    每个面的纵横比，因此aspect * height给出每个面的宽度，单位为英寸。

orient：“v” | “h”, 可选

    图的方向（垂直或水平）。这通常是从输入变量的dtype推断出来的，但可用于指定
    “分类”变量何时是数字或何时绘制宽格式数据。

color：matplotlib颜色，可选

    所有元素的颜色，或渐变调色板的种子。

palette：调色板名称，列表或字典，可选

    用于色调变量的不同级别的颜色。应该是 color_palette(), 可以解释的东西，
    或者是将色调级别映射到matplotlib颜色的字典。

legend：bool, 可选

    如果为 True 并且存在hue变量，则在图上绘制图例。t.

legend_out：bool, 可选

    如果为True，则图形尺寸将被扩展，图例将绘制在中间右侧的图形之外。

share{x,y}：bool, ‘col’, 或 ‘row’ 可选

    如果为true，则facet将跨行跨越列和/或x轴共享y轴。

margin_titles：bool, 可选

    如果为True，则行变量的标题将绘制在最后一列的右侧。此选项是实验性的，可能
    无法在所有情况下使用。

facet_kws：dict, 可选

    传递给FacetGrid的其他关键字参数的字典。

kwargs：key, value 配对

    其他关键字参数将传递给基础绘图函数。

返回值：g：FacetGrid

    返回FacetGrid对象及其上的绘图以进一步调整。
'''

#%%

#例子
#绘制单个构面以使用FacetGrid图例放置：
sns.set(style='ticks')
exercise = sns.load_dataset('exercise')
g = sns.catplot(x='time',y='pulse',hue='kind',data=exercise)

#使用不同的绘图类型可视化相同的数据：
g = sns.catplot(x='time',y='pulse',hue='kind',data=exercise,kind='violin')

#沿列的方面显示第三个分类变量
g = sns.catplot(x='time',y='pulse',hue='kind',col='diet',data=exercise)

#为构面使用不同的高度和宽高比：
g = sns.catplot(x='time',y='pulse',hue='kind',col='diet',data=exercise,
                height=5,aspect=.8)

#创建许多列构面并将它们包装到网格的行中：

titanic = sns.load_dataset('titanic')
g = sns.catplot('alive',col='deck',col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind='count',height=5,aspect=.8)

#%%

#水平绘图并将其他关键字参数传递给绘图函数：

#dodge: 使用色调嵌套时，元素是否应沿分类轴移动。
#cut:以带宽大小为单位的距离，以控制小提琴图外壳延伸超过内部极端数据点的
#密度。设置为0以将小提琴图范围限制在观察数据的范围内。
#（例如，在 ggplot 中具有与 trim=True 相同的效果）

g = sns.catplot(x='age',y='embark_town',hue='sex',row='class',
                data=titanic[titanic.deck.notnull()],
                orient='h',height=2,aspect=3,palette='Set3',
                kind='violin',dodge=True,cut=0,bw=.2)

#使用返回的FacetGrid 上的方法来调整演示文稿：
g = sns.catplot(x='who',y='survived',col='class',
                data=titanic,saturation=.5,
                kind='bar',ci=None,aspect=.6)
(g.set_axis_labels('','Survival Rate')
 .set_xticklabels(['Men','Women','Children'])
 .set_titles('{col_name} {col_var}')
 .set(ylim=(0,1))
 .despine(left=True))

#%%

#seaborn.stripplot
'''seaborn.stripplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, jitter=True, dodge=False, orient=None, color=None, 
palette=None, size=5, edgecolor='gray', linewidth=0, ax=None, **kwargs)'''

'''绘制一个散点图，其中一个变量是分类。

条形图可以单独绘制，但如果您想要显示所有观察结果以及底层分布的某些表示，它也是
一个盒子或小提琴图的良好补充。

输入数据可以以多种格式传递，包括：

    表示为列表，numpy数组或pandas Series对象的数据向量直接传递给x，y和hue参数
    在这种情况下，x，y和hue变量将决定数据的绘制方式。
    “wide-form” DataFrame, 用于绘制每个数字列。
    一个数组或向量列表。

在大多数情况下，可以使用numpy或Python对象，但最好使用pandas对象，因为关联的名
称将用于注释轴。另外，您可以使用分组变量的分类类型来控制绘图元素的顺序。

此函数始终将其中一个变量视为分类，并在相关轴上的序数位置（0,1，... n）处绘制数
据，即使数据具有数字或日期类型也是如此。
'''

#%%

'''参数：x, y, hue： 数据或矢量数据中的变量名称，可选

    用于绘制长格式数据的输入。查看解释示例。

data：DataFrame, 数组, 数组列表, 可选

    用于绘图的数据集。如果 x 和 y 不存在，则将其解释为宽格式。否则预计它将是
    长格式的。

order, hue_order：字符串列表，可选

    命令绘制分类级别，否则从数据对象推断级别。

jitter：float, True/1 是特殊的，可选

    要应用的抖动量（仅沿分类轴）。 当您有许多点并且它们重叠时，这可能很有用，
    因此更容易看到分布。您可以指定抖动量（均匀随机变量支持的宽度的一半），
    或者仅使用True作为良好的默认值

dodge：bool, 可选

    使用 hue 嵌套时，将其设置为 True 将沿着分类轴分离不同色调级别的条带。
    否则，每个级别的点将相互叠加。

orient：“v” | “h”, 可选

    图的方向（垂直或水平）。这通常是从输入变量的dtype推断出来的，但可用于指
    定“分类”变量何时是数字或何时绘制宽格式数据。

color：matplotlib颜色，可选

    所有元素的颜色，或渐变调色板的种子。

palette：调色板名称，列表或字典，可选

    用于色调变量的不同级别的颜色。应该是 color_palette(), 可以解释的东西，或
    者是将色调级别映射到matplotlib颜色的字典。

size：float, 可选

    标记的直径，以磅为单位。（虽然 plt.scatter 用于绘制点，但这里的 size 参
    数采用“普通”标记大小而不是大小^ 2，如 plt.scatter 。

edgecolor：matplotlib颜色，“灰色”是特殊的，可选的

    每个点周围线条的颜色。如果传递"灰色"，则亮度由用于点体的调色板决定。

linewidth：float, 可选

    构图元素的灰线宽度。

ax：matplotlib轴，可选

    返回Axes对象，并在其上绘制绘图。

返回值：ax：matplotlib轴

    返回Axes对象，并在其上绘制绘图。
'''

#%%

#例子

#绘制单个水平条形图：

sns.set(style='whitegrid')
tips = sns.load_dataset('tips')
ax = sns.stripplot(x=tips.total_bill)

#通过分类变量对条形图进行分组：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='day',y='total_bill',data=tips)

#添加抖动以显示值的分布(默认为True)：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='day',y='total_bill',jitter=True,data=tips)

#使用较少量的抖动：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='day',y='total_bill',jitter=0.05,data=tips)

#画水平条形图：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='total_bill',y='day',data=tips)

#围绕要点绘制轮廓(lw无效)
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='total_bill',y='day',data=tips,linewidth=1)

#将条带嵌套在第二个分类变量中：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='sex',y='total_bill',hue='day',data=tips)

#在主要分类轴上的不同位置绘制 hue 变量的每个级别：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='sex',y='total_bill',hue='day',dodge=True,data=tips)

#通过传递显式顺序来控制条带顺序：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='time',y='tip',data=tips,
                   order=['Dinner','Lunch'])

#绘制具有大点和不同美感的条带：
fig = plt.figure()
plt.subplot()
ax = sns.stripplot(x='day',y='total_bill',hue='smoker',data=tips,
                   palette='Set2',size=20,marker='D',edgecolor='gray',
                   alpha=.25)
plt.legend(loc='best')

#在箱形图上绘制观察条带：
fig = plt.figure()
plt.subplot()
ax = sns.boxplot(x='tip',y='day',data=tips,whis=np.inf)
ax = sns.stripplot(x='tip',y='day',data=tips,color='.3')

#在小提琴情节的顶部绘制观察条带：
fig = plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',data=tips,inner=None,color='.8')
ax = sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)

'''使用 catplot() 组合stripplot()和FacetGrid。这允许在其他分类变量中进行分组。
使用catplot()比直接使用FacetGrid更安全，因为它确保了跨方面的变量顺序的同步'''

g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',
                data=tips,kind='strip',jitter=True,
                height=6,aspect=.7)

#%%

#seaborn.swarmplot

'''seaborn.swarmplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, dodge=False, orient=None, color=None, palette=None, 
size=5, edgecolor='gray', linewidth=0, ax=None, **kwargs)'''

'''Input data can be passed in a variety of formats, including:

    Vectors of data represented as lists, numpy arrays, or pandas Series 
    objects passed directly to the x, y, and/or hue parameters.
    A “long-form” DataFrame, in which case the x, y, and hue variables will 
    determine how the data are plotted.
    A “wide-form” DataFrame, such that each numeric column will be plotted.
    An array or list of vectors.

In most cases, it is possible to use numpy or Python objects, but pandas 
objects are preferable because the associated names will be used to annotate 
the axes. Additionally, you can use Categorical types for the grouping 
variables to control the order of plot elements.

This function always treats one of the variables as categorical and draws 
data at ordinal positions (0, 1, … n) on the relevant axis, even when the 
data has a numeric or date type.'''

#%%

'''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as 
    wide-form. Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are inferred 
    from the data objects.

dodge：bool, optional

    When using hue nesting, setting this to True will separate the strips for 
    different hue levels along the categorical axis. Otherwise, the points for 
    each level will be plotted in one swarm.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually inferred 
    from the dtype of the input variables, but can be used to specify when the 
    “categorical” variable is a numeric or when plotting wide-form data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

size：float, optional

    Diameter of the markers, in points. (Although plt.scatter is used to draw 
    the points, the size argument here takes a “normal” markersize and not 
    size^2 like plt.scatter.

edgecolor：matplotlib color, “gray” is special-cased, optional

    Color of the lines around each point. If you pass "gray", the brightness 
    is determined by the color palette used for the body of the points.

linewidth：float, optional

    Width of the gray lines that frame the plot elements.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.
'''

'''See also

A traditional box-and-whisker plot with a similar API.A combination of 
boxplot and kernel density estimation.A scatterplot where one variable 
is categorical. Can be used in conjunction with other plots to show 
each observation.Combine a categorical plot with a class:FacetGrid'''

#%%

#Examples

#Draw a single horizontal swarm plot:

ax = sns.swarmplot(x=tips.total_bill)

#Group the swarms by a categorical variable:
plt.figure()
plt.subplot()
ax = sns.swarmplot(x='day',y='total_bill',data=tips)

#Draw horizontal swarms:
plt.figure()
plt.subplot()
ax = sns.swarmplot(x='total_bill',y='day',data=tips)

#Color the points using a second categorical variable:
plt.figure(figsize=(10,5))
plt.subplot(121)
ax = sns.swarmplot(x='day',y='total_bill',hue='sex',data=tips)

#Split each level of the hue variable along the categorical axis:
plt.subplot(122)
ax = sns.swarmplot(x='day',y='total_bill',hue='sex',data=tips,dodge=True)

#Control swarm order by passing an explicit order:
plt.figure()
plt.subplot()
ax = sns.swarmplot(x='time',y='tip',data=tips,
                   order=['Dinner','Lunch'])

#Plot using larger points:
plt.figure()
plt.subplot()
ax = sns.swarmplot(x="time", y="tip", data=tips, size=10)

#Draw swarms of observations on top of a box plot:
plt.figure()
plt.subplot()
ax = sns.boxplot(x='tip',y='day',data=tips,whis=np.inf)
ax = sns.swarmplot(x='tip',y='day',data=tips,color='.2')

#Draw swarms of observations on top of a violin plot:
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',data=tips,inner=None)
ax = sns.swarmplot(x='day',y='total_bill',data=tips,
                   color='white',edgecolor='grey')

'''Use catplot() to combine a swarmplot() and a FacetGrid. This allows 
grouping within additional categorical variables. Using catplot() is safer 
than using FacetGrid directly, as it ensures synchronization of variable order 
across facets:'''

g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',data=tips,
                kind='swarm',height=4,aspect=.7,dodge=True)

#%%

#seaborn.boxplot

'''seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, orient=None, color=None, palette=None, 
saturation=0.75, width=0.8, dodge=True, fliersize=5, 
linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)'''

'''seaborn.boxplot 接口的作用是绘制箱形图以展现与类别相关的数据分布状况。

箱形图（或盒须图）以一种利于变量之间比较或不同分类变量层次之间比较的方式
来展示定量数据的分布。图中矩形框显示数据集的上下四分位数，而矩形框中延伸
出的线段（触须）则用于显示其余数据的分布位置，剩下超过上下四分位间距的数
据点则被视为“异常值”。

输入数据可以通过多种格式传入，包括：

    格式为列表，numpy数组或pandas Series对象的数据向量可以直接传递给x，
    y和hue参数。
    对于长格式的DataFrame，x，y，和hue参数会决定如何绘制数据。
    对于宽格式的DataFrame，每一列数值列都会被绘制。
    一个数组或向量的列表。

在大多数情况下，可以使用numpy或Python对象，但更推荐使用pandas对象，因为
与数据关联的列名/行名可以用于标注横轴/纵轴的名称。此外，您可以使用分类
类型对变量进行分组以控制绘图元素的顺序。

此函数始终将其中一个变量视为分类，并在相关轴上的序数位置(0,1，... n)处
绘制数据，即使数据属于数值类型或日期类型也是如此。'''

#%%

'''参数：x, y, hue：数据或向量数据中的变量名称，可选

    用于绘制长格式数据的输入。查看样例以进一步理解。

data：DataFrame，数组，数组列表，可选

    用于绘图的数据集。如果x和y都缺失，那么数据将被视为宽格式。否则数据
    被视为长格式。

order, hue_order：字符串列表，可选

    控制分类变量（对应的条形图）的绘制顺序，若缺失则从数据中推断分类变
    量的顺序。

orient：“v” | “h”，可选

    控制绘图的方向（垂直或水平）。这通常是从输入变量的dtype推断出来的，
    但是当“分类”变量为数值型或绘制宽格式数据时可用于指定绘图的方向。

color：matplotlib颜色，可选

    所有元素的颜色，或渐变调色板的种子颜色。

palette：调色板名称，列表或字典，可选

    用于hue变量的不同级别的颜色。可以从 color_palette() 得到一些解释，
    或者将色调级别映射到matplotlib颜色的字典。

saturation：float，可选

    控制用于绘制颜色的原始饱和度的比例。通常大幅填充在轻微不饱和的颜色
    下看起来更好，如果您希望绘图颜色与输入颜色规格完美匹配可将其设置为1。

width：float，可选

    不使用色调嵌套时完整元素的宽度，或主要分组变量一个级别的所有元素的
    宽度。

dodge：bool，可选

    使用色调嵌套时，元素是否应沿分类轴移动。

fliersize：float，可选

    用于表示异常值观察的标记的大小。

linewidth：float，可选

    构图元素的灰线宽度。

whis：float，可选

    控制在超过高低四分位数时IQR的比例，因此需要延长绘制的触须线段。
    超出此范围的点将被识别为异常值。

notch：boolean，可选

    是否使矩形框“凹陷”以指示中位数的置信区间。还有其他几个参数可以
    控制凹槽的绘制方式；参见 plt.boxplot 以查看关于此问题的更多帮助信息。

ax：matplotlib轴，可选

    绘图时使用的Axes轴对象，否则使用当前Axes轴对象。

kwargs：键，值映射

    其他在绘图时传给 plt.boxplot 的参数。

返回值：ax：matplotlib轴

    返回Axes对轴象，并在其上绘制绘图。

亦可参见

boxplot和核密度估计的结合。当一个变量是分类变量的散点图。可以与其他
图表结合使用以展示各自的观测结果。分类散点图的特点是其中数据点互不重
叠。可以与其他图表结合使用以展示各自的观测结果。'''

#%%

#示例

#绘制一个单独的横向箱型图：


sns.set(style='whitegrid')
tips = sns.load_dataset('tips')
ax = sns.boxplot(x=tips.total_bill)

#根据分类变量分组绘制一个纵向的箱型图
plt.figure()
plt.subplot()
ax = sns.boxplot(x='day',y='total_bill',data=tips)

#根据2个分类变量嵌套分组绘制一个箱型图：

plt.figure()
plt.subplot()
ax = sns.boxplot(x='day',y='total_bill',hue='smoker',data=tips,
                 palette='Set3')

#当一些数据为空时根据嵌套分组绘制一个箱型图
plt.figure()
plt.subplot()
ax = sns.boxplot(x='day',y='total_bill',hue='time',data=tips,
                 palette='Set3',linewidth=2.5)

#通过显式传入参数指定顺序控制箱型图的显示顺序：
plt.figure()
plt.subplot()
ax = sns.boxplot(x='time',y='total_bill',data=tips,
                 order=['Dinner','Lunch'])

#针对DataFrame里每一个数值型变量绘制箱型图：
iris = sns.load_dataset('iris')
plt.figure()
plt.subplot()
ax = sns.boxplot(data=iris,orient='h',palette='Set2')

#使用 hue 参数无需改变箱型图的位置或宽度：
plt.figure()
plt.subplot()
tips['weekend'] = tips['day'].isin(['Sat','Sun'])
ax = sns.boxplot(x='day',y='total_bill',hue='weekend',data=tips,
                 dodge=True)

#使用 swarmplot() 展示箱型图顶部的数据点：
plt.figure()
plt.subplot()
ax = sns.swarmplot(x='day',y='total_bill',data=tips,color='.25')
ax = sns.boxplot(x='day',y='total_bill',data=tips)

'''把 catplot() 与 pointplot() 以及 FacetGrid 结合起来使用。
这允许您通过额外的分类变量进行分组。使用 catplot() 比直接使用 
FacetGrid 更为安全，因为它保证了不同切面上变量同步的顺序：'''
g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',
                data=tips,kind='box',height=4,aspect=.7)

#%%

#seaborn.violinplot
'''seaborn.violinplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, bw='scott', cut=2, scale='area', scale_hue=True, 
gridsize=100, width=0.8, inner='box', split=False, dodge=True, 
orient=None, linewidth=None, color=None, palette=None, saturation=0.75, 
ax=None, **kwargs)'''

'''结合箱型图与核密度估计绘图。

小提琴图的功能与箱型图类似。 它显示了一个（或多个）分类变量多个属性上的定量数
据的分布，从而可以比较这些分布。与箱形图不同，其中所有绘图单元都与实际数据点
对应，小提琴图描述了基础数据分布的核密度估计。

小提琴图可以是一种单次显示多个数据分布的有效且有吸引力的方式，但请记住，估计
过程受样本大小的影响，相对较小样本的小提琴可能看起来非常平滑，这种平滑具有误导
性。

输入数据可以通过多种格式传入，包括：

    格式为列表，numpy数组或pandas Series对象的数据向量可以直接传递给x，y和
    hue参数。
    对于长格式的DataFrame，x，y，和hue参数会决定如何绘制数据。
    对于宽格式的DataFrame，每一列数值列都会被绘制。
    一个数组或向量的列表。

在大多数情况下，可以使用numpy或Python对象，但更推荐使用pandas对象，因为与数据
关联的列名/行名可以用于标注横轴/纵轴的名称。此外，您可以使用分类类型对变量进
行分组以控制绘图元素的顺序。

此函数始终将其中一个变量视为分类，并在相关轴上的序数位置(0,1，... n)处绘制数
据，即使数据属于数值类型或日期类型也是如此。'''

#%%

'''参数：x, y, hue：数据或向量数据中的变量名称，可选

    用于绘制长格式数据的输入。查看样例以进一步理解。

data：DataFrame，数组，数组列表，可选

    用于绘图的数据集。如果x和y都缺失，那么数据将被视为宽格式。否则数据被视为长
    格式。

order, hue_order：字符串列表，可选

    控制分类变量（对应的条形图）的绘制顺序，若缺失则从数据中推断分类变量的顺序。

bw：{‘scott’, ‘silverman’, float}，可选

    内置变量值或浮点数的比例因子都用来计算核密度的带宽。实际的核大小由比例因子
    乘以每个分箱内数据的标准差确定。

cut：float，可选

    以带宽大小为单位的距离，以控制小提琴图外壳延伸超过内部极端数据点的密度。
    设置为0以将小提琴图范围限制在观察数据的范围内。（例如，在 ggplot 中具有与 
    trim=True 相同的效果）

scale：{“area”, “count”, “width”}，可选

    该方法用于缩放每张小提琴图的宽度。若为 area ，每张小提琴图具有相同的面积。
    若为 count ，小提琴的宽度会根据分箱中观察点的数量进行缩放。若为 width ，
    每张小提琴图具有相同的宽度。

scale_hue：bool，可选

    当使用色调参数 hue 变量绘制嵌套小提琴图时，该参数决定缩放比例是在主要分组
    变量（scale_hue=True）的每个级别内还是在图上的所有小提琴图
    （scale_hue=False）内计算出来的。

gridsize：int，可选

    用于计算核密度估计的离散网格中的数据点数目。

width：float，可选

    不使用色调嵌套时的完整元素的宽度，或主要分组变量的一个级别的所有元素的宽度。

inner：{“box”, “quartile”, “point”, “stick”, None}，可选

    控制小提琴图内部数据点的表示。若为box，则绘制一个微型箱型图。若为quartiles，
    则显示四分位数线。若为point或stick，则显示具体数据点或数据线。使用None则绘
    制不加修饰的小提琴图。

split：bool，可选

    当使用带有两种颜色的变量时，将split设置为True则会为每种颜色绘制对应半边小
    提琴。从而可以更容易直接的比较分布。

dodge：bool，可选

    使用色调嵌套时，元素是否应沿分类轴移动。

orient：“v” | “h”，可选

    控制绘图的方向（垂直或水平）。这通常是从输入变量的dtype推断出来的，但是
    当“分类”变量为数值型或绘制宽格式数据时可用于指定绘图的方向。

linewidth：float，可选

    构图元素的灰线宽度。

color：matplotlib颜色，可选

    所有元素的颜色，或渐变调色板的种子颜色。

palette：调色板名称，列表或字典，可选

    用于hue变量的不同级别的颜色。可以从 color_palette() 得到一些解释，或者将
    色调级别映射到matplotlib颜色的字典。

saturation：float，可选

    控制用于绘制颜色的原始饱和度的比例。通常大幅填充在轻微不饱和的颜色下看起来
    更好，如果您希望绘图颜色与输入颜色规格完美匹配可将其设置为1。

ax：matplotlib轴，可选

    绘图时使用的Axes轴对象，否则使用当前Axes轴对象。

返回值：ax：matplotlib轴

    返回Axes对轴象，并在其上绘制绘图。
    
一个传统的箱型图具有类似的API。当一个变量是分类变量的散点图。可以与其他图表结
合使用以展示各自的观测结果。分类散点图的特点是其中数据点互不重叠。可以与其他
图表结合使用以展示各自的观测结果。
'''

#%%

#示例

#绘制一个单独的横向小提琴图：

ax = sns.violinplot(x=tips.total_bill)

#根据分类变量分组绘制一个纵向的小提琴图
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',data=tips)

#根据2个分类变量嵌套分组绘制一个小提琴图：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='smoker',data=tips,
                    palette='muted')

#绘制分割的小提琴图以比较不同的色调变量：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='smoker',data=tips,
                    palette='muted',split=True)

#通过显式传入参数指定顺序控制小提琴图的显示顺序：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='time',y='total_bill',
                    order=['Dinner','Lunch'],data=tips)

#将小提琴宽度缩放为每个分箱中观察到的数据点数目：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count')

#将四分位数绘制为水平线而不是迷你箱型图：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count',
                    inner='quartile')

#用小提琴图内部的横线显示每个观察到的数据点：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count',
                    inner='stick')

#根据所有分箱的数据点数目对密度进行缩放：
plt.figure(figsize=(10,5))
plt.subplot(121)
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count',
                    inner='stick',scale_hue=False)
plt.subplot(122)
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count',
                    inner='stick')

#使用窄带宽来减少平滑量：
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,
                    palette='Set2',split=True,scale='count',
                    inner='stick',bw=.2)

#绘制横向小提琴图：
plt.figure()
plt.subplot()
planets = sns.load_dataset('planets')
planets = planets[planets.orbital_period < 1000]
ax = sns.violinplot(x='orbital_period',y='method',data=planets,
                    scale='width',palette='Set2')

#不要让密度超出数据中的极端数值：

plt.figure()
plt.subplot()
ax = sns.violinplot(x='orbital_period',y='method',data=planets,
                    scale='width',palette='Set2',cut=0)

#使用 hue 而不改变小提琴图的位置或宽度
plt.figure()
plt.subplot()
ax = sns.violinplot(x='day',y='total_bill',hue='weekend',
                    data=tips,dodge=False)

'''把 catplot() 与 violinplot() 以及 FacetGrid 结合起来使用。这允许您通过额外
的分类变量进行分组。使用 catplot() 比直接使用 FacetGrid 更为安全，因为它保证
了不同切面上变量同步的顺序：'''


#%%

#seaborn.boxenplot
'''seaborn.boxenplot(x=None, y=None, hue=None, data=None, order=None,
hue_order=None, orient=None, color=None, palette=None, saturation=0.75, 
width=0.8, dodge=True, k_depth='proportion', linewidth=None, 
scale='exponential', outlier_prop=None, ax=None, **kwargs)'''


'''Draw an enhanced box plot for larger datasets.

This style of plot was originally named a “letter value” plot because it 
shows a large number of quantiles that are defined as “letter values”. It 
is similar to a box plot in plotting a nonparametric representation of a 
distribution in which all features correspond to actual observations. 
By plotting more quantiles, it provides more information about the shape of 
the distribution, particularly in the tails. For a more extensive explanation, 
you can read the paper that introduced the plot:

https://vita.had.co.nz/papers/letter-value-plot.html

Input data can be passed in a variety of formats, including:

    Vectors of data represented as lists, numpy arrays, or pandas Series 
    objects passed directly to the x, y, and/or hue parameters.
    A “long-form” DataFrame, in which case the x, y, and hue variables will 
    determine how the data are plotted.
    A “wide-form” DataFrame, such that each numeric column will be plotted.
    An array or list of vectors.

In most cases, it is possible to use numpy or Python objects, but pandas 
objects are preferable because the associated names will be used to annotate 
the axes. Additionally, you can use Categorical types for the grouping 
variables to control the order of plot elements.

This function always treats one of the variables as categorical and draws 
data at ordinal positions (0, 1, … n) on the relevant axis, even when the 
data has a numeric or date type.'''

#%%

'''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as 
    wide-form. Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are 
    inferred from the data objects.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually 
    inferred from the dtype of the input variables, but can be used to specify 
    when the “categorical” variable is a numeric or when plotting wide-form 
    data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    hue levels to matplotlib colors.

saturation：float, optional

    Proportion of the original saturation to draw colors at. Large patches 
    often look better with slightly desaturated colors, but set this to 1 if 
    you want the plot colors to perfectly match the input color spec.

width：float, optional

    Width of a full element when not using hue nesting, or width of all the 
    elements for one level of the major grouping variable.

dodge：bool, optional

    When hue nesting is used, whether elements should be shifted along the 
    categorical axis.

k_depth：“proportion” | “tukey” | “trustworthy”, optional

    The number of boxes, and by extension number of percentiles, to draw. All 
    methods are detailed in Wickham’s paper. Each makes different assumptions 
    about the number of outliers and leverages different statistical properties.

linewidth：float, optional

    Width of the gray lines that frame the plot elements.

scale：“linear” | “exponential” | “area”

    Method to use for the width of the letter value boxes. All give similar 
    results visually. “linear” reduces the width by a constant linear factor, 
    “exponential” uses the proportion of data not covered, “area” is 
    proportional to the percentage of data covered.

outlier_prop：float, optional

    Proportion of data believed to be outliers. Used in conjunction with 
    k_depth to determine the number of percentiles to draw. Defaults to 0.007 
    as a proportion of outliers. Should be in range [0, 1].

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

kwargs：key, value mappings

    Other keyword arguments are passed through to plt.plot and plt.scatter 
    at draw time.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.
'''

#%%

#Examples

#Draw a single horizontal boxen plot:

ax = sns.boxenplot(x=tips.total_bill)

#%%

#Draw a vertical boxen plot grouped by a categorical variable:
plt.figure()
plt.subplot()
ax = sns.boxenplot(x='day',y='total_bill',data=tips)

#Draw a letter value plot with nested grouping by
#two categorical variables:
plt.figure()
plt.subplot()
ax = sns.boxenplot(x='day',y='total_bill',hue='smoker',
                   data=tips,palette='Set3')

#Draw a boxen plot with nested grouping when some bins are empty:
plt.figure()
plt.subplot()
ax = sns.boxenplot(x='day',y='total_bill',hue='time',
                   data=tips,linewidth=2.5)

#Control box order by passing an explicit order:
plt.figure()
plt.subplot()
ax = sns.boxenplot(x='time',y='total_bill',order=['Dinner','Lunch'],
                   data=tips)

#Draw a boxen plot for each numeric variable in a DataFrame:
plt.figure()
plt.subplot()
ax = sns.boxenplot(data=iris,orient='h',palette='Set2')

#Use stripplot() to show the datapoints on top of the boxes:
plt.figure()
plt.subplot()
ax = sns.boxenplot(x='day',y='total_bill',data=tips)
ax = sns.stripplot(x='day',y='total_bill',data=tips,color='grey')

'''Use catplot() to combine boxenplot() and a FacetGrid. This allows 
grouping within additional categorical variables. Using catplot() is 
safer than using FacetGrid directly, as it ensures synchronization of 
variable order across facets:'''

g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',
                data=tips,kind='boxen',height=4,aspect=.7)

#%%

#seaborn.pointplot

'''seaborn.pointplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, estimator=<function mean>, ci=95, n_boot=1000, 
units=None, markers='o', linestyles='-', dodge=False, join=True, 
scale=1, orient=None, color=None, palette=None, errwidth=None, 
capsize=None, ax=None, **kwargs)'''

'''Show point estimates and confidence intervals using scatter plot glyphs.

A point plot represents an estimate of central tendency for a numeric variable 
by the position of scatter plot points and provides some indication of the 
uncertainty around that estimate using error bars.

Point plots can be more useful than bar plots for focusing comparisons between 
different levels of one or more categorical variables. They are particularly 
adept at showing interactions: how the relationship between levels of one 
categorical variable changes across levels of a second categorical variable. 
The lines that join each point from the same hue level allow interactions to 
be judged by differences in slope, which is easier for the eyes than comparing 
the heights of several groups of points or bars.

It is important to keep in mind that a point plot shows only the mean (or 
other estimator) value, but in many cases it may be more informative to show 
the distribution of values at each level of the categorical variables. 
In that case, other approaches such as a box or violin plot may be more 
appropriate.

Input data can be passed in a variety of formats, including:

    Vectors of data represented as lists, numpy arrays, or pandas Series 
    objects passed directly to the x, y, and/or hue parameters.
    A “long-form” DataFrame, in which case the x, y, and hue variables will 
    determine how the data are plotted.
    A “wide-form” DataFrame, such that each numeric column will be plotted.
    An array or list of vectors.

In most cases, it is possible to use numpy or Python objects, but pandas 
objects are preferable because the associated names will be used to annotate 
the axes. Additionally, you can use Categorical types for the grouping 
variables to control the order of plot elements.

This function always treats one of the variables as categorical and draws data 
at ordinal positions (0, 1, … n) on the relevant axis, even when the data has 
a numeric or date type.'''

#%%

'''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as 
    wide-form. Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are inferred 
    from the data objects.

estimator：callable that maps vector -> scalar, optional

    Statistical function to estimate within each categorical bin.

ci：float or “sd” or None, optional

    Size of confidence intervals to draw around estimated values. If “sd”, 
    skip bootstrapping and draw the standard deviation of the observations. 
    If None, no bootstrapping will be performed, and error bars will not be 
    drawn.

n_boot：int, optional

    Number of bootstrap iterations to use when computing confidence intervals.

units：name of variable in data or vector data, optional

    Identifier of sampling units, which will be used to perform a multilevel 
    bootstrap and account for repeated measures design.

markers：string or list of strings, optional

    Markers to use for each of the hue levels.

linestyles：string or list of strings, optional

    Line styles to use for each of the hue levels.

dodge：bool or float, optional

    Amount to separate the points for each level of the hue variable along the 
    categorical axis.

join：bool, optional

    If True, lines will be drawn between point estimates at the same hue level.

scale：float, optional

    Scale factor for the plot elements.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually inferred 
    from the dtype of the input variables, but can be used to specify when the 
    “categorical” variable is a numeric or when plotting wide-form data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

errwidth：float, optional

    Thickness of error bar lines (and caps).

capsize：float, optional

    Width of the “caps” on error bars.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.
'''

#%%

#Examples
#Draw a set of vertical point plots grouped by a categorical variable:
ax = sns.pointplot(x='time',y='total_bill',data=tips)

#Draw a set of vertical points with nested grouping by a two variables:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='total_bill',hue='smoker',data=tips)

#Separate the points for different hue levels along the categorical axis:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='total_bill',hue='smoker',
                   data=tips,dodge=True)

#Use a different marker and line style for the hue levels:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='total_bill',hue='smoker',
                   markers=['o','x'],linestyles=['-','--'],
                   data=tips,dodge=True)


#Draw a set of horizontal points:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='tip',y='day',data=tips)

#Don’t draw a line connecting each point:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='tip',y='day',data=tips,join=False)

#Use a different color for a single-layer plot:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='total_bill',color='#bb3f3f',data=tips)

#Use a different color palette for the points:

#%%

plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='total_bill',hue='smoker',
                   palette='Set2',data=tips,join=True)

#Control point order by passing an explicit order:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='time',y='tip',data=tips,
                   order=['Dinner','Lunch'])

#Use median as the estimate of central tendency:
plt.figure()
plt.subplot()
ax = sns.pointplot(x='day',y='tip',data=tips,estimator=np.median)

#Show the standard error of the mean with the error bars:
plt.figure()
plt.subplot()
ax = sns.pointplot(x="day", y="tip", data=tips, ci=68)

#Show standard deviation of observations instead of a confidence interval:
plt.figure()
plt.subplot()
ax = sns.pointplot(x="day", y="tip", data=tips, ci='sd')

#Add “caps” to the error bars:
plt.figure()
plt.subplot()
ax = sns.pointplot(x="day", y="tip", data=tips,capsize=.2)


'''Use catplot() to combine a barplot() and a FacetGrid. This allows grouping 
within additional categorical variables. Using catplot() is safer than using 
FacetGrid directly, as it ensures synchronization of variable order across 
facets:'''

g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',data=tips,
                kind='point',dodge=True,
                height=4,aspect=.7)

#%%

#seaborn.barplot
'''seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, 
hue_order=None, estimator=<function mean>, ci=95, n_boot=1000, 
units=None, orient=None, color=None, palette=None, saturation=0.75, 
errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)'''

'''Show point estimates and confidence intervals as rectangular bars.

A bar plot represents an estimate of central tendency for a numeric variable 
with the height of each rectangle and provides some indication of the 
uncertainty around that estimate using error bars. Bar plots include 0 in the 
quantitative axis range, and they are a good choice when 0 is a meaningful 
value for the quantitative variable, and you want to make comparisons against 
it.

For datasets where 0 is not a meaningful value, a point plot will allow you to 
focus on differences between levels of one or more categorical variables.

It is also important to keep in mind that a bar plot shows only the mean 
(or other estimator) value, but in many cases it may be more informative to 
show the distribution of values at each level of the categorical variables. 
In that case, other approaches such as a box or violin plot may be more 
appropriate.

Input data can be passed in a variety of formats, including:

    Vectors of data represented as lists, numpy arrays, or pandas Series 
    objects passed directly to the x, y, and/or hue parameters.
    A “long-form” DataFrame, in which case the x, y, and hue variables will 
    determine how the data are plotted.
    A “wide-form” DataFrame, such that each numeric column will be plotted.
    An array or list of vectors.

In most cases, it is possible to use numpy or Python objects, but pandas 
objects are preferable because the associated names will be used to annotate 
the axes. Additionally, you can use Categorical types for the grouping 
variables to control the order of plot elements.

This function always treats one of the variables as categorical and draws data 
at ordinal positions (0, 1, … n) on the relevant axis, even when the data has 
a numeric or date type.'''

#%%

'''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as 
    wide-form. Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are inferred 
    from the data objects.

estimator：callable that maps vector -> scalar, optional

    Statistical function to estimate within each categorical bin.

ci：float or “sd” or None, optional

    Size of confidence intervals to draw around estimated values. If “sd”, 
    skip bootstrapping and draw the standard deviation of the observations. 
    If None, no bootstrapping will be performed, and error bars will not be 
    drawn.

n_boot：int, optional

    Number of bootstrap iterations to use when computing confidence intervals.

units：name of variable in data or vector data, optional

    Identifier of sampling units, which will be used to perform a multilevel 
    bootstrap and account for repeated measures design.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually inferred 
    from the dtype of the input variables, but can be used to specify when the 
    “categorical” variable is a numeric or when plotting wide-form data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

saturation：float, optional

    Proportion of the original saturation to draw colors at. Large patches 
    often look better with slightly desaturated colors, but set this to 1 if 
    you want the plot colors to perfectly match the input color spec.

errcolor：matplotlib color

    Color for the lines that represent the confidence interval.

errwidth：float, optional

    Thickness of error bar lines (and caps).

capsize：float, optional

    Width of the “caps” on error bars.

dodge：bool, optional

    When hue nesting is used, whether elements should be shifted along the 
    categorical axis.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

kwargs：key, value mappings

    Other keyword arguments are passed through to plt.bar at draw time.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.

See also

Show the counts of observations in each categorical bin.Show point estimates 
and confidence intervals using scatterplot glyphs.Combine a categorical plot 
with a class:FacetGrid.'''

#%%

#Examples

#Draw a set of vertical bar plots grouped by a categorical variable:

sns.set(style='whitegrid')
tips = sns.load_dataset('tips')
ax = sns.barplot(x='day',y='total_bill',data=tips)

#Draw a set of vertical bars with nested grouping by a two variables:
plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',hue='smoker',data=tips)

#Draw a set of horizontal bars:

plt.figure()
plt.subplot()
ax = sns.barplot(x='tip',y='day',data=tips)

#Control bar order by passing an explicit order:
plt.figure()
plt.subplot()
ax = sns.barplot(x='time',y='tip',data=tips,order=['Dinner','Lunch'])

#Use median as the estimate of central tendency:
plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',hue='smoker',
                 data=tips,estimator=np.median)

#Show the standard error of the mean with the error bars:
plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',hue='smoker',
                 data=tips,ci=68)


#Show standard deviation of observations instead of a confidence interval:
plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',hue='smoker',
                 data=tips,ci='sd')

#Add “caps” to the error bars:

plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',hue='smoker',
                 data=tips,ci='sd',capsize=.2)

#Use a different color palette for the bars:
plt.figure()
plt.subplot()
ax = sns.barplot(x='size',y='total_bill',data=tips,palette='Blues_d')

#Use hue without changing bar position or width:
tips['weekend'] = tips['day'].isin(['Sat','Sun'])
plt.figure()
plt.subplot()
ax = sns.barplot(x='day',y='total_bill',data=tips,hue='weekend',dodge=False)

#Plot all bars in a single color:
plt.figure()
plt.subplot()
ax = sns.barplot('size','total_bill',data=tips,
                 color='salmon',saturation=.5)

#Use plt.bar keyword arguments to further change the aesthetic:
plt.figure()
plt.subplot()
ax = sns.barplot('day','total_bill',data=tips,
                 linewidth=1.5,facecolor=(1,1,1,0),
                 errcolor='.2',edgecolor='.2')

'''Use catplot() to combine a barplot() and a FacetGrid. This allows 
grouping within additional categorical variables. Using catplot() is 
safer than using FacetGrid directly, as it ensures synchronization of 
variable order across facets:'''

g = sns.catplot(x='sex',y='total_bill',hue='smoker',col='time',data=tips,
                kind='bar',height=4,aspect=.7)

#%%

#seaborn.countplot

'''seaborn.countplot(x=None, y=None, hue=None, data=None, order=None,
 hue_order=None, orient=None, color=None, palette=None, saturation=0.75, 
 dodge=True, ax=None, **kwargs)'''

'''Show the counts of observations in each categorical bin using bars.

A count plot can be thought of as a histogram across a categorical, instead of 
quantitative, variable. The basic API and options are identical to those for 
barplot(), so you can compare counts across nested variables.

Input data can be passed in a variety of formats, including:

    Vectors of data represented as lists, numpy arrays, or pandas Series 
    objects passed directly to the x, y, and/or hue parameters.
    A “long-form” DataFrame, in which case the x, y, and hue variables will
    determine how the data are plotted.
    A “wide-form” DataFrame, such that each numeric column will be plotted.
    An array or list of vectors.

In most cases, it is possible to use numpy or Python objects, but pandas 
objects are preferable because the associated names will be used to annotate 
the axes. Additionally, you can use Categorical types for the grouping 
variables to control the order of plot elements.

This function always treats one of the variables as categorical and draws data 
at ordinal positions (0, 1, … n) on the relevant axis, even when the data has 
a numeric or date type.'''

#%%

'''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as 
    wide-form. Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are inferred 
    from the data objects.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually inferred 
    from the dtype of the input variables, but can be used to specify when the 
    “categorical” variable is a numeric or when plotting wide-form data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable.
    Should be something that can be interpreted by color_palette(), 
    or a dictionary mapping hue levels to matplotlib colors.

saturation：float, optional

    Proportion of the original saturation to draw colors at. Large patches 
    often look better with slightly desaturated colors, but set this to 1 
    if you want the plot colors to perfectly match the input color spec.

dodge：bool, optional

    When hue nesting is used, whether elements should be shifted along the 
    categorical axis.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

kwargs：key, value mappings




    Other keyword arguments are passed to plt.bar.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.

See also

Show point estimates and confidence intervals using bars.Combine a categorical 
plot with a class:FacetGrid.

Examples

Show value counts for a single categorical variable:'''

#%%

''''参数：x, y, hue：names of variables in data or vector data, optional

    Inputs for plotting long-form data. See examples for interpretation.

data：DataFrame, array, or list of arrays, optional

    Dataset for plotting. If x and y are absent, this is interpreted as wide-form. 
            Otherwise it is expected to be long-form.

order, hue_order：lists of strings, optional

    Order to plot the categorical levels in, otherwise the levels are inferred 
    from the data objects.

orient：“v” | “h”, optional

    Orientation of the plot (vertical or horizontal). This is usually i
    nferred from the dtype of the input variables, but can be used to 
    specify when the “categorical” variable is a numeric or when plotting 
    wide-form data.

color：matplotlib color, optional

    Color for all of the elements, or seed for a gradient palette.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

saturation：float, optional

    Proportion of the original saturation to draw colors at. Large patches 
    often look better with slightly desaturated colors, but set this to 1 
    if you want the plot colors to perfectly match the input color spec.

dodge：bool, optional

    When hue nesting is used, whether elements should be shifted along the 
    categorical axis.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

kwargs：key, value mappings

    Other keyword arguments are passed to plt.bar.

返回值：ax：matplotlib Axes

    Returns the Axes object with the plot drawn onto it.

See also

Show point estimates and confidence intervals using bars.Combine a categorical 
plot with a class:FacetGrid.'''

#%%

#Examples
#Show value counts for a single categorical variable:

titanic = sns.load_dataset('titanic')
ax = sns.countplot(x='class',data=titanic)

#Show value counts for two categorical variables:
plt.figure()
plt.subplot()
ax = sns.countplot(x='class',hue='who',data=titanic)

#Plot the bars horizontally:
plt.figure()
plt.subplot()
ax = sns.countplot(y='class',hue='who',data=titanic)

#Use a different color palette:
plt.figure()
plt.subplot()
ax = sns.countplot(x='who',data=titanic,palette='Set3')

#Use plt.bar keyword arguments for a different look:
plt.figure()
plt.subplot()
ax = sns.countplot(x='who',data=titanic,
                   facecolor=(0,0,0,0),linewidth=2.5,
                   edgecolor = sns.color_palette('dark',3))

'''Use catplot() to combine a countplot() and a FacetGrid. This allows grouping
 within additional categorical variables. Using catplot() is safer than using 
 FacetGrid directly, as it ensures synchronization of variable 
 order across facets:'''

g = sns.catplot(x='class',hue='who',col='survived',data=titanic,
                kind='count',height=4,aspect=.7)

#%%

#seaborn.jointplot

'''seaborn.jointplot(x, y, data=None, kind='scatter', stat_func=None, 
color=None, height=6, ratio=5, space=0.2, dropna=True, xlim=None, 
ylim=None, joint_kws=None, marginal_kws=None, annot_kws=None, **kwargs)'''

'''Draw a plot of two variables with bivariate and univariate graphs.

This function provides a convenient interface to the JointGrid class, 
with several canned plot kinds. This is intended to be a fairly lightweight 
wrapper; if you need more flexibility, you should use JointGrid directly.'''

#%%

'''参数：x, y：strings or vectors

    Data or names of variables in data.

data：DataFrame, optional

    DataFrame when x and y are variable names.

kind：{ “scatter” | “reg” | “resid” | “kde” | “hex” }, optional

    Kind of plot to draw.

stat_func：callable or None, optional

    Deprecated

color：matplotlib color, optional

    Color used for the plot elements.

height：numeric, optional

    Size of the figure (it will be square).

ratio：numeric, optional

    Ratio of joint axes height to marginal axes height.

space：numeric, optional

    Space between the joint and marginal axes

dropna：bool, optional

    If True, remove observations that are missing from x and y.

{x, y}lim：two-tuples, optional

    Axis limits to set before plotting.

{joint, marginal, annot}_kws：dicts, optional

    Additional keyword arguments for the plot components.

kwargs：key, value pairings

    Additional keyword arguments are passed to the function used to draw the 
    plot on the joint Axes, superseding items in the joint_kws dictionary.

返回值：grid：JointGrid

    JointGrid object with the plot on it.
'''

#%%

#Examples

#Draw a scatterplot with marginal histograms:
g = sns.jointplot(x='total_bill',y='tip',data=tips)

#Add regression and kernel density fits:
g = sns.jointplot('total_bill','tip',data=tips,kind='reg')

#Replace the scatterplot with a joint histogram using hexagonal bins:
g = sns.jointplot('total_bill','tip',data=tips,kind='hex')

#Replace the scatterplots and histograms with density estimates and align the
#marginal Axes tightly with the joint Axes:
iris = sns.load_dataset('iris')
g = sns.jointplot('sepal_width','sepal_length',data=iris,
                  kind='kde',space=0,color='g')

#Draw a scatterplot, then add a joint density estimate:
g = (sns.jointplot('sepal_width','sepal_length',data=iris,color='k')
     .plot_joint(sns.kdeplot,zorder=0,n_levels=6))

#Pass vectors in directly without using Pandas, then name the axes:
x,y = np.random.randn(2,300)
g = (sns.jointplot(x,y,kind='hex')
     .set_axis_labels('x','y'))


#Draw a smaller figure with more space devoted to the marginal plots
g = sns.jointplot('total_bill','tip',data=tips,
                  height=5,ratio=3,color='g')

#Pass keyword arguments down to the underlying plots:

g = sns.jointplot('petal_length','sepal_length',data=iris,
                  marginal_kws=dict(bins=15,rug=True),
                  annot_kws=dict(stat='r'),s=40,edgecolor='w',linewidth=1)

#%%

#seaborn.pairplot

'''seaborn.pairplot(data, hue=None, hue_order=None, palette=None, 
vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', 
markers=None, height=2.5, aspect=1, dropna=True, plot_kws=None, 
diag_kws=None, grid_kws=None, size=None)'''

'''Plot pairwise relationships in a dataset.

By default, this function will create a grid of Axes such that each variable 
in data will by shared in the y-axis across a single row and in the x-axis 
across a single column. The diagonal Axes are treated differently, drawing a 
plot to show the univariate distribution of the data for the variable in that 
column.

It is also possible to show a subset of variables or plot different variables 
on the rows and columns.

This is a high-level interface for PairGrid that is intended to make it easy 
to draw a few common styles. You should use PairGrid directly if you need more 
flexibility.'''

#%%

'''参数：data：DataFrame

    Tidy (long-form) dataframe where each column is a variable and each row is 
    an observation.

hue：string (variable name), optional

    Variable in data to map plot aspects to different colors.

hue_order：list of strings

    Order for the levels of the hue variable in the palette

palette：dict or seaborn color palette

    Set of colors for mapping the hue variable. If a dict, keys should be 
    values in the hue variable.

vars：list of variable names, optional

    Variables within data to use, otherwise use every column with a numeric 
    datatype.

{x, y}_vars：lists of variable names, optional

    Variables within data to use separately for the rows and columns of the 
    figure; i.e. to make a non-square plot.

kind：{‘scatter’, ‘reg’}, optional

    Kind of plot for the non-identity relationships.

diag_kind：{‘auto’, ‘hist’, ‘kde’}, optional

    Kind of plot for the diagonal subplots. The default depends on whether 
    "hue" is used or not.

markers：single matplotlib marker code or list, optional

    Either the marker to use for all datapoints or a list of markers with a 
    length the same as the number of levels in the hue variable so that 
    differently colored points will also have different scatterplot markers.

height：scalar, optional

    Height (in inches) of each facet.

aspect：scalar, optional

    Aspect * height gives the width (in inches) of each facet.

dropna：boolean, optional

    Drop missing values from the data before plotting.

{plot, diag, grid}_kws：dicts, optional

    Dictionaries of keyword arguments.

返回值：grid：PairGrid

    Returns the underlying PairGrid instance for further tweaking.
    
See also

Subplot grid for more flexible plotting of pairwise relationships.
'''

#%%

#Examples

#Draw scatterplots for joint relationships and histograms for
#univariate distributions:

g = sns.pairplot(iris)

#Show different levels of a categorical variable by the color of plot elements:

g = sns.pairplot(iris,hue='species')

#Use a different color palette:

g = sns.pairplot(iris,hue='species',palette='husl')

#Use different markers for each level of the hue variable:
g = sns.pairplot(iris,hue='species',markers=['o','s','d'])

#Plot a subset of variables:
g = sns.pairplot(iris,vars=['sepal_width','sepal_length'])

#Draw larger plots:
g = sns.pairplot(iris,vars=['sepal_width','sepal_length'],height=3)

#Plot different variables in the rows and columns:

g = sns.pairplot(iris,
                 x_vars=['sepal_width','sepal_length'],
                 y_vars=['petal_width','petal_length'])

#Use kernel density estimates for univariate plots:
g = sns.pairplot(iris, diag_kind="kde")

#Fit linear regression models to the scatter plots:
g = sns.pairplot(iris, kind="reg")

#Pass keyword arguments down to the underlying functions
# (it may be easier to use PairGrid directly):
g = sns.pairplot(iris,diag_kind='kde',markers='+',
                 plot_kws=dict(s=50,edgecolor='b',linewidth=1),
                 diag_kws=dict(shade=True))

#%%

#seaborn.distplot
'''seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, 
hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, 
vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)'''

'''灵活绘制单变量观测值分布图。

该函数结合了matplotlib中的 hist函数（自动计算一个默认的合适的bin大小）、
seaborn的kdeplot()和rugplot()函数。它还可以拟合scipy.stats分布并在数据上绘制
估计的PDF（概率分布函数）'''

#%%

'''a：Series、1维数组或者列表。

    观察数据。如果是具有name属性的Series对象，则该名称将用于标记数据轴。

bins：matplotlib hist()的参数，或None。可选参数。

    直方图bins（柱）的数目，若填None，则默认使用Freedman-Diaconis规则指定柱
    的数目。

hist：布尔值，可选参数。

    是否绘制（标准化）直方图。

kde：布尔值，可选参数。

    是否绘制高斯核密度估计图。

rug：布尔值，可选参数。

    是否在横轴上绘制观测值竖线。

fit：随机变量对象，可选参数。

    一个带有fit方法的对象，返回一个元组，该元组可以传递给pdf方法一个位置参数，
    该位置参数遵循一个值的网格用于评估pdf。

{hist, kde, rug, fit}_kws：字典，可选参数。

    底层绘图函数的关键字参数。

color：matplotlib color，可选参数。

    可以绘制除了拟合曲线之外所有内容的颜色。

vertical：布尔值，可选参数。

    如果为True，则观测值在y轴显示。

norm_hist：布尔值，可选参数。

    如果为True，则直方图的高度显示密度而不是计数。如果绘制KDE图或拟合密度，
    则默认为True。

axlabel：字符串，False或者None，可选参数。

    横轴的名称。如果为None，将尝试从a.name获取它；如果为False，则不设置标签。

label：字符串，可选参数。

    图形相关组成部分的图例标签。

ax：matplotlib axis，可选参数。

    若提供该参数，则在参数设定的轴上绘图。

返回值：ax：matplotlib Axes

    返回Axes对象以及用于进一步调整的绘图。

另请参见

kdeplot

显示具有核密度估计图的单变量或双变量分布。

rugplot

绘制小的垂直线以显示分布中的每个观测值。'''

#%%

#范例

#显示具有核密度估计的默认图和使用参考规则自动确定bin大小的直方图：

np.random.seed(0)
x = np.random.randn(100)
ax = sns.distplot(x)

#使用Pandas对象获取信息轴标签：
x = pd.Series(x,name='x variable')
plt.figure()
plt.subplot()
ax = sns.distplot(x)

#使用核密度估计和小的垂直线绘制分布图：
plt.figure()
plt.subplot()
ax = sns.distplot(x,rug=True,hist=False)

#用直方图和最大似然高斯分布拟合绘制分布图：
from scipy.stats import norm
plt.figure()
plt.subplot()
ax = sns.distplot(x,fit=norm,kde=False)

#在垂直轴上绘制分布图：
plt.figure()
plt.subplot()
ax = sns.distplot(x,vertical=True)

#更改所有绘图元素的颜色：
plt.figure()
plt.subplot()
ax = sns.distplot(x,color='y')

#将特定参数传递给基础绘图函数：
plt.figure()
plt.subplot()
ax = sns.distplot(x,rug=True,rug_kws=dict(color='g'),
                  kde_kws=dict(color='k',lw=3,label='KDE'),
                  hist_kws=dict(histtype='step',linewidth=3,alpha=1,
                                color='g'))

#%%

#seaborn.kdeplot
'''seaborn.kdeplot(data, data2=None, shade=False, vertical=False, kernel='gau',
 bw='scott', gridsize=100, cut=3, clip=None, legend=True, cumulative=False, 
 shade_lowest=True, cbar=False, cbar_ax=None, cbar_kws=None, ax=None, **kwargs)'''

#拟合并绘制单变量或双变量核密度估计图。

#%%

'''参数：data：一维阵列

    输入数据

**data2：一维阵列，可选。

    第二输入数据。如果存在，将估计双变量KDE。

shade：布尔值，可选参数。

    如果为True，则在KDE曲线下方的区域中增加阴影（或者在数据为双变量时使用填充的
    轮廓绘制）。

vertical：布尔值，可选参数。

    如果为True，密度图将显示在x轴。

kernel：{‘gau’ | ‘cos’ | ‘biw’ | ‘epa’ | ‘tri’ | ‘triw’ }，可选参数

    要拟合的核的形状代码，双变量KDE只能使用高斯核。

bw：{‘scott’ | ‘silverman’ | scalar | pair of scalars }，可选参数

    用于确定双变量图的每个维的核大小、标量因子或标量的参考方法的名称。需要注
    意的是底层的计算库对此参数有不同的交互：statsmodels直接使用它，而scipy将其
    视为数据标准差的缩放因子。

gridsize：整型数据，可选参数。

    评估网格中的离散点数。

cut：标量，可选参数。

    绘制估计值以从极端数据点切割* bw。

clip：一对标量，可选参数。

    用于拟合KDE图的数据点的上下限值。可以为双变量图提供一对（上，下）边界。

legend：布尔值，可选参数。

    如果为True，为绘制的图像添加图例或者标记坐标轴。

cumulative：布尔值，可选参数。

    如果为True，则绘制kde估计图的累积分布。

shade_lowest：布尔值，可选参数。

    如果为True，则屏蔽双变量KDE图的最低轮廓。绘制单变量图或“shade = False”时
    无影响。当你想要在同一轴上绘制多个密度时，可将此参数设置为“False”。

cbar：布尔值，可选参数。

    如果为True并绘制双变量KDE图，为绘制的图像添加颜色条。

cbar_ax：matplotlib axes，可选参数。

    用于绘制颜色条的坐标轴，若为空，就在主轴绘制颜色条。

cbar_kws：字典，可选参数。

    fig.colorbar（）的关键字参数。

ax：matplotlib axes，可选参数。

    要绘图的坐标轴，若为空，则使用当前轴。

kwargs：键值对

    其他传递给plt.plot（）或plt.contour {f}的关键字参数，具体取决于是绘制单变
    量还是双变量图。

返回值：ax：matplotlib Axes

    绘图的坐标轴。

另请参见

distplot

灵活绘制单变量观测值分布图。

jointplot

绘制一个具有双变量和边缘分布的联合数据集。'''

#%%

#范例

#绘制一个简单的单变量分布：

mean,cov = [0,2],[(1,5),(.5,1)]
x,y = np.random.multivariate_normal(mean,cov,size=50).T
ax = sns.kdeplot(x)


#在密度曲线下使用不同的颜色着色：
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,shade=True,color='r')

#绘制一个双变量分布
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,y)

#使用填充轮廓：
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,y,shade=True)

#使用更多的轮廓级别和不同的调色板：
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,y,n_levels=30,cmap='Purples_d')

#使用窄带宽：
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,bw=.15)

#在纵轴上绘制密度分布：
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,vertical=True)

#将密度曲线限制在数据范围内:
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,cut=0)

#为轮廓添加一个颜色条:
plt.figure()
plt.subplot()
ax = sns.kdeplot(x,y,cbar=True)

#为双变量密度图绘制两个阴影
iris = sns.load_dataset('iris')
setosa = iris.loc[iris.species=='setosa']
virginica = iris.loc[iris.species=='virginica']
plt.figure()
plt.subplot()
ax = sns.kdeplot(setosa.sepal_width,setosa.sepal_length,cmap='Reds',
                 shade=True,shade_lowest=False)
ax = sns.kdeplot(virginica.sepal_width,virginica.sepal_length,cmap='Blues',
                 shade=True,shade_lowest=False)

#%%

#seaborn.rugplot

#seaborn.rugplot(a, height=0.05, axis='x', ax=None, **kwargs)

'''a：vector

    1D array of observations.

height：scalar, optional

    Height of ticks as proportion of the axis.

axis：{‘x’ | ‘y’}, optional

    Axis to draw rugplot on.

ax：matplotlib axes, optional

    Axes to draw plot into; otherwise grabs current axes.

kwargs：key, value pairings

    Other keyword arguments are passed to LineCollection.

返回值：ax：matplotlib axes'''


#%%

#seaborn.lmplot
'''seaborn.lmplot(x, y, data, hue=None, col=None, row=None, palette=None, 
col_wrap=None, height=5, aspect=1, markers='o', sharex=True, sharey=True, 
hue_order=None, col_order=None, row_order=None, legend=True, legend_out=True, 
x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, 
n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False, 
logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, 
y_jitter=None, scatter_kws=None, line_kws=None, size=None)'''

'''Plot data and regression model fits across a FacetGrid.

This function combines regplot() and FacetGrid. It is intended as a convenient 
interface to fit regression models across conditional subsets of a dataset.

When thinking about how to assign variables to different facets, a general 
rule is that it makes sense to use hue for the most important comparison, 
followed by col and row. However, always think about your particular dataset 
and the goals of the visualization you are creating.

There are a number of mutually exclusive options for estimating the regression 
model. See the tutorial for more information.

The parameters to this function span most of the options in FacetGrid, 
although there may be occasional cases where you will want to use that class 
and regplot() directly.'''

#%%

'''参数：x, y：strings, optional

    Input variables; these should be column names in data.

data：DataFrame

    Tidy (“long-form”) dataframe where each column is a variable and each row 
    is an observation.

hue, col, row：strings

    Variables that define subsets of the data, which will be drawn on separate 
    facets in the grid. See the *_order parameters to control the order of 
    levels of this variable.

palette：palette name, list, or dict, optional

    Colors to use for the different levels of the hue variable. Should be 
    something that can be interpreted by color_palette(), or a dictionary 
    mapping hue levels to matplotlib colors.

col_wrap：int, optional

    “Wrap” the column variable at this width, so that the column facets span 
    multiple rows. Incompatible with a row facet.

height：scalar, optional

    Height (in inches) of each facet. See also: aspect.

aspect：scalar, optional

    Aspect ratio of each facet, so that aspect * height gives the width of 
    each facet in inches.

markers：matplotlib marker code or list of marker codes, optional

    Markers for the scatterplot. If a list, each marker in the list will be 
    used for each level of the hue variable.

share{x,y}：bool, ‘col’, or ‘row’ optional

    If true, the facets will share y axes across columns and/or x axes 
    across rows.

{hue,col,row}_order：lists, optional

    Order for the levels of the faceting variables. By default, this will be 
    the order that the levels appear in data or, if the variables are pandas 
    categoricals, the category order.

legend：bool, optional

    If True and there is a hue variable, add a legend.

legend_out：bool, optional

    If True, the figure size will be extended, and the legend will be drawn 
    outside the plot on the center right.

x_estimator：callable that maps vector -> scalar, optional

    Apply this function to each unique value of x and plot the resulting 
    estimate. This is useful when x is a discrete variable. If x_ci is given, 
    this estimate will be bootstrapped and a confidence interval will be drawn.

x_bins：int or vector, optional

    Bin the x variable into discrete bins and then estimate the central 
    tendency and a confidence interval. This binning only influences how the 
    scatterplot is drawn; the regression is still fit to the original data. 
    This parameter is interpreted either as the number of evenly-sized 
    (not necessary spaced) bins or the positions of the bin centers. When 
    this parameter is used, it implies that the default of x_estimator is 
    numpy.mean.

x_ci：“ci”, “sd”, int in [0, 100] or None, optional

    Size of the confidence interval used when plotting a central tendency for 
    discrete values of x. If "ci", defer to the value of the ci parameter. 
    If "sd", skip bootstrapping and show the standard deviation of the 
    observations in each bin.

scatter：bool, optional

    If True, draw a scatterplot with the underlying observations 
    (or the x_estimator values).

fit_reg：bool, optional

    If True, estimate and plot a regression model relating the x and y 
    variables.

ci：int in [0, 100] or None, optional

    Size of the confidence interval for the regression estimate. This will be 
    drawn using translucent bands around the regression line. The confidence 
    interval is estimated using a bootstrap; for large datasets, it may be 
    advisable to avoid that computation by setting this parameter to None.

n_boot：int, optional

    Number of bootstrap resamples used to estimate the ci. The default value 
    attempts to balance time and stability; you may want to increase this value 
    for “final” versions of plots.

units：variable name in data, optional

    If the x and y observations are nested within sampling units, those can be 
    specified here. This will be taken into account when computing the 
    confidence intervals by performing a multilevel bootstrap that resamples 
    both units and observations (within unit). This does not otherwise 
    influence how the regression is estimated or drawn.

order：int, optional

    If order is greater than 1, use numpy.polyfit to estimate a polynomial 
    regression.

logistic：bool, optional

    If True, assume that y is a binary variable and use statsmodels to estimate 
    a logistic regression model. Note that this is substantially more 
    computationally intensive than linear regression, so you may wish to 
    decrease the number of bootstrap resamples (n_boot) or set ci to None.

lowess：bool, optional

    If True, use statsmodels to estimate a nonparametric lowess model (locally 
    weighted linear regression). Note that confidence intervals cannot 
    currently be drawn for this kind of model.

robust：bool, optional

    If True, use statsmodels to estimate a robust regression. This will 
    de-weight outliers. Note that this is substantially more computationally 
    intensive than standard linear regression, so you may wish to decrease the 
    number of bootstrap resamples (n_boot) or set ci to None.

logx：bool, optional

    If True, estimate a linear regression of the form y ~ log(x), but plot the 
    scatterplot and regression model in the input space. Note that x must be 
    positive for this to work.

{x,y}_partial：strings in data or matrices

    Confounding variables to regress out of the x or y variables before 
    plotting.

truncate：bool, optional

    By default, the regression line is drawn to fill the x axis limits after 
    the scatterplot is drawn. If truncate is True, it will instead by bounded 
    by the data limits.

{x,y}_jitter：floats, optional

    Add uniform random noise of this size to either the x or y variables. 
    The noise is added to a copy of the data after fitting the regression, 
    and only influences the look of the scatterplot. This can be helpful when 
    plotting variables that take discrete values.

{scatter,line}_kws：dictionaries

    Additional keyword arguments to pass to plt.scatter and plt.plot.

See also

Plot data and a conditional model fit.Subplot grid for plotting conditional 
relationships.Combine regplot() and PairGrid (when used with kind="reg").

Notes

The regplot() and lmplot() functions are closely related, but the former is an 
axes-level function while the latter is a figure-level function that combines 
regplot() and FacetGrid.'''

#%%

#Examples
'''These examples focus on basic regression model plots to exhibit the various 
faceting options; see the regplot() docs for demonstrations of the other 
options for plotting the data and models. There are also other examples for 
how to manipulate plot using the returned object on the FacetGrid docs.'''

#Plot a simple linear relationship between two variables:
sns.set(color_codes=True)
tips = sns.load_dataset('tips')
g = sns.lmplot(x='total_bill',y='tip',data=tips)

#Condition on a third variable and plot the levels in different colors:
g = sns.lmplot(x='total_bill',y='tip',data=tips,hue='smoker')

#Use different markers as well as colors so the plot will reproduce to
#black-and-white more easily:
g = sns.lmplot(x='total_bill',y='tip',data=tips,
               hue='smoker',markers=['s','d'])

#Use a different color palette:
g = sns.lmplot(x='total_bill',y='tip',data=tips,
               hue='smoker',palette='Set1')

#Map hue levels to colors with a dictionary:
g = sns.lmplot(x='total_bill',y='tip',data=tips,
               hue='smoker',palette=dict(Yes='g',No='m'))

#Plot the levels of the third variable across different columns:
g = sns.lmplot(x='total_bill',y='tip',data=tips,
               col='smoker')

#Change the height and aspect ratio of the facets:
g = sns.lmplot(x='size',y='total_bill',hue='day',col='day',
               data=tips,height=6,aspect=.4,x_jitter=.1)

#Wrap the levels of the column variable into multiple rows:

g = sns.lmplot(x='total_bill',y='tip',col='day',hue='day',
               data=tips,col_wrap=2,height=3)

#Condition on two variables to make a full grid:
g = sns.lmplot(x='total_bill',y='tip',row='sex',col='time',
               data=tips,height=3)

#Use methods on the returned FacetGrid instance to further tweak the plot:
g = sns.lmplot(x='total_bill',y='tip',row='sex',col='time',
               data=tips,height=3)
g = (g.set_axis_labels('Total bill(US Dollars)','Tip')
     .set(xlim=(0,60),ylim=(0,12),
          xticks=[10,30,50],yticks=[2,6,10])
     .fig.subplots_adjust(wspace=.02))


#%%

#seaborn.regplot
'''seaborn.regplot(x, y, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, 
logistic=False, lowess=False, robust=False, logx=False, x_partial=None, 
y_partial=None, truncate=False, dropna=True, x_jitter=None, y_jitter=None, 
label=None, color=None, marker='o', scatter_kws=None, line_kws=None, ax=None)'''

'''Plot data and a linear regression model fit.

There are a number of mutually exclusive options for estimating the regression 
model. See the tutorial for more information.'''

#%%

'''x, y：string, series, or vector array

    Input variables. If strings, these should correspond with column names in 
    data. When pandas objects are used, axes will be labeled with the series 
    name.

data：DataFrame

    Tidy (“long-form”) dataframe where each column is a variable and each row
    is an observation.

x_estimator：callable that maps vector -> scalar, optional

    Apply this function to each unique value of x and plot the resulting 
    estimate. This is useful when x is a discrete variable. If x_ci is given, 
    this estimate will be bootstrapped and a confidence interval will be drawn.

x_bins：int or vector, optional

    Bin the x variable into discrete bins and then estimate the central 
    tendency and a confidence interval. This binning only influences how the 
    scatterplot is drawn; the regression is still fit to the original data. 
    This parameter is interpreted either as the number of evenly-sized 
    (not necessary spaced) bins or the positions of the bin centers. When 
    this parameter is used, it implies that the default of x_estimator is 
    numpy.mean.

x_ci：“ci”, “sd”, int in [0, 100] or None, optional

    Size of the confidence interval used when plotting a central tendency for 
    discrete values of x. If "ci", defer to the value of the ci parameter. 
    If "sd", skip bootstrapping and show the standard deviation of the 
    observations in each bin.

scatter：bool, optional

    If True, draw a scatterplot with the underlying observations 
    (or the x_estimator values).

fit_reg：bool, optional

    If True, estimate and plot a regression model relating the x and y variables.

ci：int in [0, 100] or None, optional

    Size of the confidence interval for the regression estimate. This will be 
    drawn using translucent bands around the regression line. The confidence 
    interval is estimated using a bootstrap; for large datasets, it may be 
    advisable to avoid that computation by setting this parameter to None.

n_boot：int, optional

    Number of bootstrap resamples used to estimate the ci. The default value 
    attempts to balance time and stability; you may want to increase this value 
    for “final” versions of plots.

units：variable name in data, optional

    If the x and y observations are nested within sampling units, those can be 
    specified here. This will be taken into account when computing the 
    confidence intervals by performing a multilevel bootstrap that resamples 
    both units and observations (within unit). This does not otherwise 
    influence how the regression is estimated or drawn.

order：int, optional

    If order is greater than 1, use numpy.polyfit to estimate a polynomial 
    regression.

logistic：bool, optional

    If True, assume that y is a binary variable and use statsmodels to estimate 
    a logistic regression model. Note that this is substantially more 
    computationally intensive than linear regression, so you may wish to 
    decrease the number of bootstrap resamples (n_boot) or set ci to None.

lowess：bool, optional

    If True, use statsmodels to estimate a nonparametric lowess model 
    (locally weighted linear regression). Note that confidence intervals cannot 
    currently be drawn for this kind of model.

robust：bool, optional

    If True, use statsmodels to estimate a robust regression. This will 
    de-weight outliers. Note that this is substantially more computationally 
    intensive than standard linear regression, so you may wish to decrease the 
    number of bootstrap resamples (n_boot) or set ci to None.

logx：bool, optional

    If True, estimate a linear regression of the form y ~ log(x), but plot the 
    scatterplot and regression model in the input space. Note that x must be 
    positive for this to work.

{x,y}_partial：strings in data or matrices

    Confounding variables to regress out of the x or y variables before 
    plotting.

truncate：bool, optional

    By default, the regression line is drawn to fill the x axis limits after 
    the scatterplot is drawn. If truncate is True, it will instead by bounded 
    by the data limits.

{x,y}_jitter：floats, optional

    Add uniform random noise of this size to either the x or y variables. 
    The noise is added to a copy of the data after fitting the regression, 
    and only influences the look of the scatterplot. This can be helpful when 
    plotting variables that take discrete values.

label：string

    Label to apply to ether the scatterplot or regression line 
    (if scatter is False) for use in a legend.

color：matplotlib color

    Color to apply to all plot elements; will be superseded by colors passed in 
    scatter_kws or line_kws.

marker：matplotlib marker code

    Marker to use for the scatterplot glyphs.

{scatter,line}_kws：dictionaries

    Additional keyword arguments to pass to plt.scatter and plt.plot.

ax：matplotlib Axes, optional

    Axes object to draw the plot onto, otherwise uses the current Axes.

返回值：ax：matplotlib Axes

    The Axes object containing the plot.

See also

Combine regplot() and FacetGrid to plot multiple linear relationships in a 
dataset.Combine regplot() and JointGrid (when used with kind="reg").Combine 
regplot() and PairGrid (when used with kind="reg").Plot the residuals of a 
linear regression model.

Notes

The regplot() and lmplot() functions are closely related, but the former is an 
axes-level function while the latter is a figure-level function that combines 
regplot() and FacetGrid.

It’s also easy to combine combine regplot() and JointGrid or PairGrid through 
the jointplot() and pairplot() functions, although these do not directly 
accept all of regplot()’s parameters.'''

#%%

#Examples
#Plot the relationship between two variables in a DataFrame:

ax = sns.regplot(x='total_bill',y='tip',data=tips)

#Plot with two variables defined as numpy arrays; use a different color:

np.random.seed(8)
mean,cov=[4,6],[(1.5,7),(.7,1)]
x,y = np.random.multivariate_normal(mean,cov,80).T
plt.figure()
plt.subplot()
ax = sns.regplot(x=x,y=y,color='g')

#Plot with two variables defined as pandas Series; use a different marker:
x,y = pd.Series(x,name='x_var'),pd.Series(y,name='y_var')

plt.figure()
plt.subplot()
ax = sns.regplot(x=x,y=y,marker='+')

#Use a 68% confidence interval, which corresponds with the standard
#error of the estimate:
plt.figure()
plt.subplot()
ax = sns.regplot(x=x,y=y,ci=68)

#Plot with a discrete x variable and add some jitter:
plt.figure()
plt.subplot()
ax = sns.regplot(x='size',y='total_bill',data=tips,x_jitter=.2)

#Plot with a discrete x variable showing means and confidence intervals
#for unique values:
plt.figure()
plt.subplot()
ax = sns.regplot(x='size',y='total_bill',data=tips,
                 x_estimator=np.mean)

#Plot with a continuous variable divided into discrete bins:
plt.figure()
plt.subplot(121)
ax = sns.regplot(x=x,y=y,x_bins=4)
plt.subplot(122)
ax = sns.regplot(x=x,y=y)

#Fit a higher-order polynomial regression and truncate the model prediction:
plt.figure()
plt.subplot()
ans = sns.load_dataset('anscombe')
ax = sns.regplot(x='x',y='y',data=ans.loc[ans.dataset=='II'],
                 scatter_kws=dict(s=80),truncate=True)

#Fit a robust regression and don’t plot a confidence interval:
plt.figure()
plt.subplot()
ax = sns.regplot(x='x',y='y',data=ans.loc[ans.dataset=='III'],
                 scatter_kws={'s':80},
                 robust=True,ci=None)

#Fit a logistic regression; jitter the y variable and use fewer
#bootstrap iterations:
tips['big_tip'] = (tips.tip/tips.total_bill) >.175
plt.figure()
plt.subplot()
ax = sns.regplot(x='total_bill',y='big_tip',data=tips,
                 logistic=True,n_boot=500,y_jitter=.03)

#Fit the regression model using log(x) and truncate the model prediction:
plt.figure()
plt.subplot()
ax = sns.regplot(x='size',y='total_bill',data=tips,
                 x_estimator=np.mean,logx=True,truncate=True)

#%%

#seaborn.residplot
'''seaborn.residplot(x, y, data=None, lowess=False, x_partial=None, 
y_partial=None, order=1, robust=False, dropna=True, label=None, color=None, 
scatter_kws=None, line_kws=None, ax=None)'''

'''Plot the residuals of a linear regression.

This function will regress y on x (possibly as a robust or polynomial 
regression) and then draw a scatterplot of the residuals. 
You can optionally fit a lowess smoother to the residual plot, which can 
help in determining if there is structure to the residuals.'''

#%%

'''参数：x：vector or string

    Data or column name in <cite>data</cite> for the predictor variable.

y：vector or string

    Data or column name in <cite>data</cite> for the response variable.

data：DataFrame, optional

    DataFrame to use if <cite>x</cite> and <cite>y</cite> are column names.

lowess：boolean, optional

    Fit a lowess smoother to the residual scatterplot.

{x, y}_partial：matrix or string(s) , optional

    Matrix with same first dimension as <cite>x</cite>, or column name(s) in 
    <cite>data</cite>. These variables are treated as confounding and are
    removed from the <cite>x</cite> or <cite>y</cite> variables before plotting.

order：int, optional

    Order of the polynomial to fit when calculating the residuals.

robust：boolean, optional

    Fit a robust linear regression when calculating the residuals.

dropna：boolean, optional

    If True, ignore observations with missing data when fitting and plotting.

label：string, optional

    Label that will be used in any plot legends.

color：matplotlib color, optional

    Color to use for all elements of the plot.

{scatter, line}_kws：dictionaries, optional

    Additional keyword arguments passed to scatter() and plot() for drawing 
    the components of the plot.

ax：matplotlib axis, optional

    Plot into this axis, otherwise grab the current axis or make a new one 
    if not existing.
'''

#%%

#seaborn.heatmap

'''seaborn.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, 
robust=False, annot=None, fmt='.2g', annot_kws=None, linewidths=0, 
linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False, 
xticklabels='auto', yticklabels='auto', mask=None, ax=None, **kwargs)'''

'''将矩形数据绘制为颜色编码矩阵。

这是一个坐标轴级的函数，如果没有提供给ax参数，它会将热力图绘制到当前活动的轴中。
除非cbar为False或为cbar_ax提供单独的Axes，否则将使用此轴空间的一部分绘制
颜色图。'''

'''参数：data：矩形数据集

    可以强制转换为ndarray格式数据的2维数据集。如果提供了Pandas DataFrame数据，
    索引/列信息将用于标记列和行。

vmin, vmax：浮点型数据，可选参数。

    用于锚定色彩映射的值，否则它们是从数据和其他关键字参数推断出来的。

cmap：matplotlib 颜色条名称或者对象，或者是颜色列表，可选参数。

    从数据值到颜色空间的映射。 如果没有提供，默认值将取决于是否设置了“center”。

center：浮点数，可选参数。

    绘制有色数据时将色彩映射居中的值。 如果没有指定，则使用此参数将更改默认
    的cmap。

robust：布尔值，可选参数。

    如果是True，并且vmin或vmax为空，则使用稳健分位数而不是极值来计算色彩映射
    范围。

annot:布尔值或者矩形数据，可选参数。

    如果为True，则在每个热力图单元格中写入数据值。 如果数组的形状与data相同，
    则使用它来代替原始数据注释热力图。

fmt：字符串，可选参数。

    添加注释时要使用的字符串格式代码。

annot_kws：字典或者键值对，可选参数。

    当annot为True时，ax.text的关键字参数。

linewidths：浮点数，可选参数。

    划分每个单元格的行的宽度。

linecolor：颜色，可选参数

    划分每个单元的线条的颜色。

cbar：布尔值，可选参数。

    描述是否绘制颜色条。

cbar_kws：字典或者键值对，可选参数。

    fig.colorbar的关键字参数。

cbar_ax：matplotlib Axes，可选参数。

    用于绘制颜色条的轴，否则从主轴获取。

square：布尔值，可选参数。

    如果为True，则将坐标轴方向设置为“equal”，以使每个单元格为方形。

xticklabels, yticklabels：“auto”，布尔值，类列表值，或者整形数值，可选参数。

    如果为True，则绘制数据框的列名称。如果为False，则不绘制列名称。如果是列表，
    则将这些替代标签绘制为xticklabels。如果是整数，则使用列名称，但仅绘制每个n
    标签。如果是“auto”，将尝试密集绘制不重叠的标签。

mask：布尔数组或者DataFrame数据，可选参数。

    如果为空值，数据将不会显示在mask为True的单元格中。 具有缺失值的单元格将自动
    被屏蔽。

ax：matplotlib Axes，可选参数。

    绘制图的坐标轴，否则使用当前活动的坐标轴。

kwargs：其他关键字参数。

    所有其他关键字参数都传递给ax.pcolormesh。

返回值：ax：matplotlib Axes

    热力图的轴对象。
    
另请参见

clustermap

使用分层聚类绘制矩阵以排列行和列。
'''

#%%

#范例

#为numpy数组绘制热力图
uniform_data = np.random.rand(10,12)
ax = sns.heatmap(uniform_data)

#更改默认的colormap范围：
plt.figure()
plt.subplot()
ax = sns.heatmap(uniform_data,vmin=0,vmax=1)

#使用发散色图绘制以0为中心的数据的热力图：
plt.figure()
plt.subplot()
normal_data = np.random.randn(10,12)
ax = sns.heatmap(normal_data,center=0)

#使用特定的行和列标签绘制dataframe：
flights = sns.load_dataset('flights')
flights = flights.pivot('month','year','passengers')
plt.figure()
plt.subplot()
ax = sns.heatmap(flights)

#使用整数格式的数字值注释每个小单元格：
plt.figure()
plt.subplot()
ax = sns.heatmap(flights,annot=True,fmt='d')

#在每个单元格之间添加线：
plt.figure()
plt.subplot()
ax = sns.heatmap(flights,linewidths=.5)

#使用不同的colormap：
plt.figure()
plt.subplot()
ax = sns.heatmap(flights,cmap='YlGnBu')

#将colormap置于特定值的中心：
plt.figure()
plt.subplot()
ax = sns.heatmap(flights,center=flights.loc['January',1955])

#绘制每个其他列标签，而不绘制行标签：
data = np.random.randn(50,20)
plt.figure()
plt.subplot()
ax = sns.heatmap(data,xticklabels=2,yticklabels=False)

#不绘制颜色条：
plt.figure()
plt.subplot()
ax = sns.heatmap(flights,cbar=False)

#在不同的坐标轴方向绘制颜色条：
grid_kws = dict(height_ratios=(.9,.05),hspace=.4)
f,(ax,cbar_ax) = plt.subplots(2,gridspec_kw=grid_kws)
ax = sns.heatmap(flights,ax=ax,cbar_ax=cbar_ax,
                 cbar_kws=dict(orientation='horizontal'))

#使用遮罩绘制矩阵中的一部分
corr = np.corrcoef(np.random.randn(10,200))
mask = np.zeros_like(corr)

mask[np.triu_indices_from(mask)] = True
plt.figure()
plt.subplot()
with sns.axes_style('white'):
    ax = sns.heatmap(corr,mask=mask,vmax=.3,square=True)

#%%

#seaborn.clustermap
'''seaborn.clustermap(data, pivot_kws=None, method='average', 
metric='euclidean', z_score=None, standard_scale=None, figsize=None, 
cbar_kws=None, row_cluster=True, col_cluster=True, row_linkage=None, 
col_linkage=None, row_colors=None, col_colors=None, mask=None, **kwargs)'''

#Plot a matrix dataset as a hierarchically-clustered heatmap.

#%%

'''参数：data：2D array-like

    Rectangular data for clustering. Cannot contain NAs.

pivot_kws：dict, optional

    If <cite>data</cite> is a tidy dataframe, can provide keyword arguments 
    for pivot to create a rectangular dataframe.

method：str, optional

    Linkage method to use for calculating clusters. See scipy.cluster.
    hierarchy.linkage documentation for more information: 
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

metric：str, optional

    Distance metric to use for the data. See scipy.spatial.distance.pdist 
    documentation for more options 
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html 
    To use different metrics (or methods) for rows and columns, you may 
    construct each linkage matrix yourself and provide them as {row,col}_linkage.

z_score：int or None, optional

    Either 0 (rows) or 1 (columns). Whether or not to calculate z-scores for 
    the rows or the columns. Z scores are: z = (x - mean)/std, so values in 
    each row (column) will get the mean of the row (column) subtracted, then 
    divided by the standard deviation of the row (column). This ensures that 
    each row (column) has mean of 0 and variance of 1.

standard_scale：int or None, optional

    Either 0 (rows) or 1 (columns). Whether or not to standardize that 
    dimension, meaning for each row or column, subtract the minimum and 
    divide each by its maximum.

figsize: tuple of two ints, optional

    Size of the figure to create.

cbar_kws：dict, optional

    Keyword arguments to pass to cbar_kws in heatmap, e.g. to add a label to 
    the colorbar.

{row,col}_cluster：bool, optional

    If True, cluster the {rows, columns}.

{row,col}_linkage：numpy.array, optional

    Precomputed linkage matrix for the rows or columns. 
    See scipy.cluster.hierarchy.linkage for specific formats.

{row,col}_colors：list-like or pandas DataFrame/Series, optional

    List of colors to label for either the rows or columns. Useful to evaluate 
    whether samples within a group are clustered together. Can use nested 
    lists or DataFrame for multiple color levels of labeling. If given as a 
    DataFrame or Series, labels for the colors are extracted from the 
    DataFrames column names or from the name of the Series. DataFrame/Series 
    colors are also matched to the data by their index, ensuring colors are 
    drawn in the correct order.

mask：boolean array or DataFrame, optional

    If passed, data will not be shown in cells where mask is True. Cells with 
    missing values are automatically masked. Only used for visualizing, not 
    for calculating.

kwargs：other keyword arguments

    All other keyword arguments are passed to sns.heatmap

返回值：clustergrid：ClusterGrid

    A ClusterGrid instance.

Notes

The returned object has a savefig method that should be used if you want to 
save the figure object without clipping the dendrograms.

To access the reordered row indices, 
use: clustergrid.dendrogram_row.reordered_ind

Column indices, use: clustergrid.dendrogram_col.reordered_ind'''

#%%

#Examples

#Plot a clustered heatmap:
iris = sns.load_dataset('iris')
species =iris.pop('species')
g = sns.clustermap(iris)

#Use a different similarity metric:
g = sns.clustermap(iris,metric='correlation')

#Use a different clustering method:
g= sns.clustermap(iris,method='single')

#Use a different colormap and ignore outliers in colormap limits:
g = sns.clustermap(iris,cmap='mako',robust=True)

#Change the size of the figure:
g = sns.clustermap(iris,figsize=(6,7))

#Plot one of the axes in its original organization:
g = sns.clustermap(iris,col_cluster=False)

#Add colored labels:
lut = dict(zip(species.unique(),'rbg'))
row_colors = species.map(lut)
g = sns.clustermap(iris,row_colors=row_colors)

#Standardize the data within the columns:
g = sns.clustermap(iris,standard_scale=1)

#Normalize the data within the rows:
g = sns.clustermap(iris,z_score=0)

#%%

#seaborn.FacetGrid
'''class seaborn.FacetGrid(data, row=None, col=None, hue=None, col_wrap=None, 
sharex=True, sharey=True, height=3, aspect=1, palette=None, row_order=None, 
col_order=None, hue_order=None, hue_kws=None, dropna=True, legend_out=True, 
despine=True, margin_titles=False, xlim=None, ylim=None, subplot_kws=None, 
gridspec_kws=None, size=None)'''

#用于绘制条件关系的多图网格。
'''__init__(data, row=None, col=None, hue=None, col_wrap=None, sharex=True, 
sharey=True, height=3, aspect=1, palette=None, row_order=None, col_order=None, 
hue_order=None, hue_kws=None, dropna=True, legend_out=True, despine=True, 
margin_titles=False, xlim=None, ylim=None, subplot_kws=None, gridspec_kws=None, 
size=None)'''

'''初始化matplotlib画布和FacetGrid对象。

该类将数据集映射到由行和列组成的网格中的多个轴上，这些轴与数据集中变量的级别
对应。它产生的图通常被称为“lattice”，“trellis”或“small-multiple”图形。

它还可以用hue参数表示第三个变量的级别，该参数绘制不同颜色的不同数据子集。
它使用颜色来解析第三维度上的元素，但是只绘制相互重叠的子集，并且不会像接受
“hue”的坐标轴级函数那样为特定的可视化定制“hue”参数。

当使用从数据集推断语义映射的seaborn函数时，必须注意在各个方面之间同步这些映射。
在大多数情况下，使用图形级函数（例如relplot()或catplot()）比直接使用
FacetGrid更好。
'''

#%%

'''参数：data：DataFrame数据。

    整洁的（“长形式”）dataframe数据，其中每一列是一个变量，每一行是一个
    观察实例。

row, col, hue：字符串。

    定义数据子集的变量，这些变量将在网格的不同方面绘制。请参阅*_order
    参数以控制此变量的级别顺序。

col_wrap：整形数值，可选参数。

    以此参数值来限制网格的列维度，以便列面跨越多行。与row面不兼容。

share{x,y}：布尔值，'col' 或 'row'可选

    如果为true，则跨列共享y轴或者跨行共享x轴。

height：标量，可选参数。

    每个图片的高度设定（以英寸为单位）。另见：aspect

aspect：标量，可选参数。

    每个图片的纵横比，因此aspect * height给出每个图片的宽度，单位为英寸。

palette：调色板名称，列表或字典，可选参数。

    用于色调变量的不同级别的颜色。应为color_palette()可以解释的参数，或者是
    将色调级别映射到matplotlib颜色的字典。

{row,col,hue}_order：列表，可选参数。

    对所给命令级别进行排序。默认情况下，这将是在数据中显示的级别，或者，
    如果变量是pandas分类，则为类别顺序。

hue_kws：参数-列表值的映射字典

    插入到绘图调用中的其他关键字参数，使得其他绘图属性在色调变量的级别上有
    所不同（例如散点图中的标记）。

legend_out：布尔值，可选参数。

    如果为True，则图形尺寸将被扩展，图例将绘制在中间右侧的图形之外。

despine：布尔值，可选参数。

    从图中移除顶部和右侧边缘框架。

margin_titles：布尔值，可选参数。

    如果为True，则行变量的标题将绘制在最后一列的右侧。此选项是实验性的，
    可能无法在所有情况下使用。

{x, y}lim：元组，可选参数。

    每个图片上每个轴的限制（仅当share {x，y}为True时才相关）。

subplot_kws：字典，可选参数。

    传递给matplotlib subplot（s）方法的关键字参数字典。

gridspec_kws：字典，可选参数。

    传递给matplotlib的gridspec模块（通过plt.subplots）的关键字参数字典。
    需要matplotlib> = 1.4，如果col_wrap不是None，则忽略它。

另请参见

用于绘制成对关系的子图网格。

relplot

结合关系图和FacetGrid。

catplot

结合分类图和FacetGrid。

lmplot

结合回归图和FacetGrid。

范例'''

#%%

#使用tips数据集初始化2x2网格图：
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips,col='time',row='smoker')

#在每个子图绘制一个单变量图：
g = sns.FacetGrid(tips,col='time',row='smoker')
g.map(plt.hist,'total_bill')
#注意，没有必要重新捕获返回的变量;它是相同的对象，
#但在示例中这样做使得处理doctests更加方便）

#将其他关键字参数传递给映射函数：
bins = np.arange(0,65,5)
g = sns.FacetGrid(tips,row='smoker',col='time')
g = g.map(plt.hist,'total_bill',bins=bins,color='r')

#在每个子图绘制一个双变量函数：
g = sns.FacetGrid(tips,row='smoker',col='time')
g = g.map(plt.scatter,'total_bill','tip',edgecolor='w')

#将其中一个变量分配给绘图元素的颜色
g = sns.FacetGrid(tips,col='time',hue='smoker')
g = (g.map(plt.scatter,'total_bill','tip',edgecolor='w')
     .add_legend())

#更改每个子图的高度和纵横比：
g = sns.FacetGrid(tips,col='day',height=4,aspect=.5)
g = g.map(plt.hist,'total_bill',bins=bins)

#指定绘图元素的顺序：
g = sns.FacetGrid(tips,col='smoker',col_order=['Yes','No'])
g = g.map(plt.hist,'total_bill',bins=bins,color='m')

#使用不同的调色板：
kws = dict(s=50,linewidth=.5,edgecolor='w')
g = sns.FacetGrid(tips,col='sex',hue='time',palette='Set1',
                  hue_order=['Dinner','Lunch'])
g = (g.map(plt.scatter,'total_bill','tip',**kws)
     .add_legend())

#使用字典将色调级别映射到颜色：
pal = dict(Lunch='seagreen',Dinner='gray')
g = sns.FacetGrid(tips,col='time',hue='time',palette=pal,
                  hue_order=['Dinner','Lunch'])
g = (g.map(plt.scatter,'total_bill','tip',**kws)
     .add_legend())

#另外，为色调级别使用不同的标记：
g = sns.FacetGrid(tips,col='sex',hue='time',palette=pal,
                  hue_order=['Dinner','Lunch'],
                  hue_kws=dict(marker=['^','v']))
g = (g.map(plt.scatter,'total_bill','tip',**kws)
     .add_legend())

#将包含多个级别的列变量“换行”到行中：
att = sns.load_dataset('attention')
g = sns.FacetGrid(att,col='subject',col_wrap=5,height=1.5)
g = g.map(plt.plot,'solutions','score',marker='.')

#定义一个自定义双变量函数来映射到网格
from scipy import stats
def qqplot(x,y,**kwargs):
    _,xr = stats.probplot(x,fit=False)
    _,yr = stats.probplot(y,fit=False)
    plt.scatter(xr,yr,**kwargs)

g = sns.FacetGrid(tips,col='smoker',hue='sex')
g = (g.map(qqplot,'total_bill','tip',**kws)
     .add_legend())

#%%

#定义一个使用DataFrame对象的自定义函数，并接受列名作为位置变量：
df = pd.DataFrame(data=np.random.randn(90,4),
                  columns=pd.Series(list('ABCD'),name='walk'),
                  index=pd.date_range('2015-01-01','2015-03-31',name='date'))
df = df.cumsum(axis=0).stack().reset_index(name='val')


#
def dateplot(x,y,**kwargs):
    ax = plt.gca()
    print(kwargs)
    data = kwargs.pop('data')
    data.plot(x=x,y=y,ax=ax,grid=False,**kwargs)

g = sns.FacetGrid(df,col='walk',col_wrap=2,height=3.5)
g = g.map_dataframe(dateplot,'date','val')

#%%

#绘图后使用不同的轴标签：
g = sns.FacetGrid(tips,col='smoker',row='sex')
g = (g.map(plt.scatter,'total_bill','tip',color='g',**kws)
     .set_axis_labels('Total bill(US Dollars)','Tip'))

g = sns.FacetGrid(tips,col='smoker',row='sex')
g = (g.map(plt.scatter,'total_bill','tip',color='r',**kws)
     .set(xlim=(0,60),ylim=(0,12),xticks=[10,30,50],yticks=[2,6,10]))


#为子图标题使用不同的模板：
g = sns.FacetGrid(tips,col='size',col_wrap=3)
g = (g.map(plt.hist,'tip',bins=np.arange(0,13),color='c')
     .set(xticks=[0,5,10],yticks=[2,6,10])
     .set_titles('{col_name} dinners'))

#收紧每个子图:
g = sns.FacetGrid(tips,col='smoker',row='sex',margin_titles=True)
g = (g.map(plt.scatter,'total_bill','tip',color='m',**kws)
     .set(xlim=(0,60),ylim=(0,12),
          xticks=[10,30,50],yticks=[2,6,10])
     .fig.subplots_adjust(wspace=.05,hspace=.05))

'''方法

| __init__(data[, row, col, hue, col_wrap, …]) | 初始化matplotlib画布
和FacetGrid对象。 |

| add_legend([legend_data, title, label_order]) | 绘制一个图例，可能将其放在
轴外并调整图形大小。|

| despine(**kwargs) | 从子图中移除轴的边缘框架。 |

| facet_axis(row_i, col_j) | 使这些索引识别的轴处于活动状态并返回。 |

| facet_data() | 用于每个子图的名称索引和数据子集的生成器。 |

| map(func, *args, **kwargs) | 将绘图功能应用于每个子图的数据子集。 |

| map_dataframe(func, *args, **kwargs) | 像.map一样，但是将args作为字符串传递并
在kwargs中插入数据。 |

| savefig(*args, **kwargs) | 保存图片。 |

| set(**kwargs) | 在每个子图集坐标轴上设置属性。|

| set_axis_labels([x_var, y_var]) | 在网格的左列和底行设置轴标签。 |

| set_titles([template, row_template, …]) | 在每个子图上方或网格边缘绘制标题。 |

| set_xlabels([label]) | 在网格的底行标记x轴。 |

| set_xticklabels([labels, step]) | 在网格的底行设置x轴刻度标签。 |

| set_ylabels([label]) | 在网格的左列标记y轴。 |

| set_yticklabels([labels]) | 在网格的左列上设置y轴刻度标签。 |

属性

| ax | 轻松访问单个坐标轴。 |'''


#%%

#seaborn.FacetGrid.map
#FacetGrid.map(func, *args, **kwargs)

''''Apply a plotting function to each facet’s subset of the data.

参数：func：callable

    A plotting function that takes data and keyword arguments. It must plot to 
    the currently active matplotlib Axes and take a <cite>color</cite> keyword 
    argument. If faceting on the <cite>hue</cite> dimension, it must also take 
    a <cite>label</cite> keyword argument.

args：strings

    Column names in self.data that identify variables with data to plot. 
    The data for each variable is passed to <cite>func</cite> in the order 
    the variables are specified in the call.

kwargs：keyword arguments

    All keyword arguments are passed to the plotting function.
'''

#%%

'''seaborn.FacetGrid.map_dataframe

FacetGrid.map_dataframe(func, *args, **kwargs)

Like .map but passes args as strings and inserts data in kwargs.

This method is suitable for plotting with functions that accept a long-form 
DataFrame as a <cite>data</cite> keyword argument and access the data in that
DataFrame using string variable names.

参数：func：callable

    A plotting function that takes data and keyword arguments. Unlike the 
    <cite>map</cite> method, a function used here must “understand” Pandas 
    objects. It also must plot to the currently active matplotlib Axes and 
    take a <cite>color</cite> keyword argument. If faceting on the <cite>
    hue</cite> dimension, it must also take a <cite>label</cite> keyword argument.

args：strings

    Column names in self.data that identify variables with data to plot. 
    The data for each variable is passed to <cite>func</cite> in the order 
    the variables are specified in the call.

kwargs：keyword arguments

    All keyword arguments are passed to the plotting function.

返回值：self：object

    Returns self.'''


#%%

#seaborn.PairGrid

'''class seaborn.PairGrid(data, hue=None, hue_order=None, palette=None, 
hue_kws=None, vars=None, x_vars=None, y_vars=None, diag_sharey=True, 
height=2.5, aspect=1, despine=True, dropna=True, size=None)
'''

'''Subplot grid for plotting pairwise relationships in a dataset.

This class maps each variable in a dataset onto a column and row in a grid of 
multiple axes. Different axes-level plotting functions can be used to draw 
bivariate plots in the upper and lower triangles, and the the marginal 
distribution of each variable can be shown on the diagonal.

It can also represent an additional level of conditionalization with the hue 
parameter, which plots different subets of data in different colors. 
This uses color to resolve elements on a third dimension, but only draws 
subsets on top of each other and will not tailor the hue parameter for the 
specific visualization the way that axes-level functions that accept hue will.

See the tutorial for more information.'''

'''__init__(data, hue=None, hue_order=None, palette=None, hue_kws=None, 
vars=None, x_vars=None, y_vars=None, diag_sharey=True, height=2.5, aspect=1, 
despine=True, dropna=True, size=None)'''

#nitialize the plot figure and PairGrid object.

#%%

'''参数：data：DataFrame

    Tidy (long-form) dataframe where each column is a variable and each row 
    is an observation.

hue：string (variable name), optional

    Variable in data to map plot aspects to different colors.

hue_order：list of strings

    Order for the levels of the hue variable in the palette

palette：dict or seaborn color palette

    Set of colors for mapping the hue variable. If a dict, keys should be 
    values in the hue variable.

hue_kws：dictionary of param -> list of values mapping

    Other keyword arguments to insert into the plotting call to let other plot 
    attributes vary across levels of the hue variable (e.g. the markers in a 
    scatterplot).

vars：list of variable names, optional

    Variables within data to use, otherwise use every column with a numeric 
    datatype.

{x, y}_vars：lists of variable names, optional

    Variables within data to use separately for the rows and columns of the 
    figure; i.e. to make a non-square plot.

height：scalar, optional

    Height (in inches) of each facet.

aspect：scalar, optional

    Aspect * height gives the width (in inches) of each facet.

despine：boolean, optional

    Remove the top and right spines from the plots.

dropna：boolean, optional

    Drop missing values from the data before plotting.

See also

Easily drawing common uses of PairGrid.Subplot grid for plotting conditional 
relationships.'''

#%%

#Examples

#Draw a scatterplot for each pairwise relationship:
iris = sns.load_dataset('iris')
g = sns.PairGrid(iris)
g = g.map(plt.scatter)

#Show a univariate distribution on the diagonal:
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
#(It’s not actually necessary to catch the return value every time, as it is
#the same object, but it makes it easier to deal with the doctests).

#Color the points using a categorical variable:
g = sns.PairGrid(iris,hue='species')
g = (g.map_offdiag(plt.scatter)
     .map_diag(plt.hist)
     .add_legend())

#Use a different style to show multiple histograms:
g = sns.PairGrid(iris,hue='species')
g = (g.map_diag(plt.hist,histtype='step',linewidth=3)
     .map_offdiag(plt.scatter)
     .add_legend())

#Plot a subset of variables
g = sns.PairGrid(iris,vars=['sepal_length','sepal_width'])
g = g.map(plt.scatter)

#ass additional keyword arguments to the functions
kwargs = dict(edgecolor='w')
g = sns.PairGrid(iris)
g = (g.map_diag(plt.hist,**kwargs)
     .map_offdiag(plt.scatter,**kwargs))

#Use different variables for the rows and columns:
g = sns.PairGrid(iris,x_vars=['sepal_length','sepal_width'],
                 y_vars=['petal_length','petal_width'])
g = g.map(plt.scatter)

#Use different functions on the upper and lower triangles:
g = sns.PairGrid(iris)
g = (g.map_upper(plt.scatter)
     .map_lower(sns.kdeplot, cmap="Blues_d")
     .map_diag(sns.kdeplot,lw=3,legend=True))

#%%

#Use different colors and markers for each categorical level:
g = sns.PairGrid(iris,hue='species',palette='Set2',
                 hue_kws=dict(marker=['o','s','D']))
g = (g.map(plt.scatter,linewidth=1,edgecolor='w',s=40)
     .add_legend())

'''Methods

| __init__(data[, hue, hue_order, palette, …]) 
| Initialize the plot figure and PairGrid object. 
| | add_legend([legend_data, title, label_order]) 
| Draw a legend, maybe placing it outside axes and resizing the figure. 
| | map(func, **kwargs) 
| Plot with the same function in every subplot. 
| | map_diag(func, **kwargs) 
| Plot with a univariate function on each diagonal subplot. 
| | map_lower(func, **kwargs) 
| Plot with a bivariate function on the lower diagonal subplots. 
| | map_offdiag(func, **kwargs) 
| Plot with a bivariate function on the off-diagonal subplots. 
| | map_upper(func, **kwargs) 
| Plot with a bivariate function on the upper diagonal subplots. 
| | savefig(*args, **kwargs) 
| Save the figure. 
| | set(**kwargs) 
| Set attributes on each subplot Axes. |'''

#%%

'''
seaborn.PairGrid.map

PairGrid.map(func, **kwargs)

Plot with the same function in every subplot.

参数：func：callable plotting function

    Must take x, y arrays as positional arguments and draw onto the 
    “currently active” matplotlib Axes. Also needs to accept kwargs 
    called color and label.
'''

#%%

'''
seaborn.PairGrid.map_diag

PairGrid.map_diag(func, **kwargs)

Plot with a univariate function on each diagonal subplot.

参数：func：callable plotting function

    Must take an x array as a positional argument and draw onto the 
    “currently active” matplotlib Axes. Also needs to accept kwargs 
    called color and label.

'''

#%%

'''
seaborn.PairGrid.map_offdiag

PairGrid.map_offdiag(func, **kwargs)

Plot with a bivariate function on the off-diagonal subplots.

参数：func：callable plotting function

    Must take x, y arrays as positional arguments and draw onto the 
   “currently active” matplotlib Axes. Also needs to accept kwargs called 
   color and label.
'''

#%%

'''
seaborn.PairGrid.map_lower

PairGrid.map_lower(func, **kwargs)

Plot with a bivariate function on the lower diagonal subplots.

参数：func：callable plotting function

    Must take x, y arrays as positional arguments and draw onto the 
    “currently active” matplotlib Axes. Also needs to accept kwargs 
    called color and label.
'''

#%%

'''
seaborn.PairGrid.map_upper

PairGrid.map_upper(func, **kwargs)

Plot with a bivariate function on the upper diagonal subplots.

参数：func：callable plotting function

    Must take x, y arrays as positional arguments and draw onto the 
    “currently active” matplotlib Axes. Also needs to accept kwargs called 
    color and label.

'''

#%%

#seaborn.JointGrid
'''class seaborn.JointGrid(x, y, data=None, height=6, ratio=5, space=0.2, 
dropna=True, xlim=None, ylim=None, size=None)'''

#Grid for drawing a bivariate plot with marginal univariate plots
'''__init__(x, y, data=None, height=6, ratio=5, space=0.2, dropna=True, 
xlim=None, ylim=None, size=None)

Set up the grid of subplots.'''

'''参数：x, y：strings or vectors

    Data or names of variables in data.

data：DataFrame, optional

    DataFrame when x and y are variable names.

height：numeric

    Size of each side of the figure in inches (it will be square).

ratio：numeric

    Ratio of joint axes size to marginal axes height.

space：numeric, optional

    Space between the joint and marginal axes

dropna：bool, optional

    If True, remove observations that are missing from <cite>x</cite> and 
    <cite>y</cite>.

{x, y}lim：two-tuples, optional

    Axis limits to set before plotting.

See also

High-level interface for drawing bivariate plots with several different 
default plot kinds.'''

#%%

#Examples

#Initialize the figure but don’t draw any plots onto it:
g = sns.JointGrid(x='total_bill',y='tip',data=tips)

#Add plots using default parameters:
g = g.plot(sns.regplot,sns.distplot)

#Draw the join and marginal plots separately,
#which allows finer-level control other parameters:
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(plt.scatter,color='.5',edgecolor='w')
g = g.plot_marginals(sns.distplot,kde=False,color='.5')

#%%

#Draw the two marginal plots separately:
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g.plot_joint(plt.scatter,color='m',edgecolor='white')
g.ax_marg_x.hist(tips.total_bill,color='b',alpha=.6,bins=np.arange(0,60,5))
g.ax_marg_y.hist(tips["tip"], color="r", alpha=.6,
                 orientation="horizontal",bins=np.arange(0, 12, 1))

#Add an annotation with a statistic summarizing the bivariate relationship:
from scipy import stats
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(plt.scatter,color='g',s=40,edgecolor='w')
g = g.plot_marginals(sns.distplot,kde=False,color='g')
g = g.annotate(stats.pearsonr)

#%%

#Use a custom function and formatting for the annotation
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(plt.scatter,color='g',s=40,edgecolor='w')
g = g.plot_marginals(sns.distplot,kde=False,color='g')
requare = lambda a,b :stats.pearsonr(a,b)[0]**2

g = g.annotate(requare,'{stat}:{val:.2f}',stat='$R^2$',
               loc='upper left',fontsize=12)


#Remove the space between the joint and marginal axes:
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(sns.kdeplot,cmap='Blues_d')
g = g.plot_marginals(sns.kdeplot,shade=True)

#%%

#Draw a smaller plot with relatively larger marginal axes:
g =  sns.JointGrid(x='total_bill',y='tip',data=tips,height=5,
                   ratio=3)

g = g.plot_joint(sns.kdeplot,cmap='Reds_d')
g = g.plot_marginals(sns.kdeplot,color='r',shade=True)

#Set limits on the axes:

g =  sns.JointGrid(x='total_bill',y='tip',data=tips,
                   xlim=(0,50),ylim=(0,8))
g = g.plot_joint(sns.kdeplot,cmap='Purples_d')
g = g.plot_marginals(sns.kdeplot,color='m',shade=True)

'''Methods

| __init__(x, y[, data, height, ratio, space, …]) 
| Set up the grid of subplots. 
| | annotate(func[, template, stat, loc]) 
| Annotate the plot with a statistic about the relationship. 
| | plot(joint_func, marginal_func[, annot_func]) 
| Shortcut to draw the full plot. 
| | plot_joint(func, **kwargs) 
| Draw a bivariate plot of <cite>x</cite> and <cite>y</cite>. 
| | plot_marginals(func, **kwargs) 
| Draw univariate plots for <cite>x</cite> and <cite>y</cite> separately. 
| | savefig(*args, **kwargs) 
| Wrap figure.savefig defaulting to tight bounding box. 
| | set_axis_labels([xlabel, ylabel]) 
| Set the axis labels on the bivariate axes. |'''

#%%

'''JointGrid.plot(joint_func, marginal_func, annot_func=None)

Shortcut to draw the full plot.

Use <cite>plot_joint</cite> and <cite>plot_marginals</cite> directly 
for more control.

参数：joint_func, marginal_func：callables

    Functions to draw the bivariate and univariate plots.

返回值：self：JointGrid instance

    Returns <cite>self</cite>.
'''

#%%

'''
seaborn.JointGrid.plot_joint

JointGrid.plot_joint(func, **kwargs)

Draw a bivariate plot of <cite>x</cite> and <cite>y</cite>.

参数：func：plotting callable

    This must take two 1d arrays of data as the first two positional arguments,
    and it must plot on the “current” axes.

kwargs：key, value mappings

    Keyword argument are passed to the plotting function.

返回值：self：JointGrid instance

    Returns <cite>self</cite>.

'''

#%%

'''
seaborn.JointGrid.plot_marginals

JointGrid.plot_marginals(func, **kwargs)

Draw univariate plots for <cite>x</cite> and <cite>y</cite> separately.

参数：func：plotting callable

    This must take a 1d array of data as the first positional argument, 
    it must plot on the “current” axes, and it must accept a “vertical” 
    keyword argument to orient the measure dimension of the plot vertically.

kwargs：key, value mappings

    Keyword argument are passed to the plotting function.

返回值：self：JointGrid instance

    Returns <cite>self</cite>.

'''

#%%

#seaborn.set
'''seaborn.set(context='notebook', style='darkgrid', palette='deep', 
font='sans-serif', font_scale=1, color_codes=True, rc=None)'''

'''Set aesthetic parameters in one step.

Each set of parameters can be set directly or temporarily, see the referenced 
functions below for more information.'''

'''参数：context：string or dict

    Plotting context parameters, see plotting_context()

style：string or dict

    Axes style parameters, see axes_style()

palette：string or sequence

    Color palette, see color_palette()

font：string

    Font family, see matplotlib font manager.

font_scale：float, optional

    Separate scaling factor to independently scale the size of the font elements.

color_codes：bool

    If True and palette is a seaborn palette, remap the shorthand color 
    codes (e.g. “b”, “g”, “r”, etc.) to the colors from this palette.

rc：dict or None

    Dictionary of rc parameter mappings to override the above.
    
'''

#%%

'''seaborn.axes_style

seaborn.axes_style(style=None, rc=None)

Return a parameter dict for the aesthetic style of the plots.

This affects things like the color of the axes, whether a grid is enabled by 
default, and other aesthetic elements.

This function returns an object that can be used in a with statement to 
temporarily change the style parameters.

参数：style：dict, None, or one of {darkgrid, whitegrid, dark, white, ticks}

    A dictionary of parameters or the name of a preconfigured set.

rc：dict, optional

    Parameter mappings to override the values in the preset seaborn style 
    dictionaries. This only updates parameters that are considered part of 
    the style definition.
'''

#%%

'''
seaborn.set_style

seaborn.set_style(style=None, rc=None)

Set the aesthetic style of the plots.

This affects things like the color of the axes, whether a grid is enabled by 
default, and other aesthetic elements.

参数：style：dict, None, or one of {darkgrid, whitegrid, dark, white, ticks}

    A dictionary of parameters or the name of a preconfigured set.

rc：dict, optional

    Parameter mappings to override the values in the preset seaborn style 
    dictionaries. This only updates parameters that are considered part of the 
    style definition.

See also

return a dict of parameters or use in a with statement to temporarily set the 
style.set parameters to scale plot elementsset the default color palette 
for figures

Examples

>>> set_style("whitegrid")

>>> set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})
'''

#%%

'''seaborn.plotting_context

seaborn.plotting_context(context=None, font_scale=1, rc=None)

Return a parameter dict to scale elements of the figure.

This affects things like the size of the labels, lines, and other elements of 
the plot, but not the overall style. The base context is “notebook”, and the 

other contexts are “paper”, “talk”, and “poster”, which are version of 
    
the notebook parameters scaled by .8, 1.3, and 1.6, respectively.

This function returns an object that can be used in a with statement to 
temporarily change the context parameters.

参数：context：dict, None, or one of {paper, notebook, talk, poster}

    A dictionary of parameters or the name of a preconfigured set.

font_scale：float, optional

    Separate scaling factor to independently scale the size of the font elements.

rc：dict, optional

    Parameter mappings to override the values in the preset seaborn context 
    dictionaries. This only updates parameters that are considered part of the 
    context definition.

See also

set the matplotlib parameters to scale plot elementsreturn a dict of 
parameters defining a figure styledefine the color palette for a plot'''


#%%

#Examples
c = sns.plotting_context('poster')
c = sns.plotting_context('notebook',font_scale=1.5)
c = sns.plotting_context('talk',rc=dict(linewidth=2))

with sns.plotting_context('paper'):
    f,ax = plt.subplots()
    ax.plot('total_bill','tip',data=tips)


#%%

'''
seaborn.set_context

seaborn.set_context(context=None, font_scale=1, rc=None)

Set the plotting context parameters.

This affects things like the size of the labels, lines, and other elements of 
the plot, but not the overall style. The base context is “notebook”, and 
the other contexts are “paper”, “talk”, and “poster”, which are version of 
the notebook parameters scaled by .8, 1.3, and 1.6, respectively.

参数：context：dict, None, or one of {paper, notebook, talk, poster}

    A dictionary of parameters or the name of a preconfigured set.

font_scale：float, optional

    Separate scaling factor to independently scale the size of the font elements.

rc：dict, optional

    Parameter mappings to override the values in the preset seaborn context 
    dictionaries. This only updates parameters that are considered part of the 
    context definition.

See also

return a dictionary of rc parameters, or use in a with statement to temporarily 
set the context.set the default parameters for figure styleset the default color 
palette for figures

Examples

>>> set_context("paper")

>>> set_context("talk", font_scale=1.4)

>>> set_context("talk", rc={"lines.linewidth": 2})

'''

#%%

#seaborn.set_color_codes

#seaborn.set_color_codes(palette='deep')

'''Change how matplotlib color shorthands are interpreted.

Calling this will change how shorthand codes like “b” or “g” are 
interpreted by matplotlib in subsequent plots.'''

'''参数：palette：{deep, muted, pastel, dark, bright, colorblind}

    Named seaborn palette to use as the source of colors.
'''

'''See also

Color codes can be set through the high-level seaborn style manager.Color 
codes can also be set through the function that sets the matplotlib 
color cycle.'''

#%%

#Examples

#Map matplotlib color codes to the default seaborn palette.

sns.set_color_codes()
plt.plot([0,1],color='r')

#Use a different seaborn palette.
sns.set_color_codes("dark")
plt.plot([0,1],color='g')
plt.plot([0,2],color='m')

#%%

'''
seaborn.reset_defaults

seaborn.reset_defaults()

Restore all RC params to default settings.
'''

#%%

'''
seaborn.reset_orig

seaborn.reset_orig()

Restore all RC params to original settings (respects custom rc).
'''

#%%

'''seaborn.set_palette

    译者：Modrisco

seaborn.set_palette(palette, n_colors=None, desat=None, color_codes=False)

通过searborn调色板设置matplotlib色彩循环

参数：palette：seaborn color paltte | matplotlib colormap | hls | husl

    调色板参数。 应该可以被 color_palette() 函数处理。

n_colors：int

    色彩循环中的颜色数量。默认数量与palette模式有关, 查看
    color_palette()文档了解更多内容。

desat：float

    每种颜色去饱和的比例。

color_codes：bool

    如果为True，并且palette是seaborn调色板, 则将颜色代码简写 
    (例如“b”, “g”, “r”等等)映射到当前调色板上。

另外
在with语句中临时设置调色板或色彩循环。设置参数以调整绘图元素的默认参数。'''

#%%

#例子

sns.set_palette('Reds')

sns.set_palette('Set1',8,.75)

#%%

#seaborn.color_palette

#seaborn.color_palette(palette=None, n_colors=None, desat=None)

#返回一个颜色列表来定义一个调色板。

'''Available seaborn palette names:

有 deep, muted, bright, pastel, dark, colorblind 六种颜色模式

Other options:

matplotlib Colormap 的名字、‘ch: ’, ‘hls’, ‘husl’，
或任一 matplotlib 接受的不同格式颜色列表。

调用此函数并设置 palette=None 会返回当前 matplotlib 色彩循环。

matplotlib 调色板的顺序可以通过在调色板名称后添加 “_r” 来倒置，
同样，添加 “_d” 可以将调色板设置为深色模式。
（这些选项为互斥属性，返回的颜色列表同样可以被取反）
'''

#%%

'''参数：palette：None, string, or sequence, optional

    调色板或者 None 值来返回给当前调色板。如果是序列，输入颜色会被使用，
    可能会被循环化并降低饱和度。

n_colors：int, 可选

    调色板中的颜色数。如果为 None，则默认值将取决于调色板的指定方式。已命名
    调色板默认有 6 种颜色，抓取当前调色板或传递颜色列表不会更改颜色数，除非作
    出指定。要求比调色板中存在的颜色更多的颜色会导致调色板循环化。

desat：float, 可选

    每种颜色的去饱和比例。

返回值：palette：RGB 元组序列。

    调色板。操作类似于列表，但可以用作上下文管理器，并具有转换为十六进制颜色代
    码的 as_hex 方法。

另外

设置所有的默认颜色循环。重新分配颜色代码，如 “b”、“g” 等。从seaborn 调色
板中选择颜色。'''

#%%

#例子

#不带参数的调用将返回当前默认颜色循环中的所有颜色：
sns.palplot(sns.color_palette())

#显示另一个 “seaborn 调色板”，具有与默认 matplotlib 颜色循环相同的基本色调
#顺序，但颜色更吸引人。默认情况下，使用调色板名称进行调用将返回6种颜色：
sns.palplot(sns.color_palette('muted'))

#使用一个内置 matplotlib clolormap 的离散值：
sns.palplot(sns.color_palette('RdBu',n_colors=7))

#创建自定义 cubehelix 调色板
sns.palplot(sns.color_palette('ch:9.0,-.3,dark=.3'))

#使用一个明确的 matplotlib 调色板并降低一些饱和度：
sns.palplot(sns.color_palette('Set1',n_colors=8,desat=.5))

#创建 “dark”（深色）matplotlib 顺序调色板变体。(当对应于有序变量的
#多条线或点进行着色时，如果您不希望最轻的线不可见，则可以使用此选项)：
sns.palplot(sns.color_palette('Blues_d'))

#作为上下文管理器使用：
with sns.color_palette('husl',8):
    plt.figure()
    plt.subplot()
    plt.plot([np.zeros(8),np.arange(8)])


#%%

#seaborn.husl_palette
#seaborn.husl_palette(n_colors=6, h=0.01, s=0.9, l=0.65)
'''在 HUSL 色调空间中获得一组均匀间隔的颜色。
h, s, 和 l 值应该在 0 和 1 之间。'''

'''参数：n_colors：int

    调色板中的颜色数

h：float

    第一个色调

s：float

    饱和度

l：float

    亮度

返回值：palette：seaborn 调色板

    类似列表的颜色对象的 RGB 元组。

另外
在 HSL 系统中使用等间距圆形色调创建一个调色板。'''

#%%

#例子

#使用默认参数创建一个有 10 种颜色的调色板：

sns.palplot(sns.husl_palette(10))

#创建一个以不同色调值开头的 10 种颜色的调色板：
sns.palplot(sns.husl_palette(10,h=.5))

#创建一个比默认颜色更暗的 10 种颜色的调色板：
sns.palplot(sns.husl_palette(10,l=.4))

#创建 10 种颜色的调色板，其饱和度低于默认值：
sns.palplot(sns.husl_palette(10,s=.4))

#%%

#seaborn.hls_palette
#seaborn.hls_palette(n_colors=6, h=0.01, l=0.6, s=0.65)

'''在 HLS 色调空间中获取一组均匀间隔的颜色。
h, s, 和 l 值应该在 0 和 1 之间。'''

'''参数：n_colors：int

    调色板中的颜色数

h：float

    第一个色调

l：float

    亮度

s：float

    饱和度

返回值：palette：seaborn 调色板

    类似列表的颜色对象的 RGB 元组。

另外
在 HUSL 系统中使用等间距圆形色调创建一个调色板。'''

#%%

#例子

#使用默认参数创建一个有 10 种颜色的调色板：
sns.palplot(sns.hls_palette(10))

#创建一个以不同色调值开头的 10 种颜色的调色板：
sns.palplot(sns.hls_palette(10,h=.5))

#创建一个比默认颜色更暗的 10 种颜色的调色板：
sns.palplot(sns.hls_palette(10,l=.4))

#创建 10 种颜色的调色板，其饱和度低于默认值：
sns.palplot(sns.hls_palette(10,s=.4))

#%%

#seaborn.cubehelix_palette
'''seaborn.cubehelix_palette(n_colors=6, start=0, rot=0.4, gamma=1.0, hue=0.8, 
light=0.85, dark=0.15, reverse=False, as_cmap=False)'''

'''用 cubehelix 系统制作顺序调色板。

生成亮度呈线性减小(或增大)的 colormap。这意味着 colormap在转换为黑白模式时
(用于打印)的信息将得到保留，且对色盲友好。“cubehelix” 也可以作为基于 
matplotlib 的调色板使用，但此函数使用户可以更好地控制调色板的外观，并且具有一
组不同的默认值。

除了使用这个函数，还可以在 seaborn 中使用字符串速记生成 cubehelix 调色板。 
请参见下面的示例。'''

#%%

'''参数：n_colors：int

    调色板中的颜色数。

start：float, 0 <= start <= 3

    第一个色调。

rot：float

    围绕调色板范围内的色相控制盘旋转。

gamma：float 0 <= gamma

    Gamma 系数用以强调较深 (Gamma < 1) 或较浅 (Gamma > 1) 的颜色。

hue：float, 0 <= hue <= 1

    颜色的饱和度。

dark：float 0 <= dark <= 1

    调色板中最暗颜色的强度。

light：float 0 <= light <= 1

    调色板中最浅颜色的强度。

reverse：bool

    如果为 True 值，则调色板将从暗到亮。

as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是颜色列表。

返回值：palette or cmap：seaborn 调色板或者 matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值。

另外

启动交互式小部件以调整 cubehelix 调色板参数。创建具有暗低值的连续调色板。
创建具有亮低值的连续调色板。

参考'''

#%%

#例子

#生成默认调色板：
sns.palplot(sns.cubehelix_palette())


#从相同的起始位置向后旋转：
sns.palplot(sns.cubehelix_palette(rot=-.4))

#使用不同的起点和较短的旋转：
sns.palplot(sns.cubehelix_palette(start=-2.8,rot=-.1))

#反转亮度渐变方向：
sns.palplot(sns.cubehelix_palette(reverse=True))

#生成一个 colormap 对象：
x = np.arange(25).reshape((5,5))
cmap = sns.cubehelix_palette(as_cmap=True)
plt.figure()
plt.subplot()
ax = sns.heatmap(x,cmap=cmap)

#使用完整的亮度范围：
cmap = sns.cubehelix_palette(dark=0,light=1,as_cmap=True)
plt.figure()
plt.subplot()
ax = sns.heatmap(x,cmap=cmap)

#使用 color_palette() 函数接口：
sns.palplot(sns.color_palette('ch:3,r=.2,l=.6'))

#%%

#seaborn.dark_palette
'''seaborn.dark_palette(color, n_colors=6, reverse=False, 
as_cmap=False, input='rgb')'''

'''制作一个混合深色和 color 模式的顺序调色板。

这种调色板适用于数据集的范围从相对低值(不感兴趣)到相对高值(很感兴趣)时。

可以通过多种方式指定 color 参数，包括用于在 matplotlib 中定义颜色的所有选项，
以及由 seborn 处理的其他几个颜色空间。也可以使用 XKCD color survey 中的
颜色名字数据库。

如果您在使用 IPython notebook，您还可以通过 choose_dark_palette() 
函数交互式选择调色板。'''

#%%

'''参数：color：高值的基色

    十六进制、RGB 元组或者颜色名字。

n_colors：int, 可选

    调色板中的颜色数。

reverse：bool, 可选

    如果为 True 值，则反转混合的方向。

as_cmap：bool, optional

    如果为 True 值，则返回 matplotlib colormap 而不是列表。

input：{‘rgb’, ‘hls’, ‘husl’, xkcd’}

    用于解释输入颜色的颜色空间。前三个选项适用于元组输入，后者适用于字符串输入。

返回值：palette or cmap：seaborn color palette or matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值。

另外

创建具有暗低值的连续调色板。创建有两种颜色的发散调色板。'''

#%%

#例子
#从一个 HTML 颜色生成一个调色板：
sns.palplot(sns.dark_palette('purple'))

#生成亮度降低的调色板：
sns.palplot(sns.dark_palette('seagreen',reverse=True))

#从 HUSL 空间种子生成选项板：
sns.palplot(sns.dark_palette((260,75,60),input='husl'))

#生成一个 colormap 对象：
cmap = sns.dark_palette("2ecc71",as_cmap=True)
plt.figure()
plt.subplot()
ax = sns.heatmap(x,cmap=cmap)

#%%

'''seaborn.light_palette

seaborn.light_palette(color, n_colors=6, reverse=False, 
as_cmap=False, input='rgb')

制作一个混合浅色和 color 模式的顺序调色板。

这种调色板适用于数据集的范围从相对低值(不感兴趣)到相对高值(很感兴趣)时。

可以通过多种方式指定 color 参数，包括用于在 matplotlib 中定义颜色的所有选项，
以及由 seborn 处理的其他几个颜色空间。也可以使用 XKCD color survey 中的颜色
名字数据库。

如果您在使用 IPython notebook，您还可以通过 choose_light_palette() 
函数交互式选择调色板。

参数：color：高值的基色

    十六进制、input 中的元组或者颜色名字。

n_colors：int, 可选

    调色板中的颜色数。

reverse：bool, 可选

    如果为 True 值，则反转混合的方向。

as_cmap：bool, 可选

    如果为 True 值，则返回 matplotlib colormap 而不是列表。

input：{‘rgb’, ‘hls’, ‘husl’, xkcd’}

    用于解释输入颜色的颜色空间。前三个选项适用于元组输入，后者适用于字符串输入。

返回值：palette or cmap：seaborn color palette or matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值。

另外

创建具有暗低值的连续调色板。创建有两种颜色的发散调色板。

例子

从一个 HTML 颜色生成一个调色板：'''

#%%

#例子

#从一个 HTML 颜色生成一个调色板：
sns.palplot(sns.light_palette('purple'))

#生成亮度降低的调色板：
sns.palplot(sns.light_palette('purple',reverse=True))

#从 HUSL 空间种子生成选项板：
sns.palplot(sns.light_palette((260,75,60),input='husl'))

#生成一个 colormap 对象
cmap = sns.light_palette('seagreen',as_cmap=True)
plt.figure()
plt.subplot()
sns.heatmap(x,cmap=cmap)

#%%

'''seaborn.diverging_palette

seaborn.diverging_palette(h_neg, h_pos, s=75, l=50, sep=10, n=6, 
center='light', as_cmap=False)

在两个 HUSL 颜色直接建立一个发散调色板。

如果您在使用 IPython notebook，您还可以通过 choose_diverging_palette() 
函数交互式选择调色板。

参数：h_neg, h_pos：float in [0, 359]

    图的正负范围的锚定色调

s：[0, 100] 范围内的浮点数，可选

    图的两个范围的锚定饱和度

l：[0, 100] 范围内的浮点数，可选

    图的两个范围的锚定亮度

n：int，可选

    调色板中的颜色数（如果为not，返回一个colormap）

center：{“light”, “dark”}, 可选

    调色板中心为亮或暗

as_cmap：bool, 可选

    如果为 true，返回一个 matplotlib colormap 而不是一个颜色列表。

返回值：palette or cmap：seaborn color palette or matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值。

另外

创建具有暗值的连续调色板。创建具有亮值的连续调色板。'''

#%%

#例子

#生成一个蓝-白-红调色板：
sns.palplot(sns.diverging_palette(240,10,n=9))

#生成一个更亮的绿-白-紫调色板：
sns.palplot(sns.diverging_palette(150,275,s=80,l=55,n=9))

#生成一个蓝-黑-红调色板:
sns.palplot(sns.diverging_palette(250,15,s=80,l=55,n=9,center='dark'))
cmap = sns.diverging_palette(220,20,as_cmap=True,sep=20)
plt.figure()
plt.subplot()
sns.heatmap(x,cmap=cmap)

#%%

'''seaborn.blend_palette

seaborn.blend_palette(colors, n_colors=6, as_cmap=False, input='rgb')

创建在颜色列表之间混合的调色板。

参数：colors：由 input 解释的各种格式的颜色序列。

    十六进制码，html 颜色名字，或者 input 空间中的元组。

n_colors：int, 可选

    调色板中的颜色数。

as_cmap：bool, 可选

    如果为 True 值，则返回 matplotlib colormap 而不是列表。

返回值：palette or cmap：seaborn 调色板或 matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值'''

#%%

'''
seaborn.xkcd_palette

    译者：Modrisco

seaborn.xkcd_palette(colors)

使用来自xkcd color survey的颜色名字生成调色板。

查看完整的 xkcd 颜色列表： https://xkcd.com/color/rgb/

这是一个简单的 seaborn.xkcd_rgb 字典的装饰器。

参数：colors：字符串列表

    seaborn.xkcd_rgb 字典中的 key 的列表。

返回值：palette：seaborn 调色板

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 对象，
    具体取决于 as_cmap 参数的值。

另外

使用 Crayola crayon colors 创建调色板。
'''

#%%

'''
seaborn.crayon_palette

seaborn.crayon_palette(colors)

通过 Crayola crayons 颜色名字生成调色板。

颜色列表在这里获取： 
https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

这是一个简单的 seaborn.crayons 字典的装饰器。

参数：colors：字符串列表

    List of keys in the seaborn.crayons dictionary.

返回值：palette：seaborn 调色板

    Returns the list of colors as rgb tuples in an object that behaves 
    like other seaborn color palettes.返回一个类似 serborn 调色板的对象，
    其中包括 RGB 元组构成的的颜色列表。

另外

使用来自xkcd color survey的颜色名字创建调色板。
'''

#%%

'''seaborn.mpl_palette

    译者：Modrisco

seaborn.mpl_palette(name, n_colors=6)

从一个 matplotlib 调色板中返回离散颜色。

请注意，这会正确处理定性的 colorbrewer 调色板，但如果您要求的颜色多于特定的
定性调色板，提供的颜色将会比您预期的少。相反，使用 color_palette() 函数请求
一个定性 colorbrewer 调色板将会返回预期数目的颜色，但是是循环型的。

如果您在使用 IPython notebook，您还可以通过 choose_colorbrewer_palette() 
函数交互式选择调色板。

参数：name：string

    调色板名字，应该是一个被命名的 matplotlib colormap。

n_colors：int

    调色板中离散颜色的个数。

返回值：palette or cmap：seaborn 调色板或者 matplotlib colormap

    类似列表的颜色对象的 RGB 元组，或者可以将连续值映射到颜色的 colormap 
    对象，具体取决于 as_cmap 参数的值。
'''

#%%

#生成一个含有 8 种颜色的定性 colorbrewer 调色板：
sns.palplot(sns.mpl_palette('Set2',8))

#生成一个连续的 colorbrewer 调色板：
sns.palplot(sns.mpl_palette('Blues'))

#生成一个发散调色板：
sns.palplot(sns.mpl_palette('seismic',8))

#生成一个 “dark” 顺序调色板：
sns.palplot(sns.mpl_palette('GnBu_d'))

#%%

'''
seaborn.choose_colorbrewer_palette


seaborn.choose_colorbrewer_palette(data_type, as_cmap=False)

在 ColorBrewer 集中选择一个调色板。

这些调色板内置于 matplotlib 库中，可以通过名字在 seaborn 函数中调用，
或者作为对象返回给这个函数。

参数：data_type：{‘sequential’, ‘diverging’, ‘qualitative’}

    描述您想要实现可视化的数据类型。查看 serborn 调色板文档来了解更多如何取值。
    注意，您可以传递子字符串（例如，‘q’ 代表 ‘qualitative‘）

as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是离散颜色的列表。

返回值：pal or cmap：颜色列表或 matplotlib colormap

    可以被传递给 plotting 函数的对象。

另外

创建具有暗低值的连续调色板。创建具有亮低值的连续调色板。从选中的颜色中创建发
散调色板。使用 cubehelix 创建连续调色板或者 colormap。
'''

#%%

'''
seaborn.choose_cubehelix_palette


seaborn.choose_cubehelix_palette(as_cmap=False)

启动交互式小部件以创建顺序 cubehelix 调色板。

这与 cubehelix_palette() 函数相对应。这种调色板在数据集的范围从相对低值
(不感兴趣)到相对高值(很感兴趣)时很有用。cubehelix 系统允许调色板在整个范围
内具有更多的色调变化，这有助于区分更广泛的值。

需要 2.0 以上版本 IPython，必须在 notebook 中使用。

参数：as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是离散颜色的列表。

返回值：pal or cmap：颜色列表或 matplotlib colormap

    可以被传递给 plotting 函数的对象。

另外

使用 cubehelix 创建连续调色板或者 colormap。
'''

#%%

'''
seaborn.choose_light_palette

seaborn.choose_light_palette(input='husl', as_cmap=False)

启动交互式小部件以创建亮色顺序调色板。

与 light_palette() 函数相对应。 这种调色板在数据集的范围从相对低值(不感兴趣)
到相对高值(很感兴趣)时很有用。

需要 2.0 以上版本 IPython，必须在 notebook 中使用。

参数：input：{‘husl’, ‘hls’, ‘rgb’}

    色彩空间用于定义种子值。请注意，此默认值与 light_palette() 的默认输入值不同。

参数：as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是离散颜色的列表。

返回值：pal or cmap：颜色列表或 matplotlib colormap

    可以被传递给 plotting 函数的对象。

另外

创建具有暗低值的连续调色板。创建具有亮低值的连续调色板。使用 cubehelix 
创建连续调色板或者 colormap。
'''

#%%

'''
seaborn.choose_dark_palette

    译者：Modrisco

seaborn.choose_dark_palette(input='husl', as_cmap=False)

启动交互式小部件以创建暗色顺序调色板。

与 dark_palette() 函数相对应。这种调色板在数据集的范围从相对低值(不感兴趣)到
相对高值(很感兴趣)时很有用。

需要 2.0 以上版本 IPython，必须在 notebook 中使用。

参数：input：{‘husl’, ‘hls’, ‘rgb’}

    色彩空间用于定义种子值。请注意，此默认值与 dark_palette() 的默认输入值不同。

参数：as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是离散颜色的列表。

返回值：pal or cmap：颜色列表或 matplotlib colormap

    可以被传递给 plotting 函数的对象。

另外

创建具有暗低值的连续调色板。创建具有亮低值的连续调色板。使用 cubehelix 创建连
续调色板或者 colormap。
'''

#%%

'''
seaborn.choose_diverging_palette

    译者：Modrisco

seaborn.choose_diverging_palette(as_cmap=False)

启动交互式小部件以创建一个发散调色板。

这与 diverging_palette() 函数相对应。这种调色板适用于对低值和高值都感兴趣并且
中间点也有意义的数据。（例如，相对与某些基准值的分数变化）。

需要 2.0 以上版本 IPython，必须在 notebook 中使用。

参数：as_cmap：bool

    如果为 True 值，则返回 matplotlib colormap 而不是离散颜色的列表。

返回值：pal or cmap：颜色列表或 matplotlib colormap

    可以被传递给 plotting 函数的对象。

另外

生成一个发散调色板或者 colormap。从 colorbrewer 集中交互式选择调色板，包括发散
调色板。
'''

#%%

'''
seaborn.load_dataset

    译者：Modrisco

seaborn.load_dataset(name, cache=True, data_home=None, **kws)

从在线库中获取数据集（需要联网）。

参数：name：字符串

    数据集的名字 (<cite>name</cite>.csv on 
    https://github.com/mwaskom/seaborn-data)。 
    您可以通过 get_dataset_names() 获取可用的数据集。

cache：boolean, 可选

    如果为True，则在本地缓存数据并在后续调用中使用缓存。

data_home：string, 可选

    用于存储缓存数据的目录。 默认情况下使用 ~/seaborn-data/

kws：dict, 可选

    传递给 pandas.read_csv

'''

#%%

'''seaborn.despine


seaborn.despine(fig=None, ax=None, top=True, right=True, 
left=False, bottom=False, offset=None, trim=False)

从图中移除顶部和右侧脊柱。

fig : matplotlib 值, 可选

去除所有轴脊柱，默认使用当前数值。

ax : matplotlib 轴, 可选

去除特定的轴脊柱。

top, right, left, bottom : boolean, 可选

如果为 True，去除脊柱。

offset : int or dict, 可选

绝对距离（以磅为单位）应将脊椎移离轴线（负值向内移动脊柱）。 
单个值适用于所有脊柱; 字典可用于设置每侧的偏移值。

trim : bool, 可选

如果为True，则将脊柱限制为每个非去除脊柱的轴上的最小和最大主刻度。'''

#%%

'''
seaborn.desaturate

    译者：Modrisco

seaborn.desaturate(color, prop)

减少颜色的饱和度。

参数：color：matplotlib 颜色

    十六进制，rgb 元组或者html颜色名字

prop：float

    颜色的饱和度将乘以该值

返回值：new_color：rgb 元组

    RGB元组表示去饱和的颜色代码

'''

#%%

'''
seaborn.saturate

    译者：Modrisco

seaborn.saturate(color)

返回具有相同色调的完全饱和的颜色。

参数：color：matplotlib 颜色

    十六进制，rgb 元组或者html颜色名字

返回值：new_color：rgb 元组

    RGB元组表示的饱和颜色代码

'''

#%%

'''
seaborn.set_hls_values

seaborn.set_hls_values(color, h=None, l=None, s=None)

独立修改一个颜色的 h, l 或 s 值。

参数：color：matplotlib 颜色

    十六进制，rgb 元组或者html颜色名字

h, l, s：0 到 1 之间的浮点数，或者为 None

    hls 空间中的新值。

返回值：new_color：rgb 元组

    RGB元组表示中的新颜色代码

'''
