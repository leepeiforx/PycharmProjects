# list tuple,str,dict,set

# %%
# list的创建与删除
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
a_list = []  # 创建控列表

list((3, 7, 9, 10, 11))  # 讲元组转换为列表

list(range(1, 10, 2))  # 将range对象转换为列表

list('hello world')  # 将字符串转换为列表

list({3, 8, 5})  # 将字典的'键'转换为列表

list({'a': 3, 'b': 9, 'c': 78})  # 将字典的"键:值"转换为列表

x = list()  # 创建控列表

del x  # 删除列表对象

# %%
import sys

sys.getrefcount(1)  # 查看值的引用次数
x = 1
sys.getrefcount(1)  # 有新变量引用该值,其引用计数器+1
y = 2
sys.getrefcount(1)
del x
del y
sys.getrefcount(1)

import gc

gc.collect()  # 立刻进行垃圾回收,返回被清理的对象数量

# %%
# 列表元素访问

x = list('python')
print(x)

print(x[0])  # 下标为0的元素,即第一个元素
print(x[-1])  # 下标为-1的元素,即最后一个元素

# %%
# 列表常用方法

str_list = ['python', 'c++', 'a', 'o', 'c']
str_list.append(x)
str_list.extend(x)
str_list.insert(1, 'c')
str_list.remove('y')
str_list.pop(2)
str_list.index('o')
str_list.count('o')
str_list.reverse()
reversed(str_list)
str_list.sort(key=str, reverse=False)  # False为升序
sorted(str_list, key=str, reverse=True)
str_list.clear()
str_list.copy()

# %%
# 列表对象支持的运算符
'+'

x = [1, 2, 3]
print(id(x))
x = x + [4]  # 连接两个列表
print(id(x))  # 内存地址发生改变

x += [5]  # 为列表追加元素
print(id(x))  # 内存地址不变
print(x)

# %%
# '*'序列重复
x = [1, 2, 3, 4]
print(id(x))
x = x * 2  # 元素重复,返回新列表
print(id(x))  # 地址发生改变

x *= 2  # 元素重复,原地进行
print(id(x))  # 地址不变

print([1, 2, 3] * 0)  # 重复0次,清空

# %%
# 内置函数对列表的操作

x = list(range(11))
import random

random.shuffle(x)  # 打乱列表中元素的顺序
print(x)

all(x)  # 测试是否所有元素都等价于true
any(x)  # 测试收复年存在等价于true的元素
max(x)
max(x, key=str)
min(x)
sum(x)
len(x)

list(zip(x, [1] * 11))  # 多列表元素重新组合
list(zip(range(1, 4)))  # zip()函数也可以用于一个序列或迭代对象
list(zip(['a', 'b', 'c'], [1, 2]))  # 如果两个序列不等长,以短的为准
enumerate(x)  # 枚举列表元素,返回enuerate对象
list(enumerate(x))  # enumerate对象可以转换为列表,元素,集合

# %%
# 列表推导式语法与应用
# [expression for expr1 in sequence1 if condiction]
a_list = [x * x for x in range(10)]
# 列表推导式在逻辑上等价于一个循环语句,只是形式上更为简洁
a_list = list(map(lambda x: x * x, range(10)))
a_list = list(map(lambda x: pow(x, 2), range(10)))

freshfruit = ['banana', 'loganberry', 'passion fruit']
a_list = [x.strip() for x in freshfruit]

a_list = list(map(lambda x: x.strip(), freshfruit))

a_list = list(map(str.strip, freshfruit))

sum([2 ** i for i in range(64)])

# %%
# 实现嵌套列表的平铺
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[num for elem in vec for num in elem]
# [num 外层循环 内层循环]

from itertools import chain

print(list(chain(*vec)))


# 多层嵌套平铺

def flat_list(lst):
    result = []

    def nested(lst):
        for item in lst:
            if isinstance(item, list):
                nested(item)
            else:
                result.append(item)

    nested(lst)
    return result


lst = [[1, 2, 3], [4, [5, 6]], [8, [9, [10]]]]

print(flat_list(lst))

# %%
# 过滤不符合条件的元素
import os

