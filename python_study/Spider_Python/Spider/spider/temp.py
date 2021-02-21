import requests

import re

#
link = 'http://bj.xiaozhu.com/'
res = requests.get(link)
prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>(.*?)</span>', res.text)
for price in prices:
    print(price[0])
