# 1. 导入numpy库并简写为 np (★☆☆)
import numpy as np

# %%
# 2. 打印numpy的版本和配置说明 (★☆☆)
print(np.__version__)
# np.show_config

# %%
# 3. 创建一个长度为10的空向量 (★☆☆)
array = np.empty(shape=(10,))
print(array, '\n', array.shape)

# %%
# 4. 如何找到任何一个数组的内存大小？ (★☆☆)
print(array.size)
print('{} bytes'.format(array.size * array.itemsize))

# %%
# 5.如何从命令行得到numpy中add函数的说明文档? (★☆☆)¶
print(np.info(np.add))

# %%
# 6. 创建一个长度为10并且除了第五个值为1的空向量 (★☆☆)¶
array = np.empty(shape=(10,))
array[4] = 1
print(array)

# %%
# 7. 创建一个值域范围从10到49的向量(★☆☆)
array = np.arange(10, 50)
print(array)

# 8. 反转一个向量(第一个元素变为最后一个) (★☆☆)
array = array[::-1]
print(array)

# %%
# 9. 创建一个 3x3 并且值从0到8的矩阵(★☆☆)
array = np.arange(0, 9).reshape(3, 3)
print(array)

# %%
# 10. 找到数组[1,2,0,0,4,0]中非0元素的位置索引 (★☆☆)¶
nonz = np.random.randint(0, 10, size=(10,))
print(np.nonzero(nonz), '\n', nonz, '\n', nonz[np.nonzero(nonz)])

# %%
# 11. 创建一个 3x3 的单位矩阵 (★☆☆)
eye = np.eye(3)
print(eye)

# %%
# 12. 创建一个 3x3x3的随机数组 (★☆☆)¶
"""
注意:
np.random.random为随机数组
np.random.randn() 从标准正态分布中返回一个或多个样本值。
numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中
"""

array_random = np.random.random((3, 3))
print(array_random)

# %%
# 13. 创建一个 2x5 的随机数组并找到它的最大值和最小值 (★☆☆)
"""
注意max和min中axis的参数,0表示求列的最值,1表示行
"""
array_max_min = np.random.random((2, 5))
print(array_max_min)
print(array_max_min.max())
print(array_max_min.min())
print('col max: {}'.format(array_max_min.max(axis=0)))
print('row max: {}'.format(array_max_min.max(axis=1)))

# 14. 创建一个长度为30的随机向量并找到它的平均值 (★☆☆)¶
"""
axis的参数,0表示求列的均值,1表示行
"""
array_avg = np.random.random((3, 4))
print(array_avg)
print(np.average(array_avg))
print('row avg: {}'.format(np.average(array_avg, axis=1)))
print('col avg: {}'.format(np.average(array_avg, axis=0)))

# %%
# 15. 创建一个二维数组，其中边界值为1，其余值为0 (★☆☆)
array = np.ones((5, 5))
array[1:-1, 1:-1] = 0
print(array)

# 16. 对于一个存在在数组，如何添加一个用0填充的边界? (★☆☆)
array = np.random.random((3, 3))
np.pad(array, pad_width=1, mode='constant', constant_values=0)

# %%
# 17. 以下表达式运行的结果分别是什么? (★☆☆)
# (提示: NaN = not a number, inf = infinity)

print(0 * np.nan)
# nan
print(np.nan == np.nan)
# False
print(np.inf > np.nan)
# False
print(np.nan - np.nan)
# nan
print(0.3 == 3 * 0.1)
# False

# 18. 创建一个 5x5的矩阵，并设置值1,2,3,4落在其对角线下方位置 (★☆☆)¶
array = np.diag(range(1, 5), k=-1)
print(array)

# 19. 创建一个8x8 的矩阵，并且设置成棋盘样式 (★☆☆)¶
array = np.zeros((8, 8))
array[::2, ::2] = 1
array[1::2, 1::2] = 1
print(array)

# 20. 考虑一个 (6,7,8) 形状的数组，其第100个元素的索引(x,y,z)是什么?
"""
注: index从(0,0,0) 开始排
"""
print(np.unravel_index(100, (6, 7, 8)))

