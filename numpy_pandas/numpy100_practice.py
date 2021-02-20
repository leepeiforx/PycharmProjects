# %%

# 1.导入 NumPy
import numpy as np

# %%

# 2. 查看 NumPy 版本信息
print(np.__version__)

# %%

# 3. 通过列表创建一维数组
np.array([1, 2, 3])

# %%

# 4.通过列表创建二维数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
# %%

# 5. 创建全为0的二维数组
np.zeros((2, 2))

# %%

# 6.创建全为1的三维数组
np.ones((3, 3, 3))

# %%
# 7.创建一维等差数组
np.linspace(0, 10, num=10, endpoint=False)
np.arange(11)

# %%
# 8.创建二维等差数组
np.arange(6).reshape((3, 2))

# %%

# 9.创建单位矩阵（二维数组）
np.eye(3)

# %%

# 10.创建等间隔一维数组
np.linspace(0, 10, 6)

# %%
# 11.创建二维随机数组
print(np.random.rand(3, 3))

# %%
# 12.创建二维随机整数数组（数值小于 5）
print(np.random.randint(0, 5, size=(3, 3)))


# %%
# 13. 依据自定义函数创建数组
def return_minus(x1):
    return x1 - 1


arr_func = np.fromfunction(return_minus, (5,))
print(arr_func)

# %%

# 数组运算
# 14.一维数组加法运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

# %%

# 15.一维数组减法运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a - b)

# %%

# 16.一维数组乘法运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a * b)

# %%

# 17. 一维数组除法运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a / b)

# %%
# 矩阵运算
a_2d = np.array([[1, 2], [3, 4]])
b_2d = np.array([[5, 6], [7, 8]])
# 18. 矩阵加法运算
print(a_2d + b_2d)
# 19. 矩阵减法运算
print(a_2d - b_2d)
# 20. 矩阵元素间乘法运算
print(a_2d * b_2d)
# 21. 矩阵乘法运算
print(np.dot(a_2d, b_2d))
# 22. 数乘矩阵
print(a_2d * 2)
# 23. 矩阵的转置
print(a_2d.T)
print(np.transpose(a_2d))
print(a_2d.transpose())
# 24. 矩阵求逆
print(np.linalg.inv(a_2d))

# %%

# 数学函数
# 25.三角函数
a = np.array([0, 1, 2])
print(np.sin(a))

# %%

# 26.以自然对数函数为底数的指数函数
np.exp(a)
# 27. 数组的方根的运算（开平方）
print(np.sqrt(a))
print(np.power(a, 0.5))
# 28. 数组的方根的运算（立方）
print(np.power(a, 3))

# %%

# 29.数组切片和索引
# 一维数组索引
a = np.array([1, 2, 3])
print(a[0], a[-1])
# 一维数组切片
print(a[:2], a[:-1])
# 二维数组索引
a_2d = np.arange(16).reshape((4, 4))
print(a_2d[2, 3], '\n', a_2d[-1, -1])
# 二维数组切片（取第 2 列）
print(a_2d[:, 1])
# 二维数组切片（取第 2，3 行）
print(a_2d[1:3, :])

# %%

# 30.数组形状操作
a = np.random.rand(3, 2)

# %%

# 31.查看数组形状
print(a.shape)

# %%

# 32.更改数组形状（不改变原始数组）
b = a.reshape(2, 3)

# %%

# 33.更改数组形状（改变原始数组）
b.resize(3, 2)

# %%

# 37. 展平数组
a = np.arange(0, 16).reshape(4, 4)
# print(a)
# print(np.ravel(a)[7])
np.ravel(a)

# %%

# 38. 垂直拼合数组
a = np.random.randint(10, size=(3, 3))
b = np.random.randint(10, size=(3, 3))
c = np.vstack((a, b))
print(c)

# %%

# 39.水平拼合数组
np.hstack((a, b))

# %%

# 40.沿纵轴分割数组
print(a)
np.vsplit(a, 3)

# %%

# 41.数组排序
a = np.array(([1, 4, 3], [6, 2, 9], [4, 7, 2]))
# 返回每列最大值
print(np.max(a, axis=1))
# 返回每行最小值
print(np.min(a, axis=0))
# 返回每列最大值索引
print(np.argmax(a, axis=1))
# 返回每行最小值索引
print(np.argmin(a, axis=0))

