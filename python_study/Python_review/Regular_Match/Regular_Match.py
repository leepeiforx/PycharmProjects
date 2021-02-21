'''正则表达式语法'''

# 正则表达式基本语法

'''正则表达式常用元字符'''
'''
.       匹配除换行符之外的任意单个字符
*       匹配位于*之前的字符或子模式的0次或多次出现
+       匹配位于+之前的字符或子模式的1次或多次出现
-       在[]之内用来表示范围
|       匹配位于|之前或之后的字符
^       匹配以^后面的字符或模式开头的字符串
$       匹配以$前面的字符或模式结束的字符串
?       匹配位于"?"之前的0个或1个字符或子模式,即问号之前的字符或子模式是可选的
        紧随任何其他限定符(*,+,?,{n},{n,},{n,m}之后时,表示"非贪心"匹配模式,
        "非贪心"模式匹配尽可能短的字符串,而默认的"贪心"模式匹配尽可能长的字符串.
        例如,在字符串"oooo"中,"o+?"只匹配单个o,而o+匹配所有o
\       表示位于\之后的为转义字符
\num    此处的num是一个正整数,表示前面字符或子模式的编号,例如,"(.)\1"匹配两个连续的相同字符
\f      匹配一个换行符
\n      匹配一个换行符
\r      匹配一个回车符
\b      匹配单词头或单词尾
\B      与\b含义相反
\d      匹配任何数字,相当于[0-9]
\D      与\d意义相反,相当于[^0-9]
\s      匹配任何空白字符,包括空格,制表符,换页符,可与[\f\n\r\t\v]等效
\S      与\s含义相反
\w      匹配任何字母,数字以及下划线,相当于[a-zA-Z0-9_]
\W      与\w相反,与[^a-zA-Z0-9_]等效
()      将位于()内的内容作为一个整体来对待
{}      按{}中指定的次数进行匹配,例如{3,8}表示前面的字符或模式至少3次而至多重复8次
[]      匹配位于[]中的任意一个字符
[^xyz]  ^放在[]内表示反向字符集,匹配除x,y,z之外的任何字符
[a-z]   字符范围,匹配指定范围内的任何字符
[^a-z]  反向范围字符,匹配除小写英文字母之外的任何字符
'''

"""如果以\开头的元字符与转义字符相同,则需要使用\\,或者使用原始字符串,在字符串加上字符r或者R表示原始字符串,
字符串中的任何字符都不再进行转义"""

# %%
# 正则表达式扩展语法
"""
(?P<groupname>)     为子模式命名
(?iLmsux)           设置匹配模式,可以是几个字母的组合,每个字母含义与编译标志相同
(?:...)             匹配但不捕获该匹配的子表达式
(?P=groupname)      表示在此之前的命名为groupname的子模式
(?#...)             表示注释
(?<=...)            用于正则表达式之前,如果<=后的内容出现在字符串中则匹配,但不返回<=之后的内容
(?=...)             用于正则表达式之前,如果=后的内容出现在字符串中则匹配,但不返回=之后的内容             
(?!=...)            用于正则表达式之前,如果!=后的内容出现在字符串中则匹配,但不返回!=之后的内容     
(?!...)             用于正则表达式之前,如果!后的内容出现在字符串中则匹配,但不返回!之后的内容 
"""

