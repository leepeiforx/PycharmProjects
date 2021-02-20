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
# #��������
obj_1['insert_temp_col']= ''

#ɾ����
# del obj_1['insert_temp_col']
# # print(obj_1)
# print(obj_1['year'])
# print(obj_1.state)
#
# obj_2 = pd.DataFrame(pop)
# print(obj_2)

#��������
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

#����ָ�����ϵ���
# new_obj = obj_1.drop(['one','three'])
# print(new_obj)

#����,ѡȡ�͹���
obj_4 = pd.Series(np.arange(4.), index=['a','b','c','d'])
# print(obj_4['b'],'\n',obj_4['c':'d'])
#
# print(obj_1[obj_1['pop']>2])
#
# print(obj_1.ix[obj_1.year< 2002, :3])


#������������ݶ���
s1= pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = pd.Series([-2.1,3.6,-1.5,3.1,-1],index=['a','c','e','f','g'])
# print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape(3,3),columns=list('abc'),
                   index=['ohio','utah','colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bcd'),
                   index=['utah','ohio','texas','oregon'])


#���������������ֵ,.add������(df2)�д��ڶ�df1��û�еĲ���Ϊ0

df1.add(df2,fill_value = 0)

df3 = df1.add(df2,fill_value = 0)
# print(df3.reindex(columns=df2.columns,fill_value = 0))

frame = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),
                     index=['utah','ohio','texa','oregon'])

series2 =pd.Series(range(3), index=list('bde'))

series4 = pd.Series(range(4),index=['utah','ohio','texa','oregon'])

# print(series2)

# #ˮƽ�㲥
# print(frame+series2)
# #��ֱ�㲥
# print(frame.add(series4,axis = 0))

#���������
#����
obj_sort = pd.Series(range(4),index=list('dabc'))

# print(obj_sort.sort_values())
# print(obj_sort.sort_index())
''
frame_obj = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three','one'],
                         columns=list('dabc'))

frame_f = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),
                       index=['utah','ohio','texa','oregon'])

#����Ӧ�ú�ӳ��
# print(frame_f)
# print(np.abs(frame_f))

# Ԫ�ؼ����鷽��
def f(x):
    return pd.Series([x.max(), x.min()], index=['max', 'min'])

f0 = lambda x:x.max()-x.min()
# print(frame_f.apply(f0))
# print(frame_f.apply(f0, axis=1))
#
# print(frame_f.apply(f, axis=1))
#Ԫ�ؼ�python����Ҳ��ʹ��,(applymap)
format = lambda x: '%.2f'%x

# print(frame_f.applymap(format))
#
# print(frame_obj.sort_index(axis=0))
# print(frame_obj.sort_index(axis=1))

#pandas��ȡcsv�ļ�
#��csv�ļ�����UTF-8����,��Ҫ����encoding����
csv_path =r'D:\System_files\Desktop\reguar_expression\temp_csv.csv'
# csv_table = pd.read_csv(csv_path,encoding='gb18030',header=None)
#����
#����������ʹ��index_col,(�������ö������Ϊ������)
csv_table = pd.read_csv(csv_path,encoding='gbk',names=['a','b','c'],index_col=['a'])
# print(csv_table)

#NA����
csv_table = pd.read_csv(csv_path, encoding='gbk', names=['a', 'b', 'c'],
                        index_col=['a'], na_values=['NULL'])
#�������ֶ�Ϊ����ָ����ͬ��NA���ֵ
sentials = {'b':['foo', 'NA'],
            'c': ['two']}
csv_table = pd.read_csv(csv_path, encoding='gbk', names=['a', 'b', 'c'],
                        index_col=['a'], na_values=sentials)

# #ͳ��NAN����
# print((csv_table.isnull().sum()))
# #ɾ��NAN
# print(csv_table.dropna())
# #�滻NAN
# print(csv_table.fillna('change'))

#����ȡ�ı��ļ�
# result = pd.read_csv(csv_path,encoding='gbk',nrows=1000)
# print(result)


