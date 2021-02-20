import requests
from lxml import etree
from bs4 import BeautifulSoup
import re

# %%
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                  (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
}

link = r'https://book.douban.com/top250'
r = requests.get(link, headers=headers)
html = etree.HTML(r.text)
result = etree.tostring(html)
# print(result)

# %%
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
# %%
# Xpath

urls = ['https://www.lesmao.co/plugin.php?id=group&page={}'.format(str(i)) for i in range(1, 3)]


# print(urls)


def re_spider(urls):
    for url in urls:
        pics = []
        r = requests.get(url, headers=headers)
        titles = re.findall('.jpg" alt=(.*?)/></a></div>', r.text)
        comments = re.findall('<div class="data">\s+(.*?)\s+</div>', r.text)
        imgs = re.findall('target="_blank"><img src="((.*?)+\s+(.*?)+.jpg)', r.text)
        for img in imgs:
            pics.append(img[0])
            for i in range(len(pics)):
                pics[i] = pics[i].replace('\r', '')
                pics[i] = pics[i].replace('\n', '')


re_spider(urls)

