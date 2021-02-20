"""在python,字符串属于不可变有序序列,使用单引号(这是最常用的),双引号,三单引号或三双引号作为定界符
并且不同定界符之间可以嵌套"""

'''除了支持序列通用操作(包括双向索引,比较大小,计算长度,元素访问,切片,成员测试等)以外,字符串类型还支持一些特有
的用法,例如字符串的格式化,查找,替换,排版等.但由于字符串属于不可变序列,不能直接对字符串对象进行元素增加,修改与
删除等操作,切片操作也只能访问其中的元素而不能使用切片修改字符串中的字符.另外,字符串对象提供的replace()和translate()
方法以及大量排版方法也不是对原字符串直接修改替换,而是返回一个新字符串作为结果'''

'''python支持段子付出驻留机制,对于短字符串,将其复制给多个不同的对象时,内存只有一个副本,多个对象共享该副本.
然而,这一点并不适用于长字符串,当把一个长字符串赋值给多个变量时,这些变量并不共享相同的内存地址'''

"""
字符串驻留机制
对于短字符串，将其赋值给多个不同的对象时，内存中只有一个副本，多个对象共享该副
本。长字符串不遵守驻留机制。
驻留适用范围
由数字，字符和下划线（_）组成的python标识符以及整数[-5,256]。"""
# a = '1234'
# b = '1234'
# print(id(a) == id(b))

"""
驻留时机
python中的驻留发生在compile_time,而不是run_time。
"""
str1 = '1' + '2'
str2 = '1'
str3 = str2 + '2'
print(str3 is '12')
print(id(str1), id(str3))

str1 = 'stenwaves'
str2 = 'stenwaves'
print(str1 is str2)
print(id(str1))
print(id(str2))

str3 = 'sten waves'
str4 = 'sten waves'
print(str3 is str4)
print(id(str3))
print(id(str4))

# %%
'''如果需要判断一个变量是否为字符串,可以使用内置方法ininstance()或type(),除了支持Unicode编码
的str类型之外,python还支持字节串类型bytes,str类型字符串可以通过encode()方法使用指定的字符串
编码格式称为bytes对象,而bytes对象则可以通过decode()方法使用正确的编码格式解码成str字符串.另外可以
使用内置函数str()和bytes()在这两种类型之间进行转换.'''

type('中国')
type('中').encode('gbk')  # 编码成字节串,采用GBK编码格式
isinstance('中国', str)
type('中国') == str
type(('中国').encode()) == bytes

'中国'.encode()  # 默认使用UTF-8进行编码
# bytes('中国', 'gbk')
# str(_, 'gbk')

# %%
# 字符串编码格式简介
import sys

sys.getdefaultencoding()  # 查看默认编码格式

s = '山东烟台'
len(s)  # 字符串长度,或者包含的字符个数
s = '山洞掩体 ABCD'
len(s)  # 中文与英文字符同样对爱,都算一个字符

姓名 = '张三'  # 使用中文名作为变量名
print(姓名)

'''python扩展库chardet可以用来检测字节串所采用的编码格式,并提供一个可信度以供参考(有时候可能不准)
常用来判断文本文件的编码格式'''

import chardet

x = '姓名'.encode()
chardet.detect(x)
x = '姓名'.encode('GBK')
chardet.detect(x)
x = '姓名'.encode('cp936')
chardet.detect(x)

# %%
# 转义字符与原始字符串
'''
\b 退格,把光标移动到前一列位置
\f 换页符
\n 换行符
\r 回车
\t 水平制表符
\v 垂直制表符
\\ 一个斜杠\
\' 单引号'
\" 双引号"
'''

# %%
# 字符串格式化
''

""" % [-] [+] [0] [m] [.n] 格式字符 % x"""
'''
% 格式标志,表示格式开始
[-] 指定左对齐输出
[+] 对整数加正号
[0] 指定空位填0
[m] 指定最小宽度
[.n] 指定精度
格式字符 指定类型
% 格式运算符
x 待转换的表达式
'''