# %%
# 正则表达式集锦
'''
1.最简单的正则表达式是普通字符串,智能匹配自身
2.'[pjc]ython可以匹配'python','jyphon','cython'
3.'[a-zA-Z0-9]可以匹配一个任意大小写字母或数字
4.'[^abc]'可以一个匹配任意除'a','b','c'之外的字符
5,'python|perl' 或'p(ython|erl)'都可以匹配python或perl
6 r'(http://)?(www\.)?python.\org' 智能匹配http://www.python.org,'http://python.org','www.python.org'和'python.org'
7.'^http'只能匹配所有以http开头的字符串
8.(pattern)*,允许模式重复0次或多次
9.(pattern)+,允许模式重复1次或多次
10.(pattern){m,n}: 允许模式重复m~n次,注意逗号后面不要有空格
11.'(a|b)*c'匹配(包含0个)a或b,后面紧跟一个字母c
12.'ab{1,}': 等价于ab+,匹配以字母a开头后面紧跟一个或多个字母b的字符串
13.^[a-zA-Z]{1}([a-zA-Z0-9._]){4,19}$,匹配长度为5~20的字符串,必须以字母开头并且后面可带数字,字母,'_','.'的字符串
14.^(\w){6,20}$,匹配长度6~20的字符串,可以包含字母,数字,下划线
15.^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$, 检查给定字符串是否为合法IP地址
16.^(13[4-9]\d{8}|(15[01289]\d{8}$,检查给定字符串是否为移动手机号码
17,^[a-zA-Z]+$,检查给定字符串是否只包含英文大小写字母
18,^\w+@(\w+\.)+\w+$,检查给定字符串是否为合法的电邮地址
19,^(\-)?\d+(\.\d{1,2})?$,检查给定字符串是否为最多带有2位小数的整数或负数
20,[\u4e00-\u9fa5],匹配给定字符串中的常用汉字
21,\d{4}-\d{1,2}-d{1,2}, 匹配指定格式的日期
22,\d{18}|\d{15},检查给定字符串是否为合法身份证格式
23,^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[,._]).{8,}$ 检查给定字符串是否为强密码,必须同时包含英文大写字母,英文小写字母,数字或
                                                    特殊符号(如英文逗号,英文句号,下划线),并且长度必须至少8位
24,'(?!=[\'\"\/:=%).+',如果给定字符串中包含',",/,=,%和?则匹配失败
25,'(.)\\1+',匹配任意字符或模式一次或多次重复出现
26,'((?P<f>\b\w+\b)\s+(?P=f))',匹配连续出现两次的单词
27,'((?P<f>.)(?P=f)(?P<g>.)(?P=g))',匹配AABB形式的成语或字母组合
'''
'''需要注意的十,正则表达式指示进行形式上的检查,并不一定保证内容一定正确.'''

# %%
# 直接使用正则表达式模块re处理字符串

# re模块中的方法
'''
compile(pattern,[,flags])           创建模式对象
escape(string)                      将字符串中的所有特殊正则表达式字符转义
findall(pattern,string[,flags])     列出字符串中模式的所有匹配项
finditer(pattern,string,flags=0)    返回包含所有匹配项的迭代对象,其中每个匹配项都是match对象
fullmatch(pattern,string,flags=0)   尝试把模式作用于整个字符串,返回match对象或None
match(pattern,string[,flags])       从字符串开始处匹配模式,返回match对象或None              
purge()                             清空正则表达式缓存
search(pattern,string[,flags])      在整个字符串中寻找模式,返回match对象或None
split(pattern,string[,maxsplit=0])  根据模式匹配项分割字符串
sub(pat,repl,string[,count=0])      将字符串所有pat的匹配项用repl替换,返回新字符串,repl可以是字符串或返回字符串的可调用对象
                                    该可调用对象作用于每个匹配的match对象
subn(pat,repl,string[,count=0])     将字符串所有pat的匹配项用repl替换,返回包含新字符串和替换次数的二元组,repl可以是字符串或
                                    返回字符串的可调用对象,该可调用对象作用于每个匹配的match对象
'''
'''
其中flags的值可以是re.I(表示忽略大小写),re.L(支持本地字符集的字符),re.M(多行匹配模式),re.S(使元字符"."匹配任意字符,包括换行符)
re.U(匹配unicode字符),re.X(忽略模式中的空格,并可以使用#注释)的不同组合(使用|进行组合)
'''

import re

text = 'alpha.beta...gamma delta'
re.split('[\.]+', text, maxsplit=2)  # 最多分隔2次
re.split('[\.]+', text, maxsplit=1)  # 做多分隔1次
pat = '[a-zA-Z]+'
re.findall(pat, text)  # 查找所有单词
pat = '{name}'
text = 'Dear {name}...'
re.sub(pat, 'Mr.Li', text)  # 字符串替换
s = 'a s d'
re.sub('a|s|d', 'good', s)
s = "It's a very good good idea."
re.sub(r'(\b\w+) \1', r'\1', s)