print([filename for filename in os.listdir('.') if filename.endswith('py')])

alist = [-1, -4, 6, 7, 5, -2.3, 9, -11]
[i for i in alist if isinstance(i, int) and i > 0]

socres = {'zhang san': 45, 'li si': 78, 'wang wu': 40, 'zhou liu': 96, 'zhao qi': 65,
          'sun ba': 90, 'zheng jiu': 78, 'wu shi': 99, 'ddong shiyi': 60}

highest = max(socres.values())
lowest = min(socres.values())
average = round(sum(socres.values()) / len(socres), 1)
print(highest, lowest, average)

highest_person = [name for name, score in socres.items() if score == highest]
print(highest_person)

from random import randint

x = [randint(1, 10) for i in range(20)]
print(x)
m = max(x)
[index for index, value in enumerate(x) if value == m]

# 同时遍历多个列表或可迭代对象
[(x, y) for x in [1, 2, 3] for y in [1, 3, 4] if x != y]

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x == 1 and y != x]

# 实现矩阵的转置
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
var = [[row[i] for row in matrix] for i in range(4)]
print(var)
list(map(list, zip(*matrix)))


# 列表推导式中可以使用函数或复杂表达式

def f(v):
    if v % 2 == 0:
        v = v ** 2
    else:
        v = v + 1
    return v


print([f(var) for var in [2, 3, 4, -1] if var > 0])

# 列表推动导师支持文件对象迭代
with open(r'D:\spider\-[01-01] 【转帖】 性感猎物-美女秘书芷晴.txt', 'r', encoding='utf-8') as fp:
    print([line for line in fp])

print(len([filename for filename in os.listdir(r'D:\spider')]))

# %%
# 切片
alist = list(range(3, 18))
print(alist[:])
alist[::-1]  # 逆序
alist[::2]  # 隔一个取一个,获取偶数位置的元素
alist[1::2]  # 隔一个取一个,获取奇数位置的元素
alist[3:6]  # 指定切片的开始和结束位置
alist[0:100]  # 切片结束位置大于列表长度时,从列表尾部截断
# alist[100]  # 抛出异常,不允许越界
alist[100:]  # 切片开始位置>列表长度时,返回空列表
alist[-15:3]  # 进行必要的截断
len(alist)
alist[-3:-10:-1]  # 位置3在位置-10的右侧,-1表示反向切片
alist[3:-5]  # 位置3在-5的左侧,正向切片

# 使用切片为列表增加元素
alist = [3, 5, 7]
alist[len(alist):]
alist[len(alist):] = [9]  # 在列表的尾部增加元素

alist[3:] = [4, 5, 6]  # 切片连续,等号两边的列表长度可以不相等
alist[::2] = [0] * 3  # 隔一个修改一个
alist[::2] = ['a', 'b', 'c']  # 隔一个修改一个

alist[1::2] = range(3)  # 序列解包的用法
alist[1::2] = map(lambda x: x != 5, range(3))
alist[1::2] = zip('abc', range(3))  # map ,filter,zip对象都支持这样的用法
# alist[::2] = [2]    # 切片不连续时等号两边列表的长度必须相等
print(alist)

# 使用切片删除列表中的元素
alist = [3, 5, 7, 9]
alist[:3] = []  # 删除列表中的前3个元素
print(alist)

# 可以结合del命令删除列表中的部分元素,并且切片元素可以不连续
alist = [3, 5, 7, 9, 11]
# del alist[:3]
del alist[::2]
alist

# 切片得到的是列表的浅复制
alist = [3, 5, 7]
blist = alist[:]
# alist == blist    # 两个列表的值相等
# alist is blist    # 浅复制,不是同一个对象
id(alist) == id(blist)  # 两个列表对象的地址不相等
id(alist[0]) == id(blist[0])  # 相同的值在内存中只有一份
blist[1] = 8
x = [[1], [2], [3]]  # 如果列表种包含列表或其他可变序列
y = x[:]
y[0] = [4]      # 直接修改y种下表为0的元素值,不影响
print(x, y)

y[1].append(5)  # 通过列表对象的方法原地增加元素
print(x)
print(y)
