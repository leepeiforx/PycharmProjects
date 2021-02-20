# 基本语法
def fib(n):
    """
    :param n: accept an interger n
    :return: the numbers less than n in Fibonacci Sequence
    """
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    # print()


fib(1000)


# %%
# 函数的嵌套定义,可调用对象及修饰器

def myMap(iterable, op, value):  # 自定义函数
    if op not in '+-*/':
        return 'Wrong Operator'

    def nested(item):  # 嵌套函数定义

        # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
        # eval(expression[, globals[, locals]])
        # 参数
        # expression -- 表达式。
        # globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
        # locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
        return eval(repr(item) + op + repr(value))

    return map(nested, iterable)  # 使用在函数内部定义的函数


list(myMap(range(5), '+', 5))


# 利用函数嵌套和递归定义帕斯卡公式
def f2(n, i):
    cache2 = dict()

    def f(n, i):
        if n == i or i == 0:
            return 1
        elif (n, i) not in cache2:
            cache2[(n, i)] = f(n - 1, i) + f(n - 1, i - 1)
        return cache2[(n, i)]

    return f(n, i)


print(f2(3, 2))

# %%
# 可调用对象
'''函数属于python的可调用对象之一,由于构造方法的存在,类也是可以调用的,像list,tuple,dict,set这样的工厂函数实际上都是使用了
类的构造方法.另外,任何包含__call__()方法的类的对象都是可以调用的'''


def linear(a, b):
    def result(x):  # 在python中,函数是可以嵌套定义的
        return a * x + b

    return result  # 返回可被调用的函数


linear = linear(0.3, 2)
print(linear(2))


# 可调用对象类的定义
class linear2:

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):  # 关键
        return x * self.a + self.b


taxes = linear2(1, 2)
print(taxes(3))


# %%
# 修饰器
# 修饰器本质上也是一个函数,只不过这个函数接受其他函数作为参数并对其进行一定的改造之后返回新函数

def before(func):
    def wrapper(*args, **kwargs):
        print('Before function called')
        return func(*args, **kwargs)

    return wrapper


