# 需求,爬取糗事百科中糗图板块下所有的糗图图片
import requests
import re
import os

# %%

if __name__ == '__main__':
    # 如何爬取图片数据 使用聚焦爬虫将页面中的糗图进行解析

    # 创建一个文件夹,保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(str(1))
    urls = ['https://www.qiushibaike.com/imgrank/page/{}/'.format(str(i)) for i in range(1, 5)]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    # content返回二进制形式的图片数据
    # text返回字符串,json()返回obj
    pattern = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
    img_src_list = []
    for url in urls:
        page_text = requests.get(url, headers=headers).text
        img_src_list.append(re.findall(pattern, page_text, re.S))


    for img_list in img_src_list:
        for src in img_list:
            # 拼接出一个完整的图片src
            src = 'https:' + src
            # 请求到图片的二进制数据
            img_data = requests.get(src, headers=headers).content
            # 生成图片的名称
            img_name = src.split('/')[-1]
            # 图片存储路径
            img_path = './qiutuLibs/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功')
    print('Done')
