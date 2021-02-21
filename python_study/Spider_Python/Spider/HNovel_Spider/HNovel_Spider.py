import numpy as np
import pandas as pd
import re
import requests
import time
from selenium import webdriver as wb


# %%

def random_ip():
    # 随机选择代理IP
    ips = ['115.221.240.39:9999	',
           '39.137.69.10:80',
           '36.25.243.251:80',
           '39.137.95.74:80',
           '39.137.95.69:8080',
           '221.180.170.104:8080',
           '39.137.69.8:8080',
           '101.4.136.34:81']

    i = np.random.randint(0, len(ips))
    return ips[i]


def get_title(link):
    ip = random_ip()
    proxy = {
        'https': ip
    }
    res = requests.get(link, proxies=proxy)
    res.encoding = 'utf-8'
    res = res.text
    pattern = '<td class="tal"(.*?)+\W+a href="(.*?)" target=.*class="subject">(.*?)</a>'
    titles = re.findall(pattern=pattern, string=res)

    data = {}
    data_list = []
    for tl in titles:
        data['title'] = tl[2]
        data['href'] = 'http://ty.cxb2048.com/2048/' + tl[1]
        data_list.append(data)
        data = {}
    df = pd.DataFrame(data_list)
    df.to_csv(r'C:\Users\bolat\PycharmProjects\PyProjects\Spider\HNovel_Spider\2046.csv',
              mode='a+', encoding='gbk')


# if __name__ == '__main__':
# nows = time.perf_counter()
# links = ['http://ty.cxb2048.com/2048/thread.php?fid-52-page-{}.html'.format(str(i)) for i in range(145, 681)]
# current_index = 145
# for link in links:
#     time1 = time.perf_counter()
#     print('正在爬取第', current_index, '页数据......')
#     get_title(link)
#     print('Done')
#     time.sleep(np.random.randint(2, 5))
#     current_index += 1
#     print('用时:', round(time.perf_counter()-time1, 1), '秒')
#
# cost = time.perf_counter() - nows
# print('总用时cost:', cost)

#%%

def get_title_sel(link):
    chrome_options = wb.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = wb.Chrome(options=chrome_options)
    driver.get(link)
    items = driver.find_elements_by_xpath('//tr[@class="tr3 t_one"]')
    for item in items:
        hrefs = item.find_elements_by_xpath('./td[2]/a')[0]
        hrefs = hrefs.get_attribute('href')
        print(hrefs)
        title = item.find_elements_by_xpath('./td[2]/a')[0]
        title = title.text
        print(title)

link = r'http://ty.cxb2048.com/2048/thread.php?fid-52.html'
get_title_sel(link)


#%%
