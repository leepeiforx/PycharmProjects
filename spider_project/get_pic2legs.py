import requests
import time
from lxml import etree
import os
import random


def get_pic_href(url):
    page_text = requests.get(url, headers=headers, proxies=proxy).text
    page_info = etree.HTML(page_text)
    file_name = page_info.xpath('/html/body/div[1]/div/div[2]/div[1]/p/strong/text()')[0].strip('\n')
    if not os.path.exists(save_path + '\\' + file_name):
        os.mkdir(save_path + '\\' + file_name)
    file_path = save_path + '\\' + file_name

    pic_hrefs_list = []
    links = page_info.xpath('//a[@class="thumbnail"]/@href')
    for link in links:
        link = link.replace('image', 'images')
        link = link.replace('html', 'jpg')
        link = 'http://www.uuleg.com' + link
        pic_hrefs_list.append(link)
    return pic_hrefs_list, file_path


def download_pic(pic_url_lists, file_path):
    print('下载路径为:', file_path)
    for url in pic_url_lists:
        response = requests.get(url, headers=headers, proxies=proxy).content
        title = url.split('/')[-1]
        save_path = file_path + '\\' + title
        with open(save_path, 'wb') as fp:
            fp.write(response)
            print('get:', title)
            time.sleep(random.randint(1, 3))
    print('Done')


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    proxy = {
        'http': '127.0.0.1:57816',
        'https': '127.0.0.1:57816'
    }
    url = r''

    save_path = r'H:\下载\imgs'
    pic_hrefs_list, file_path = get_pic_href(url)
    download_pic(pic_hrefs_list, file_path)