# 常用格式字符
'''
%s  字符串(采用str()显示)
%r  字符串(采用repr()显示)
%c  单个字符
%b  二进制整数
%d  十进制整数
#i  十进制整数
%o  八进制整数
#x  十六进制整数
%e  指数(基底写为e)
%E  指数(基底写为E)
%f,%F   浮点数
%g  指数(e)或浮点数(根据现实长度)
%G  指数(E)或浮点数(根据现实长度)
%%  字符%
'''

x = 1235
so = "%o" % x
print(so, type(so))

sh = "%x" % x
print(sh, type(sh))

se = "%e" % x
print(se, type(se))

print("%s" % x)  # 等价于str()

print("%d,%c" % (65, 65))  # 使用远足对字符串进行格式化,按位置进行对应

# print("%d"%"555")   # 试图将字符串转换为整数进行输出,抛出异常

print("%s" % [1, 2, 3])

str((1, 2, 3))  # 可以使用str()函数将任意类型数据转换为字符串

# %%
# 使用format()方法进行字符串格式化

'''在字符串格式化方法format()中可以使用的格式主要有b(二进制格式),c(把整数转换为unicode字符),
d(十进制形式),o(八进制形式),x(小写十六进制形式),X(大写十六进制形式),f/F(固定长度的浮点数格式),
%(使用固定长度浮点数显示百分数)'''

print(1 / 3)
print('{0:.3f}'.format(1 / 3))  # 保留3位小数
print('{0:%}'.format(3.5))  # 格式转化为百分数

print('{0:_},{0:_x}'.format(100000))
print('the number {0:,} in hex is {0:#x}, in oct is{0:#o}'.format(55))
print('the number {0:,} in hex is {0:#o},the number {1:,} in oct is {1:#o}'.format(5555, 55))
print('my name is {name},my age is {age}, and my qq is {qq}'.format(name='Dong', qq='4545134145', age=20))
position = (5, 9, 13)
print('X:{0[0]};Y:{0[1]};Z:{0[2]}'.format(position))

weather = [('Monday', 'rain'), ('Tuesday', 'sunny'), ('Wedenday', 'sunny'),
           ('Thursday', 'rain'), ('Friday', 'cloudy')]

formatter = 'Weather of {0[0]} is {0[1]}'.format
for item in map(formatter, weather):
    print(item)

for item in weather:
    print(formatter(item))

# %%
# 格式化的字符串常量
# Formatted String Literals,其含义与字符串对象的format()方法类似,但形式更加简洁

name = 'Dong'
age = 39
f'My name is {name} , and I am {age} years old'

width = 10
precision = 4
value = 11 / 3
print(f'result:{value:{width}.{precision}}')

# %%
# 使用template模块进行格式化
'''python标准库string提供了用于字符串格式化的模块类Template,用于大量信息的格式化,尤其适用于
网页模版内容的替换和格式化'''

from string import Template

t = Template('My name is ${name}, and is ${age} years old.')  # 创建模版
d = {'name': 'Dong', 'age': 39}
t.substitute(d)

tt = Template('My name is $name, and is $age years old.')
tt.substitute(d)

html = '''<html><head>${head}</head><body>${body}</body></html>'''

t = Template(html)
d = {'head': 'test', 'body': 'this is only a test.'}
t.substitute(d)

# %%
# 字符串常用操作
'find, rfind, index, rindex, count'
s = 'apple,peach,banana,peach,pear'
# print(len(s))
s.find('peach')  # 返回第一次出现的位置
s.find('peach', 7)  # 从指定位置开始查找
s.find('peach', 7, 20)  # 从指定范围中查找
s.rfind('p')  # 从字符串尾部向前查找
s.index('p')  # 返回首次出现的位置

s.index('pear')
# s.index('ppp')  # 指定子字符串不存在时抛出异常
s.count('p')  # 统计子字符串出现的次数
s.count('ppp')  # 不存在时返回0