# %%
# 21. 用tile函数去创建一个 8x8的棋盘样式矩阵(★☆☆)¶
"""
Numpy的 tile() 函数，就是将原矩阵横向、纵向地复制。
tile 是瓷砖的意思，顾名思义，这个函数就是把数组像瓷砖一样铺展开来。
"""

array = np.array([[1, 0], [0, 1]])
array_tile = np.tile(array, (4, 4))
print(array_tile)


# 22. 对一个5x5的随机矩阵做归一化(★☆☆)

def z_score(arr):
    a_max = np.max(arr)
    a_min = np.min(arr)
    f = (arr - a_min) / (a_max - a_min)
    return f


array = np.random.random((5, 5))
print(z_score(array))

# %%
"""
23. 创建一个将颜色描述为(RGBA)四个无符号字节的自定义dtype？(★☆☆)
"""
color = np.dtype([('r', np.ubyte, 1), ('g', np.ubyte, 1),
                  ('b', np.ubyte, 1), ('a', np.ubyte, 1)])

# %%
# 24. 一个5x3的矩阵与一个3x2的矩阵相乘，实矩阵乘积是什么？ (★☆☆)¶

arr53 = np.arange(1, 16).reshape(5, 3)
array32 = np.arange(1, 7).reshape(3, 2)
array = np.dot(arr53, array32)
print(array)

# %%
# 25. 给定一个一维数组，对其在3到8之间的所有元素取反 (★☆☆)¶
array = np.arange(1, 10)
array[(array >= 3) & (array <= 8)] *= -1
print(array)

# %%
# 26. 下面脚本运行后的结果是什么? (★☆☆)¶
print(sum(range(5), -1))
from numpy import *

print(sum(range(5), -1))

# %%
# 27. 考虑一个整数向量Z,下列表达合法的是哪个? (★☆☆)¶
"""
Z**Z  
2 << Z >> 2  
Z <- Z  
1j*Z  
Z/1/1  
Z<Z>Z
"""

'错误的是 Z<Z>Z'
z = np.arange(5)
print(z)
print(2 << z >> 2)
print(2 > z < 2)
# 2 << Z >> 2  # false
# Z<Z>Z    # false

# %%
"""28. 下列表达式的结果分别是什么?(★☆☆)"""
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))


# %%
"""29. 如何从零位对浮点数组做舍入 ? (★☆☆)"""
"""
numpy.copysign(array1,array2)       将第二个数组中值得符号复制给第一个数组中值
numpy.ceil(array)                   向上取整,也就是取比这个数大的整数 
numpy.random.uniform(low,high,size)
功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
"""
z = np.random.uniform(-10, 10, 10)
print(np.copysign(np.ceil(np.abs(z)), z))
print(z)

# %%
# 30. 如何找到两个数组中的共同元素? (★☆☆)
arr1 = np.random.randint(0, 10, 5)
arr2 = np.random.randint(0, 10, 5)
print(arr1, arr2)
print(np.intersect1d(arr1, arr2))

# %%
#
'''31. 如何忽略所有的 numpy 警告(尽管不建议这么做)? (★☆☆)'''
# Suicide mode on
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
print(Z)

# Back to sanity
_ = np.seterr(**defaults)

# An equivalent way, with a context manager:
with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0

# %%
# 32. 下面的表达式是正确的吗? (★☆☆)
"""
np.sqrt(-1) 
这句代码的输出是nan，因为在实数域里不能对一个负数开平方。
"""

# np.sqrt(-1) == np.emath.sqrt(-1)
"""
np.emath.sqrt(-1)
这句代码的输出是1j，也就是一个虚数（python里虚数不能直接写j，前面必须要加一个常数），
这样是不是就理解了前面说的“数学函数的输出数据类型与输入的某些域中的输入数据类型不同”，从实数域可以变到复数域。
"""

# %%
# 33. 如何得到昨天，今天，明天的日期? (★☆☆)

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print('yesterday is {}'.format(str(yesterday)))
print('today is {}'.format(str(today)))
print('tomorrow is {}'.format(str(tomorrow)))

