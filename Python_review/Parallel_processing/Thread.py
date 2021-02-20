# 1 多线程编程

# 线程概念和标准库threading

'''线程是操作系统调度的基本单位,负责执行包含在进程地址空间中的代码并反问其中的资源,当一个进程被创建时
操作系统会自动位置创建一个线程,通常称为主线程.一个进程可以包含多个线程,主线程根据需要在动态创建其他
子线程,操作系统为每个线程保存单独的寄存器环境和单独的对战,但是他们共享进程的地址空间,对象句柄,代码,数据和其他资源.
线程总是在某个进程的上下文中被创建,运行和结束,不可以脱离进程而独立存在.但允许属于同一个进程的多个线程之间进行数据共享
和同步控制.一般而言,除主线程'''

'''标准库threading是python支持多线程编程的重要模块,该模块实在底层模块_thread的基础上开发的更高层次的线程
编程接口,提供了大量的方法和类来支持多线程编程'''

"""
active_count(),activeCount()        返回当前处于alive状态的Thread对象数量
current_thread(),currentThread()    返回当前Thread对象
get_indent()                     返回当前线程的线程标识符,线程标识符是一个非负整数,这个整数本身没有并没有特殊含义
                                 只是用来标识线程,可能会被循环利用
enumerate()                      返回处于alive状态的所有Thread对象列表
local()                          线程局部数据类
main_thread()                    返回主线程对象,即启动python解释器的线程对象
stack_size([size])               返回创建线程时使用的栈的大小,如果指定size参数,则用来制定后续创建的线程使用的栈的大小,
                                 size必须是0(表示使用系统默认值)或大于32K的正整数
setprofile(func)                 设置之后每个线程启动之前都会把func函数传递给sys.setprofile()
settrace(func)                   设置之后每个线程启动之前都会把func函数传递给sys.settrace()
TIMEOUT_MAX                      线程同步获取锁时的最大允许等待时间
Thread                           线程类,用于创建和管理线程
Event                            事件类,用于线程同步
Condition                        条件类,用于线程同步
Lock,RLock                       锁类,用于线程同步
Semaphore,BoundedSemaphore       信号量类,用于现场同步
Timer                            用于在指定时间之后调用一个函数
"""

# 线程对象
'''标准库中的threading的Thread类用来创建和管理线程对象,支持使用两种法来创建
    1. 直接使用Thread类实例化一个线程对象并传递一个可调用参数作为对象
    2. 继承Thread类并在派生类中重写__init__()和run()方法
   创建了线程对象以后,可以调用其start()方法来启动,该方法自动调用该类对象,此时该线程处于alive状态,直至线程的run()方法
   运行结束.'''

# Thread对象的主要成员
"""
start()             自动调用run()方法,启动线程,执行线程代码,每个线程只能启动一次
run()               线程代码,用来实现线程的功能与业务逻辑,可以在子类中重写该方法来自定义线程的行为
__init__(self,group=None,target=None,name=None,args=(),kwarg=None,verbose=None)
                    构造方法
name                读取或设置线程的名字
ident               线程标识,非0数字或None(线程未被启动)
is_alive(),isAlive()    测试线程是否处于alive状态
daemon              布尔值,表示线程是否为守护线程
join(timeout=None)  等待线程结束或超时返回
"""

'''另外,threading还支持Timer类来创建定时启动的线程,调用线程的start()方法之后,线程会在指定的时间(单位是秒)
之后再调用线程函数.'''
import threading


def demo(v):
    print(v)


t = threading.Timer(3, demo, args=(5,))  # 创建线程
t.start()  # 启动线程,3s之后调用demo函数
t.cancel()  # 如果仍在等待时间到达,则取消

# 1.join([timeout])
'''阻塞当前线程,等待被调线程结束或超时后再执行当前线程的后续代码,参数timeout用来指定最长等待时间,
单位是秒.方法join()返回后被调用isAlive()方法,如果得到True则说明线程仍在运行并且join()方法,是因为超时
而返回的,如果返回False,则说明join方法()是因为线程运行结束而返回的.一个线程可以调用多次join()方法(如果
线程已经结束,join()会立即返回),但不允许对当前线程调用join(),否则会抛出异常'''

from threading import Thread
import time