# %%

# 数组统计
# 42.统计数组各列的中位数(这里的0,1表示行列和上面的最值的表示相反)
print(np.median(a, axis=0))
# 统计数组各行的算术平均值
print(np.mean(a, axis=1))
# 统计数组各列的加权平均值
print(np.average(a, axis=0))
# 统计数组各行的方差
print(np.var(a, axis=1))
# 统计数组各列的标准偏差
print(np.std(a, axis=0))

# %%
# 创建一个 5x5 的二维数组，其中边界值为1，其余值为0
z = np.ones((5, 5))
z[1:-1, 1:-1] = 0
print(z)

# %%

# 43.使用数字 0 将一个全为 1 的 5x5 二维数组包围?
z = np.ones((5, 5))
# numpy.pad(array, pad_width, mode='constant', **kwargs)
# array为要填补的数组
# pad_width是在各维度的各个方向上想要填补的长度,如（（1，2），（2，2）），
# 表示在第一个维度上水平方向上padding=1,垂直方向上padding=2,
# 在第二个维度上水平方向上padding=2,垂直方向上padding=2。
# 如果直接输入一个整数，则说明各个维度和各个方向所填补的长度都一样。
#  mode为填补类型，即怎样去填补，有“constant”，“edge”等模式，
# 如果为constant模式，就得指定填补的值，如果不指定，则默认填充0

z3 = np.pad(z, pad_width=[(1, 1), (1, 1)], mode='constant', constant_values=0)
print(z3)

# %%

# 44.创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方
# 对角矩阵
# numpy.diag(v,k=0)
#     v : array_like.
#
# 如果v是2D数组，返回k位置的对角线。
#
# 如果v是1D数组，返回一个v作为k位置对角线的2维数组。
#
#     k : int, optional
#
# 对角线的位置，大于零位于对角线上面，小于零则在下面。
z = np.diag(np.linspace(1, 5, num=4, endpoint=False), k=-1)
print(z)

# %%

# 45.创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置
z = np.random.randint(1, 10, size=(10, 10))

for x in range(np.shape(z)[0]):
    for y in range(np.shape(z)[1]):
        if x == y and x % 2 != 0:
            z[x, y] = 0
        elif x == y and x % 2 == 0:
            z[x, y] = 1
print(z)

# %%

# 46.创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数
arr_ar = np.arange(11)
# 方案1
np.where((arr_ar > 1) & (arr_ar <= 9), arr_ar * -1, arr_ar)
# 方案2
arr_ar[(1 < arr_ar) & (arr_ar <= 9)] *= -1
print(arr_ar)

# %%

# 47.找出两个一维数组中相同的元素
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
print(Z1)
print(Z2)
print(np.intersect1d(Z1, Z2))

# %%

