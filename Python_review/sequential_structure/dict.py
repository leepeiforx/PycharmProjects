# 字典的创建与删除
adict = {'server': 'db.driverintopython3.org', 'database': 'mysel'}

x = dict()  # 空字典
x = {}  # 空字典
keys = list('abcd')
values = [1, 2, 3, 4]
dict2 = dict(zip(keys, values))  # 根据已有数据创建字典
d = dict(name='done', age=30)  # 以关键字参数的形式创建字典
adict = dict.fromkeys(['name', 'age', 'sex'])  # 以给定内容为键

# python还支持使用字典推导式快速生成符合特定条件的字典
d2 = {i: str(i) for i in range(5)}
x = list('ABCD')
y = list('abcd')
{i: j for i, j in zip(x, y)}

# %%
# 字典元素的访问
adict = {'age': 30, 'score': [98, 96], 'name': 'dong', 'sex': 'female'}
adict['age']  # 指定的'键'存在,返回对应的值
# adict['adress'] # 指定的'键'不存在,抛出异常

# 为了避免程序运行时引发异常而导致崩溃,在使用下标的方式访问字典元素时,最好配合条件判断或者异常处理结构

if 'age' in adict:
    print(adict['age'])
else:
    print('Not Exists')

try:
    print(adict['adress'])
except:
    print('Not Exists')

# 字典对象提供了一个get()方法用来返回指定'键'对应的'值',并且允许指定该值不存在时返回特定的'值'

adict.get('age')
adict.get('address', 'Not Exists')  # 指定该值不存在时返回特定的'值'

import string
import random

x = string.ascii_letters + string.digits
print(x)
z = ''.join((random.choice(x) for i in range(1000)))  # 生成1000个随机字符(0~9a~zA~Z)
d = dict()
for ch in z:  # 遍历字符串,统计频次
    d[ch] = d.get(ch, 0) + 1
for k, v in sorted(d.items()):
    print(k, ':', v)

# 字典对象的setdefault()方法用于返回指定'键'对应的'值',如果字典中不存在该'键',就添加一个新元素并设置该'键'
# 对应的'值'(默认为None)

adict.setdefault('address', 'SDIBT')  # 增加新元素
print(adict)

'''对字典对象直接进行迭代或遍历时默认是遍历字典的'键',如果需要遍历字典的元素必须使用字典对象的items()方法明确说明,
如果需要遍历字典的'值'则必须使用字典对象的values()方法明确说明,当使用len,max,min,sum,sorted,enumerate,map,filter等
内置函数以及成员测试符in对字典进行操作时,也遵循同样的原则'''

for item in adict:  # 默认遍历字典的'键'
    print(item, end=' ')

for item in adict.items():  # 明确指定遍历字典的元素
    print(item, end=' ')

adict.items()

adict.keys()

adict.values()

# %%
# 字典的添加,修改与删除

adict['age'] = 39  # 修改元素值
adict['phonenum'] = '185-xxxx-xxxx'  # 添加新元素
adict  # 使用字典时并不需要太在意元素顺序

# 使用字典对象的update()方法实现批量更新/添加字典对象
adict.update({'age': 20, 'sex': 'male'})
adict

# 字典的setdefault()方法也可以用来添加字典元素

# 字典的删除可以使用del命令

# 字典对象的pop()和popitem()方法可以弹出并删除指定的元素
adict.popitem()  # 弹出一个元素,对空字典会抛出异常
print(adict.popitem())
# adict.pop('sex')
print(adict)

# clear()方法用于清空字典对象中的所有元素
adict.clear()
print(adict)

# %%
# 标准库collections中与字典有关的类
# OrderedDict类
import collections

x = collections.OrderedDict()  # 有序字典(按照插入元素顺序)
x['a'] = 3
x['c'] = 8
x['b'] = 5
print(x)

# defaultdict类
import string
import random

x = string.ascii_letters + string.digits
z = ''.join([random.choice(x) for i in range(1000)])

from collections import defaultdict

frequences = defaultdict(int)  # 所有值默认为0
print(frequences)

for item in z:
    frequences[item] += 1  # 修改每个字符的频次
frequences.items()

# 创建defaultdict对象时,传递的参数表示字典中值的类型还可以是任何合法的python类型
games = defaultdict(list)  # 使用list作为值类型

games['name'].append('dong')  # 可以直接为字典games添加元素
games['name'].append('zhang')
games['score'].append(90)
games['score'].append(93)
print(games)

# counter类
from collections import Counter

frequences = Counter(z)
frequences.items()
frequences.most_common(1)  # 返回出现次数最多的1个字符及其频率
frequences.most_common(3)  # 返回出现次数最多的前3个字符及其频率
