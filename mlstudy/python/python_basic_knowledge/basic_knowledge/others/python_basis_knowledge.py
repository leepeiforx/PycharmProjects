import random

#装饰器
def before(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Before function called.')
        # return result
    return wrapper

def after(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('After function called.')
        # return result
    return wrapper

@before
# @after
def test():
    print('trial')

#函数示例
def average(*args):
    avg = sum(args)/len(args)
    g = [i for i in args if i >avg]
    return (avg,)+tuple(g)


def check_number(s):
    result = [0,0]
    for ch in s:
        if ch.islower():
            result[0]+=1
        elif ch.isupper():
            result[1]+=1
    return result

def reversed_list(lst,k):
    x = lst[k-1::-1]
    y = lst[:k-1:-1]
    return list(reversed(x+y))
    li = lit[k:]+lit[:k]

from collections import deque
q = deque(range(20))
#循环右移位
q.rotate(3)
#循环左移位
q.rotate(-3)

def yanghui(t):
    print([1])
    line =[1,1]
    print(line)
    for i in range(2,t):
        r = []
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line = [1]+r+[1]
        print(line)


from collections import defaultdict
def yanghui_new(n):
    triangle = defaultdict(int)
    for row in range(n):
        triangle[row,0]=1
        print(triangle[row,0],end='\t')
        for col in range(1,row+1):
            triangle[row,col]=triangle[row-1,col-1]+triangle[row-1,col]
            print(triangle[row,col],end='\t')
        print('\n')

yanghui_new(5)

def even_to2_prime(n):

    def IsPrime(p):
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        for i in range(3, int(p**0.5)+1, 2):
            if p % i == 0:
                return False
        return True

    if isinstance(n, int) and n > 0 and n%2 == 0:
        for i in range(2,n//2+1):
            if IsPrime(i) and IsPrime(n-i):
                print(i,'+',n-i,'=',n)

def lcm_gcd(m,n):
    if m < n :
        m,n = n,m
        p = m * n
        while m % n !=0:
            m,n = n,m%n
        return (n,p//n)


def gcd_lcm(m,n):
    if m < n :
        m,n = n,m
        import math
        r = math.gcd(m,n)
        return (r,(m*n)//r)

def sort_list_by_num(lst,n):
    t1 = [i for i in lst if i < n]
    t2 = [i for i in lst if i > n]
    return t1+[n]+t2

def sort_list_by_num_v2(lst,n):
    t1 = []
    t2 = []
    for i in lst:
        if i < n:
            t1.append(i)
        elif i > n:
            t2.append(i)
    return t1 + [n] + t2

def str_matching_rage(orgin,userInput):
    if not(isinstance(orgin,str) and isinstance(userInput,str)):
        print('The two parameters must be strings.')
        return
    right = sum(1 for o,u in zip(orgin,userInput) if o==u)
    return round(right/len(userInput),2)


from random import randint
from math import sqrt

testData = [randint(10, 100000) for i in range(50)]
maxData = max(testData)
primes = [p for p in range(2, maxData) if 0 not in
          [p % d for d in range(2, int(sqrt(p))+1)]]

def factoring(n):
    # '对大数进行因数分解'
    if not isinstance(n,int):
        print('Must give an interger.')
        return
    # '开始分解,把所有的因素都加入到result列表中'
    result = []
    for p in primes:
        while n != 1:
            if n % p == 0:
                n = n/p
                result.append(p)
            else:
                break
        else:
            result ='*'.join(map(str,result))
            return result
    #考虑参数本身就是素数的情况
    if not result:
        return n

# for data in testData:
#     r = factoring(1)
#     print(data,'=',r)
#     #测试分解结果是否正确
#     print(data == eval(r))


from random import randint

def guess(maxValue = 100,maxTimes=5):
    value = randint(1,maxValue)
    for i in range(maxTimes):
        prompt = 'Start to guess:' if i == 0 else 'Guess again:'
        try:
            x = int(input(prompt))
        except:
            print('must input an ingeter between 1 and ',maxValue)
        else:
            #猜对了
            if x ==value:
                print('congratulation!')
                break
            elif x > value:
                print('Too big!')
            else:
                print('too small')
    else:
        print('Game over,Fail')
        print('The value is ',value)

def natural_number_sum(v,n):
    # v must be in 1 and 0
    assert type(n) == int and 0<v<10
    result ,t =0,0
    for i in range(n):
        t = t*10 + v
        result += t
    return result

def call_number(lst,k):
    from itertools import cycle
    t_lst = lst[:]
    while len(t_lst)>1:
        #创建cycel对象
        c = cycle(t_lst)
        #从1到k报数
        for i in range(k):
            t = next(c)
        #一个人out,圈子缩小
        index = t_lst.index(t)
        t_lst = t_lst[index+1:]+t_lst[:index]
        return t_lst[0]

def hannoi_tower(num, src, dst, temp=None):
    #声明用来记录移动次数的变量为全局变量
    global times
    #确认参数类型和范围
    assert type(num) == int
    assert num > 0
    #只剩最后或只有一个盘子需要移动,也就是函数递归调用的结束条件
    if num == 1:
        print('The {0} times move:{1} => {2}'.format(times, src, dst))
        times += 1
    else:
        #递归调用函数自身
        #先把除最后一个盘子之外的所有盘子移动到临时柱子上
        hannoi_tower(num-1, src, temp, dst)
        #把最后一个盘子直接移动到目标柱子上
        hannoi_tower(1, src, dst)
        #把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
        hannoi_tower(num-1, temp, dst, src)


#用来记录移动次数的变量
times = 1
#A表示最初放盘子的柱子,C时目标柱子,B为临时柱子
hannoi_tower(3,'A','C','B')

def black_hole_num(n):
    '''参数n表示数字的位数,例如n=3时则返回495,n=4时则返回6174'''
    start = 10**(n-1)
    end = 10**n

    #测试每一个数
    for i in range(start, end):
        #由这几个数组成的最大数即最小数
        max_num = ''.join(sorted(str(i),reverse=True))
        min_num = ''.join(reversed(max_num))
        max_num,min_num = map(int,(max_num,min_num))
        if max_num - min_num == i:
            print(i)
        else:
            print ('None exists!')


from random import randint
from itertools import  permutations
exps = ('(%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)',
        '(%s %s (%s %s %s) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = '+-*/'

def test24(v):
    result = []
    #python允许函数嵌套定义
    #这个函数对字符串表达式求值并验证是否等于24
    def check(exp):
        try:
            #有可能出现除以0的异常,所以加入异常处理结构
            return int(eval(exp)) == 24
        except:
            return False
    #全排列,枚举4个数的所有可能排序
    for a in permutations(v):
        #查找4个数的当前排列能实现24的表达式
        t = [exp % (a[0],op1,a[1],op2,a[2],op3,a[3])for op1 in ops for op2 in ops
             for op3 in ops for exp in exps if check(exp%(a[0],op1,a[1],op2,a[2],op3,a[3])) ]
        if t:
            result.append(t)
    return result


# for i in range(20):
#     print('='*20)
#     #生产随机数字进行测试
#     lst = [randint(1,14) for j in range(4)]
#     r = test24(lst)
#     if r:
#         print(r)
#     else:
#         print('No answer for.',lst)


def makeChanges(total,changes=[1,2,5,10,20,50,100],result =None):
    #计算换零钱的所有可能方案
    if result is None:
        result = []
    if total ==0:
        yield result
    for change in changes:
        #兑换的零钱不能超过总金额,并且每个结果都是唯一的
        if change > total or (len(result)>0 and result[-1] < change):
            continue
        for r in makeChanges(total-change,changes,result+[change]):
            yield r

def myMax_Min(iterable):
    '''返回序列中的最大值和最小值'''
    tMax = tMin = iterable[0]
    for item in iterable[1:]:
        if item > tMax:
            tMax = item
        elif item < tMin:
            tMin = item
    return tMax,tMin

