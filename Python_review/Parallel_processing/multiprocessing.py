# 多进程编程

'''进程时正在执行中的应用程序.一个进程是正在执行中的一个程序使用资源的总和,包括虚拟地址空间,代码,数据,对象句柄,环境变量和
执行单元等.一个应用程序同时打开并执行多次,就会创建多个进程'''

'''python标准库multiprocessing用来实现进程的创建与管理以及进程见的同步和数据交换,用法和threading类似,是支持并行处理的
重要模块.标准库multiprocessing同时支持本地并发与远程并发,有效避免了全局解释器锁(GIL,Global Interpreter Lock)问题,
可以更有效的利用CPU资源,尤其适合多核和多CPU环境'''

# %%
# 进程创建与管理
'''通过multiprocessing中的Process类来创建一个进程对象,然后通过调用进程对象的start()方法来启动,通过调用join()方法等待一个
进程执行结束'''

# 进程创建与启动

from multiprocessing import Process
from Python_Develope.self_module.flock import f

p = Process(target=f, args=('bob',))  # 创建进程
p.start()  # 启动进程
p.join()  # 等待进程运行结束

# %%
# 进程同步技术
'''在需要协同工作完成大型任务时,多个进程间的同步非常重要.进程同步方法与线程同步方法类似,代码稍微改写一下即可'''
from multiprocessing import Process, Lock
from Python_Develope.self_module.flock import flock

# lock = Lock()  # 创建锁对象
# for num in range(10):
#     Process(target=flock, args=(lock, num)).start()

# 使用Event对象实现进程同步
from multiprocessing import Process, Event
from Python_Develope.self_module.flock import f1

if __name__ == '__main__':
    e = Event()
    for num in range(10):
        Process(target=f1, args=(e, num)).start()

# %%
# Pool对象
'''multiprocessing还提供了Pool对象支持数据的并行操作.Pool对象提供了大量的方法支持并行操作
    1.apply(func[,arg[,kwds]]): 调用函数func,并传递参数args和kwds,同时阻塞当前进程直至函数返回,
    函数func只会在进程池的一个工作进程中运行.
    
    2.apply_sync(func[,args[,kwds[,callback[,error_callback]]]]);apply()的变形,返回结果对象,可以通过对象的get()方法
    获取其中的记过;参数callback和error_callback都是单参数函数,当结果对象可用时会自动调用callback,该调用失败会自动error_callback
    
    3.map(func,iterable[,chunksize]);内置函数map()的秉性版本,但只能接受一个可迭代对象作为参数,该方法会阻塞当前进程直至结果可用.
    该方法会把迭代对象iterable切分成多个块再作为独立的任务提交给进程池,块的大小可以通过参数chunksize(默认值为1)来设置
    
    4.map_async(func,iterable[,chunksize[,callback[,error_callback]]]);与map()方法类似,但返回结果对象,需要使用结果对象的
    get()方法来获取其中的值
    
    5.imap(func,iterable[,chunksize[,callback[,error_callback]]])map()方法的惰性求值版本,返回迭代器对象
    
    6.imap_unordered(func,iterable[,chunksize]):与imap()方法类似,但不保证结果会按参数iterable原来的元素的先后顺序返回
    
    7.starmap(func,iterable[,chunksize[,callback]):类似于map()方法,但要求参数iterable中的元素为迭代对象
    并可解包为函数func的参数
    
    8.starmap(func,[iterable[,chunksize[,callback[,error_back]]]):方法starmap()和map_async()的组合,返回结果对象
    
    9.close(): 不允许再向进程池提交任务,当所有已提交任务完成后工作进程会退出.
    
    10.terminate():立即结束工作进程,当线程池对象被回收时会自动调用该方法
    
    11.join():等待工作进程结束,在此之前必须先调用close()或terminate()
    
    '''

# 并发计算二维数组每行的平均值
from multiprocessing import Pool
from Python_Develope.self_module.flock import f_mean as f

if __name__ == '__main__':
    x = [list(range(10)), list(range(20, 30)), list(range(50, 60)), list(range(80, 90))]
    with Pool(5) as p:  # 创建包含5个进程的进程池
        print(p.map(f, x))  # 并发运行

# Pool对象的方法在不同情况下引发异常的处理方法

import multiprocessing
import sys
from Python_Develope.self_module.flock import mul, plus, f_error, calculate


def test():
    # 创建包含4个进程的进程池
    with multiprocessing.Pool(4) as pool:
        tasks = [(mul, (i, 7)) for i in range(10)] + [(plus, (i, 8)) for i in range(10)]
        print('Testing error handing:')
        try:
            print(pool.apply(func=f_error, args=(5,)))
        except ZeroDivisionError:
            print('\tGot ZeroDivisionError as expected from pool.apply()')
        else:
            raise AssertionError('expected ZeroDivisionError')

        try:
            print(pool.map(f_error, list(range(10))))
        except ZeroDivisionError:
            print('\tGot ZeroDivisionError as expected from pool.map()')
        else:
            raise AssertionError('expected ZeroDivisionError')

        try:
            print(list(pool.imap(f_error, list(range(10)))))
        except ZeroDivisionError:
            print('\tGot ZeroDivisionError as expected from pool.imap()')
        else:
            raise AssertionError('expected ZeroDivisionError')

        it = pool.imap(f_error, list(range(10)))
        for i in range(10):
            try:
                x = next(it)
            except ZeroDivisionError:
                if i == 5:
                    pass
            except StopIteration:
                break
            else:
                if i == 5:
                    raise AssertionError('expected ZeroDivisionError')

        assert i == 9
        print('\tGot ZeroDivisionError as expected from IMapIterator.next()')
        print()

        # 测试超时是否正常
        print('Testing ApplyResult.get() with timeout:', end=' ')
        res = pool.apply_async(calculate, tasks[0])
        while True:
            sys.stdout.flush()
            try:
                sys.stdout.write('\n\t%s' % res.get(0.02))
                break
            except multiprocessing.TimeoutError:
                sys.stdout.write('.')
        print()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    test()

# %%
# Manager对象
'''Manager对象提供了不同进程间共享数据的方式,甚至可以在网络上不同价格机器上运行的进程间共享数据.Manager对象控制了一个拥有
list,dict,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Barrier,Queue,Value,Array,Namespace等对象的服务端
进程,并且运行其他进程通过代理来操作这些对象'''

# 使用Manager对象实现进程间数据交换

from multiprocessing import Manager, Process
from Python_Develope.self_module.flock import  f_manager


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        t = manager.Value('i', 0)
        p = Process(target=f_manager, args=(d, l, t))
        p.start()
        p.join()
        for item in d.items():
            print(item)
        print(l)
        print(t.value)