# def func1(x, y):
#     for i in range(x, y):
#         print(i, end=' ')
#     print()
#     time.sleep(10)  # 等待10s
#
#
# t1 = Thread(target=func1, args=(15, 20))  # 创建线程对象,args时传递给函数的参数
# t1.start()  # 启动线程
# t1.join(5)  # 等待线程t1运行结束或等待5s
# t2 = Thread(target=func1, args=(5, 10))
# t2.start()
# print('\n')

"""
首先输出15,19这5个整数,然后程序暂停5s以后继续输出5~9这5个整数,如果将join(5)注释掉,两个线程的输出结果会重叠在一起,
这是因为两个线程冰法运行,而不是等待一个结束以后再运行第二个.如果把time.sleep(10)这一行注释掉再运行,会发现两个程序的输出之间
没有时间间隔,这是因为线程对象的join()方法当线程运行结束或超时之后返回,虽然指定了超时时间为5s,而实际上线程函数瞬间就执行结束了
"""

# is_alive()
'''用来测试线程是否处于运行状态,如果仍在运行则返回True,如果尚未启动或运行则返回False'''

# def func1():
#     time.sleep(10)
#
#
# t1 = Thread(target=func1, args=())
# print('t1:', t1.is_alive())  # 线程还未运行,返回False
# t1.start()
# print('t1:', t1.is_alive())  # 线程还在运行,返回True
# t1.join(5)  # join()方法因超时而结束
# print('t1:', t1.is_alive())  # 线程还在运行,返回True
# t1.join()  # 等待线程结束
# print('t1:', t1.is_alive())  # 线程已结束,返回False

# daemon属性
'''在多线程编程中,如果子线程需要访问主线程中的某个资源(比如某个变量),当退出程序时主线程结束后这些资源将不再存在,子线程
继续运行时会因为无法访问资源而引发异常导致崩溃.需要一种机制保证主线程结束时可以同时结束子线程,或者使主线程等待子线程运行
结束后再结束,线程的deamon属性能够满足该需求
    在程序运行过程中有一个主线程,若在主线程中穿件了子线程,当当主线程结束时根据子线程daemon属性值不同会发生一下两种情况之一
        1.如果某个子线程的daemon属性为False,主线程结束时会检测该子线程是否结束,如果该子线程还在运行,则主线程会等待到它完成
        之后再退出
        2.如果某个子线程的daemon属性为True,主线程结束时不会对这个子线程进行检查而直接退出,同时所有ddaemon值为True的子线程
        将随主线程一起结束,无论是否运行完成
    属性deamon默认值为False,如果需要修改,必须在调用start()方法启动线程之前设置.另外,上述并不适用于IDLE环境中的交互模式或脚本'
    运行模式,因为在该环境中的主线程只有在退出python IDLE时才终止.'''

# class MyThread(threading.Thread):  # 继承Thread类,创建自定义线程类
#     def __init__(self, num, threadname):
#         # threading.Thread.__init__(self, name=threadname)
#         super(MyThread, self).__init__(name=threadname)
#         self.num = num
#
#     def run(self) -> None:
#         time.sleep(self.num)
#         print(self.num)
#
#
# t1 = MyThread(1, 't1')  # 创建自定义线程类对象,daemon默认值为False
#
# t2 = MyThread(5, 't2')
# t2.daemon = True  # 设置线程对象的daemon属性为True
# print(t1.daemon)
# print(t2.daemon)
# t1.start()  # 启动线程
# t2.start()

# Lock/RLock对象

'''Lock是比较低级的同步原语,当被锁定以后不属于特定的线程.一个锁有两种状态:locked和unlocked,刚创建的
Lock对象处于unlocked状态.如果锁处于unlocked状态,acquire()方法将其修改为locked并立即返回;如果锁已处于
locked状态,则阻塞当前线程并等待其他线程释放锁,然后将其修改为locked并立即返回.release()方法用来将锁的
状态由locked修改为unlocked并立即返回.如果锁状态本身已经是unlocked,调用该方法将会抛出异常
    可重入锁RLock对象也是一种常用的线程同步原语,可被同一个线程acquire()多次,.当处于locked状态时,某线程
拥有该锁;当处于unlocked状态时,该锁不属于任何线程.RLock对象的acquire()/release()调用对可以嵌套,仅当最后一个
或者最外层release()执行结束后,锁才会被设置为unlocked状态'''

