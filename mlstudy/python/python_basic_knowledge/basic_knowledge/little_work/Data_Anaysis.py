import numpy as np
import random
from matplotlib import pyplot as plt
import pandas as pd
import sys

# arr = np.arange(4).reshape((2, 2))
#
# arr2 = np.arange(4).reshape((2, 2))
#
# x = np.array([[1, 2, 3],[4, 5, 6]])
# y = np.array([[6, 23], [-1, 7], [8, 9]])
#
# print(x.shape)
# print(x.dot(y))
# print(np.dot(x, np.ones(3)))
#
# print(np.ones(3).shape)

position = 0
walk = [position]
steps = 100
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


obj = pd.Series([4,7,-5,1],index= ['a','b','c','d'])
data = {'state':['ohio','ohio','hoio','nevada','nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5, 1.7, 1.6, 2.4, 2.9]}

pop = {'nevada':{2001:2.4, 2002:2.9},
        'ohio':{'pop':4,'list':3}
}
obj_1 = pd.DataFrame(data,columns=['state', 'year', 'pop', 'debt'],
                     index=['one','two', 'three', 'four', 'five'])
# #插入新列
obj_1['insert_temp_col']= ''

#删除列
# del obj_1['insert_temp_col']
# # print(obj_1)
# print(obj_1['year'])
# print(obj_1.state)
#
# obj_2 = pd.DataFrame(pop)
# print(obj_2)

#重新索引
# frame =pd.DataFrame(np.arange(9).reshape((3, 3)),index=['a', 'c', 'd'],
#                     columns=['ohio', 'texas', 'california'])
# print(frame)
# frame2 = frame.reindex(['a','b','c','d'] )
# states = ['texas','utah','californina']
# print(frame2)
# frame3 = frame.reindex(columns = states)
# print(frame3)
# frame4 = frame.reindex(index=['a','b','c','d'], columns= states)
# print(frame4)

#丢弃指定轴上的项
# new_obj = obj_1.drop(['one','three'])
# print(new_obj)

#索引,选取和过滤
obj_4 = pd.Series(np.arange(4.), index=['a','b','c','d'])
# print(obj_4['b'],'\n',obj_4['c':'d'])
#
# print(obj_1[obj_1['pop']>2])
#
# print(obj_1.ix[obj_1.year< 2002, :3])


#算数运算和数据对齐
s1= pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = pd.Series([-2.1,3.6,-1.5,3.1,-1],index=['a','c','e','f','g'])
# print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape(3,3),columns=list('abc'),
                   index=['ohio','utah','colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bcd'),
                   index=['utah','ohio','texas','oregon'])


#在算数方法中填充值,.add填充后面(df2)中存在而df1中没有的部分为0

df1.add(df2,fill_value = 0)

df3 = df1.add(df2,fill_value = 0)
# print(df3.reindex(columns=df2.columns,fill_value = 0))

frame = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),
                     index=['utah','ohio','texa','oregon'])

series2 =pd.Series(range(3), index=list('bde'))

series4 = pd.Series(range(4),index=['utah','ohio','texa','oregon'])

# print(series2)

# #水平广播
# print(frame+series2)
# #垂直广播
# print(frame.add(series4,axis = 0))

#排序和排名
#排序
obj_sort = pd.Series(range(4),index=list('dabc'))

# print(obj_sort.sort_values())
# print(obj_sort.sort_index())
''
frame_obj = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three','one'],
                         columns=list('dabc'))

frame_f = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),
                       index=['utah','ohio','texa','oregon'])

#函数应用和映射
# print(frame_f)
# print(np.abs(frame_f))

# 元素级数组方法
def f(x):
    return pd.Series([x.max(), x.min()], index=['max', 'min'])

f0 = lambda x:x.max()-x.min()
# print(frame_f.apply(f0))
# print(frame_f.apply(f0, axis=1))
#
# print(frame_f.apply(f, axis=1))
#元素级python函数也可使用,(applymap)
format = lambda x: '%.2f'%x

# print(frame_f.applymap(format))
#
# print(frame_obj.sort_index(axis=0))
# print(frame_obj.sort_index(axis=1))

#pandas读取csv文件
#因csv文件不是UTF-8编码,需要设置encoding参数
csv_path =r'D:\System_files\Desktop\reguar_expression\temp_csv.csv'
# csv_table = pd.read_csv(csv_path,encoding='gb18030',header=None)
#或者
#设置索引列使用index_col,(可以设置多个列作为索引列)
# csv_table = pd.read_csv(csv_path,encoding='gbk',names=['a','b','c'],index_col=['a'])
# print(csv_table)