def after(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(' called')
        return result

    return wrapper


@before
@after
def test():
    print(3)


test()


# 使用装饰器提供用户名检查功能
def check_permission(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("Sorry,you are not allowed")
        print('checked')
        return func(*args, **kwargs)

    return wrapper


class ReadWriterFile(object):
    # 把check_permission作为修饰器使用
    @check_permission
    def read(self, username, filename):
        with open(filename, 'r') as fj:
            return fj.read()

    def write(self, username, filename, content):
        with open(filename, 'a+') as fj:
            return fj.write(content)

    # 把check_permission作为普通函数使用
    write = check_permission(write)


t = ReadWriterFile()
file_path = r'C:\Users\bolat\Desktop\XMind\temp.txt'
print('Originally')
print(t.read(username='admin', filename=file_path))
print('Now,try to write to a file')
t.write(username='admin', filename=file_path, content='\n Hello world')
print('After calling to write')
print(t.read(username='admin', filename=file_path))

# %%
from functools import wraps


# 定义装饰器
def cachedFunc(func):
    #  使用字典存储中间结果
    cache = {}

    # 对目标函数进行改写
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    #  返回修改过的函数
    return wrapper


# 使用修改器
@cachedFunc
def f3(n, i):
    if n == i or i == 0:
        return 1
    else:
        return f3(n - 1, i) + f3(n - 1, i - 1)


print(f3(4, 3))


@cachedFunc
def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


fib10 = fib1(10)
print(type(fib10))


# %%
# 函数成员对象的动态性

def func():
    print(func.x)  # 查看函数的成员x


# 现在函数还没有成员x,故报错
# func()


func.x = 3  # 动态为函数添加成员
print(func.x)  # 在外部也可以直接访问函数成员

del func.x  # 删除函数成员后不可再次访问

# func.x

# %%
# 函数的递归调用
import random


def recursive_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + recursive_sum(lst[1:])


random_num = [random.randint(1, 10) for i in range(10)]
print(random_num)
print(recursive_sum(random_num))


# %%
def factors(num, fac=[]):
    # 每次都从2处查找因数
    for i in range(2, int(num ** 0.5) + 1):
        # 找到因数
        if num % i == 0:
            fac.append(i)
            # 对这个商继续分解,重复该过程
            factors(num // i, fac)
            # 注意,下面的break非常重要
            break
        else:
            # 不可分解了
            fac.append(num)


faces = []
n = random.randint(2, 100)
factors(n, faces)
result = '*'.join(map(str, faces))
if n == eval(result):
    print(n, '= ' + result)


# %%
# 函数参数
# 一般来说,在函数内部修改形参不会影响到实参
def add_one(a):
    a += 1


a = 3
add_one(a)
a

'''然而,列表,字典,集合这样的可变序列类型作为函数参数时,如果在函数内部通过列表,字典,集合对象自身的方法
修改参数中的元素师,同样的作用会体现在实参上'''


def modify(v):
    v[0] = v[0] + 1


a = [2]
modify(a)
a


def modify2(v, item):
    v.append(item)


a = [2]
modify2(a, 3)
a


def modify3(d):
    d['age'] = 39


a = {'name': 'DONG', 'age': 37, 'sex': 'male'}
modify3(a)
a


def modify4(s, v):
    s.add(v)


s = {1, 2, 3}
modify4(s, 4)
s


# %%
# 位置参数
def demo(a, b, c):  # 所有形参参数都是位置参数
    print(a, b, c)


demo(3, 4, 5)

demo(3, 5, 4)
demo(3, 5, 4, 1)  # 实参和形参的数量必须相同


# %%
# 默认值参数
# 在调用函数时,是否为默认值参数传递实参是可选的
# 任何一个默认值参数右边都不能再出现没有默认值的普遍位置参数
def say(message, times=3):
    print(message * times)


# 查看默认值参数的当前值
say.__defaults__

'''多次调用函数并且部位默认值参数传递值时,默认值参数只有在定义时进行一次解释和初始化,对于列表,字典这种可变类型
的默认值参数,这一点可能会导致严重的逻辑错误'''


def demo(newitem, old_list=[]):
    old_list.append(newitem)
    return old_list


print(demo('5', [1, 2, 3, 4]))

print(demo('aaa', ['a', 'b']))

print(demo('a'))

print(demo('b'))  # 注意此处的输出结果

print(demo('c'))


# 一般来说,要避免使用列表,字典,集合或其他可变序列作为函数参数的默认值,上述函数可修改为:
def demo(newitem, old_list=None):
    if old_list is None:
        old_list = []
    old_list.append(newitem)
    return old_list


'''另一个需要注意的问题是,如果在定义函数时某个参数的默认值为另一个变量的值,那么参数的默认值只依赖于
函数定义时该变量的值,或者说函数的默认值参数时在函数定义时确定值的,所以只会被初始化一次'''
i = 3


def f(n=i):
    print(n)


f()

i = 5
f()


# %%
# 关键参数
def demo(a, b, c=3):
    print(a, b, c)


demo(3, 6)  # 按位置传递参数

demo(c=8, a=9, b=0)  # 关键参数

# %%
# 可变长度参数
'''*parameter, 和**parameter,
前者用来接收任意多个实参并将其放在一个元组中,
后者接收类似于关键参数一样显式赋值形式的多个实参并将其放入字典中'''


def demo(*p):
    print(p)


demo(1, 2, 3)
demo([1, 2, 3])
demo(range(1, 10))


def demo(**p):
    for item in p.items():
        print(item)


demo(x=1, y=2, z=3)


# 在函数定义中增加以下外围的检查代码,可以组织用户调用函数时传入无效参数

def demo(a, b, **kwargs):
    for para in kwargs.keys():
        # 只允许传入x,y,z这样的关键字参数
        if para not in ('x', 'y', 'z'):
            raise Exception('{0} is not a vaild parameter'.format(para))
    print(a + b + sum(kwargs.values()))


demo(1, 2)  # 可以不给kwargs传值,默认为空字典
demo(1, 2, x=3)
demo(1, 2, xx=3)  # 不接受xx这样的参数名


# %%
# 强制函数的某些参数必须以关键参数形式进行传值
def demo(a, b, *, c):  # 参数c必须以关键参数进行传值
    print(a + b + c)


demo(1, 2, c=0)


def demo(a, b, *args, c):  # 参数c必须以关键参数进行传值
    print(a + b + c + sum(args))


demo(1, 2, 3, 4, 5, c=0)

'''如果需要强制函数的所有参数都必须以关键参数形式进行传值,可以在定义函数时把单独一个星号*作为函数第一个参数'''


def demo(*, a, b):
    print(a, b)


demo(a=1, b=0)


# 使用修饰器实现相同的功能
def mustbekeywords(func):
    import inspect
    # 获取位置参数和默认值参数列表
    positions = inspect.getfullargspec(func).args

    def wrapper(*args, **kwargs):
        for pos in positions:
            if pos not in kwargs:
                raise Exception(pos + 'must be keyword parameter')
            return func(*args, **kwargs)

    return wrapper


@mustbekeywords
def demo(a, b, c):
    return a, b, c


# demo(a=1, b=2,3)

# %%
# 强制函数的所有参数必须以位置参数形式进行传值

def onlypositions(func):
    import inspect
    # 获取位置参数和默认值参数列表
    positions = inspect.getfullargspec(func).args

    def wrapper(*args, **kwargs):
        # 检查关键参数列表
        for para in kwargs:
            if para in positions:
                raise Exception(para + 'can not be keyword parameter.')
            return func(*args, **kwargs)

    return wrapper


@onlypositions
def demo1(x, y, z):
    print(x + y + z)


demo1(1, 1, 1)


# %%
# 传递参数时的序列解包

def demo(a, b, c):  # 可以接收多个位置参数的函数
    print(a + b + c)


seq = [1, 2, 3]

demo(*seq)  # 对列表进行解包

tup = (1, 2, 3)
demo(*seq)  # 对元组进行解包

dic = {1: 'a', 2: 'b', 3: 'c'}
demo(*dic)  # 对字典的键进行解包
demo(*dic.values())  # 对字典的值进行解包

set = {1, 2, 3}
demo(*set)  # 对集合进行解包

'''如果实参是个字典,可以使用**对其进行解包'''
p = {'a': 1, 'b': 2, 'c': 3}


def f(a, b, c=4):
    print(a, b, c)


f(**p)


def demo(**p):  # 接收字典形式可变长度参数的函数
    for item in p.items():
        print(item)


p = {'a': 1, 'b': 2, 'c': 3}
demo(**p)  # 对字典进行解包

"""如果一个函数需要以多种形式来接收参数,
定义时一般把位置参数放在最前面,
然后是默认值参数,
接下来是一个型号的可变长度参数,
最后是两个星号的可变长度参数,
调用函数时,一般也按照这个顺序进行参数传递"""


def demo(a, b, c):  # 定义函数
    print(a, b, c)


demo(*(1, 2, 3))  # 调用,序列解包

demo(1, *(2, 3))  # 位置参数和序列解包同时使用

demo(1, *(2,), 3)

# demo(a=1, *(2, 3))  # 一个星号的序列解包相当于位置参数
# 优先处理,引发异常


# demo(b=1, *(2, 3))  #  一个星号的序列解包相当于位置参数
# 重复给b赋值,引发异常

demo(c=3, *(1, 2))

# 序列解包不能再关键参数解包之后
# demo(**{'a': 1, 'b': 2}, *(3,))

# demo(*(3,), **{'a': 1, 'b': 2})  # 一个星号的序列解包相当于位置参数
# 优先处理,引发异常

demo(*(1,), **{'b': 2, 'c': 3})

# %%
# 标注函数参数与返回值类型
'''所谓标注函数参数和返回值类型的形式并不起什么作用,只是看上去比较清晰而已,真正起作用的是其中的assert语句'''


def test(x: int, y: int) -> int:
    '''

    :param x: must be intergers
    :param y:  must be intergers
    :return:  must be intergers
    '''

    assert isinstance(x, int)
    assert isinstance(y, int)
    z = x + y
    assert isinstance(z, int)
    return z


test(1, 0)

# %%
# 变量作用域
# 全局变量与局部变量

'''在函数内部通过global关键字来声明或或定义全局变量分为两种情况
1.一个变量已在函数外定义,如果在函数内需要修改这个变量的值,并将修改的结果反映到函数之外,可以在函数内用关键字
global明确声明要使用已定义的同名全局变量
2,在函数内部直接使用global关键字将一个变量声明为全局变量,如果在函数外没有定义该全局变量,在调用这个函数之后,会
创建新的全局变量'''


# 局部变量和全局变量的用法

def demo():
    global x  # 声明或创建全局变量,必须在使用x之前执行
    x = 3
    y = 4
    print(x, y)


x = 5  # 在函数外定义了全局变量
demo()  # 本次调用修改了全局变量
print(x)
# print(y)  # 局部变量在函数结束运行后自动删除,不再存在

del x  # 删除了全局变量
# print(x)


# 如果在某个作用域内有为变量赋值的操作,那么该变量将被认为是该作用域内的局部变量
x = 10


def demo():
    # print(x)    # 这条语句会引发异常,因为变量x现在还不存在
    # x = x + 1   # UnboundLocalError: local variable 'x' referenced before assignment
    print(x)


'''如果局部变量与全局变量具有相同的名字,那么该局部变量会在自己的作用于内暂时隐藏同名的全局变量'''


def demo():
    x = 3
    print(x)


x = 5  # 创建全局变量
demo()
print(x)  # 函数调用后,不会印象全局变量x的值

# %%
'''如果需要在不同模块之间共享全局变量的话,可以编写一个专门的模块来时限这一目的'''

# 加入在模块A.py中有如下的变量定义
# globals_variable = 0

# 而在B.py中使用以下语句修改该全局变量的值
# import A
# A.globals_variable = 1

# 在模块C.py中使用以下语句来访问全局遍历的值
# import A
# print(A.globals_variable)

'''内置函数globals()和locals()分别返回包含当前作用域内所有全局变量和局部变量的名称和值的字典'''
a = (1, 2, 3, 4, 5)
b = 'hello world'


def demo():
    a = 3
    b = [1, 2, 3]
    print('locals', locals())
    print('globals', globals())


demo()

# %%
# nonlocal变量
'''关键字nonlocal声明的变量会引用距离最近的非全局作用域的变量,要求声明的变量已经存在,
关键字nonlocal不会创建新变量'''


def scope_test():
    def do_local():
        spam = '这是局部变量'

    def do_nonlocal():
        nonlocal spam  # 这里要求spam必须是已存在的变量
        spam = '既不是局部变量,也不是全局变量'

    def do_global():
        global spam  # 如果全局作用域内没有spam,就自动创建一个
        spam = '全局变量'

    spam = '原来的值'
    do_local()
    print('局部变量赋值后:', spam)

    do_nonlocal()
    print('nonlocal变量赋值后:', spam)
    print(spam, '\n')

    do_global()
    print('全局变量赋值后:', spam)


scope_test()
print('全局变量', spam)

# %%
# lambda表达式
'''lambda 表达式常用来声明匿名函数,级没有函数名字的临时使用小函数,常用在临时需要一个类似于
函数的功能但又不香定义函数的场合.例如,内置函数sorted()和列表方法sort()的key参数,内置函数map()
和filter()的第一个参数,等等.lambda表达式只可以包含一个表达式,不允许包含其他复杂的语句,但在表达式
可以调用其他函数,该表达式的计算结果相当于函数的返回值'''

f = lambda x, y, z: x + y + z  # 也可以给lambda表达式起个名字
print(f(1, 2, 3))  # 把lambda表达式当作函数使用

g = lambda x, y=2, z=3: x + y + z  # 支持默认值参数
print(g(1))

L = [(lambda x: x ** 2), (lambda x: x ** 3), (lambda x: x ** 4)]  # 调用时支持使用关键参数
print(L[0](2), L[1](3), L[2](4))
D = {'f1': (lambda: 3 + 2), 'f2': (lambda: 2 * 3), 'f3': (lambda: 2 ** 3)}
print(D['f1'](), D['f2'](), D['f3']())

L = [i for i in range(1, 6)]
list(map(lambda x: x + 10, L))  # lambda表达式座位函数参数


def demo(n):
    return n * n


demo(5)
a_list = list(range(1, 6))
list(map(lambda x: demo(x), a_list))  # lambda表达式作为函数参数

data = list(range(20))
import random

random.shuffle(data)
data.sort(key=lambda x: x)  # 用作列表的sort()方法中,作为函数参数

data.sort(key=lambda x: len(str(x)))  # 使用lambda表达式指定排序规则
data.sort(key=lambda x: len(str(x)), reverse=True)
data

#  在使用lambda表达式时,要注意变量作用域可能会带来的问题
r = []
for x in range(10):
    r.append(lambda: x ** 2)

r[1]()

# 修改为下面的代码,则可以得到正确的结果
r = []
for x in range(10):
    r.append(lambda n=x: n ** 2)

r[0]()
r[2]()

'''下面的例子更能说明问题,这里的lambda表达式相当于只有一条return i语句的小函数,
调用时真正的返回值取决于全局变量i的当前值'''
f = lambda: i
i = 3
print(f())
i = 5
print(f())

# %%
# 生成器函数设计要点
'''包含yield语句的函数可以用来创建生成器对象,这样的函数也成为生成器函数,yield语句与return语句作用类似
,都是用来从函数中返回值,return语句一旦执行立刻结束函数的运行,而每次执行到yield语句并返回一个值之后会暂停
或挂起后面的代码的执行,下次通过生成器对象的__next__()方法,内置函数next(),for循环遍历生成器对象元素或其他方式
显式"索要"数据时恢复执行,生成器具有惰性求值的特点,适合大数据处理'''


def f():
    a, b = 1, 1  # 序列解包,同时为多个元素赋值
    while True:
        yield a  # 暂停执行,需要时再产生一个新元素
        a, b = b, a + b  # 序列解包,继续产生新元素


# a = f()
# for i in range(10):   # 斐波那契数列中前10个元素
#     print(a.__next__(), end='\t')

for i in f():  # 斐波那契数列中第一个大于100的元素
    if i > 100:
        print(i, end='\t')
        break

a = f()  # 创建生成器对象
print(type(a))
next(a)  # 使用内置函数next()获取生成器对象中的元素
next(a)  # 每次索取新元素时,由yield语句生成
next(a)
a.__next__()  # 也可以调用生成器对象的__next__()方法


def f():
    # yield from 'abcdefg'    # 使用yield表达式创建生成器
    for i in list('abcdefg'):
        yield i


x = f()
next(x)
next(x)
for item in x:
    print(item, end='\t')


# 生成器对象还支持使用send()方法传入新值,从而该百年后续生成的数据
def gen(start, end):
    i = start
    while i < end:
        v = (yield i)
        if v:
            i = v
        else:
            i += 1


print('\n')
g = gen(1, 101)
next(g)
g.__next__()
g.send(9)  # 传入新值,改变后续生成的数据
next(g)

'''python标准库itertools提供一个count(start,step)函数,用来连续不断的生成无穷个数,这些数中的第一个是start(默认为0)
,相邻两个数的差是step(默认为1),这里使用生成器模拟count()函数'''


def count(start, step):
    num = start
    while True:
        yield num  # 无穷循环
        num += step  # 返回一个数,暂停执行,等待下一次索要数据


x = count(3, 5)
for i in range(10):
    print(next(x), end='\t')

for i in range(10):
    print(next(x), end='\t')

'''python标准库inspect中的isgeneratorfunction()函数可以用来判断一个函数是否是生成器函数'''


def test(a, b):  # 普通函数
    return a + b


import inspect

inspect.isgeneratorfunction(test)


def test():
    yield from range(1, 10)


inspect.isgeneratorfunction(test)
t = test()
for item in t:
    print(item, end='\t')