chunk = pd.read_csv(csv_path,encoding='gbk',chunksize=1000)
tot = pd.Series([])
for piece in chunk:
    tot = tot.add(piece['��ҵ��'].value_counts(),fill_value =0)

# sorted(tot,reverse=False)
# print(tot)

#�ļ�д�����ı���ʽ
out_file =r'D:\System_files\Desktop\reguar_expression\out.csv'
tot.to_csv(out_file,na_rep='NULL',index=False,header=False)

#�ϲ����ݼ�
#pandas.maerge  , pandas.concat
df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                   'data1':(range(7))})
df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':(range(3))})

# print(df1)
# print(df2)

#��û��ָ����,��mergeĬ�ϰ��ص����е�������Ϊ��
df_merge = pd.merge(df1,df2,on='key')
# print(df_merge)

df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],
                   'data1':(range(7))})
df4 = pd.DataFrame({'rkey':['a','b','d'],
                    'data2':(range(3))})

#���������һ��,��Ҫ��������on(Ĭ��merge������'inner'����)
df_merge2 =pd.merge(df3,df4,left_on='lkey',right_on='rkey')
# print(df_merge2)

#'how'�����������ӷ�ʽ(left,right,outer,inner)
df_left =pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='left')
df_right =pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='right')
df_outer = pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='outer')
df_inner = pd.merge(df3,df4,left_on='lkey',right_on='rkey',how='inner')
# print(df_left)
# print(df_right)
# print(df_outer)
# print(df_inner)

#������ϲ�,����һ����������ɵ��б���
left = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','three'],
                     'lval':[1,2,3]})
right =pd.DataFrame({'key1':['foo','foo','bar','bar'],
                     'key2':['one','two','three','four'],
                     'rval':[4,5,6,7]})
plural_merge = pd.merge(left,right,on=['key1','key2'],how='outer')
# print(plural_merge)

#�����ϵĺϲ�
#left_index =True #right_index=True
left_index = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','three'],
                     'lval':[1,2,3]},index=['a','b','c'])
right_index =pd.DataFrame({'key1':['foo','foo','bar','bar'],
                     'key2':['a','b','c','d'],
                     'rval':[4,5,6,7]})
df_merge_index =pd.merge(left_index,right_index,left_index=True,right_on='key2',
                         how='outer')
#��λ�����
lefth = pd.DataFrame({'key1':['ohio','ohio','ohio','nevada','nevada'],
                      'key2':[2000,2001,2002,2001,2002],
                      'data':np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6,2)),index=[['nevada','nevada','ohio','ohio','ohio','ohio'],
                                                          [2001,2000,2000,2000,2001,2002]],
                      columns=['event1','event2'])
# print(lefth)
# print(righth)
#���������,�������б���ʽ���������ϲ����Ķ���(ע����ظ�����ֵ�Ĵ���)
complex_left_merge = pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='left')
# print(complex_left_merge)

complex_outer_merge = pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='outer')
# print(complex_outer_merge)

#ͬʱʹ�úϲ�˫��������
left2 = pd.DataFrame([[1.,2],[3.,4],[5.,6]],index=['a','c','e'],
                     columns=['ohio','nevada'])
right2 = pd.DataFrame([[7,8],[9.,10],[11.,12],[13,14]],index=['b','c','d','e'],
                      columns=['missour1','alabama'])
# print(left2)
# print(right2)
both_index_merge = pd.merge(left2,right2,how='outer',left_index=True,right_index=True)
# print(both_index_merge)

#ʹ��join�����ϲ�(Ĭ��������)ע��join�����iterable
left_use_join = left2.join(right2,how='outer')
# print(left_use_join)
#���ڼ������ϲ�,������join����һ��DataFrame
another = pd.DataFrame([[7,8],[9.,10],[11.,12.],[16.,17.]],index=['a','c','e','f'],columns=['new york','oregon'])
left_use_join2 = left2.join([right2,another])
# print(left_use_join2)

#��������,Ҳ��Ϊ����,�󶨻�ѵ�,np�е�concatenate
arr=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

#axis=1��ʾ���жѵ�
# arr_con = np.concatenate([arr,arr],axis=1)
arr_con = np.concatenate([arr,arr],axis=0)
# print(arr_con)

