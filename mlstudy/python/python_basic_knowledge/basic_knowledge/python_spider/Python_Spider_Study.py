# coding=utf-8
import re
import requests
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_web_info(url):
    wb_data = requests.get(url, headers=headers)
    return wb_data


def judgement_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'


qiubai_urls = ['https://www.qiushibaike.com/text/page/{}/'.format(i) for i in range(1, 5)]


def get_qiubai_info(urls):
    for url in urls:
        time.sleep(2)
        wb_data = get_web_info(url)
        ids = re.findall('<h2>(.*?)</h2>', wb_data.text, re.S)
        levels = re.findall('<div class="articleGender manIcon">(.*?)</div>', wb_data.text, re.S)
        sexs = re.findall('<div class="articleGender (.*?)">', wb_data.text, re.S)
        contents = re.findall('<div class="content">.*?<span>(.*?)</span>', wb_data.text, re.S)
        laugths = re.findall('<span class="stats-vote">.*?<i class="number">(.*?)</i>', wb_data.text, re.S)
        comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i>', wb_data.text, re.S)
        for id, level, sex, content, laugth, comment in zip(ids, levels, sexs, contents, laugths, comments):
            data = {
                'id': id.strip(),
                'level': level,
                'sex': judgement_sex(sex),
                'content': content.strip(),
                'laugth': laugth,
                'comment': comment
            }
            print(data)


douban_book_rank_250 = 'https://book.douban.com/top250'
res = get_web_info(douban_book_rank_250)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)
