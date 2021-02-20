import requests
import re

link = r'http://nlegs.com/'

url = r'http://nlegs.com/girls/2020/02/11/13571.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                  (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
}


def nleg_spider(url):
    imgs = []
    r = requests.get(url, headers=headers)
    hrefs = re.findall('<div class="panel-body">\s+<a href="(.*?)">', r.text)
    for i in range(len(hrefs)):
        hrefs[i] = 'http://nlegs.com/' + hrefs[i]
    print(len(hrefs), '\n')
    print(hrefs)
    # for href in hrefs:
    #     r = requests.get(href, headers=headers)
    #     # img = re.search('<div class="row">\s+.*?\s+src="(.*?)">', r.text)
    #     print(r.text)


nleg_spider(url)

