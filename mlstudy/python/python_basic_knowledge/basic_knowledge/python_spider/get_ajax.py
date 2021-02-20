from lxml import etree
import requests
import csv
import re


class Spider:
    file_path = open(r'C:\Users\Administrator\Desktop\da\jianshu_info(ajax).csv',
                     'wt', newline='')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    pars = []

    def __init__(self):
        filed = ['标题', '作者', '评论数', '点赞数']
        writer = csv.writer(self.file_path)
        writer.writerow(filed)

    def totalPage(self):
        for i in range(1, 16):
            data = '&'.join(self.pars)
            url = 'http://www.jianshu.com/?'+data+'&page={}'.format(i)

    def getData(self, url):
        print(url)
        html = requests.get(url, headers=self.headers).text
        response = etree.HTML(html)
        selectors = requests.xpath('//*div[@id="list-container"]/ul/li')
        for sel in selectors:
            one = 'seen_snote_ids[]='+one.xpath('@data-note-id')[0]
            self.pars.append(one)
        item = {}
        flag = 0
        like = re.findall('<span><i class="iconfont ic-list-like"></i>\s+(\d+)</span',html)
        comment = re.findall(r'iconfont ic-list-comments (\d+)', html)
        result =response.xpath('//*div[@id="list-container"]/ul/li/div')
        for res in result:
            item[1] = res.xpath('a/text()')[0]
            item[2] = res.xpath('div/a[1]/text')[0]
            item[3] = comment[flag]
            item[4] = like[flag]

        flag += 1
        row = [item[i] for i in range(1, 9)]
        self.writer.writerow(row)

if __name__ == '__main__':
    jian = Spider()
    jian.totalPage()