#NA处理
# csv_table = pd.read_csv(csv_path,encoding='gbk',names=['a','b','c'],
#                         index_col=['a'],na_values=['NULL'])
# #可以用字段为各列指定不同的NA标记值
# sentials = {'b':['foo','NA'],
#             'c':['two']}
# csv_table = pd.read_csv(csv_path,encoding='gbk',names=['a','b','c'],
#                         index_col=['a'],na_values=sentials)

# #统计NAN个数
# print((csv_table.isnull().sum()))
# #删除NAN
# print(csv_table.dropna())
# #替换NAN
# print(csv_table.fillna('change'))

#逐块读取文本文件
# result = pd.read_csv(csv_path,encoding='gbk',nrows=1000)
# print(result)


# chunk = pd.read_csv(csv_path,encoding='gbk',chunksize=1000)
# tot = pd.Series([])
# for piece in chunk:
#     tot = tot.add(piece['作业帮'].value_counts(),fill_value =0)

# sorted(tot,reverse=False)
# print(tot)

#文件写出到文本格式
# out_file =r'D:\System_files\Desktop\reguar_expression\out.csv'
# tot.to_csv(out_file,na_rep='NULL',index=False,header=False)

#合并数据集
#pandas.maerge  , pandas.concat
df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                   'data1':(range(7))})
df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':(range(3))})

# print(df1)
# print(df2)

#若没有指定列,则merge默认按重叠的列的列名作为键
df_merge = pd.merge(df1,df2,on='key')
# print(df_merge)

df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],
                   'data1':(range(7))})
df4 = pd.DataFrame({'rkey':['a','b','d'],
                    'data2':(range(3))})

#如果列名不一致,需要设置左右on(默认merge做的是'inner'连接)
df_merge2 =pd.merge(df3,df4,left_on='lkey',right_on='rkey')
# print(df_merge2)

#'how'参数设置连接方式(left,right,outer,inner)
df_left =pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='left')
df_right =pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='right')
df_outer = pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='outer')
df_inner = pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='inner')
# print(df_left)
# print(df_right)
# print(df_outer)
# print(df_inner)

#多个键合并,传入一个由列名组成的列表即可
left = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','three'],
                     'lval':[1,2,3]})
right =pd.DataFrame({'key1':['foo','foo','bar','bar'],
                     'key2':['one','two','three','four'],
                     'rval':[4,5,6,7]})
plural_merge = pd.merge(left,right,on=['key1','key2'],how='outer')
# print(plural_merge)

#索引上的合并
#left_index =True #right_index=True
left_index = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','three'],
                     'lval':[1,2,3]},index=['a','b','c'])
right_index =pd.DataFrame({'key1':['foo','foo','bar','bar'],
                     'key2':['a','b','c','d'],
                     'rval':[4,5,6,7]})
df_merge_index =pd.merge(left_index,right_index,left_index=True,right_on='key2',
                         how='outer')
#层次化索引
lefth = pd.DataFrame({'key1':['ohio','ohio','ohio','nevada','nevada'],
                      'key2':[2000,2001,2002,2001,2002],
                      'data':np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6,2)),index=[['nevada','nevada','ohio','ohio','ohio','ohio'],
                                                          [2001,2000,2000,2000,2001,2002]],
                      columns=['event1','event2'])
# print(lefth)
# print(righth)
#这种情况下,必须以列表形式致命用作合并键的多列(注意对重复索引值的处理)
complex_left_merge = pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='left')
# print(complex_left_merge)

complex_outer_merge = pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='outer')
# print(complex_outer_merge)

#同时使用合并双方的索引
left2 = pd.DataFrame([[1.,2],[3.,4],[5.,6]],index=['a','c','e'],
                     columns=['ohio','nevada'])
right2 = pd.DataFrame([[7,8],[9.,10],[11.,12],[13,14]],index=['b','c','d','e'],
                      columns=['missour1','alabama'])
# print(left2)
# print(right2)
both_index_merge = pd.merge(left2,right2,how='outer',left_index=True,right_index=True)
# print(both_index_merge)

#使用join方法合并(默认左连接)注意join里面的iterable
left_use_join = left2.join(right2,how='outer')
# print(left_use_join)
#对于简单索引合并,可以向join传入一组DataFrame
another = pd.DataFrame([[7,8],[9.,10],[11.,12.],[16.,17.]],index=['a','c','e','f'],columns=['new york','oregon'])
left_use_join2 = left2.join([right2,another])
# print(left_use_join2)

#轴向连接,也成为连接,绑定或堆叠,np中的concatenate
arr=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

#axis=1表示按列堆叠
# arr_con = np.concatenate([arr,arr],axis=1)
arr_con = np.concatenate([arr,arr],axis=0)
# print(arr_con)

