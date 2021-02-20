# coding=utf-8

from lxml import etree
import requests
from bs4 import BeautifulSoup
import re
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

qiubai_urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
               for i in range(1, 36)]

qiubai_url = 'https://www.qiushibaike.com/text/page/1'

def re_spider(url):
    wb_data = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', wb_data.text, re.S)
    levels = re.findall('<div class="articleGender manIcon">(.*?)</div>', wb_data.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', wb_data.text, re.S)
    laugths = re.findall('<span class="stats-vote">.*?<i class="number">(.*?)</i>', wb_data.text, re.S)
    comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i>', wb_data.text, re.S)
    for id, level, content, laugth, comment in zip(ids, levels, contents, laugths, comments):
        data = {
            'id': id.strip(),
            'level': level,
            'content': content.strip(),
            'laugth': laugth,
            'comment': comment
        }
        return data


def bs_spider( url ):             #Beautifulsoup爬虫
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    ids = soup.select('div.author.clearfix > a > h2')
    levels = soup.select('div.author.clearfix > div')
    contents = soup.select('a > div > span')
    laugths = soup.select('span.stats-vote > i')
    comments = soup.select('a > i.number')
    for id, level, content, laugth, comment in zip(ids, levels, contents, laugths, comments):
        data = {
            'id': id.get_text().strip(),
            'level': level.get_text(),
            'content': content.get_text().strip(),
            'laugth': laugth.get_text(),
            'comment': comment.get_text()
        }
        return (data)

def lxml_spider(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[contains(@class ,"article block untagged mb15")]')
    try:
        for url_info in url_infos:
            id = url_info.xpath('div[1]/a[2]/h2/text()')
            level = url_info.xpath('div[1]/div/text()')
            content = url_info.xpath('a[1]/div/span')
            laugh = url_info.xpath('div[2]/span[1]/i/text()')
            comment = url_info.xpath('div[2]/span[2]/a/i/text()')
            data = {
                'id': id,
                'level': level,
                'content': content,
                'laugh': laugh,
                'comment': comment
            }
            return(data)
    except IndexError:
        pass

if __name__ == '__main__':
    for name,spider in [('Regex',re_spider),('BeautifulSoup',bs_spider),('lxml',lxml_spider)]:
        start = time.time()
        for url in qiubai_urls:
            spider(url)
        end = time.time()
        print(name, end-start)



