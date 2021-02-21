import requests
import time
from bs4 import BeautifulSoup

# %%
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Hosts': 'http://bj.xiaozhu.com/'
}
link = r'http://bj.xiaozhu.com/'

r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')


def judege_sex(class_name):
    if class_name == 'member_boy_ico':
        return 'male'
    else:
        return 'female'


def get_links(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#page_list > ul > li >a')
    for link in links:
        href = link.get('href')
        get_info(href)

def get_info(href):
    wb_data = requests.get(href, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.pho_info > h4 > em')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    for title, address, price, img, name, sex in zip(titles, addresses, prices, imgs, names, sexs):
        data = {
            'title': title.get_text().strip(),
            'address': address.get_text().strip(),
            'price': price.get_text(),
            'img': img.get('src'),
            'name': name.get_text(),
            'sex': judege_sex(sex.get('class'))
        }
        print(data)



if __name__ == '__main__':
    urls = r'http://bj.xiaozhu.com/'
    get_links(urls)
    time.sleep(2)


