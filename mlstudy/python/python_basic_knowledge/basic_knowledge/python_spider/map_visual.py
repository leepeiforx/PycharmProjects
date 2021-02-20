# coding = utf-8

from lxml import etree
import requests
import json
import csv

fp = open(r'C:\Users\Administrator\Desktop\da\map.csv',
          'wt', newline='', encoding='utf-8')

writer = csv.writer(fp)
writer.writerow(('address', 'longitude', 'latitude'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


def get_user_address(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    if selector.xpath('//div[2]/div/div[3]/div[2]/ul/li[4]/text()'):
        address = selector.xpath('//div[2]/div/div[3]/div[2]/ul/li[4]/text()')
        get_geo(address[0].split('·')[0])
    else:
        pass


def get_user_url(url):
    url_part = 'https://www.qiushibaike.com'
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[contains(@class ,"article block untagged mb15")]')
    for url_info in url_infos:
        url_part_urls = url_info.xpath('div/a[2]/@href')
        if len(url_part_urls) == 1:
            user_part_url = url_part_urls[0]
            get_user_address(url_part + user_part_url)


def get_geo(address):
    par = {
        'address': address,
        'output': 'json',
        'ak': 'FFSaIYCjGG9fZapPpdvFjgCaR1rUZnhu'
    }

    api = 'http://api.map.baidu.com/geocoder/v2/'

    res = requests.get(api, params=par)
    json_data = json.loads(res.text)
    try:
        geo = address
        print(geo)
        lng = json_data['result']['location']['lng']
        print(lng)
        lat = json_data['result']['location']['lat']
        print(lat)
        writer.writerow((geo, lng, lat))
    except IndexError:
        pass
    except Exception:
        pass


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}'.format(str(i))
            for i in range(1, 36)]
    for url in urls:
        get_user_url(url)