# %%
"""34. 如何得到所有与2016年7月对应的日期？ (★★☆)¶"""
array_day = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(array_day)

# %%
# 35. 如何直接在位计算(A+B)\*(-A/2)(不建立副本)? (★★☆)¶

"""
out	
n维数组，None，或者多维数组组成的元组，可选参数	
指定结果存储的位置。若提供此参数，其必须与输入数组扩充后的维度保持一致。
如果不提供此参数或者此参数为None，返回一个新建的数组。若此参数为元组，
其长度和输出值的个数保持一致。
"""

a = np.ones(3) * 1
b = np.ones(3) * 2
c = np.ones(3) * 3

np.add(a, b, out=b)
np.divide(a, 2, out=a)
np.negative(a, out=a)
np.multiply(a, b, out=a)

# %%
# 36. 用五种不同的方法去提取一个随机数组的整数部分(★★☆)
z = np.random.uniform(-10, 10, 10)

# 1.z - z%1 (向下取整)
print(z)
print(z - z % 1)
# 2.around  (四舍五入)
print(np.around(z, 0))
#  3.ceil(向上取整)
print(np.ceil(z))
#   4.floor(向下取整)
print(np.floor(z))
#   5.trunc(向0取整)
print(np.trunc(z))
#   6.rint   四舍五入
print(np.rint(z))
#   7.astype
print(z.astype(int))

# %%
'''37. 创建一个5x5的矩阵，其中每行的数值范围从0到4 (★★☆)'''
"""
当矩阵 x 非常大时，在Python中计算显式循环可能会很慢。注意，
向矩阵 x 的每一行添加向量 v 等同于通过垂直堆叠多个 v 副本来形成矩阵 vv，
然后执行元素的求和x 和 vv。 我们可以像如下这样实现这种方法：
"""

"""
如果数组不具有相同的rank，则将较低等级数组的形状添加1，
直到两个形状具有相同的长度。
如果两个数组在维度上具有相同的大小，或者如果其
中一个数组在该维度中的大小为1，则称这两个数组在维度上是兼容的。
个数组的大小大于1的任何维度中，第一个数组的行为就像沿着该维度复制一样
"""
array = np.zeros((5, 5))
arr1 = np.arange(0, 5)
array = array + arr1
print(array)


# %%
# 38. 通过考虑一个可生成10个整数的函数，来构建一个数组(★☆☆)
# (提示: np.fromiter)

def generator():
    for i in range(10):
        yield i


array_gen = np.fromiter(generator(), count=-1, dtype=int)
print(array_gen)

# %%
# 39. 创建一个长度为10的随机向量，其值域范围从0到1，但是不包括0和1 (★★☆)

array = np.linspace(0, 1, 11, endpoint=False)[1:]
print(array)

# %%
# 40. 创建一个长度为10的随机向量，并将其排序 (★★☆)
array = np.random.random(10)
print(array)
array.sort()
print(array)

# %%
"""41.对于一个小数组，如何用比 np.sum更快的方式对其求和？(★★☆)"""
# (提示: np.add.reduce)
array = np.arange(10)
print(np.add.reduce(array))

# %%
"""42. 对于两个随机数组A和B，检查它们是否相等(★★☆)"""
a = np.random.randint(0, 2, 5)
b = np.random.randint(0, 2, 5)
# Assuming identical shape of the arrays and a tolerance for the comparison of values
eq = np.allclose(a, b)
print(eq)
# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
eq = np.array_equal(a, b)
print(eq)

a = np.array([1, 0])
b = np.array([0, 1])
print(np.allclose(a, b))
print(np.array_equal(a, b))

# %%
'''43. 创建一个只读数组(read-only) (★★☆)'''
z = np.zeros(10)
z.flags.writeable = False
z[0] = 1

# %%
'''44. 将笛卡尔坐标下的一个10x2的矩阵转换为极坐标形式(★★☆)'''
z = np.random.random((10, 2))
x, y = z[:, 0], z[:, 1]
r = np.sqrt(x ** 2, y ** 2)
t = np.arctan(y, x)
print(r)
print(t)