# 自定义线程类
# class MyThread(threading.Thread):
#     def __init__(self):
#         # threading.Thread.__init__(self)
#         super(MyThread, self).__init__()
#
#     #  重写run()方法
#     def run(self) -> None:
#         global x
#         # 获取锁,如果成功则进入临界区
#         lock.acquire()
#         x = x + 3
#         print(x)
#         # 退出临界区,释放锁
#         lock.release()
#
#
# lock = threading.RLock()
# # 也可以使用Lock类实现加锁和线程同步
# # lock = threading.Lock()
#
# # 存放多个线程的列表
# t1 = []
# for i in range(10):
# #     创建线程并添加列表
#     t = MyThread()
#     t1.append(t)
#
# # 多个线程互斥访问的变量
# x = 0
# # 启动列表中的所有线程
# for i in t1:
#     i.start()


"""需要注意的是,多线程同步时如果需要获得多个锁才能进入临界区的话,可能会发生死锁,在多线程编程时一定要注意
并认真检查和避免这种情况"""


# 以下代码就可能发生死锁,类似于"哲学家就餐问题"

class MyThread1(threading.Thread):
    def __init__(self):
        super(MyThread1, self).__init__()

    def run(self) -> None:
        lock1.acquire()  # 获取一个锁
        lock2.acquire()  # 获取另一个锁
        # 实际功能代码,(略)
        lock2.release()
        lock1.release()


class MyThread2(threading.Thread):
    def __init__(self):
        super(MyThread2, self).__init__()

    def run(self) -> None:
        lock1.acquire()  # 获取一个锁
        lock2.acquire()  # 获取另一个锁
        # 实际功能代码,(略)
        lock2.release()
        lock1.release()


lock1 = threading.RLock()
lock2 = threading.RLock()
t1 = MyThread1()
t2 = MyThread2()
t1.start()
t2.start()

# %%
# condition对象
'''使用condition对象可以在某些事件触发后才处理数据或执行特定的功能代码,可以用于不同线程之间的通信或通知,已实现更高级的
同步.condition对象除了具有acquire和release方法之外,还有wait,wait_for,notify,notify_all等方法'''
''' wait(timeout=None)方法释放锁,并阻塞当前线程知道超时或其他线程针对同一个condition对象调用notify/notify_all方法.
被唤醒的线程会重新尝试取锁并在成功获取锁之后结束wait方法,然后继续执行
    wait_for(predicate,timout=None)方法阻塞,当前线程直到超时或条件得到满足
    notify(n=1)唤醒或等待该condition对象的一个或多个线程,该方法不负责释放锁
    notify_all()方法会唤醒等待该condition的所有线程
'''

"""通过生产者-消费者问题演示condition的用法,程序中生产者产生线程和消费者线程共享一个列表,生产者在列表尾部添加元素,
消费者从列表收不获取并删除元素,如果列表长度达到了20表示已满,生产者等待,如果列表已空则消费者等待"""

from random import randint
from time import sleep


# 自定义生产者线程类
class Producer(threading.Thread):
    def __init__(self, threadName):
        super(Producer, self).__init__(name=threadName)

    def run(self) -> None:
        global x
        while True:
            # 获取锁
            con.acquire()
            # 假设共享列表最多能容纳20个晕啊素
            if len(x) == 20:
                # 表示列表已满,生产者等待
                con.wait()
                print('Producer is waiting')
            else:
                print('Producer:', end='')
                # 产生新元素,添加至共享列表
                x.append(randint(1, 1000))
                print(x)
                sleep(1)
                # 唤醒等待条件的线程
                con.notify()
            # 释放锁
            con.release()


class Consumer(threading.Thread):
    def __init__(self, threadName):
        super(Consumer, self).__init__(name=threadName)

    def run(self) -> None:
        global x
        while True:
            con.acquire()
            if not x:
                # 等待
                con.wait()
                print('Consumer is waiting')
            else:
                print(x.pop(0))
                print(x)
                sleep(2)
                con.notify()
            con.release()


# 创造线程condition对象以及生产者,消费者线程
con = threading.Condition()
c = Consumer('Consumer')
x = []
p = Producer('Producer')
p.start()
c.start()
p.join()
c.join()

# %%
# Queue对象
'''queue模块提供的Queue类实现多线程编程所需要的锁原语,是线程安全的,不需要额外的同步机制,尤其适合需要在多个
线程之间信息交换的场合.Queue类对象的get()和put()方法都支持一个超时参数timeout,调用该方法时如果超时参数会
报出异常'''

# 使用Queue类实现多线程同步,模拟生产者/消费者问题
import queue
import threading
import time