# 48.使用 NumPy 打印昨天、今天、明天的日期?
yesterday = np.datetime64('today', 'D') - np.timedelta64('1', 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64('1', 'D')
print(yesterday, today, tomorrow)

# %%

# 49.使用五种不同的方法去提取一个随机数组的整数部分
arr_rondom = np.random.uniform(0, 10, 10)
print('原始值', arr_rondom)
print('方法1:', arr_rondom.astype(int))
print('方法2:', np.trunc(arr_rondom))
print('方法3:', np.floor(arr_rondom))
print('方法4:', np.around(arr_rondom))
print('方法2:', arr_rondom - arr_rondom % 1)

# %%

# 50.创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5
z = np.zeros((5, 5))
z += np.arange(5)
print(z)

# %%

# 51.创建一个长度为 5 的等间隔一维数组，
# 其值域范围从 0 到 1，但是不包括 0 和 1
print(np.linspace(0, 1, num=6, endpoint=False)[1:])

# %%

# 52.创建一个长度为10的随机一维数组，并将其按升序排序
arr_random = np.random.rand(10)
print(np.sort(arr_random))
arr_random.sort()
print(arr_random)

# %%

# 53.创建一个 3x3 的二维数组，并将列按升序排序
arr_random = np.random.rand(3, 3)
arr_random.sort(axis=0)
print(arr_random)

# %%

# 54.创建一个长度为 5 的一维数组，并将其中最大值替换成 0
z = np.random.rand(5)
z[np.argmax(z)] = 0
z[z.argmax()] = 0
print(z)

# %%

# 55.打印每个 NumPy 标量类型的最小值和最大值
for dtype in [np.int8, np.int32, np.int64]:
    print('The minimum value of {}:'.format(dtype), np.iinfo(dtype).min)
    print('The maximum value of {}:'.format(dtype), np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print('The minimum value of {}:'.format(dtype), np.iinfo(dtype).min)
    print('The maximum value of {}:'.format(dtype), np.iinfo(dtype).max)

# %%

# 将 float32 转换为整型
z = np.arange(10, dtype=np.float32)
print(z)
z = z.astype(np.int32, copy=False)
print(z)
# %%
# 将随机二维数组按照第 3 列从上到下进行升序排列
z = np.random.randint(0, 10, (5, 5))
print('排列前', z)
print('排列后', z[z[:, 2].argsort()])

# %%
# 从随机一维数组中找出距离给定数值（0.5）最近的数
z = np.random.randint(0, 10, size=(5,))
value = 0.5
m = z[np.abs(z - value).argmin()]
print(z)
print(m)

# %%

# 将二维数组的前两行进行顺序交换
a = np.arange(10).reshape((2, 5))
print(a)
a[[0, 1]] = a[[1, 0]]
print(a)

# %%
# 找出随机一维数组中出现频率最高的值
z = np.random.randint(0, 10, 50)
# print(z)
print(np.bincount(z))
print(z[np.bincount(z).argmax()], np.bincount(z).max(initial=0))

# %%

# 找出给定一维数组中非 0 元素的位置索引
z = np.nonzero([1, 0, 2, -1, 0, 0])
print(z)

# %%

# 71. 对于给定的 5x5 二维数组，在其内部随机放置 p 个值为 1 的数
p = 3
z = np.zeros((5, 5))
# 方案1
# for i in range(p):
#     z[np.random.randint(0,5),np.random.randint(0,5)]=1
# 方案2
np.put(z, np.random.choice(range(5 * 5), p), 1)
print(np.random.choice(range(5 * 5), p))
print(z)

# %%

# 对于随机的 3x3 二维数组，减去数组每一行的平均值
z = np.random.randint(0, 10, size=(3, 3))
print(z)
z = z - z.mean(axis=1, keepdims=True)
z2 = z - z.mean(axis=1, keepdims=False)
print(z)
print(z2)

# %%

# 获得二维数组点积结果的对角线数组
a = np.random.uniform(0, 1, (3, 3))
b = np.random.uniform(0, 1, (3, 3))
print(np.dot(a, b))
# 方案1(较慢)
print(np.diag(np.dot(a, b)))
# 方案2(较快)
print(np.sum(a * b.T, axis=1))
# 方案3?
print(np.einsum("ij, ji->i", a, b))

# %%

# 找到随机一维数组中前 p 个最大值
p = 5
z = np.random.randint(0, 100, 50)
print(z[z.argsort()[-p:]])

# %%

# 计算随机一维数组中每个元素的 4 次方数值
z = np.random.randint(0, 5, 5)
x = np.power(z, 4)
print(z)
print(x)

# %%

# 对于二维随机数组中各元素，保留其 2 位小数
z = np.random.rand(5, 5)
print(z)
np.set_printoptions(precision=2)
print(z)

# %%

# 使用科学记数法输出 NumPy 数组
z = np.random.rand(5, 5)
print(z)
print(z / 1e3)

# %%

# 使用 NumPy 找出百分位数（25%，50%，75%）
z = np.arange(10)
print(z)
print(np.percentile(z, q=[25, 50, 75]))

# %%

# 找出数组中缺失值的总数及所在位置
z = np.random.rand(5, 5)
z[np.random.randint(5, size=5), np.random.randint(5, size=5)] = np.nan
print('缺失值总量:', np.isnan(z).sum())
print('缺失值索引:', np.where(np.isnan(z)))
print(z)

# %%

# 从随机数组中删除包含缺失值的行
print(z, '\n')
print(z[np.sum(np.isnan(z), axis=1) == 0])

# %%

# 统计随机数组中的各元素的数量
z = np.random.randint(0, 100, 25).reshape((5, 5))
print(np.unique(z, return_counts=True))

# %%

# 将数组中各元素按指定分类转换为文本值?
z = np.random.randint(1, 3, 10)
print(z)
label_map = dict(zip((1, 2, 3), ('汽车', '公交车', '火车')))
print(label_map)
print(np.array([label_map[x] for x in z]).reshape((2, -1)))

# %%

# 将多个 1 维数组拼合为单个 Ndarray
z1 = np.arange(3)
z2 = np.arange(4, 7)
z3 = np.arange(7, 11)
print(z)
print(np.concatenate([z1, z2, z3]))

# %%

# 打印各元素在数组中升序排列的索引
a = np.random.randint(1, 100, 20)
print(a.argsort())

# %%

# 得到二维随机数组各行的最大值
a = np.random.randint(1, 20, size=(4, 5))
print(a)
print(a.max(axis=1, initial=0))

# %%

# 得到二维随机数组各行的最小值（区别上面的方法）?
print(np.apply_along_axis(np.min, axis=1, arr=a))

# %%

# 87. 计算两个数组之间的欧氏距离
a = np.array([1, 2])
b = np.array([7, 8])
# 数学方法
print(np.sqrt(np.power((8 - 2), 2) + np.power((7 - 1), 2)))

# numpy?
print(np.linalg.norm(b - a))

# %%

# 打印复数的实部和虚部
a = np.array([1 + 2j, 3 + 4j, 5 + 6j])
print("实部:", a.real)
print('虚部', a.imag)

# %%

# 求解给出矩阵的逆矩阵并验证
matrix = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(matrix)

# allclose
assert np.allclose(np.dot(inv, matrix), np.eye(2))


# np.dot(inv,matrix) == np.eye(2)

# %%

# 使用 Z-Score 标准化算法对数据进行标准化处理?
def z_score(array, axis=None):
    amin = array.min(axis=axis, keepdims=True)
    amax = array.max(axis=axis, keepdims=True)
    result = (array - amin) / (amax - amin)
    return result


z = np.random.randint(10, size=(5, 5))
np.set_printoptions(precision=2)
print('Z标准化后', '\n', z_score(z))


# %%

# 使用 L2 范数对数据进行标准化处理?
def I2_normalize(v1, axis=1, order=2):
    I2 = np.linalg.norm(v, ord=order, axis=axis, keepdims=True)
    I2[I2 == 0] = 1
    return v1 / I2


z = np.random.randint(10, size=(5, 5))
print(z)
print('范数标准化后', '\n', I2_normalize(z))

# %%

# 使用 NumPy 计算变量直接的相关性系数?
z = np.array([[1, 2, 1, 9, 10, 3, 2, 6, 7],  # 特征 A
              [2, 1, 8, 3, 7, 5, 10, 7, 2],  # 特征 B
              [2, 1, 1, 8, 9, 4, 3, 5, 7]])  # 特征 C
print(np.corrcoef(z))

# %%

# 使用 NumPy 计算矩阵的特征值和特征向量?
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w, v = np.linalg.eig(m)
# 我们可以通过 P'AP=M 公式反算，验证是否能得到原矩阵。
# v * np.diag(w) * np.linalg.inv(v)
print(m)
print(v)
# print(v*np.diag(w)*np.linalg.inv(v))
print(np.dot(v, np.diag(w), np.linalg.inv(v)))

# %%

# 使用 NumPy 计算 Ndarray 两相邻元素差值?
z = np.random.randint(1, 10, 10)
print(z)
print(np.diff(z, n=1))
print(np.diff(z, n=2))
print(np.diff(z, n=3))

# %%

# 使用 NumPy 将 Ndarray 相邻元素依次累加
z = np.random.randint(1, 10, 10)
np.cumsum(z)

# %%

# 使用 NumPy 按列连接两个数组?
m1 = np.array([1, 2, 3])
m2 = np.array([4, 5, 6])
print('按列连接', np.c_[m1, m2])
print(np.vstack((m1, m2)).T)
print('m1:', m1)
print('m2', m2)

# %%

# 使用 NumPy 按行连接两个数组?
m1 = np.array([1, 2, 3])
m2 = np.array([4, 5, 6])
# np.r_[m1, m2]
print('按行连接', np.r_[m1, m2])
print('按行连接', np.hstack([m1, m2]))
print('m1:', m1)
print('m2', m2)

# %%

# 构造9*9乘法表
np.fromfunction(lambda x1, y1: (x1 + 1) * (y1 + 1), (9, 9))