'''一般而言,实际开发时应优先考虑使用python内置函数和内置对象自身提供的方法,运行速度快,并且运行稳定'''

from string import ascii_letters
from random import choice
from time import time

letters = ''.join([choice(ascii_letters) for i in range(999999)])
letters2 = ''.join([choice('ab') for i in range(999999)])


def position_of_character(sentence, ch):
    result = []
    index = 0
    index = sentence.find(ch, index + 1)
    while index != -1:
        result.append(index)
        index = sentence.find(ch, index + 1)
    return result


def demo(s, c):
    result = []
    for i, ch in enumerate(s):
        if ch == c:
            result.append(i)
    return result


for f in (position_of_character, demo):
    start = time()
    positions = f(letters, 'a')
    print(time() - start)

'''综合来说,首先应该分析待处理的数据有什么样的特点(例如,数据种类数量,带查找元素而分布密度等),然后
才能设计最优的算法和最有效的实现方法.但一般而言,python内置函数,内置对象的方法和标准库对象的效率
要高于自己编写的代码'''

# split,rsplit,partition,rpartition
'''字符串对象split和rsplit方法分别雍来义指定字符作为分割扶,从字符串左端和右端开始讲起分割成多个字符串,
并返回包含分割结果的列表'''
s = 'apple,peach,banana,peach,pear'
s1 = s.split(',')  # 使用逗号进行分隔
s = '2014-10-31'
t = s.split('-')
print(t)
list(map(int, t))

'''对于split()和rsplit()方法,如果不指定分隔符,则字符串中的任何空白符号(包括空格,换行符,制表符等)
的连续出现都将被认为是分隔符,返回包含最终分割结果的列表'''

s = 'hello world \n\n my name is dong'
s.split()
s = '\n\nhello world \n\n\n my name is dong'
s.split()
s = '\n\nhello\t\t world \n\n\n my name \t is dong'
s.split()

'''另外,split()和rsplit()方法允许指定最大分割次数(注意,并不是必须分隔这么多次)'''
s = '\n\nhello\t\t word \n\n\n my name is dong'
# s.split(maxsplit=1)
s.split(maxsplit=2)
s.split(maxsplit=10)

'''调用split()方法如果不传递任何参数,将使用任何空白字符作为分隔符,如果字符串存在连续的空白字符
split()方法将作为一个空白字符对待.但是,明确传递参数指定split()使用的分隔符时,情况略有不同'''
'a,,,bb,,ccc,'.split(',')
'a\t\t\tbb\t\tccc'.split('\t')
'a\t\t\tbb\t\tccc'.split()

'''字符串对象的partition()和rpartition()方法以制定字符串为分割符将原字符串分割为3部分,即分隔符
之前的字符串,分隔符字符串和分隔符之后的字符串.如果指定的分隔符不自爱原字符串中,则返回原字符串和两个
空字符串.如果字符串中有多个分隔符,那么partition()把从左往右遇到的第一个分隔符作为分隔符,rpartition
把从右往左遇到的第一个分隔符作为分隔符'''
s = 'apple,peach,banana,pear'
s.partition(',')
s.rpartition('banana')
'ababaabab'.partition('a')
'abababab'.rpartition('a')

# %%
# join
'''字符串的join方法用来将列表中的多个字符串进行连接,并在相邻两个字符串之间插入指定的字符
返回新字符串'''
li = ['apple', 'peach', 'banana', 'pear']
sep = ','
sep.join(li)
':'.join(li)
''.join(li)

'使用split()和join()方法可以删除字符串多余的空白字符,如果连续多个空白字符,只保留一个'
x = 'aaa    bb   c  dd  c d e fff'
' '.join(x.split())


def equavilent(s1, s2):  # 判断两个字符串在python意义上是否等价
    if s1 == s2:
        return True
    elif ' '.join(s1.split()) == ' '.join(s2.split()):
        return True
    elif ''.join(s1.split()) == ''.join(s2.split()):
        return True
    else:
        return False


