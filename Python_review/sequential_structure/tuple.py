# 元组创建与元素访问
x = (1, 2, 3)  # 直接把元组赋值给一个变量

type(x)  # 使用type()函数查看变量类型
x[0]  # 元组支持使用下标访问特定位置的元素

x[-1]  # 最后一个元素,元组支持双向索引
# x[1] = 4  # 元组是不可变的

x = (3)  # 这和x=是一样的
x = (3,)  # 如果元组中只有一个元素,必须在后面多写一个逗号
x = ()  # 空元组
x = tuple()  # 空元组
tuple(range(5))  # 将其他迭代对象转换为元组

# 很多内置函数的返回值也包含了若干元组的可迭代对象
list(enumerate(range(5)))

list(zip(range(3), 'abcedfg'))

# 元组与列表的异同点

x = ([1, 2], 4)  # 包含列表的元组
x[0][0] = 5  # 修改元组中的列表元素
print(x[0].append(9))  # 为元组中的列表增加元素
print(x)
# x[0] = x[0] + 10  # 试图修改元组中的值,失败
print(x)
y = x[0]  # y和x[0]指向同一个列表
y += [11]  # 通过y可以影响元组x中的第一个列表
y = y + [12]  # 这个和y += [12] 有本质上的区别
print(y)

hash((1,))  # 元组,数字,字符串都是可哈希的
hash(3)
hash('hello')
hash([1, 2])

# %%
# 生成器表达式
g = ((i + 2) * 2 for i in range(10))  # 创建生成器对象
tuple(g)
list(g)  # 此时生成器对象已经遍历结束,没有元素了
g = ((i + 2) * 2 for i in range(10))
g.__next__()  # 使用生成器对象的__next__()方法获取元素
g.__next__()  # 获取下一个元素
next(g)  # 使用函数next()获取生成器对象中的元素
g = ((i + 2) * 2 for i in range(10))

for item in g:  # 使用循环直接遍历生成器对象中的元素
    print(item, end=' ')

x = filter(None, range(20)) #filter对象也有类似的特点
1 in x
5 in x
2 in x  # 不可再次访问已经访问过的元素

x = map(str,range(20))  #map对象也有类似的特点
'0' in x
'0' in x    # 不可再次访问已经访问过的元素

#%%
# 当生成器推导式中包含多个for语句时,在创建生成器对象的时候只对第一个for语句进行检查和计算,在调用内置函数next()或生成器对象的
# __next__()方法获取值的时候才会计算和检查其他for语句
# lst =[x1*y1 for x1 in range(3) for z in range(5)]
# print(lst)

tuple2 = (x1*y1 for x1 in range(3) for z in range(6))
# tuple2.__next__()
next(tuple2)