#pd�е�concatע��concat�������iterable
s1 =pd.Series([0, 1], index=['a','b'])
s2 =pd.Series([2, 3, 4], index=['c','d','e'])
s3 =pd.Series([5, 6], index=['f', 'g'])
pd_concat = pd.concat([s1,s2,s3],axis=0)
# pd_concat = pd.concat([s1,s2,s3],axis=1)
# print(pd_concat)
s4 = pd.concat([s1*5,s3])
# print(s1,s4)
s5 = pd.concat([s1, s4],axis=1,sort=True)

#join_axes ָ��Ҫ����������ʹ�õ�����
s5_index =pd.concat([s1, s4],axis=1,sort=True,join_axes=[['a','b','c','d']])
# print(s5)
# print(s5_index)

s6=pd.concat([s1,s4],axis=1,join='inner')
# print(s6)

#�����λ�����,ʹ��keys
# s_layer_index = pd.concat([s1,s1,s3],keys=['one','two','three'])
#��axis =1��series���кϲ�,��keys�ͻ��Ϊdataframe����ͷ,ͬ�����߼���dataframeҲ����

s_layer_index = pd.concat([s1,s1,s3],axis=1, keys=['one','two','three'],sort=True)
# print(s_layer_index)

df_layer1 =pd.DataFrame(np.arange(6).reshape((3, 2)), index=['a', 'b', 'c'],
                        columns=['one', 'two'])
df_layer2 = pd.DataFrame(5+np.arange(4).reshape((2,2)), index=['a', 'c'],
                         columns=['three','two'])
df_layer = pd.concat([df_layer1,df_layer2],sort=False,keys=['level1','level2'])
# print(df_layer)

#�����������ֵ�,���ֵ�ļ��ͻᵱ��keysѡ���ֵ
df_dict = pd.concat({'level1':df_layer1,'level2':df_layer2},axis=1)
# print(df_dict)
#unstack ��-ת-��
# print(s_layer_index.unstack())

#����ǰ���������޹ص�dataframe������,��
df_ignore_1 = pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
df_ignore_2 = pd.DataFrame(np.random.randn(2,3),columns=['b','d','a'])
# print(df_ignore_1)
# print(df_ignore_2)
df_not_ignore = pd.concat([df_ignore_1,df_ignore_2],ignore_index=True)
df_ignore =pd.concat([df_ignore_1,df_ignore_2],ignore_index=True)

# print(df_not_ignore)
# print(df_ignore)

#�ϲ��ص�����(������if-else)�����ڸ�������
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

#���ܺ�������ת
#stack ��-ת-��
#unstack ��-ת-��
data_for_stack = pd.DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['ohio','colorado'],
                                                                     name='state'),
                          columns=pd.Index(['one','two','three'],name='number'))
result_stack = data_for_stack.stack()
# print(data_for_stack)
# print(result_stack)

#����һ����λ�������Series,������unstack��������Ϊһ��dataframe
result_unstack = data_for_stack.unstack()
#Ĭ�������,unstack�������������ڲ�(stackҲ��),����ֲ㼶��ı�Ż����Ƽ��ɶ������������unstack����.
# print(result_unstack)

result_state_unstack = data_for_stack.unstack('state')
# print(result_state_unstack)

#����������еļ���ֵ�����ڸ��������ҵ��Ļ�,��unstack�������ܻ�����ȱʧ����(Ĭ��),��˸��������
s1_unstack =pd.Series([0,1,2,3],index=['a','b','c','d'])
s2_unstack =pd.Series([4,5,6],index=['c','d','e'])
data_unstack = pd.concat([s1_unstack,s2_unstack],keys=['one','two'])

# print(data_unstack.unstack())
# print(data_unstack.unstack().stack())

#�ڶ�dataframe����unstack����ʱ,��Ϊ��ת��ļ��𽫻��Ϊ����е���ͼ���
df_unstack = pd.DataFrame({'left':result_stack,'right':result_stack+5},
                          columns=pd.Index(['left','right'],name='side'))