equavilent('pip list', ' pip   list')

equavilent('[1,2,3]', '[1,2,3')

equavilent('[1,2,3]', '[1,2,3,4]')

# %%
# lower(),upper(),capitalize(),title(),swapcase()

s = 'What is your name?'
s.lower()  # 返回小写字符串
s.upper()  # 返回大写字符串
s.capitalize()  # 字符串首字母大写
s.title()  # 每个单词的首字母大写
s.swapcase()  # 大小写互换

# %%
# replace(),maketrans(),translate()

'''字符串方法replace()用来替换字符串中指定字符或字符串中所有重复出现,每次智能体换一个字符或一个字符串,
把指定的字符串参数作为一个整体对待,类似于Word,WPS,记事本等文本编辑器的查找与替换功能.该方法并不修改原字符串
而是返回一个新字符串'''

s = '中国,中国'
print(s.replace('中国', '中华人民共和国'))
print('abcdabc'.replace('abc', 'ABC'))

'''字符串对象的maketrans()方法用来生成字符映射表,而translate()方法用来根据映射表中定义的对应关系替换字符串并
替换其中的字符,使用这两个方法的组合可以同时处理多个不同的字符,replace()则无法满足这一要求'''

# 创建映射表,将字符'abcdef123'一一映射为'uvwxyz@#$'
table = ''.maketrans('abcdef123', 'uvwxyz@#$')
s = 'python is a great programming language,I lisk it'
# s. translate(table)

# 凯撒加密
import string


def kaisa(s, k):
    lower = string.ascii_lowercase  # 小写字母
    upper = string.ascii_uppercase  # 大写字母
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)
    return s.translate(table)  # 创建映射表


kaisa(s, 3)

# %%
# strip(),rstrip(),lstrip()
'''这几个方法用来分别删除两端,右端或左端连续的空白字符或指定字符'''

s = ' abc   '
s2 = s.strip()
print(s2)
'\n\nhello world\n\n'.strip()
'aaaaasssasadf'.strip('a')  # 删除指定字符
'aaaadddssssf'.strip('af')
'aaaaassddffaaa'.rstrip('a')  # 删除字符串右端指定字符
'aaaassddfffaa'.lstrip('a')  # 删除字符串左端指定字符

'这三个函数的参数指定的字符串并不作为一个整体对待,而是在原字符串的两侧,右侧,左侧删除参数字符串包含的所有字符' \
'一层一层地从外往里扒'
'aabbccddeeeffg'.strip('af')  # 字母f不在字符串的两侧,所以不删除
'aabbccddeeeffg'.strip('gaf')
'aabbccddeeeffg'.strip('gaef')
'aabbccddeeeffg'.strip('gbaef')
'aabbccddeeeffg'.strip('gbaedfc')

# %%
# startswith(),endswith()
'''这两个字符串用来判断是否以指定字符串开始或结束,可以用来接收两个整数参数来限定字符串的检测范围'''

s = 'Beautiful is better than ugly'
s.startswith('Be')
s.startswith('Be', 5)  # 指定检测范围的起始位置
s.startswith('Be', 0, 5)  # 指定监测范围的起始和结束位置

# %%
# isalnum(),isalpha(),isdigit(),isdecimal(),isnumeric(),isspace(),isupper(),islower()
'''用来测试字符串是否是数字或字母,是否为字母,是否是数字字符,是否为空白字符,是否为大写字母以及是否是小写字母'''

'1234abcd'.isalnum()
'1234abcd'.isalpha()  # 全部为英文时返回True
'1234abcd'.isdigit()  # 全部为数字时返回True
'1234.0'.isdigit()
# '九'.isdigit()
'九'.isnumeric()  # isnumeric()方法支持汉字数字
'九'.isdecimal()
'Ⅲ'.isnumeric()  # isnumeric()方法支持罗马数字