class Producer(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name=threadName)

    def run(self) -> None:
        global myqueue
        # 在队列尾部追加元素
        time.sleep(1)
        try:
            myqueue.put(self.getName(), timeout=1)
            print(self.getName(), ' put', self.getName(), ' to queue')
        except:
            pass


class Consumer(threading.Thread):
    def __init__(self, threadName):
        super(Consumer, self).__init__(name=threadName)

    def run(self) -> None:
        global myqueue

        # 在队列首部获取元素
        time.sleep(0.1)
        try:
            print(self.getName(), ' get', myqueue.put(timeout=1.1), ' from queue')
        except:
            pass


myqueue = queue.Queue(5)
plist = []
clist = []
for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

# 依次启动生产者和消费者线程
for p, c in zip(plist, clist):
    p.start()
    c.start()

# %%
# Event对象
"""Event对象是一种简单的线程通信技术,一个线程设置event对象,另一个线程等待Event对象.Event对象的set()方法可以设置Event对象内部的
信号标志为真;clear()方法可以清除Event对象内部的信号标志,将其设置为假;isSet()方法用来判断其内部信号标志的状态;wait()方法在其内部
信号状态为真时会立刻执行并返回,若Event对象的信号标志为假,wait()方法就一直等待至超时或者内部信号状态为真."""
import threading


class MyThread(threading.Thread):
    def __init__(self, threadName):
        super(MyThread, self).__init__(name=threadName)

    def run(self) -> None:
        global myevent
        # 根据Event对象是否已设置做出不同的响应
        if myevent.isSet():
            # 清除标志
            myevent.clear()
            # 等待
            myevent.wait()
            print(self.getName() + ' set')
        else:
            print(self.getName() + ' not set')
            # 设置标志
            myevent.set()


myevent = threading.Event()
# 设置标志
for i in range(10):
    t = MyThread(str(i))
    t.start()

# %%
# Semaphore与BoundedSemaphore
'''
Semaphore对象维护着一个内部计数器,调用acquire()方法时该计数器-1,调用release()方法时+1,适用于需要控制特定资源的并发访问线程数量
的场合,调用acquire()方法时,如果计数器已经为0则阻塞当前线程直到有其他线程调用了release()方法,所以计数器的值永远不会小于0.
Semaphore对象可以调用任意次release()方法(如果真的出现这种情况,很可能是有bug),而BoundedSemaphore对象可以保证计数器的值不会超过特定
的值,与Lock/RLock,Condition对象一样,Semaphore和BoundedSemaphore对象也支持上下文管理协议,支持with关键字
'''

# 使用BoundedSemaphore对象限制特定资源的并发访问线程数量
import time


def worker(value):
    with sema:
        print(value)
        time.sleep(6)


# 同一时刻最多允许2个线程访问特定资源
sema = threading.BoundedSemaphore(2)
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

# %%
# Barrier对象
'''Barrier对象常用来实现这样的线程同步,多个线程运行到某个时间点以后每个线程都需要等着其他线程都准备好以后再同时进行下一步工作.
类似赛马需要先用栅栏拦住,每个试图穿过栅栏的选手都需要说明自己准备好了,当所有选手都表示准备好以后,栅栏打开,所有选手同时冲出栅栏'''

import random
import threading
import time


def worker(arg):
    # 假设每个线程需要不同的时间来完成准备工作
    time.sleep(random.randint(1, 20))
    # 假设已知任何线程的准备工作最多需要20s
    # 每个线程调用wait(),返回值不一样
    r = b.wait(20)
    if r == 0:
        print(arg)


def printok():
    print('ok')


# 允许3个线程等待
# 如果调用wait()时没有指定超时时间,默认为20s
b = threading.Barrier(parties=3, action=printok, timeout=20)

# 创建并启动3个线程,线程数量必须与Barrier对象的parties一致
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

# 下面的代码模拟一个类似的场景,服务器启动时需要一定的时间,在服务器做好准备工作之前不允许客户端发起连接请求
# b = threading.Barrier(parties=2,timeout=5)
# def server():
#     # 启动服务器,准备接收客户端的连接,代码略
#     b.wait()
#     while True:
#         # 接收客户端连接,处理客户端请求,代码略
#
# def client():
#     # 等待服务器启动
#     b.wait()
#     while True:
#         # 建立连接,和服务器进行通信
#
# # 分别建立并启动服务器线程和客户端线程
# threading.Thread(target=server).start()
# threading.Thread(target=client).start()