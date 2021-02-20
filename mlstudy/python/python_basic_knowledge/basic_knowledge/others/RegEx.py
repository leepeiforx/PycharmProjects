import re                                       #导入re模块

re_test = 'alpha.beta...gamma delta'            #测试用字符串
re.split('[\. ]+',re_test)                       #使用指定字符作为分隔符进行分割
re.split('[\. ]+',re_test,maxsplit=2)            #最多分隔2次
re.split('[\. ]+',re_test,maxsplit=1)
pat = '[a-zA-Z]+'                                #查找所有的单词
re.findall(pat,re_test)
pat = '{name}'
re_test2 ='Dear {name}...'
re.sub(pat,'Mr.Dong',re_test2)
s ='a s d'
re.sub('a|s|d', 'good', s)
s1 = "It's a very very very good idea."
s2 =  re.sub(r'(\b\w+) \1', r'\1', s1)

re.sub('a', lambda x:x.group(0).upper(), 'aaa abc abde')                  #全部大写

re.sub('[a-zA-Z]', lambda x:chr(ord(x.group(0)) ^ 32), 'aaa abc abde')      #大小写互换

re.subn('a','dfg','aaa abc abde')                                           #返回新字符串和替换次数

re.escape('http://www.python.org')                      #字符串转义

print(re.match('done|quit', 'done'))                     #匹配成功,返回match对象
print(re.match('done|quit', 'doe'))                      #匹配不成功,返回None

str1 = 'aaa         bb    c d e ffff     ggg'
result_str1 = ' '.join(str1.split())                     #直接使用字符串对象方法
print(result_str1)

result_str2 = re.sub('\s+',' ',str1)                     #使用re模块的字符串替换方法
print(result_str2)

email = 'tony@tiremove_thisger.net'
m = re.search('remove_this',email)                       #使用search()+切片删除字符串指定的内容
email[:m.start()]+email[m.end():]

re.sub('remove_this','',email)                           #直接使用re模块的sub()方法

email.replace('remove_this','')                          #直接使用字符串替换方法

example ='Beautiful is better than ugly.'                #以'\'开头的元字符实现字符串的特定搜索
re.findall('\\bb.+?\\b',example)
re.findall('\\bb\w+\\b',example)
re.findall('\\Bh\w+?\\b',example)
print(re.findall('\\Bh\w+?\\b',example))                 #不以h开头且含有h字母的单词剩余部分

web_str ='<html><head>This is head.</head><body>This is body.</body></html>'
pattern_web = r'<html><head>(.+?)</head><body>(.+?)</body></html>'

result_wb_str = re.search(pattern_web, web_str)
result_wb_str.group(1)
result_wb_str.group(2)