'''另外,python标准库unicodedata还提供了不同形式数字字符到10进制数字的转换方法'''
import unicodedata

unicodedata.numeric('2')
unicodedata.numeric('九')
unicodedata.numeric('Ⅲ')

# %%
# center,ljust,rjust,zfill
'''用于对字符串继续排版,其中center,ljust,rjust返回指定宽度的新字符,原字符串居中,左对齐或右对齐出现在新字符串中,如果指定的
宽度大于字符串长度,则使用指定的字符(默认是空格)进行填充,zfill()返回之内搞定宽度的字符串,在左侧以字符串0进行填充'''

'hello world'.center(20)  # 居中对齐,以空格进行填充
'hello world'.center(20, '=')  # 居中对齐,以字符=进行填充
'hello world'.ljust(20, '=')  # 左对齐
'hello world'.rjust(20, '=')  # 右对齐

'abc'.zfill(5)  # 在左侧填充数字字符0
'abc'.zfill(2)  # 指定宽度小于字符串长度时,返回字符串本身
'abc'.zfill(20)

# %%
# 字符串对象支持的运算符

'''python支持使用运算符"+"连接字符串,但该运算符涉及大量数据的赋值,效率非常低,不适合大量长字符串的连接'''

import timeit

# 使用列表推导式生成1000个字符串
strlist = ['this is a long string that will not keep in memory.' for n in range(10000)]


# 使用字符串对象的join方法连接多个字符串
def use_join():
    return ''.join(strlist)


# 使用运算符'+'连接多个字符串
def use_plus():
    result = ''
    for stremp in strlist:
        result = result + stremp
    return result


if __name__ == '__main__':
    # 重复运行次数
    times = 1000
    jointimer = timeit.Timer('use_join()', 'from __main__ import use_join')
    print('time for join', jointimer.timeit(number=times))
    plustimer = timeit.Timer('use_plus()', 'from __main__ import use_plus')
    print('time for plus', plustimer.timeit(number=times))

''' 另外,timeit模块支持下面代码演示的用法,从运行结果可以看出,当需要对大量数据进行类型转换时,内置函数map()可以提供
非常高的效率'''

join_timer = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

map_timer = timeit.timeit('"-".join(map(str,range(100)))', number=10000)
print(join_timer)
print(map_timer)

# %%
# python字符串支持与整数运算的乘法运算,表示序列重复,也就是字符串内容的重复
'abcd' * 3

'''最后,与列表,元组,字典,集合一样,也可以使用成员测试符in来判断一个字符串是否出现在另一个字符串中,返回True或False'''
'a' in 'abcd'
'ac' in 'abcde'  # 关键字in左边的字符串作为一个整体对待
'j' not in 'abcde'

# words = ['测试', '非法', '暴力']
# test = input('请输入:')
# for word in words:
#     if word in test:
#         print('非法')
#         break
#     else:
#         print(word)

words = ['测试', '非法', '暴力', '话']
text = '这句话里含有非法内容'
for word in words:
    if word in text:
        text = text.replace(word, '***')

print(text)

# %%
# 适用于字符串对象的内置函数
'''除了字符串对象提供的方法以外,很多python内置函数也可以对字符串进行操作'''
x = 'hello world'
len(x)  # 字符串长度
max(x)  # 最大字符
min(x)
list(zip(x.upper(), x.lower()))  # zip()也可作用于字符串
sorted(x)
list(reversed(x))
list(map((lambda i, j: i + j), x, x))

# 内置函数eval()用来把任意字符转换为python表达式并进行求值
eval('3+4')  # 计算表达式的值
a = 3
b = 4
eval('a+b')  # 这时候要求变量a和b已存在
import math

eval('math.sqrt(3)')