# %%
# 45. 创建一个长度为10的向量，并将向量中最大值替换为1 (★★☆)
array = np.random.random(10)
print(array)
array[array.argmax()] = 1
print(array)

# %%
'''46. 创建一个结构化数组，并实现 x 和 y 坐标覆盖 [0,1]x[0,1] 区域 (★★☆)'''

z = np.zeros((5, 5), [('x', float), ('y', float)])
print(z)
z['x'], z['y'] = np.meshgrid(np.linspace(0, 1, 5), np.linspace(0, 1, 5))
print(z)

# %%
'''47. 给定两个数组X和Y，构造Cauchy矩阵C (Cij =1/(xi - yj))'''
x = np.arange(8)
y = x + 0.5
c = 1.0 / np.subtract.outer(x, y)
print(np.subtract(x, y))
print(np.linalg.det(c))
# %%
'''48. 打印每个numpy标量类型的最小值和最大值？ (★★☆)'''
# Z = np.arange(100)
# v = np.random.uniform(0,100)
# index = (np.abs(Z-v)).argmin()
# print (Z[index])


# %%
'''48. 打印每个numpy标量类型的最小值和最大值？ (★★☆)'''
for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)

for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)

# %%
# 49. 如何打印一个数组中的所有数值? (★★☆)¶

z = np.zeros((10, 10))
np.set_printoptions(threshold=z.shape[0] * z.shape[1])
print(z)

# %%
# 50. 给定标量时，如何找到数组中最接近标量的值？(★★☆)
array = np.arange(10)
v = np.random.uniform(0, 100)

index = (np.abs(array - v).argmin())
print(array[index])

# %%
'''51. 创建一个表示位置(x,y)和颜色(r,g,b)的结构化数组(★★☆)'''
z = np.zeros(10, [('position', [('x', float, 1), ('y', float, 1)]),
                  ('color', [('r', float, 1), ('g', float, 1), ('b', float, 1)])])
print(z.shape)

# %%
# 52. 对一个表示坐标形状为(100,2)的随机向量，找到点与点的距离(★★☆)
z = np.random.random((100, 2))
x, y = np.atleast_2d(z[:, 0], z[:, 1])
d = np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)
print(d)

'''方法2'''
# Much faster with scipy
import scipy.spatial

D = scipy.spatial.distance.cdist(z, z)
print(D)

# %%
# 53. 如何将32位的浮点数(float)转换为对应的整数(integer)?
array = np.arange(10, dtype=float)
array = array.astype(dtype=int, copy=False)
print(array)

# %%
# 54. 如何读取以下文件? (★★☆)
# (提示: np.genfromtxt)

# %%
'''55. 对于numpy数组，enumerate的等价操作是什么？(★★☆)¶'''
z = np.arange(9).reshape(3, 3)
for index, value in np.ndenumerate(z):
    print(index, value)

for index in np.ndindex(z.shape):
    print(index, z[index])

# %%
# 57. 对一个二维数组，如何在其内部随机放置p个元素? (★★☆)
# (提示: np.put, np.random.choice)
p = 3
array = np.zeros((3, 3))
print(array)
np.put(array, np.random.choice(range(9), p, replace=False), np.random.randint(1, 10, 3))
print(array)

# %%
# 58. 减去一个矩阵中的每一行的平均值 (★★☆)
'''
注意mean里面的axis和keepdims参数
'''

array = np.arange(16).reshape(4, 4)
amean = array.mean(axis=1, keepdims=True)
print(array)
print(array - amean)

'''mean求出来为一行,因为numpy的广播机制,所以将其转换为一列,然后和array相减即可'''
# 方法2
# y = array - array.mean(axis=1).reshape(-1, 1)
# print(y)

# %%
# 59. 如何通过第n列对一个数组进行排序? (★★☆)¶

z = np.random.randint(0, 10, size=(3, 3))
print(z)
print(z[z[:, -1].argsort()])

# %%
# 60. 如何检查一个二维数组是否有空列？(★★☆)
'''~表示取反
any表示至少有一个实数,False表示全部为0即空列
'''
z = np.random.randint(0, 3, (4, 10))
print(z)
print(z.any(axis=0))

