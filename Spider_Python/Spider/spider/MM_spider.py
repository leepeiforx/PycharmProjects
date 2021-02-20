import requests
from bs4 import BeautifulSoup
import time

# %%
# 获取网页
link = r'http://www.santostang.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                  (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
}
# 有时爬虫会遇到服务器长时间不返回， 这时爬虫程序就会一直等待，
# 造成爬虫程序没有顺利地执行。 因此， 可以用Requests在timeout参数设定的秒数结束之后停止等待响应。
# 意思就是， 如果服务器在 timeout 秒内没有应答， 就返回 异常。
r = requests.get(link, headers=headers, timeout=1.01)

# print(r.text)

# 提取数据
soup = BeautifulSoup(r.text, 'lxml')
title = soup.find('h1', class_='post-title').a.text.strip()

#
# 1) r.tex t是服务器响应的内容， 会自动根据响应头部的字符编码进行解码。
# 2) r.encoding是服务器内容使用的文本编码。
# 3) r.status_code用于检测响应的状态码， 如果返回200， 就表示请求成功了：
# 如果返回的是4xx， 就表示客户端错误； 返回5xx则表示服务器错误响应。
# 我们可以用r.status code来检测请求是否正确响应。
# 4) r.content 是字节方式的响应体， 会自动解码gzip和deflate编码的响应数据。
# 5) r.json（）是Requests中内置的JSON解码器。
# print('文本编码', r.encoding)
# print('响应状态码', r.status_code)
# print('字符串方式的响应体', r.text)


# 为了请求特定的数据， 我们需要在URL的查询字符串中加入某些数据。如果
# 你是自己构建URL， 那么数据一般会跟在一个问号后面， 并且以键／值的形式放在
# URL中， 如https://www.lesmao.co/plugin.php?id=group&page=2在Requests中，
# 可以直接把这些参数保存在字典中， 用params构建至URL中。
key_dicts = {'id': 'group', 'page': '2'}
r = requests.get('https://www.lesmao.co/plugin.php', params=key_dicts)
print('URL已经正确编码', r.url)
print('字符串方式的响应体\n', r.text)

