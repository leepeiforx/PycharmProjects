import os
from statistics import mean


def f(name):
    print('module name', __name__)
    # print('parent process', os.getpgid())  # 查看父进程的ID
    print('process id', os.getpid())  # 查看当前进程的ID
    print('hello', name)


def flock(lock, i):
    with lock:  # lock对象支持上下文管理协议
        print('hello world')


def f1(e, i):
    if e.is_set():
        e.wait()
        print('hello world', i)
        e.clear()
    else:
        e.set()


def f_mean(x):
    return mean(x)


import multiprocessing
import time
import random
import sys


def calculate(func, args):
    # 调用mul或plus函数计算结果并返回格式化后的字符串
    # 括号里的*表示解包
    result = func(*args)
    return '{3} says {1}{2} = {0}'.format(func.__name__, args, result,
                                          multiprocessing.current_process().name)


def culculatestar(args):
    return calculate(*args)


def mul(a, b):
    time.sleep(0.5 * random.random())
    return a * b


def plus(a, b):
    time.sleep(0.5 * random.random())
    return a + b


def f_error(x):
    # 当x=5时该函数引发异常
    return 1 / (x - 5)


def f_manager(d, l, t):
    d['name'] = 'Dong'
    d['age'] = 31
    d['sex'] = 'Male'
    d['address'] = 'xining'
    l.reverse()
    t.values = 3
