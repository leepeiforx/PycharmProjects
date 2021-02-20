import re
from bs4 import BeautifulSoup
import requests

href = 'https://www.xsnvshen.com/album/32682'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

res = requests.get(href, verify=False)
bs = BeautifulSoup(res.text, 'lxml')
img = bs.select('#bigImg')
img = 'https:' + img[0].get('src')
number = bs.select('#time > span:nth-child(1)')
number = number[0].get_text().replace('共 ', '').replace(' 张', '')
number = int(number) + 1
img_href = img[:-7]
img_href1 = [img_href + '00{}.jpg'.format(i) for i in range(1, 10)]
img_href2 = [img_href + '0{}.jpg'.format(i) for i in range(10, number)]
img_list = img_href1 + img_href2
for img in img_list:
    print(img)