'''在python3.X中,input()将用户的输入一律按字符串对待,如果需要将其还原为本来的类型,对于简单的整数,实数,复数可以用
int,float,complex函数进行转换,而对于列表,元组或其他复杂结构则需要使用内置函数eval(),不能直接使用list(),tuple()直接
进行转换.不管使用int(),float(),complex()函数还是eval()函数,在转换时最好配合异常处理结构,以避免因为数据类型不符合
要求或者无法正确求值而抛出异常'''

x = input()
try:
    print(eval(x))
except:
    print('wrong input')

# %%
# 字符串对象的切片操作
'''切片也适用于字符串,但仅限于读取其中的元素,不支持字符串修改'''

'Explicit is better than implicit'[:5]

'Explicit is better than implicit'[9:24]
path = r'c:/bootmgr/s/test.bmp'
path[:-4] + '_new' + path[-4:]

# %%
# 其他相关模块

# textwrap模块
'''python标准库textwrap提供了更加友好的排版函数'''
import textwrap

doc = '''Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!'''

# 1 wrap(text,width=70)函数对一段文本进行自动换行,每一行不超过width个字符.
# import pprint
# pprint.pprint(textwrap.wrap(doc))   # 默认长度最大为70

# fill(text,width=70)函数对一段文字进行排版并自动换行,等价于'\n'.join(wrap(text,...))

# print(textwrap.fill(doc, width=20))      # 按指定宽度进行排版


'''
shorten(text,width,**kwargs)函数截断文本以适应宽度.该函数首先把文本中所有连续空白字符替换(或折叠)为一个空白字符,
如果能够适应指定的宽度就返回,否则就在文本尾部丢弃足够多的单词并替换为指定的占位符'''
from textwrap import shorten

shorten('Hello     World!', width=15)  # 宽度足以容纳所有字符
shorten('Hello     World!', width=10)  # 指定的宽度大小
shorten('Hello     World!', width=11)
shorten('Hello     World!', width=11, placeholder='.')  # 指定占位符
shorten('Hello     World!', width=5, placeholder='...')  # 指定的宽度太小

'''
indent(text,prefix,predicate=None)函数对文本进行锁紧并未所有非空行增加指定的前导字符或前缀,听过
predicate可以更加灵活地控制为哪些行增加前导字符'''

from textwrap import indent

example = '''
hello 
    world
    a 
    
good'''
# print(indent(example, '+' * 4))  # 默认为所有非空行增加前缀
# print(indent(example, '+' * 4, lambda line: True))  # 为所有行增加前缀
print(indent(example, '+' * 4, lambda line: len(line) < 3))  # 只为长度小于3的行增加前缀

'''5,dedent(text)函数用来删除文本中每一行的所有公共前导空白字符'''
from textwrap import dedent

example = '''
    hello
    world
good'''
print(dedent(example))

'''TextWrapper类'''
'''前面介绍的wrap,fill,shorten函数在内部都是先创建一个TextWrappper类的实例,然后再调用该实例的方法,如果需要
频繁调用这几个函数的的话,就会重复创建TextWrapper类的实例,严重影响效率,可以创建TextWrapper类的实例然后再调用该实例
的方法'''
from textwrap import TextWrapper

wrapper = TextWrapper(width=70, initial_indent='+', placeholder='...')
print(wrapper.wrap('hello world' * 40))
print(wrapper.fill('hello world' * 40))

# %%
# zlib模块提供的压缩功能
'''python标准库zlib提供的compress()和decompress()函数可以用于数据的压缩和解压缩,在压缩字符串之前需要先编码为字符串'''

import zlib

x = 'python程序设计系列图书'.encode()
# len(x)
y = zlib.compress(x)
print(len(x), len(y))  # 对于重复比比较小的信息,压缩比小
x = ('python程序设计系列图书' * 50).encode()
y = zlib.compress(x)
print(len(x), len(y))

zlib.decompress(y).decode()

# %%
# 字符串常量
'''python标准库string提供了英文字母大小写,数字字符,标点符号等常量,可以直接使用'''
import string

