import re
import requests

# %%
a = 'xx ixxjshdxxlovexxsffaxxpythonxx'
infor = re.findall('xx(.*?)xx', a)
print(infor)

# %%
# re模块的search（）函数匹配并提取第一个符合规律的内容，返回一个正则表达式对象。
# search（） 函数的语法如下：
# re.match(pattern,string,flags=O)
# 其中：
# (1) pattern 为匹配的正则表达式。
# (2) string 为要匹配的字符串。
# (3) flags 为标志位，用于控制正则表达式的匹配方式，如是否区分大小写，多行匹配等。

a = 'oneltwo2three3'
infors = re.search('\d+', a)
print(infors)

print(infors.group())

# %%
# re 模块提供了sub()函数用于替换字符串中的匹配工页,sub()函数的语法如下：
# re.sub(pattern , repl , string , count=O , flags=O)
# 其中：
# (l）pattern为匹配的正则表达式。
# (2) repl为替换的字符串。
# (3) string 为要被查找替换的原始字符串。
# (4) counts 为模式匹配后替换的最大次数，默认0 表示替换所有的匹配。
# (5) flags 为标志位，用于控制正则表达式的匹配方式，如是否区分大小写，多行匹配等。

phone = '123-345-79879'
new_phone = re.sub('\D', '', phone)
print(new_phone)

#%%
# findall()函数匹配所有符合规律的内容，并以列表的形式返回结果。
infos = re.findall('\d', a)
print(infos)

#%%
link = 'http://bj.xiaozhu.com/'
res = requests.get(link)
prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>(.*?)</span>', res.text)
for price in prices:
    print(price[0])

#%%
# re 模块中包含一些可选标志修饰符来控制匹配的模式
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别（ locale-aware ）匹配
# re.M 多行匹配，影响^和$
# re.S 使匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符。这个标志影响＼w, \W, \b，\B．
# re.X 该标志通过给予更灵活的格式，以便将正则表达式写得更易理解

a = '<div>指数</div>'
word = re.findall('<div>(.*?)</div>', a)
print(word)
b = '''<div>指数
    </div>'''
word2= re.findall('<div>(.*?)</div>', b)
print(word2)
# 因为findall()函数是逐行匹配的，当第l 行没有匹配到数据时，就会从第2 行开
# 始重新匹配，这样就没法匹配到div 标签中的文字信息，这时便可通过re.S 来进行跨行匹配。
word3 = re.findall('<div>(.*?)</div>', b, re.S)
print(word3)
# 跨行匹配的结果会有一个换行符， 这种数据需要清洗才能存入数据库，strip（）方法去除换行符。
print(word3[0].strip())