# print(df_unstack)
# print(df_unstack.unstack('state'))
# print(df_unstack.unstack('state').stack('side'))


#'����ʽ'��תΪ'���ʽ'
pass

#����ת��
#�Ƴ��ظ�����pd.duplicated(����һ�������͵�Series)
data_duplicated = pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})
# print(data_duplicated)
# print(data_duplicated.duplicated())
#drop_duplicates,���ڷ���һ��ɾ���ظ��е�dataframe
# print(data_duplicated.drop_duplicates())
#���Ϸ���Ĭ���ж�ȫ����
#ָ���ظ���ɾ��
data_duplicated['v1']=range(7)
# print(data_duplicated)
data_duplicated.drop_duplicates()
# print(data_duplicated.drop_duplicates())
#duplicated��drop_duplicatesĬ�ϱ�����һ�����ֵ�ֵ���,����take_last�������һ��(���ڸ�Ϊkeep)
d_=data_duplicated.drop_duplicates(['k1','k2'],keep='last')
# print(d_)

#���ú�����ӳ���������ת��
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

#�滻ֵ
#replace
data_replace = pd.Series([1.,-999.,2.,-999.,-1000.,3.])
# print(data_replace)


# print(data_replace.replace(-999.,np.nan))

#һ�����滻���
# print(data_replace.replace([-999.,-1000,],np.nan))

#�Բ�ֵͬ���в�ͬ�滻
# print(data_replace.replace([-999.,-1000,],[np.nan,0]))

#����Ĳ���Ҳ������dict
# print(data_replace.replace({-999.:np.nan,-1000.:0}))

#������������
data_reindex = pd.DataFrame(np.arange(12).reshape((3,4)),
                            index=['ohio','colorado','new york'],
                            columns=['one','two','three','four'])
# print(data_reindex)

#map����
# data_reindex.index = data_reindex.index.map(str.upper)
# print(data_reindex)

#renameĬ��ֻ�������ݼ���ת����(�����޸�ԭʼ����)����Ҫԭ���޸�,���޸�inplace = True
data_reindex.rename(index = str.title,columns = str.upper)
# print(data_reindex.rename(index = str.title,columns = str.upper))
#rename���Խ���ֵ��Ͷ���ʵ�ֲ������ǩ�ĸ���
data_reindex.rename(index={'ohio':'indiana'},columns={'three':'peekaboo'})
# print(data_reindex.rename(index={'ohio':'indiana'},columns={'three':'peekaboo'}))
data_reindex.rename(index = str.title,columns = str.upper,inplace=True)
# print(data_reindex)

#��ɢ������Ԫ����(�����ڷ���)
ages =[20,22,25,27,23,23,21,37,61,45,41,32]

group_names = ['youth','young adult','middle age','senior']
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
#�޸ıն˷���right=False
cats_change = pd.cut(ages,bins,right=False,labels=group_names)
# print(cats,'\n',cats_change)
# print(pd.value_counts(cats_change))

#������Ԫ(����)�������Ǿ���߽�,precision(���ݾ���)
data_edge_number = np.random.randn(20)
cut_by_edge_number = pd.cut(data_edge_number,4,precision=2)
# print(cut_by_edge_number)

#qcut(cut�����޷�����ʹ���������к�����ͬ���������ݵ�)��,qcutʹ�õ���
#������λ��,��˿��Եõ���С������ȵ���Ԫ(����)
data_for_qcut = np.random.randn(1000)
data_qcut = pd.qcut(data_for_qcut,4,precision=1) #���ķ�λ�������и�

#qcut�����Զ����λ��(0~1֮��,�����˵�)
index_for_user_defined_qcut = [0, 0.1, 0.5, 0.9, 1.]

data_user_defined_qcut = pd.qcut(data_for_qcut,index_for_user_defined_qcut)

# print(pd.value_counts(data_user_defined_qcut))

#���͹����쳣ֵ
data_for_outlier = pd.DataFrame(np.random.rand(1000,4))
#describe,���������Է���
print(data_for_outlier.describe())
col = data_for_outlier[3]