#pd中的concat注意concat里面的是iterable
s1 =pd.Series([0, 1], index=['a','b'])
s2 =pd.Series([2, 3, 4], index=['c','d','e'])
s3 =pd.Series([5, 6], index=['f', 'g'])
pd_concat = pd.concat([s1,s2,s3],axis=0)
# pd_concat = pd.concat([s1,s2,s3],axis=1)
# print(pd_concat)
s4 =pd.concat([s1*5,s3])
# print(s1,s4)
s5 = pd.concat([s1, s4],axis=1,sort=True)

#join_axes 指定要再其他轴上使用的索引
s5_index =pd.concat([s1, s4],axis=1,sort=True,join_axes=[['a','b','c','d']])
# print(s5)
# print(s5_index)

s6=pd.concat([s1,s4],axis=1,join='inner')
# print(s6)

#构造层次化索引,使用keys
# s_layer_index = pd.concat([s1,s1,s3],keys=['one','two','three'])
#按axis =1对series进行合并,则keys就会成为dataframe的列头,同样的逻辑对dataframe也适用

s_layer_index = pd.concat([s1,s1,s3],axis=1, keys=['one','two','three'],sort=True)
# print(s_layer_index)

df_layer1 =pd.DataFrame(np.arange(6).reshape((3, 2)), index=['a', 'b', 'c'],
                        columns=['one', 'two'])
df_layer2 = pd.DataFrame(5+np.arange(4).reshape((2,2)), index=['a', 'c'],
                         columns=['three','two'])
df_layer = pd.concat([df_layer1,df_layer2],sort=False,keys=['level1','level2'])
# print(df_layer)

#如果传入的是字典,则字典的键就会当作keys选项的值
df_dict = pd.concat({'level1':df_layer1,'level2':df_layer2},axis=1)
# print(df_dict)
#unstack 列-转-行
# print(s_layer_index.unstack())

#处理当前分析工作无关的dataframe行索引,将
df_ignore_1 = pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
df_ignore_2 = pd.DataFrame(np.random.randn(2,3),columns=['b','d','a'])
# print(df_ignore_1)
# print(df_ignore_2)
df_not_ignore = pd.concat([df_ignore_1,df_ignore_2],ignore_index=True)
df_ignore =pd.concat([df_ignore_1,df_ignore_2],ignore_index=True)

# print(df_not_ignore)
# print(df_ignore)

#合并重叠数据(类似于if-else)类似于覆盖数据
#np.where
a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index=['f','e','d','c','b','a'])
b = pd.Series(np.arange(len(a)),dtype=np.float64,index=['f','e','d','c','b','a'])
# print(a)
# print(b)
a_if_else = np.where(pd.isnull(a),b,a)
# print(a_if_else)
#combine_first
a_c_f = b[:].combine_first(a[:])
# print(a_c_f)

#重塑和轴向旋转
#stack 列-转-行
#unstack 行-转-列
data_for_stack = pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['ohio','colorado'],
                                                                     name='state'),
                          columns=pd.Index(['one','two','three'],name='number'))
result_stack = data_for_stack.stack()
# print(data_for_stack)
# print(result_stack)

#对于一个层次化索引的Series,可以用unstack将其重排为一个dataframe
result_unstack = data_for_stack.unstack()
#默认情况下,unstack操作的是其最内层(stack也是),传入分层级别的编号或名称即可对其他级别进行unstack操作.
# print(result_unstack)

result_state_unstack = data_for_stack.unstack('state')
# print(result_state_unstack)

#如果不是所有的级别值都能在各分组中找到的话,则unstack操作可能会引入缺失数据(默认),因此该运算可逆
s1_unstack =pd.Series([0,1,2,3],index=['a','b','c','d'])
s2_unstack =pd.Series([4,5,6],index=['c','d','e'])
data_unstack = pd.concat([s1_unstack,s2_unstack],keys=['one','two'])

# print(data_unstack.unstack())
# print(data_unstack.unstack().stack())

#在对dataframe进行unstack操作时,作为旋转轴的级别将会成为结果中的最低级别
df_unstack = pd.DataFrame({'left':result_stack,'right':result_stack+5},
                          columns=pd.Index(['left','right'],name='side'))
# print(df_unstack)
# print(df_unstack.unstack('state'))
# print(df_unstack.unstack('state').stack('side'))


#'长格式'旋转为'宽格式'
pass

#数据转换
#移除重复数据pd.duplicated(返回一个布尔型的Series)
data_duplicated = pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})
# print(data_duplicated)
# print(data_duplicated.duplicated())
#drop_duplicates,用于返回一个删除重复行的dataframe
# print(data_duplicated.drop_duplicates())
#以上方法默认判断全部列
#指定重复列删除
data_duplicated['v1']=range(7)
# print(data_duplicated)
data_duplicated.drop_duplicates()
# print(data_duplicated.drop_duplicates())
#duplicated及drop_duplicates默认保留第一个出现的值组合,设置take_last则保留最后一个(现在改为keep)
d_=data_duplicated.drop_duplicates(['k1','k2'],keep='last')
# print(d_)

