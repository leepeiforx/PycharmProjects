from selenium import webdriver as wb
import numpy as np
import pandas as pd
import time
import re


# %%
def get_index(link):
    data = {}
    data_list = []
    chrome_options = wb.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = wb.Chrome(options=chrome_options)
    driver.get(link)
    items = driver.find_elements_by_xpath('//div[@class="group"]')
    for item in items:
        imgs = item.find_elements_by_xpath('./div[@class="photo"]/a/img')[0]
        title = imgs.get_attribute('alt')
        imgs_link = imgs.get_attribute('src')
        hrefs = item.find_elements_by_xpath('./div[@class="photo"]/a')[0]
        hrefs = hrefs.get_attribute('href')

        data['img_src'] = imgs_link
        data['title'] = title
        data['href'] = hrefs

        data_list.append(data)
        data = {}

    # print(data_list)
    return data_list


if __name__ == '__main__':
    links = ['https://www.lesmao.co/plugin.php?id=group&page={}'.format(str(i)) for i in range(1, 21)]

    current_index = 1
    file_path = r'C:\Users\bolat\PycharmProjects\PyProjects\Spider\MM_spider\lesmao_spider.csv'
    time_counter = time.perf_counter()
    for link in links:
        time1 = time.perf_counter()
        print('正在爬取第', current_index, '页数据')
        data_list = get_index(link)
        df = pd.DataFrame(data_list)
        df.to_csv(file_path, mode='a+', encoding='gbk')
        current_index += 1
        print('用时:', round(time.perf_counter() - time1, 1), '秒')
        time.sleep(np.random.randint(2, 5))
    cost = time.perf_counter() - time_counter
    print('总用时:', cost, '秒')
