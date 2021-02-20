import numpy as np
from datetime import  datetime,date,time
import bisect
import pandas as pd
excel_path =r'D:\System_files\Desktop\劳动竞赛最终奖励数据.xlsx'
exc_table = pd.read_excel(excel_path,sheet_name='培训费奖励',na_values='')
print(exc_table)

data1 = [6, 7.5, 8, 0 ,1]
arr1 = np.array(data1)
# print(arr1)
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr_ones = np.ones(16).reshape((4, 4))
arr_zero = np.zeros(10).reshape((2, 5))
# print(arr_ones)
# print(arr_zero)
# print(arr2)
# print(arr2.shape)
# print(arr2.ndim)
# print(arr2.dtype)
arr_empty = np.empty((3,3))
# print(arr_empty)

arr_type_change = np.arange(20).reshape((4,5))
ap = arr_type_change.astype(np.float64)
# print(arr_type_change.dtype)
# print(ap.dtype)
#
# print(arr1[3])
# print(arr1[1:3])
arr1[3:5]=-0.1
# print(arr1)
arr_copy = arr1.copy()

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d[2])
# print(arr2d[2,:])
# print(arr2d[2:,:])
# print(arr2d[:,:2])
# print(arr2d[1,:2])
# print(arr2d[1,:2])
# print(arr2d[1:2,:2])

# print(arr2d[1,1])
# print(arr2d[1][0])
# print(arr2d[:2,1:])



arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr3d)
# print(arr3d[1,0])
# print(arr3d[:2,1:])
# print(arr3d[2])


names = np.array(['bob','joe','will','bob','will','joe'])
data = np.random.randn(6,4)
# print(names == 'bob')
# print(data)
# print(data[names =='bob'])
# print(data[names !='will'])


dt1 = datetime(2011,10,29,20,30,21)
# print(dt.date())
# print(dt.day)
# print(dt.minute)

# dt_t = dt.time()

#strftime用于将datetime格式化为字符串
# print(dt1.strftime('%y-%m-%d %H:%M'))
#strptime可以将字符串转化为datetime对象
dt_s=datetime.strptime('20091031','%Y%m%d')
# print(dt_s)

dt1.replace(minute=0,second=0)
dt2 = datetime(2011,11,15,22,30)
delta = dt2 - dt1
# print(delta)
delta_plus = dt1+delta
# print(delta_plus)

a = [7,2,5,1,3]
a.sort()
# print(a)
b = ['saw','small','he','foxes','six']
b.sort(key=len,reverse=True)
# print(b)
c= [1,2,2,2,3,4,7]
#bisect.bisect用来确定新元素被插入到哪个位置才能保持原列表的有序性
#bisect.insort用来确实地将新新元素插入到那个位置上
# print(bisect.bisect(c,2))
bisect.insort(c,5)
# print(c)

#内置的序列函数
#enumerate
some_list = ['foo','bar','baz']
mapping = dict((v,i) for i,v in enumerate(some_list))
# print(mapping)

#sorted
sort_list =[1,-1,2,3,0,4,6]
# print(sorted(sort_list))
# print(sort_list)

#zip
seq1 = ['foo','bar','baz']
seq2 = ['one','two','three']
seq3 = [True,False]

print(list(zip(seq1,seq2,seq3)))

for i,(a,b) in enumerate(zip(seq1,seq2)):
    print('%d: %s,%s'%(i,a,b))

#利用zip进行解包
pitchers=[('nolan','ryan'),('roger','clemens'),('schilling','curt')]
first_name, last_name =zip(*pitchers)
print(first_name)
print(last_name)

#reversed
print(list(reversed(range(10))))

#字典
empty_dict = {}

d1 = {'a':'some value','b':[1, 2, 3, 4]}
d1[7] = 'an interger'
print(d1)
print(d1['b'])

#del和pop(删除指定值将其返回)可以删除值
# del d1[7]
# ret = d1.pop('a')
# print(ret)
# print(d1)
print(d1.values())
print(d1.keys())

#update字典合并
d1.update({
    'b':'foo',
    'c':12
})
print(d1)

#从序列类型创建字典
# mapping = {}
# for key,value in zip(key_list,value_list):
#     mapping[key] = value

mapping = dict(zip(range(5),reversed(range(5))))
print(mapping)

