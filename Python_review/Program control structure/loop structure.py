# for循环与while循环

'''while循环一般用于循环次数难以提前确定的情况,for循环一般用于循环次数可以提前确定的情况
尤其适用于枚举或遍历序列或迭代对象中元素的集合,对于带有else子句的循环结构,如果循环结构因为
条件表达式不成立或循环遍历结束而自然结束时则执行else后面的语句,如果循环因为执行了break语句而
导致了循环提前结束则不会执行else后面的语句'''

a_list = ['a', 'b', 'python', 'z', 'example']
for i, v in enumerate(a_list):
    print('列表第{0}个元素是{1}'.format(i, v))

# 输出1~100之间能被7整除但同时不能被5整除的所有整数
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
else:
    print('Done')

# 使用嵌套的循环结构打印9*9乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0} * {1} = {2}'.format(i, j, i * j))
else:
    print('Done')

# %%
# break语句和continue语句
'''一旦break语句执行,将使得break语句所属层次的循环提前结束;
continue语句是提前结束本次循环,忽略continue之后的语句,进入下一次循环'''

for i in range(100, 1, -1):
    if i % 2 == 0:
        continue
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            #  结束内循环
            break
    else:
        print(i)
        # 结束外循环
        break

#%%
# 循环代码优化技巧
# 应尽量减少循环结构内部不不必要或无关的计算,与循环儿u管的代码应该尽可能的提取到循环之外
digits = [1, 2, 3, 4]
for i in range(1000):
    result = []
    for i in digits:
        for j in digits:
            for k in digits:
                result.append(i*100+j*10+k)
print(result)

for i in range(1000):
    result = []
    for i in digits:
        i = i *100
        for j in digits:
            j = j*10
            for k in digits:
                result.append(i+j+k)
print(result)

# 另外,在循环中尽量引用局部变量,局部变量的访问和查询速度比全局变量略快
import math
for i in range(1000000):
    math.sin(i)

loc_sin = math.sin
for i in range(1000000):
    loc_sin(i)

#%%
# 精彩案例