import os
import requests
from lxml import etree
import time
import random


def get_pic(link, hd, proxies=None):
    page_info = requests.get(link, headers=hd, proxies=proxies)
    page_info.encoding = 'utf-8'
    page_text = page_info.text
    page_info = etree.HTML(page_text)

    _title = page_info.xpath('//*[@id="subject_tpc"]/text()')[0]
    pic_list = page_info.xpath('//div[@id="read_tpc"]/img/@src')

    fp = r'H:\下载\imgs\{}'.format(_title)
    if not os.path.exists(fp):
        os.mkdir(fp)
    else:
        pass
    print('下载路径:{}'.format(fp))
    print('开始下载')

    start_time = time.perf_counter()
    for pic in pic_list:
        pic_name = pic.split('/')[-1]
        if pic_name not in os.listdir(fp):  # 检查是该pic是否已经被下载,如果没有,则下载它
            try:
                s = requests.session()
                s.keep_alive = False  # 关闭多余连接
                pic_info = requests.get(pic).content
                time.sleep(random.randint(1, 3))
            except ConnectionError:
                print('链接错误,请重试')
                break
            else:
                pic_path = fp + '\\' + pic_name
                with open(pic_path, 'wb') as f_save:
                    f_save.write(pic_info)
                    f_save.close()
                    print(pic_name, '下载完成')
        else:
            continue
    end_time = time.perf_counter()
    print('共耗时:', round((end_time - start_time), 2))


if __name__ == '__main__':
    proxy = {'http': '127.0.0.1:57816',
             'https': '127.0.0.1:57816'}

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    url = r'https://s1.v5uh.xyz/2048/read.php?tid-1972966-fpage-14.html'
    get_pic(url, headers)
