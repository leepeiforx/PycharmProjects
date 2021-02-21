# 枚举类型
from enum import Enum  # 导入模块中的类


class Color(Enum):
    red = 1
    blue = 2
    green = 3


Color.red  # 访问枚举类的成员
type(Color.red)  # 查看枚举类成员的类型
isinstance(Color.red, Color)
x = dict()
x[Color.red] = 'red'  # 枚举类成员可哈希,可以作为字典的'键'
x
Color(2)  # 返回指定值对应的枚举类成员
Color['red']
r = Color.red
r.name
r.value
list(Color)  # 枚举类是可以迭代的

# %%
# 数组类型
# 标准库array提供的Array类支持数组的创建和使用,可以创建数组类型包括整数,实数,Unicode字符等
from array import array

a = 'Hello World'
sa = array('u', a)  # 创建可变字符串对象
print(sa)
print(sa.tostring())  # 查看可变字符串对象内容
print(sa.tounicode())  # 查看可变字符串对象内容
sa[0] = 'F'
print(sa)  # 修改指定位置上的字符
sa.insert(5, 'w')  # 在指定位置插入字符
print(sa)
sa.remove('l')  # 删除指定字符的首次出现
print(sa)
array('u', 'Felow world')
sa.remove('w')
print(sa)
array('u', 'Felo World')
ia = array('I')
for i in range(5):
    ia.append(i)
ia[0] = 5
ia

# %%
# 队列
# python标准库queue提供了LILO队列类Queue,LIFO队列类LifoQueue,优先级队列类PriorityQueue,标准库collections提供了双端队列
from queue import Queue  # LILO队列

q = Queue()  # 创建队列对象
q.put(0)  # 在队列尾部插入元素
q.put(1)
q.put(2)
print(q.queue)  # 查看队列中的元素
q.get()  # 返回并删除队列的头部元素
q.get()
q.get()

from queue import LifoQueue  # LIFO队列

q = LifoQueue()  # 创建LIFO队列
q.put(0)
q.put(1)
q.put(2)
print(q.queue)
q.get()
q.get()
q.queue
q.get()  # 对空队列调用get()方法会阻塞当前线程

from queue import PriorityQueue  # 优先级队列

# 二叉堆
q = PriorityQueue()
q.put(3)  # 插入元素
q.put(8)  # 插入元素
q.put(100)
q.queue  # 查看优先级队列中的所有元素
q.put(1)  # 插入元素,自动调整优先级队列
q.put(2)
q.queue
q.get()  # 返回并删除优先级最低的元素
q.get()
q.get()
q.get()

# %%
from collections import deque

q = deque(maxlen=5)  # 创建双端队列
for item in [3, 5, 7, 9, 11]:
    q.append(item)

q.append(13)  # 队列满,自动溢出
q.append(15)
deque([3, 5, 7, 9, 11], maxlen=5)
q.appendleft(5)  # 从左侧添加元素,右侧自动溢出
q.popleft()  # 弹出并返回最左端元素
q.pop()  # 弹出并返回最右端元素\
q.insert(2, 10)  # 在中间位置插入元素
q += [1, 2]  # 追加多个元素
q *= 2  # 序列重复
q.count(10)  # 返回元素的出现次数
q.rotate(2)  # 循环右移2个元素
q.rotate(-2)  # 循环左移2个元素

# %%
# 具名元组
from collections import namedtuple

point = namedtuple('Point', ['x', 'y', 'z'])  # 创建具名元组表
point
p = point(3, 4, 5)
p
p.x  # 访问成员
p._fields  # 查看字段列表
p._replace(x=30, z=9)  # 替换成员值,返回新对象
# p.x = 7  # 不允许这样直接赋值
d = dict()
d[p] = 'spirit positon'  # 具名元组对象可以作为字典的'键'
d

# %%
# 堆
# 堆是一个特殊的二叉树,其中每个父节点的值都小于或等于其所有子节点的值
import heapq
import random

data = random.sample(range(1000), 10)  # 生成随即测试数据
print(data)
heapq.heapify(data)
print(data)
heapq.heappop(data)  # 删除并返回最小元素,自动调整堆
heapq.heappop(data)
heapq.heappop(data)
data
heapq.heappushpop(data, 1000)  # 弹出最小元素,同时新元素入堆
heapq.heapreplace(data, 500)  # 弹出最小元素,同时新元素入堆
data
heapq.nlargest(3, data)  # 返回最大的前3个元素
heapq.nsmallest(2, data, key=str)  # 返回指定顺序规则侠最小的3个元素

