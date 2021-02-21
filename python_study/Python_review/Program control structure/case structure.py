# 单分支选择结构
x = input('Input two numbers')
a, b = map(int, x.split(','))
if a > b:
    a, b = b, a
print(a, b)

# %%
# 双分支选择结构
jitu, tui = map(int, input('请输入鸡兔总数和腿总数:').split(','))
tu = (tui - jitu * 2) / 2
if int(tu) == tu:
    print('鸡: {0},兔: {1}'.format(int(jitu - tu), int(tu)))
else:
    print('数据不准确,无解')

# %%
# 三元运算符
# value1 if condition else value2
a = 5
print(6) if a > 3 else print(5)
print(6 if a > 3 else 5)
b = 6 if a > 13 else 5
print(b)

import math

x = math.sqrt(9) if 5 > 3 else random.randint(1, 100)  # 此时还未导入random模块,但是5>3成立,所有可以正常运行
print(x)
# import random
# 需要计算第二个表达式,但此时未导入random模块,因而报错
y = math.sqrt(9) if 2 > 3 else random.randint(1, 100)
print(y)


# %%
# 多分支选择结构
def func(score):
    if score > 100 or score < 0:
        return 'Wrong score, must betwwen 0 and 100'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'


print(func(80))


# %%
# 选择结构的嵌套
# 使用潜逃选择结构时,一定要严格控制好不同级别代码块的缩进量
def func(score):
    degree = 'DCBAAE'
    if score > 100 or score < 0:
        return 'Wrong score, must betwwen 0 and 100'
    else:
        index = (score - 60) // 10
        if index > 0:
            return degree[index]
        else:
            return degree[-1]


print(func(88))

# 构造跳转表实现多分支选择结构
funcDict = {
    '1': lambda: print('You input 1'),
    '2': lambda: print('You input 2'),
    '3': lambda: print('You input 3'),
}

x = input('Input an interger to call different function:')
func = funcDict[x]
func = funcDict.get(x, None)
if func:
    func()
else:
    print('Wrong Interger')

