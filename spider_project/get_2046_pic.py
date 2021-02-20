import os
import requests
from lxml import etree
import time
import random


# %%


def get_pic(link, hd, proxy=None):
    page_info = requests.get(link, headers=hd, proxies=proxy)
    page_info.encoding = 'utf-8'
    page_text = page_info.text
    page_info = etree.HTML(page_text)

    title = page_info.xpath('//*[@id="subject_tpc"]/text()')[0]
    pic_lst = page_info.xpath('//div[@id="read_tpc"]/img/@src')

    if not os.path.exists(r'spider_project\{}'.format(title)):
        os.mkdir(r'spider_project\{}'.format(title))
    else:
        pass
    file_path = r'spider_project\{}'.format(title)

    print('开始下载')
    start = time.perf_counter()
    for pic in pic_lst:
        pic_name = pic.split('/')[-1]
        if pic_name not in os.listdir(file_path):  # 检查是该pic是否已经被下载,如果没有,则下载它
            try:
                pic_info = requests.get(pic).content
                time.sleep(random.randint(1, 3))
            except ConnectionError:
                print('链接错误,请重试')
                break
            else:
                with open(file_path + r'\{}'.format(pic_name), 'wb') as fp:
                    fp.write(pic_info)
                    fp.close()
                    print(pic_name, '下载完成')
        else:
            continue
    end = time.perf_counter()
    print('共耗时{}'.format(round((end - start), 2)))


if __name__ == '__main__':
    proxy = {'http': '127.0.0.1:57816',
             'https': '127.0.0.1:57816'}

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    url = r'https://s1.v5uh.xyz/2048/read.php?tid-3110365.html'
    get_pic(url, headers, proxy=proxy)
