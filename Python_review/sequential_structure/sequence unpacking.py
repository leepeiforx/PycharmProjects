# 序列解包

x, y, z = 1, 2, 3  # 多个对象同时赋值
v_tuple = (False, 3.5, 'exp')
(x, y, z) = v_tuple
# x, y, z = v_tuple
x, y, z = range(3)  # 可以对range对象进行序列解包
x, y, z = iter([1, 2, 3])  # 可以对迭代对象进行序列解包
x, y, z = map(str, range(3))  # 使用可迭代的map对象进行序列解包
# a, b = b, a  # 交换两个变量的值

'''序列解包还可用于列表,字典,enumerate对象,filter对象,zip对象等,对字典使用时,默认
是对字典'键'进行操作,如果对'键:值'进行操作时,应使用字典的items()方法说明,如果需要对
字典的'值'进行操作时,使用values()方法明确指定'''
a = [1, 2, 3]
s = list('abc')
b, c, d = a
x, y, z = sorted([1, 3, 2])
a_dict = dict(zip(s, a))
x, y, z = a_dict  # 使用字典时不需要太考虑元素的顺序
print(x, y, z)
x, y, z = a_dict.items()
b, c, d = a_dict.values()

a, b, c = 'ABC'  # 字符串也支持使用序列解包

# 使用序列解包可以方便同时遍历多个序列
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
for k, v in zip(keys, values):
    print((k, v), end=' ')
x = ['a', 'b', 'c']
for k, v in enumerate(x):
    print('The value on position {0} is {1}'.format(k, v))

for k, v in a_dict.items():
    print((k, v), end=' ')

# %%
# 下面代码演示序列解包的另类用法及错误的用法
print(*(1, 2, 3), 4, *(5, 6))

*range(4), 6

# *range(4)   # 不允许这样使用

{*range(4), 4, *(5, 6, 7)}
{'x': 1, **{'y': 2}}

a, b, c = range(3)
# a,b,c = *range(3)   # 不允许这样使用

# 下列代码看起来与序列解包类似,但严格来讲算是序列解包的逆运算,与函数的可变长度参数一样
a, *b, c = 1, 2, 3, 4, 5
print(a, b, c)

a, *b, c = tuple(range(20))
print(b)

# *b = 1,2,3,4    # 等号左侧必须为列表,元组或多个变量

