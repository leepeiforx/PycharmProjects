import numpy as np
import time
from selenium import webdriver as wb


# %%
def start_spider(url):
    chrome_option = wb.ChromeOptions()
    chrome_option.add_argument('--headless')
    driver = wb.Chrome(options=chrome_option)
    driver.get(url)
    time.sleep(5)
    iframe = driver.find_element_by_id('g_iframe')
    driver.switch_to.frame(iframe)

    comments = driver.find_elements_by_class_name('u-hd4')[1]
    # print(comments.text)
    comments = comments.text.split('(')[1].split(')')[0]
    return comments, driver


def get_max_page(new_comments):
    """ 根据评论总数, 计算出总分页数 """
    print('=== ' + new_comments + '  ===')
    # 每页显示 20 条最新评论
    offset = 20
    max_page = round(int(new_comments) / offset)
    print('一共有', max_page, '个分页')
    return max_page

def go_nextpage(driver):
    new_botton = driver.find_elements_by_xpath('//div[@class="m-cmmt"]/div[3]/div/a')[-1]
    if new_botton.text == '下一页':
        new_botton.click()


def get_comments(is_fisrt, driver):
    items = driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]/div[@class="itm"]')
    # 通常首页的数据中包含 15 条精彩评论, 20 条最新评论, 这里只保留最新评论(这个方法不准确)
    if is_first:
        items = items[15: len(items)]

    data_list = []
    data = {}

    for each in items:

        # 用户ID
        userIds = each.find_elements_by_xpath('./div[@class="head"]/a')[0]
        userIds = userIds.get_attribute('href').split("=")[1]
        # print(userId)

        # 用户昵称
        nickNames = each.find_elements_by_xpath("./div[@class='cntwrap']/div[1]/div/a")[0].text

        # 评论内容
        comments = each.find_elements_by_xpath('./div[@class="cntwrap"]/div[1]/div')[0]
        comments = comments.text.split('：')[1]

        # 点赞数
        like = each.find_elements_by_xpath("./div[@class='cntwrap']/div[@class='rp']/a[1]")[0]
        like = like.text
        if like:
            like = like.split('(')[1].split(')')[0]
        else:
            like = '0'
        # 头像地址
        avator = each.find_elements_by_xpath('./div[@class="head"]/a/img')[0]
        avator = avator.get_attribute('src')

        data['userId'] = userIds
        data['nickName'] = nickNames
        data['comment'] = comments
        data['like'] = like
        data['avator'] = avator
        print(data)
        data_list.append(data)
        data = {}
    print(data_list)
    return data_list


if __name__ == '__main__':

    url = r'https://music.163.com/#/song?id=1356540446'
    comment_num, driver = start_spider(url)
    max_page = get_max_page(comment_num)

    current = 1
    is_first = True
    while current <= int(max_page):
        print('正在抓取第', current, '页数据')
        if current == 1:
            is_first = True
        else:
            is_first = False
        data_list = get_comments(is_first, driver)

        go_nextpage(driver)
        time.sleep(np.random.randint(10, 12))
        current += 1
