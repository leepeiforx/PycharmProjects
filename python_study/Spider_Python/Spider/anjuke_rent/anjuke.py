import requests
from lxml import etree

links = 'https://xa.zu.anjuke.com/?from=navigation'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
res = requests.get(links, headers=headers)
html = etree.HTML(res.text)
title_lists = html.xpath('//div[@class="zu-info"]/h3/a/b')
data_list = []
for tl in title_lists:
    data_list.append(tl.text)

print(data_list)

#%%
