# %%
# 1.导入numpy (★☆☆)
import numpy as np

# %%
# 2.输出numpy版本和配置
print(np.__version__)

# %%
# 3.创建一个长度为10的数组
z = np.zeros(10)
print(z)

# %%
# 4.如何获得任一数组的内存大小 (★☆☆)
print(z.size, z.itemsize)

# %%
# 5. 如何通过命令行获得numpy add function的doc? (★☆☆)
# %run `python -c "import numpy; numpy.info(numpy.add)"`


# %%
# 6.创建一个长度为10的空数组，并把第五个元素设为1 (★☆☆)
z = np.empty(10)
z[4] = 5
print(z)

# %%
# 7. 创建一个值为[10，49]的数组 (★☆☆)

arr = np.arange(10, 50)
print(arr)

# %%
# 8. 转换一个数组（第一个元素变为最后一个） (★☆☆) 倒序
arr = arr[::-1]
print(arr)

# %%
# 9. 创建一个值为[0,8]的3*3矩阵 (★☆☆)
arr = np.arange(9).reshape(3, 3)
print(arr)

# %%
# 10. 从[1,2,0,0,4,0]中找到非零元素的索引值 (★☆☆)
arr = np.array([1, 2, 0, 0, 4, 0])
arr.nonzero()

# %%
# 11. 创建一个3*3的对角矩阵 (★☆☆)
arr = np.eye(3, 3)
print(arr)

z = np.arange(9).reshape(3, 3)
arr = np.diag(np.diag(z))
print(arr)

# %%
# 12,创建一个333的随机数组 (★☆☆)
arr = np.random.randn(3, 3, 3)
print(arr)

arr = np.random.random((3, 3, 3))
print(arr)

arr = np.random.rand(3, 3, 3)
print(arr)

# 13创建一个10*10的随机矩阵，并找到最大值与最小值
arr = np.random.randint(0, 10, size=(10, 10))
print(arr)
print(arr.max())
print(arr.min())

# %%
# 14.创建一个大小30的随机数组，并计算其均值 (★☆☆)
arr = np.random.randint(0, 10, size=(5, 6))
# axis=0 -> 行
arr_meanby_r = arr.mean(axis=0)
print(arr_meanby_r)
# axis=1 -> 列
arr_meanby_c = arr.mean(axis=1)
print(arr_meanby_c)

# 15.创建一个以边缘为1，内部为0的2维数组
arr = np.ones([4, 4])
arr[1:-1, 1:-1] = 0
print(arr)

# %%
# 16 如何在现有数组周围添加边框（填充0）
ones = np.ones((5, 5))
arr = np.pad(ones, pad_width=2, mode='constant')
print(arr, ones)

# %%
# 17. 下列表达式的输出是什么? (★☆☆)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
# 1,nan     2,False     3,False,    4,nan   5,False

# %%
# 18,在对角线下方创建一个值为1,2,3,4的5x5矩阵 (★☆☆)
arr_diag = np.diag(range(1, 5), k=-1)
arr_diag = np.diag([1, 2, 3, 4], k=-1)
arr_diag = np.diag(np.arange(4) + 1, k=-1)
print(arr_diag)

# %%
# 19,创建一个8x8矩阵并用棋盘图案填充它 (★☆☆)
z = np.zeros((8, 8))
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print(z)

# %%
# 20, 给定一个678的数组，如何输出第100个元素的（x，y，z）的值


# %%
# 21. 使用tile函数创建棋盘格8x8矩阵 (★☆☆)


# %%
# 22,归一化一个5*5的随机矩阵 (★☆☆)
arr = np.random.random((5, 4))
arrmax = arr.max(axis=0)
arrmin = arr.min(axis=0)
arr = (arr - arrmin) / (arrmax - arrmin)
print(arr)

Z = np.random.random((5, 5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin) / (Zmax - Zmin)
print(Z)

# %%
# 23,创建一个自定义dtype，将颜色描述为四个无符号字节（RGBA） (★☆☆)


# %%
# 24,将5x3矩阵乘以3x2矩阵 (★☆☆)
arr1 = np.random.random((5, 3))
arr2 = np.random.randn(3, 2)
arr3 = np.dot(arr1, arr2)

print(arr3)

# %%
# 25,给定一维数组，否定所有在3到8之间的元素。 (★☆☆)
arr = np.arange(9)
arr = arr[(arr >= 3) & (arr <= 8)]
print(arr)

# %%
# 26. 下列脚本的输出？ (★☆☆)
# print(sum(range(5), -1))
# print(sum(range(5), -1))
from numpy import *

print(sum(range(5), -1))

# %%
# 27. 考虑整数向量Z，这些表达式中哪些是合规的？ (★☆☆)
Z = np.arange(9)

print(Z)
# print(Z ** Z)
print(2 << Z)
# print(Z < - Z)
# print(1j * Z)
# print(Z / 1 / 1)
# print(Z<Z>Z)
# print(Z<Z>Z) 该项不合规

# %%
# 28. 下列脚本的输出是什么?
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

# 1 warning nan
# 2 warning 0
# 3 浮点数...


# %%
# 29.如何将浮点数组从零舍入？（★☆☆）
arr = np.random.uniform(0, 10, 10)
print(arr)
# print(np.ceil(np.abs(arr)))
print(np.copysign(np.ceil(np.abs(Z)), Z))

# %%
# 30,如何找到两个数组中同时出现的值? (★☆☆)
arr1 = np.random.randint(0, 10, 10)
arr2 = np.random.randint(0, 10, 10)
print(arr1, arr2)
print(np.intersect1d(arr1, arr2))

# %%
# 31. 如何忽略所有的Numpy Warning? (★☆☆)
defaults = np.seterr(all='ignore')
z = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)
z = np.ones(1) / 0

# An equivalent way, with a context manager:

with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0

# %%
# 32,以下表达式是否为True? (★☆☆)
print(np.sqrt(-1) == np.emath.sqrt(-1))

# %%
# 33,如何获得昨天、今天和明天的日期? (★☆☆)
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(yesterday, today, tomorrow)

# %%
# 34,如何获得2016年7月整月的日期? (★★☆)
z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(z)

# %%
# 35. 如何就地计算((A+B)*(-A/2))? (★★☆)
a = np.ones(3) * 1
b = np.ones(3) * 2
c = np.ones(3) * 3
np.add(a, b, out=b)
np.divide(a,2,out=a)
np.negative(a,out=a)
print(np.multiply(a,b))

#%%
# 36,使用5种不同的方法提取随机数组的整数部分 (★★☆)

z = np.random.uniform(-10,10,10)
print(z - z%1)
print(np.floor(z))
print(np.ceil(z) - 1)
print(z.astype(int))
print(np.trunc(z))

#%%
#37, 创建一个5*5的矩阵，每一行的值均为0到4 (★★☆)
a = np.zeros((5,5))
b = np.arange(5)
print(a+b)

#%%
# 38. 设计生成10个整数的生成器函数并使用它来构建数组 (★☆☆)

def generate():
    for i in range(10):
        yield i

arr = np.fromiter(generate(),dtype=int,count=-1)
print(arr)


#%%
# 39. 创建一个大小为10的向量，其值范围为(0,1) (★★☆)