# %%
# 61. 从数组中的给定值中找出最近的值 (★★☆)
"""
ndarray.flat    1-D iterator over the array. /将数组转换为1-D的迭代器 flat返回的是一个迭代器，可以用for访问数组每一个元素
ndarray.flatten(order=’C’)  将数组的副本转换为一个维度，并返回
    可选参数，order：{‘C’,‘F’,‘A’,‘K’}
    ‘C’：C-style，行序优先
    ‘F’：Fortran-style，列序优先
    ‘A’：if a is Fortran contiguous in memory ,flatten in column_major order
    ‘K’：按照元素在内存出现的顺序进行排序
默认为’C’
"""
array = np.random.uniform(0, 1, 1000).reshape(20, 50)
a = 0.5
# m = array.flat[np.abs(array - a).argmin()]
# t = array[np.abs(array - a).argmin()]
print(array[array.argmin()])
# print(array)
# print(t)
# print(m)

# %%
'''62. 如何用迭代器(iterator)计算两个分别具有形状(1,3)和(3,1)的数组? (★★☆)'''
a = np.arange(3).reshape(3, -1)
b = np.arange(3).reshape(-1, 3)
it = np.nditer([a, b, None])
for x, y, z in it:
    z[...] = x + y
print(it.operands[2])

# %%
'''63. 创建一个具有name属性的数组类(★★☆)'''

# class NamedArray(np.ndarray):
#     def __new__(cls, array, name="no name"):
#         obj = np.asarray(array).view(cls)
#         obj.name = name
#         return obj
#     def __array_finalize__(self, obj):
#         if obj is None: return
#         self.info = getattr(obj, 'name', "no name")

# Z = NamedArray(np.arange(10), "range_10")
# print (Z.name)

# %%
'''64. 考虑一个给定的向量，如何对由第二个向量索引的每个元素加1(小心重复的索引)? (★★★)'''
# (提示: np.bincount | np.add.at)

array = np.zeros(10)
print(array.size)
i = np.random.randint(0, array.size, 20)
array += np.bincount(i, minlength=array.size)
print(i)
print(array)

# 方法2
# np.add.at(array, i, 1)
# print(array)

# %%
'''65. 根据索引列表(I)，如何将向量(X)的元素累加到数组(F)? (★★★)'''

x = [1, 2, 3, 4, 5, 6]
i = [1, 3, 9, 3, 4, 1]
f = np.bincount(i, x)
print(f)

# %%
'''66. 考虑一个(dtype=ubyte) 的 (w,h,3)图像，计算其唯一颜色的数量(★★★)'''
# (提示: np.unique)

w, h = 16, 16
I = np.random.randint(0, 2, (h, w, 3)).astype(np.ubyte)
# Note that we should compute 256*256 first.
# Otherwise numpy will only promote F.dtype to 'uint16' and overfolw will occur
F = I[..., 0] * (256 * 256) + I[..., 1] * 256 + I[..., 2]
n = len(np.unique(F))
print(n)

# %%
'''67. 考虑一个四维数组，如何一次性计算出最后两个轴(axis)的和？ (★★★)'''
array = np.arange(0, 16).reshape(2, 2, 2, 2)
s = array.sum(axis=(-2, -1))
np.set_printoptions(16)
print(array)
print(s)

# 方法2
s = array.reshape(array.shape[:-2] + (-1,)).sum(axis=-1)
print(s)

# %%

'''68. 考虑一个一维向量D，如何使用相同大小的向量S来计算D子集的均值？(★★★)'''
D = np.random.uniform(0, 1, 100)
S = np.random.randint(0, 10, 100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)
print(D)

# %%
# 69. 如何获得点积 dot prodcut的对角线? (★★★)

a = np.arange(9).reshape(3, 3)
b = np.arange(1, 10).reshape(3, 3)
c = np.dot(a, b)
print(c)
print(np.diag(np.dot(a, b)))

# %%
# 70. 考虑一个向量[1,2,3,4,5],如何建立一个新的向量，在这个新向量中每个值之间有3个连续的零？(★★★)
a = np.array([1, 2, 3, 4, 5])
z = np.zeros(a.size * 4)
z[::4] = a
print(z)

