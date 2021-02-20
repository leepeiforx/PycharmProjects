from multiprocessing.dummy import Pool
from lxml import etree
import requests
import os

# %%


# 需求:爬取梨视频的视频数据
# 原则,线程池只负责处理阻塞且耗时的操作
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

# 对下述url发起请求,解析出视频详情页url和视频的名称
url = 'https://www.pearvideo.com/category_5'

page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
video_titles = tree.xpath('//div[@class="vervideo-bd"]/a/div[2]/text()')
video_hrefs = tree.xpath('//div[@class="vervideo-bd"]/a/@href')
video_hrefs = ['https://www.pearvideo.com/' + video_href for video_href in video_hrefs]


download_lst = []
# 对详情页的url发起请求
for video_href in video_hrefs:
    datail_page_text = requests.get(video_href, headers=headers).text
    detail_tree = etree.HTML(datail_page_text)
    video_title = detail_tree.xpath('//h1[@class="video-tt"]/text()')[0]
    video_id = video_href[-7:]
    jsp_url = 'https://www.pearvideo.com/videoStatus.jsp'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Referer': video_href
    }
    param = {
        'contId': video_id
    }
    #     从详情页中解析出视频的地址
    web_info = requests.get(jsp_url, params=param, headers=headers).json()
    video_png = web_info['videoInfo']['video_image']
    video_url = web_info['videoInfo']['videos']['srcUrl']
    cont = 'cont-' + video_id
    video_url = video_url.replace(video_url.split('-')[0].split('/')[-1], cont)
    video_info = {
        'name':video_title,
        'url':video_url
    }
    download_lst.append(video_info)


def get_video_data(dic):
    _url = dic['url']
    name = dic['name']
    # 创建用于保存视频的文件夹
    if not os.path.exists('./PearVideoLibs'):
        os.mkdir('PearVideoLibs')
    #  得到视频的二进制数据
    video_data = requests.get(_url, headers=headers).content
    fp = './PearVideoLibs/{}.mp4'.format(name)
    print('开始下载{}'.format(name))
    with open(fp, 'wb') as fn:
        fn.write(video_data)
        fn.close()
    print('下载{}完成'.format(name))

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(get_video_data, download_lst)
    pool.close()
    pool.join()
    print('Done')