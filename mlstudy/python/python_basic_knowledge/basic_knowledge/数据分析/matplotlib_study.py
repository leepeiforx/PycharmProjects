# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:56:19 2019

@author: bolat
"""
#%%
#Matplotlib 二维图像绘制方法
import matplotlib.pyplot as plt
import numpy as np

#%%
plt.plot([1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

plt.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
[1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
#绘制电子波谱图
#maplotlib.pyplot.angle_spectrum

#绘制柱状图
#matplotlib.pyplot.bar

#绘制直方图(水平)
#matplotlib.pyplot.barh

#绘制水平直方图
#matplotlib.pyplot.broken_barh

#绘制等高线图
#matplotlib.pyplot.contour

#绘制误差线
#matplotlib.pyplot.errorbar

#绘制六边形图案
#matplotlib.pyplot.hexbin

#绘制柱形图
#matplotlib.pyplot.hist

#绘制水平柱状图
#matplotlib.pyplot.hist2d

#绘制饼状图
#matplotlib.pyplot.pie

#绘制量场图
#matplotlib.pyplot.quiver

#散点图
#matplotlib.pyplot.scatter

#绘制光谱图
#matplotlib.pyplot.specgram

#%%
x = np.linspace(-2*np.pi,2*np.pi,1000)
y = np.sin(x)

plt.plot(x,y)
#%%
plt.bar(x,y)
#%%
plt.bar([1,2,3],[1,2,3])
#%%
plt.pie([1,2,3,4,5])
#%%
#量场图
x,y = np.mgrid[0:10,0:10]
plt.quiver(x,y)

#%%
#等高线图
x = np.linspace(-5,5,500)
y = np.linspace(-5,5,500)
X,Y = np.meshgrid(x,y)

#等高线公式
Z = (1-X/2+X**3+Y**4)*np.exp(-X**2-Y**2)
plt.contourf(X,Y,Z)

#%%
#定义图表样式
#设置线型的透明度，从0.0~1.0
#alpha=

#设置线型的颜色
#color=

#设置线型的填充样式
#fillstyle=

#设置线型的样式
#linestyle=

#设置线型的宽度
#linewidth=

#设置标记点的样式
#marker=

x = np.linspace(-2*np.pi,2*np.pi,1000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,color='r',linestyle='--',linewidth=.4,alpha=.8)
plt.plot(x,y2,color='b',linestyle='-',linewidth=.4,alpha=.8)

#%%
#散点图
# scatter(x, y, s=None, c=None, marker=None, cmap=None,
#         norm=None, vmin=None, vmax=None, 
#         alpha=None, linewidths=None, 
#         verts=None, edgecolors=None, 
#         plotnonfinite=False, data=None, *, **kwargs)

#s:散点的大小
#c:散点的颜色
#marker:散点样式
#cmap:定义多类别散点的颜色
#alpha:点的透明度
#edgecolors:散点边缘颜色

x = np.random.rand(100)
y = np.random.rand(100)

colors = np.random.rand(100)
size = np.random.normal(50,60,10)

plt.scatter(x,y,s=size,c=colors)

#%%
##饼状图
#pie(x, explode=None, labels=None, colors=None, autopct=None, 
#    pctdistance=0.6, shadow=False, labeldistance=1.1, 
#    startangle=None, radius=None, counterclock=True,
#    wedgeprops=None, textprops=None, center=(0, 0), 
#    frame=False, rotatelabels=False, data=None, *)
#label:各类别标签
#color:各类别颜色
#size:各类别占比
#explode:各类别偏移半径
#shadow:是否添加阴影
#autopct:数值标签显示样式

label = ['Cat','Dog','Cattle','Sheep','Horse']
color = ['r','g','r','g','y']
size = [1,2,3,4,5]
explode = [0,0,0,0,0.2]

plt.pie(size,colors=color,labels=label,
        explode=explode,shadow=True,autopct='%1.1f%%')
plt.axes('equal')

#%%
#组合图形样式

x = [1,3,5,7,9,11,13,15,17,19]
y_bar = [3,4,6,8,9,10,9,11,7,8]
y_line = [2,3,5,7,8,9,8,10,6,7]
plt.bar(x,y_bar)
plt.plot(x,y_line,'-o',color='y')

#%%
#定义图形位置

x = np.linspace(0,10,20)
y = x*x + 2

#新建图形图像
fig = plt.figure()
#控制画布的左,下,宽度,高度
axes1 = fig.add_axes([0.5,0.5,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y,'r')
axes2.plot(y,x,'g')



#%%
#另一种添加画布的方式
x = np.linspace(0,10,20)
y = x*x + 2
#fig,axes = plt.subplots(nrows=1,ncols=2)
#for ax in axes:
#    ax.plot(x,y,'r')

#通过设置 plt.subplots 的参数，可以实现调节画布尺寸和显示精度。
    
# 通过 figsize 调节尺寸, dpi 调节显示精度
fig,axes = plt.subplots(figsize=(16,9),dpi=50)
axes.plot(x,y,'r')

#%%
#规范绘图方法

#添加图标题、例 添加图标题、例
fig,axes = plt.subplots()
#横轴名称
axes.set_xlabel('x label')
#纵轴名称
axes.set_ylabel('y label')
#图形名称
axes.set_title('title')

axes.plot(x,x**2)
axes.plot(x,x**3)

#图例
axes.legend(['y=x**2','y=x**3'],loc=0)

#线型、颜色透明度 线型、颜色透明度
fig,axes =plt.subplots()
axes.plot(x,x+1,color='red',alpha=.5,linewidth=.25)
axes.plot(x,x+2,color='#1155dd',linewidth=.5)
axes.plot(x,x+3,color='#15cc55',linewidth=1.0)
axes.plot(x,x+4,color='blue',linewidth=2.0)          

#虚线类型
axes.plot(x,x+5,color='red',lw=2,linestyle='-')
axes.plot(x,x+6,color='red',lw=2,linestyle='-.')
axes.plot(x,x+7,color='red',lw=2,linestyle=':')
axes.plot(x,x+8,color='red',lw=2,linestyle='--')
#虚线交错宽度
line,= axes.plot(x,x+9,color='black',lw=1.5)
line.set_dashes([5,10,15,10])

#符号
axes.plot(x,x+10,color='green',lw=2,ls='--',marker='+')
axes.plot(x,x+11,color='green',lw=2,ls='--',marker='o')
axes.plot(x,x+12,color='green',lw=2,ls='--',marker='s')
axes.plot(x,x+13,color='green',lw=2,ls='--',marker='1')

# 符号大小和颜色
axes.plot(x,x+14,color='purple',lw=2,ls='-',marker='o',markersize=2)
axes.plot(x,x+15,color='purple',lw=2,ls='-',marker='o',markersize=4)
axes.plot(x,x+16,color='purple',lw=2,ls='-',marker='o',markersize=8,
          markerfacecolor='red')
axes.plot(x,x+17,color='purple',lw=2,ls='-',marker='o',markersize=8,
          markerfacecolor='yellow',markeredgewidth=2,markeredgecolor='blue')

#%%
#画布网格、坐标轴范围
fig,axes = plt.subplots(1,2,figsize=(10,5))
axes[0].plot(x,x**2,x,x**3,lw=2)
axes[0].grid(True)

axes[1].plot(x,x**2,x,x**3)
axes[1].set_ylim([0,60])
axes[1].set_xlim([2,5])
#%%

n = np.array([0,1,2,3,4,5])

fig,axes =plt.subplots(1,4,figsize=(16,5))
axes[0].scatter(x,x+0.25*np.random.randn(len(x)))
axes[0].set_title('scatter')

axes[1].step(n,n**2,lw=2)
axes[1].set_title('step')

axes[2].bar(n,n**2,align='center',width=.5,alpha=.5)
axes[2].set_title('bar')

axes[3].fill_between(x,x**2,x**3,color='green',alpha=.5)
axes[3].set_title=('fill_between')

#%%
#图形标注方法
fig,axes = plt.subplots()
x_bar = [10,20,30,40,50]
y_bar = [0.5,0.6,0.3,0.4,0.8]
bars = axes.bar(x_bar,y_bar,color='blue',label=x_bar,width=2)

for i,rect in enumerate(bars):
    print(i)
    print(rect)
    # 获取柱形图横坐标
    x_text = rect.get_x()
#    获取柱子的高度并增加 0.01
    y_text = rect.get_height()+0.01
    print(x_text)
    print(y_text)
    # 标注文字
    plt.text(x_text,y_text,'%.1f'%y_bar[i])
#除了文字标注之外，
#还可以通过 matplotlib.pyplot.annotate() 方法向图像中添加箭头等样式标注  
    plt.annotate('Min',xy=(32,0.3),xytext=(36,0.3),
                 arrowprops=dict(facecolor='black',width=1,headwidth=9))
    
#%%
x = np.linspace(-np.pi,np.pi,50)
sin = np.sin(x)
cos = np.cos(x)

fig,ax = plt.subplots(figsize=(8,5),dpi=80)

#plt.figure(figsize=(8,5),dpi=80)
#axes = plt.subplot(111)
ax.spines['right'].set_color=('none')
ax.spines['top'].set_color=('none')



#通过axes对象设置刻度显示的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 设置底边的移动范围，移动到y轴的0位置
# data:移动轴的位置到交叉轴的指定坐标 
# outward:不太懂  axes:0.0 - 1.0之间的值，整个轴上的比例  
#center:('axes',0.5) zero:('data',0.0)
#ax.spines['bottom'].set_position(('data', 0))
#ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax.plot(x,sin,'r',lw=2.5,ls='-',label='Sin Function')
ax.plot(x,cos,'b',lw=2.5,ls='-',label='Cos Function')


plt.xlim(x.min()*1.1,x.max()*1.1)

plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(sin.min()*1.1,sin.max()*1.1)
plt.yticks([-1,1],[r'$-1$',r'$1$'])


t = np.pi*(2/3)
plt.plot([t,t],[0,np.cos(t)],ls='--',lw=1.5,color='blue')
#plt.scatter([t,],[np.cos(t),],50,color='blue')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t,np.cos(t)),xycoords='data',
             xytext=(-90,-50),textcoords='offset points',fontsize=16,
             arrowprops =dict(arrowstyle='->',
                              connectionstyle='arc3,rad=.2'))

plt.plot([t,t],[0,np.sin(t)],ls='--',lw=1.5,color='red')
#plt.scatter([t,],[np.sin(t),],50,color='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t,np.sin(t)),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3,rad=.2'))
plt.legend(loc='upper left',frameon = False)
