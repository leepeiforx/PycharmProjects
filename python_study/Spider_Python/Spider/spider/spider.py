import requests
from bs4 import BeautifulSoup

link = r'http://bj.xiaozhu.com/'
link2 = r'https://www.lesmao.co/plugin.php?'
r = requests.get(link2)
p = {
    'id': 'group',
    'page': 2
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}

soup = BeautifulSoup(r.text, 'lxml')
try:
    print(soup.prettify())
except ConnectionError:
    print('连接错误')
