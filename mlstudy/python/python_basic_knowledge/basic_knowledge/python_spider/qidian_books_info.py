import requests
import openpyxl
from lxml import etree
import time

qidian_books_urls = ['https://www.qidian.com/all?orderId=&style=1&page={}'.format(str(i))
                     for i in range(1, 61219)]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_qidian_info(url):
    wb_data = requests.get(url, headers=headers)
    selector = etree.HTML(wb_data.text)
    book_infos = selector.xpath('//div[@class = "book-mid-info"]')
    for info in book_infos:
        book_name = info.xpath('h4/a/text()')[0]
        author = info.xpath('p[1]/a[1]/text()')[0]
        type = info.xpath('p[1]/a[2]/text()')[0]
        sub_type = info.xpath('p[1]/a[3]/text()')[0]
        lodaing = info.xpath('p[1]/span/text()')[0]
        briefs = info.xpath('p[2]/text()')[0].strip()
        num_of_words = info.xpath('p[3]/span/text()')
        print(num_of_words)


##字数选项(num_of_words)存在字体反扒
if __name__ == '__main__':
    get_qidian_info('https://www.qidian.com/all?orderId=&style=1&page=1')
