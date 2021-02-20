#coding = utf-8
import requests
from lxml import etree
import csv
import time

douban_urls = ['https://book.douban.com/top250?start={}'.format(str(i))
               for i in range(0, 250, 25)]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}



def get_wb_info(url):
    wb_data = requests.get(url, headers=headers)
    selector = etree.HTML(wb_data.text)
    book_info_urls = selector.xpath('//tr[@class = "item"]')
    for book_info_url in book_info_urls:
        book_name = book_info_url.xpath('td[2]/div/a/@title')[0]
        foreign_name = book_info_url.xpath('td[2]/div/span[1]/text()')
        book_infos = book_info_url.xpath('td[2]/p[1]/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price =book_infos.split('/')[-1]
        rank_num = book_info_url.xpath('td[2]/div[2]/span[2]/text()')[0]
        quote = book_info_url.xpath('td[2]/p[2]/span/text()')
        comments = book_info_url.xpath('td[2]/div[2]/span[3]/text()')[0].strip().replace(' ','').replace('\n','')
        comment = comments if len(comments) !=0 else "空"
        url = book_info_url.xpath('td[2]/div/a/@href')
        writer.writerow((book_name,foreign_name,author,publisher,date,price,rank_num,quote,comment,url))

if __name__ == '__main__':
    fp = open(r'c:\users\administrator\desktop\da\douban_book_top250.csv','wt',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('book_name','foreign_name','author','publisher','date','price','rank_num','quote','comment','url'))
    for url in douban_urls:
        get_wb_info(url)
    fp.close()