#利用函数或映射进行数据转换
data_trans = pd.DataFrame({'food':
                               ['bacon','pulled pork','bacon','pastrami','corned beef',
                                'bacon','pastrami','honey ham','nova lox','others'],
                           'ounces':[4,3,12,6,7.5,8,3,5,6,7]})

meat_to_animal = {'bacon':'pig',
                  'pulled pork':'pig',
                  'pastrami':'cow',
                  'corned beef':'cow',
                  'honey ham':'pig',
                  'nova lox':'salmon'
                  }
data_trans['animals'] = data_trans['food'].map(str.lower).map(meat_to_animal)

#替换值
#replace
data_replace = pd.Series([1.,-999.,2.,-999.,-1000.,3.])
# print(data_replace)


# print(data_replace.replace(-999.,np.nan))

#一次性替换多个
# print(data_replace.replace([-999.,-1000,],np.nan))

#对不同值进行不同替换
# print(data_replace.replace([-999.,-1000,],[np.nan,0]))

#传入的参数也可以是dict
# print(data_replace.replace({-999.:np.nan,-1000.:0}))

#重命名索引轴
data_reindex = pd.DataFrame(np.arange(12).reshape((3,4)),
                            index=['ohio','colorado','new york'],
                            columns=['one','two','three','four'])
# print(data_reindex)

#map方法
# data_reindex.index = data_reindex.index.map(str.upper)
# print(data_reindex)

#rename默认只创建数据集的转换版(而非修改原始数据)若需要原地修改,则修改inplace = True
data_reindex.rename(index = str.title,columns = str.upper)
# print(data_reindex.rename(index = str.title,columns = str.upper))
#rename可以结合字典型对象实现部分轴标签的更新
data_reindex.rename(index={'ohio':'indiana'},columns={'three':'peekaboo'})
# print(data_reindex.rename(index={'ohio':'indiana'},columns={'three':'peekaboo'}))
data_reindex.rename(index = str.title,columns = str.upper,inplace=True)
# print(data_reindex)

#离散化和面元划分(类似于分组)
ages =[20,22,25,27,23,23,21,37,61,45,41,32]

group_names = ['youth','young adult','middle age','senior']
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
#修改闭端方向right=False
cats_change = pd.cut(ages,bins,right=False,labels=group_names)
# print(cats,'\n',cats_change)
# print(pd.value_counts(cats_change))

#传入面元(分组)数量而非具体边界,precision(数据精度)
data_edge_number = np.random.randn(20)
cut_by_edge_number = pd.cut(data_edge_number,4,precision=2)
# print(cut_by_edge_number)

#qcut(cut可能无法用于使各个分组中含有相同数量的数据点)而,qcut使用的是
#样本分位数,因此可以得到大小基本相等的面元(分组)
data_for_qcut = np.random.randn(1000)
data_qcut = pd.qcut(data_for_qcut,4,precision=1) #按四分位数进行切割

#qcut可以自定义分位数(0~1之间,包括端点)
index_for_user_defined_qcut = [0, 0.1, 0.5, 0.9, 1.]

data_user_defined_qcut = pd.qcut(data_for_qcut,index_for_user_defined_qcut)

# print(pd.value_counts(data_user_defined_qcut))

#检测和过滤异常值
np.random.seed(12345)
data_for_outlier = pd.DataFrame(np.random.rand(1000,4))
#describe,数据描述性分析
# print(data_for_outlier.describe())
col = data_for_outlier[3]
#选出全部含有"大于0.5或-0.5"的记录,可以用dataframe的any方法
# print(data_for_outlier[(np.abs(data_for_outlier)>0.5).any(1)])
#将值限制在区间-0.5到0.5之内
data_for_outlier[np.abs(data_for_outlier)>0.5]=np.sign(data_for_outlier)*0.5
# print(data_for_outlier)

#排列和随机采样

#排列
df_arrange =pd.DataFrame(np.arange(5*4).reshape((5,4)))
sampler = np.random.permutation(5)
# print(sampler)
#permutation(不用替换方式选取随机子集)
# print(df_arrange.take(sampler))
# print(df_arrange)
# print(df_arrange.take(np.random.permutation(len(df_arrange))[:3]))
#替换方式产生样本
bag = np.array([5,7,-1,6,4])
sampler_1 = np.random.randint(0,len(bag),size=10)
draws = bag.take(sampler_1)
# print(draws)