'AAA Abc Abde'
re.sub('[a-z]', lambda x: x.group(0).upper(), 'aaa abc abde')
re.sub('[a-zA-Z]', lambda x: chr(ord(x.group(0)) ^ 32), 'aaa Abc abde')

re.subn('a', 'dfg', 'aaa abc abd')

re.escape('http://www.python.org')  # 字符串转义

print(re.match('done|quit', 'done'))  # 匹配成功,返回match对象

print(re.match('done|quit', 'doe!'))  # 匹配不成功,返回None

# 下面的代码使用不同的方法删除字符串中多余的空格,如果遇到连续多个空格则只保留一个,同时删除字符串两侧的所有空白字符
s = 'aaa      bb    c d e fff   '
' '.join(s.split())  # 直接使用字符对象的方法

' '.join(re.split('[\s]+', s.strip()))  # 同时使用re模块中的函数和字符串对象的方法

re.sub('[\s]+', ' ', s.strip())  # 直接使用re模块字符串替换方法

# 下面的代码使用几种不同的方法来删除字符串中指定的内容
email = 'tony@tiremove_thisger.net'
m = re.search('remove_this', email)  # 使用search()方法返回的match对象
email[:m.start()] + email[m.end():]  # 字符串切片

re.sub('remove_this', '', email)  # 直接使用re模块的sub()方法

email.replace('remove_this', '')  # 直接使用字符串替换方法

# 下面的代码使用以\开头的元字符时限字符串的特定搜索
example = 'Beautiful is better than ugly.'
re.findall(r'\bb.+?\b', example)  # 以字母b开头的完整单词,此处问号"?"表示非贪心模式

re.findall(r'\bb.+\b', example)  # 贪心模式的匹配结果

print(re.findall(r'\bb\w*\b', example))

print(re.findall(r'\Bh.+?\b', example))  # 不以h开头且含有h字母的单词剩余部分

re.findall('\w+', example)  # 所有单词

re.findall(r'\b\w.+?\b', example)  # 使用原始字符串

re.split('\s', example)  # 使用任何空白字符分隔字符串

re.findall('\d+\.\d.\d+', 'python 3.7.6')  # 查找并返回x.x.x形式的数字

re.findall('\d+\.\d.\d+', 'python 3.7.6 python 2.7.8')

s = '<html><head>This is head.</head><body>This is body</body></html>'
pattern = r'<html><head>(.+)</head><body>(.+)</body></html>'
result = re.search(pattern, s)
result.group(0)
result.group(1)
result.group(2)

# %%
# 使用正则表达式对象处理字符串
# 1,match,search,findall
"""
正则表达式对象的match(string[,pos[,endpos]])方法在字符串开头或指定位置进行搜索,模式必须出现现在字符串开头或指定位置
search(string[,pos[,endpos]])方法在整个字符串或指定范围中进行搜索
findll(string[,pos[,endpos]])方法字符串中查找所有符合正则表达式的字符串并以列表形式返回
"""
example = 'ShanDong Institute of Business and Technology'
pattern = re.compile(r'\bB\w+\b')  # 查找以B开头的单词
pattern.findall(example)  # 使用正则表达式对象的findall()方法

pattern = re.compile(r'\w+g\b')  # 查找以g结尾的单词
pattern.findall(example)

pattern = re.compile(r'\b[a-zA-Z]{3}\b')  # 查找3个字母长的单词
pattern.findall(example)

pattern.match(example)  # 从字符串开头开始匹配,失败返回空值
pattern.search(example)  # 在整个字符串中搜索,成功

pattern = re.compile(r'\b\w*a\w*\b')  # 查找所有含有字母a的单词
pattern.findall(example)

text = 'He was carefully disguised but captured quickly by police.'
re.findall(r'\w+ly\b', text)  # 查找所有以ly结尾的单词