x = string.digits + string.ascii_letters + string.punctuation
print(x)

import random


def gererateStrongPwd(k):  # 生成制定长度的随机密码字符串
    return ''.join((random.choice(x) for i in range(k)))


gererateStrongPwd(10)

# %%
# 可变字符串
'''在python中,字符串属于不可变对象,不支持元的修改,如果需要修改其中的值,只能重新创建一个新的字符串对象.如果确实需要一个
支持原地修改的unicode字符串对象,可以使用io.StringIO()对象或array模块'''

from io import StringIO

s = 'Hello World'
sio = StringIO(s)  # 创建可变字符串对象
sio
sio.tell()  # 返回当前位置
sio.read()  # 从当前位置开始读取字符串
sio.getvalue()  # 返回可变字符串的全部内容
sio.tell()
sio.seek(6)  # 重新定位当前位置
sio.write('SDIBT')  # 从当前位置开始写入字符串,自动移动指针
sio.read()  # 从当前位置开始读取字符串
sio.getvalue()
sio.tell()

s = 'Hello world'
from array import array

sa = array('u', s)  # 创建可变字符串对象
print(sa)
print(sa.tostring())  # 查看可变字符串对象内容
print(sa.tounicode())  # 查看可变字符串内容
sa[0] = 'F'  # 修改制定位置上的字符
print(sa)
sa.insert(5, 'w')  # 在指定位置上插入字符
print(sa)
sa.remove('l')  # 删除指定字符的首次出现
print(sa)
sa.remove('w')
print(sa)

# %%
# 中英文分词
'''如果字符串中有连续的英文和中文,可以根据字符串的规律自己编写代码将其切分'''

x = '狗 dog 猫 cat 杯子 cup 桌子 table 你好'
c = []
e = []
t = ''
for ch in x:
    if 'a' <= ch.lower() <= 'z':
        t += ch
    elif t:
        e.append(t)
        t = ''
if t:
    e.append(t)
    t = ''

for ch in x:
    if 0x4e00 <= ord(ch) <= 0x9fa5:  # 基本汉字unicode编码范围
        t += ch
    elif t:
        c.append(t)
        t = ''
if t:
    c.append(t)
    t = ''

print(c)
print(e)

'''python拓展库jieba和snownlp很好的支持了中文分词.在自然语言处理领域经常需要对文字进行分词,
分词的准确度直接影响了后续文本处理和挖掘算法的最终结果'''
import jieba

x = '分词的准确度直接影响了后续文本处理和挖掘算法的最终结果'
jieba.cut(x)
list(jieba.cut(x))
list(jieba.cut('纸杯'))
print(list(jieba.cut('花纸杯')))

jieba.add_word('花纸杯')  # 增加词条
print(list(jieba.cut('花纸杯')))  # 使用新题库进行分词

import snownlp

snownlp.SnowNLP('学而时习之,不亦说乎').words
snownlp.SnowNLP(x).words

# %%
# 汉字到拼音得到转换
'''python扩展库pypinyin支持汉字到拼音的转换,并且可以和分词扩展库配合使用'''
from pypinyin import lazy_pinyin, pinyin

lazy_pinyin('中行')
lazy_pinyin('中行', 1)  # 带声调的拼音
lazy_pinyin('中行', 2)  # 另一种拼音形式,数字表示前面字母的声调
lazy_pinyin('中行', 3)  # 只返回拼音首字母
lazy_pinyin('重要', 1)  # 能够根据词组智能识别多音字
lazy_pinyin('重阳', 1)
pinyin('重阳')  # 返回拼音
pinyin('重阳节', heteronym=True)  # 返回多音字的所有读音

x = '中英文混合test123'
lazy_pinyin(x)  # 自动调用已安装的Jieba扩展库分词功能
lazy_pinyin(jieba.cut(x))
x = '今年的疫情有点严重'
sorted(x, key=lambda ch: lazy_pinyin(ch))  # 按拼音对汉字进行排序