# %%
'''71. 考虑一个维度(5,5,3)的数组，如何将其与一个(5,5)的数组相乘？(★★★)'''
A = np.ones((5, 5, 3))
B = 2 * np.ones((5, 5))
print(A * B[:, :, None])

# %%
# 72. 如何对一个数组中任意两行做交换? (★★★)¶
a = np.arange(25).reshape(5, 5)
a[[0, 1]] = a[[1, 0]]
print(a)

# %%
'''74. 给定一个二进制的数组C，如何产生一个数组A满足np.bincount(A)==C(★★★)
(提示: np.repeat)
'''
c = np.array([1, 1, 2, 3, 4, 4, 6])
a = np.repeat(np.arange(len(c)), c)
print(a)

# %%
'''77. 如何对布尔值取反，或者原位(in-place)改变浮点数的符号(sign)？(★★★)¶
(提示: np.logical_not, np.negative)'''

z = np.random.randint(0, 2, 100)
print(z)
np.logical_not(z, out=z)
print(z)

# %%
# 81. 考虑一个数组Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
# 如何生成一个数组R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ...,[11,12,13,14]]? (★★★)¶
# 参考
'''https://blog.csdn.net/shwan_ma/article/details/78244044?utm_medium=distribute.pc_
relevant_t0.none-task-blog-searchFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant_
t0.none-task-blog-searchFromBaidu-1.control'''

Z = np.arange(1, 15, dtype=np.uint32)
R = np.lib.stride_tricks.as_strided(Z, (11, 4), (4, 4))
print(R)

# %%
'''
82. 计算一个矩阵的秩(★★★)
(提示: np.linalg.svd)
'''
Z = np.random.uniform(0, 1, (10, 10))
U, S, V = np.linalg.svd(Z)  # Singular Value Decomposition
rank = np.sum(S > 1e-10)
print(rank)

# %%
# 83. 如何找到一个数组中出现频率最高的值？
# (提示: np.bincount, argmax)

z = np.random.randint(0, 10, 50)
print(z)
print(np.bincount(z))
print(np.bincount(z).argmax())

# %%
'''84. 从一个10x10的矩阵中提取出连续的3x3区块(★★★)'''
#  参考81
# Z = np.random.randint(0,5,(10,10))

Z = np.arange(0, 100).reshape(10, 10)
n = 4
i = 1 + (Z.shape[0] - 4)
j = 1 + (Z.shape[1] - 4)

print(Z.strides)
C = np.lib.stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
print(C)

# %%
# 89. 如何找到一个数组的第n个最大值? (★★★)
z = np.arange(1000)
np.random.shuffle(z)

n = 3
# slow
print(z[np.argsort(z)[-n]])

# 方法2
# Fast
# argpartition
print(z[np.argpartition(-z, n)[:n]])

# %%
# 90. 给定任意个数向量，创建笛卡尔积(每一个元素的每一种组合)(★★★)¶


# %%
# 92. 考虑一个大向量Z, 用三种不同的方法计算它的立方(★★★)
# np.power(z,3)
# z*z*z


# %%
'''
93. 考虑两个形状分别为(8,3) 和(2,2)的数组A和B. 如何在
数组A中找到满足包含B中元素的行？(不考虑B中每行元素顺序)？ (★★★)¶
'''
# numpy中包含的newaxis可以给原数组增加一个维度


a = np.random.randint(0, 5, (8, 3))
b = np.random.randint(0, 5, (2, 2))

c = (a[..., np.newaxis, np.newaxis] == b)
rows = np.where(c.any((3, 1)).all(1))[0]
print(rows)
print(a, '\n', b)

# %%
# 94. 考虑一个10x3的矩阵，分解出有不全相同值的行 (如 [2,2,3]) (★★★)

z = np.random.randint(0, 3, (10, 3))

e = np.all(z[:, :-1] == z[:, 1:], axis=1)
print(z)
print(z[~e])
print(z[e])

# %%
# 96. 给定一个二维数组，如何提取出唯一的(unique)行?(★★★)
Z = np.random.randint(0, 2, (6, 3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ)
