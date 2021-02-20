import requests
import time
import re
from random import randint
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

renting_urls = ['https://cd.zu.anjuke.com/fangyuan/x1-zj40-lx1-mt1-p{}/'.format(i)
                for i in range(1, 11)]

fp = open(r'C:\Users\Administrator\Desktop\da\house_info.csv', 'w', newline='')

dic = {}


def get_web_info(url):
    wb_data = requests.get(url, headers=headers).text
    return wb_data


def get_house_info(info):
    house_intros = re.findall('<h3>\s+.*?title=(.*?)_soj=', info, re.S)
    house_layouts = re.findall('<p class="details-item tag">\s+(.*?)<span>', info, re.S)
    prices = re.findall('<div class="zu-side">\s+<p><strong>(\d+)</strong>', info)
    areas = re.findall('\|</span>(.*?)<span>\|</span>', info, re.S)
    floors = re.findall('<span>\|<\/span>\D+.*<i class="iconfont jjr-icon">', info)
    ids = re.findall('(<a target=.*?>)([\u4e00-\u9fa5]+.*?)</a>', info)
    locations = re.findall('(.*?)\s+</address>', info)
    hrefs = re.findall('<div class="zu-itemmod"\s+link=(.*_id=\d+)".*>', info)
    time.sleep(randint(2, 5))

    for house_intro, house_layout, price, area, floor, id, location, href in zip(house_intros, house_layouts,
                                                                                 prices, areas, floors, ids, locations,
                                                                                 hrefs):
        fl_rp1 = floor.replace('<span>|</span>', '').replace('<i class="iconfont jjr-icon">', '')

        data = {
            'house_intro': house_intro.strip(),
            'house_layout': house_layout.strip(),
            'price': float(price),
            'area': area,
            'floor': fl_rp1.strip(),
            'id': id[1],
            'location': location.strip().split('-')[0],
            'detail_loc': location.strip().split('-')[1],
            'href': href
        }
        writer.writerow(data.values())


if __name__ == '__main__':
    writer = csv.writer(fp)
    writer.writerow(('名称', '布局', '价格', '大小', '层高', '小区名称', '行政区', '详细位置'))
    for url in renting_urls:
        info = get_web_info(url)
        get_house_info(info)
    fp.close()