# %%
# 2,sub,subn
'''正则表达式对象的sub(repl,string[,count=0]),和subn(repl,string[,count=0])方法用来实现字符串替换功能,其中repl
可以为字符串或返回字符串的可调用对象
'''
import this

example = this.s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

example = "".join([d.get(c, c) for c in example])

pattern = re.compile(r'\bb\w*\b', re.I)  # 匹配以B或b开头的按此
print(pattern.sub('*', example))  # 将符合条件的单词替换为*
print(pattern.sub(lambda x: x.group(0).upper(), example))  # 把所有匹配项都改为大写

pattern = re.compile(r'\bb\w*\b')  # 匹配以字母b开头的单词
print(pattern.sub('*', example))

# %%
# split()
'''正则表达式对象的split(string[,maxsplit=0])方法用来实现字符串分割'''
example = 'one,two,three,four/five,six?seven[eight]nine|ten'
pattern = re.compile(r'[,/?[\]|]')  # 指定多个可能的分隔符
pattern.split(example)

example = 'one1two2three3four4five5six6seven7eight8nine9ten10'
pattern = re.compile(r'\d+')
pattern.split(example)

example = 'one two   three  four,five,..,.six.seven,eight8nine9ten10'
pattern = re.compile(r'[\s,.\d]+')
pattern.split(example)

# %%
# match对象
'''正则表达式或正则表达式对象的match()方法和search()方法匹配成功后都会返回match对象,
match对象的主要方法有
    group(){返回匹配的一个或多个子模式内容},
    groups(){返回一个包含匹配的所有子模式内容的元组},
    groupdict(){返回包含匹配的所有命名子模式内容的字典},
    start()返回指定子模式内容的起始位置
    end()返回子模式内容的结束位置的前一个位置
    span()返回一个包含指定子模式起始位置和结束位置前一个位置的元组'''

m = re.match(r'(\w+) (\w+)', 'Issac Newton,physicist')
m.group(0)  # 返回整个模式内容
m.group(1)  # 返回第一个个子模式内容
m.group(2)  # 返回第二个个子模式内容
m.group(1, 2)  # 返回指定的多个子模式内容

# 下面的代码演示子模式扩展语法的用法
m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
m.group('first_name')  # 使用命名打得子模式
m.group('last_name')
m = re.match(r'(\d+).(\d+)', '24.1632')  # 返回所有匹配的子模式(不包括第0个)
m.groups()
m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
m.groupdict()  # 以字典形式返回匹配的记过
exampleString = '''There should be one -- and preferably only one --obvious way 
to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.'''
pattern = re.compile(r'(?<=\w\s)never(?=\s\w)')  # 查找不在句子开头和结尾的never
matchResult = pattern.search(exampleString)
matchResult.span()

pattern = re.compile(r'(?<=\w\s)never')  # 查找位于句子末尾的单词
matchResult = pattern.search(exampleString)
matchResult.span()

pattern = re.compile(r'(?:is\s)better(\sthan)')  # 查找前面是is的better than组合
matchResult = pattern.search(exampleString)
matchResult.span()
print(matchResult.group(0))
print(matchResult.group(1))

pattern = re.compile(r'\b(?i)n\w+\b')  # 表示以n或N字母开头的所有单词
index = 0
while True:
    matchResult = pattern.search(exampleString, index)
    if not matchResult:
        break
    print(matchResult.group(0), ':', matchResult.span(0))
    index = matchResult.end(0)

pattern = re.compile(r'(?<!not\s)be\b')  # 查找前面没有单词not的be
index = 0
while True:
    matchResult = pattern.search(exampleString, index)
    if not matchResult:
        break
    print(matchResult.group(0), ':', matchResult.span(0))
    index = matchResult.end(0)

print(exampleString[13:15])

pattern = re.compile(r'(\b\w*(?P<f>\w+)(?P=f)\w*\b)')  # 匹配连续相同字母的单词

# index = 0
# while True:
#     matchResult = pattern.search(exampleString, index)
#     if not matchResult:
#         break
#     print(matchResult.group(0), ':', matchResult.group(2))
#     index = matchResult.end(0) + 1

pattern.findall(exampleString)
