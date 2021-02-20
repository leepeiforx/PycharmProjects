from lxml import etree
import requests
import os

# %%
if __name__ == '__main__':
    file_path = r'D:\file\python爬虫课件\第三章：数据解析'
    html_file = file_path + '/test.html'
    # 实例化一个etee对象,并且将需要解析的源码加载到该对象上
    tree = etree.parse(html_file)
    r = tree.xpath('//div[@class="song"]/img/@src')[0]
    print(r)

# %%
# 需求:爬取58二手房房源信息
if __name__ == '__main__':
    url = 'https://xa.58.com/ershoufang/e204/'
    param = {
        'from': 'esf,esf_list',
        'PGTID': '0d30000c-001e-378c-7ce7-8bf95c202f52',
        'ClickID': 1
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    page_text = requests.get(url, params=param, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="property-content-title"]/h3/text()')
    fp = open('./58house.txt', 'w', encoding='utf-8')
    i = 0
    for li in li_list:
        i += 1
        title = li.strip(' ')
        fp.write(title + '\n')
        print('第{}行已下载完成'.format(i))
    fp.close()
    print('Done')

# %%
# 需求:解析下载图片数据
if __name__ == '__main__':
    url1 = 'http://pic.netbian.com/4kmeinv/'
    url2 = ['http://pic.netbian.com/4kmeinv/index_{}.html'.format(str(i)) for i in range(2, 6)]
    li_list = [url1]
    if not os.path.exists('pic'):
        os.mkdir('./pic')
    file_path = r'C:\Users\bolat\PycharmProjects\pythonProject\pic'
    for url in url2:
        li_list.append(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    for url in li_list:
        print('正在抓取{}数据'.format(url))
        page = requests.get(url, headers=headers)
        page.encoding = 'gbk'
        page_text = page.text
        tree = etree.HTML(page_text)
        pic_list = tree.xpath('//ul[@class="clearfix"]/li/a/@href')

        for pic in pic_list:
            href = 'http://pic.netbian.com' + pic
            detail_page = requests.get(href, headers)
            detail_page.encoding = 'gbk'
            datail_page_text = detail_page.text
            tree = etree.HTML(datail_page_text)
            title = tree.xpath('//div[@class="view"]/div[1]//text()')[0]
            href = tree.xpath('//div[@class="view"]/div[2]/a/img/@src')[0]
            # 得到图片的源地址需要手动添加头
            href = 'http://pic.netbian.com/' + href

            # 图片不能直接下载,需要通过requests获取二进制文件,然后将二进制写入文件中
            img_data = requests.get(href, headers=headers).content
            f_abs_p = file_path + '/{}.jpg'.format(title)
            fp = open(f_abs_p, 'wb')
            fp.write(img_data)
            fp.close()
            # print(title, '下载完成')
        print('抓取{}数据完成'.format(url))
    print('Done')

# %%
# 需求:解析出所有城市名称https://www.aqistudy.cn/historydata/
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    city_lst = tree.xpath('//ul[@class="unstyled"]/div[2]/li/a/text()')

# %%
# 需求:简历模版下载

if __name__ == '__main__':
    original_url = 'https://sc.chinaz.com/jianli/'
    url_lst = [original_url]
    temp_urls = ['https://sc.chinaz.com/jianli/hushi_{}.html'.format(str(i)) for i in range(2, 6)]
    for ul in temp_urls:
        url_lst.append(ul)
    #     创建一个空文件夹用以存放下载文件
    if not os.path.exists('jianliLibs'):
        os.mkdir('./jianliLibs')

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    page = requests.get(original_url, headers=headers)
    page.encoding = 'urf-8'
    page_text = page.text
    tree = etree.HTML(page_text)
    url_lst = tree.xpath('//div[@id="container"]/div/p/a/@href')
    download_hrefs = []
    file_path = r'C:\Users\bolat\PycharmProjects\pythonProject\jianliLibs'
    for url in url_lst:
        url = 'https:' + url
        detail_page = requests.get(url, headers=headers)
        detail_page.encoding = 'utf-8'
        datail_page_text = detail_page.text
        download_lst = etree.HTML(datail_page_text)
        if download_lst.xpath('//div[@class="down_wrap"]'):
            title = download_lst.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
            download_link = download_lst.xpath('//div[@class="down_wrap"]/div[2]/ul//li[1]/a/@href')[0]
            # 下载压缩包,音频,图片等内容一律用requests请求响应并返回二进制文档
            download_data = requests.get(download_link, headers=headers).content
            file_name = file_path + '/{}.zip'.format(title)
            with open(file_name, 'wb') as fp:
                fp.write(download_data)
                print(title, '已下载')
    print('Done!')
