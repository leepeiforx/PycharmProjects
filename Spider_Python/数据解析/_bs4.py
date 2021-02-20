from bs4 import BeautifulSoup
import requests

# %%
if __name__ == '__main__':
    file_path = r'D:\file\python爬虫课件\第三章：数据解析'
    html_file = file_path + '/test.html'
    with open(html_file, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'lxml')
        # print(soup.a)  # soup.tagName 返回html中第一次出现的tagName标签
        # print(soup.div)

        # find('tagName') : 返回等同于soup.tagName
        # print(soup.find('div'))  # print(soup.div)
        # print(soup.find('div', class_='song'))      # 这里的class_也可以是id,attr
        # print(soup.findAll('a'))

        # print(soup.select('.tang'))
        # print(soup.select('.tang > ul > li > a')[0])        # '>'号表示一个层级
        # print(soup.select('.tang > ul a')[0])       # 空格表示多个层级

        # print(soup.select('.tang > ul a')[0].text)
        # print(print(soup.select('.tang > ul a')[0].string))
        # print(soup.select('.tang > ul a')[0].get_text())

        # print(soup.select('.tang > ul')[0].text)
        # print(soup.select('.tang > ul')[0].string)

    print(soup.select('.tang > ul a')[0]['href'])

    # %%
    # 需求:爬取三国演义小说所有章节标题和章节内容
    if __name__ == '__main__':
        # 对首页的页面进行爬取
        url = 'http://sanguo.5000yan.com/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        }
        page = requests.get(url, headers=headers)
        page.encoding = 'utf-8'
        page_text = page.text
        # 在首页中解析出章节的标题和详情页url
        # 实例化BeautifulSoup,需要将页面数据加载到该对象中
        soup = BeautifulSoup(page_text, 'lxml')
        lst = soup.select('.list > ul > li')
        fp = open('./sangguo.txt', 'w+', encoding='utf-8')
        for l in lst:
            title = l.string
            detail_href = 'http://sanguo.5000yan.com/' + l.a['href']
            # 对详情页发起请求,解析出章节内容
            datail_page = requests.get(detail_href, headers=headers)
            datail_page.encoding = 'utf-8'
            datail_page_text = datail_page.text
            # 解析详情页的内容
            detail_soup = BeautifulSoup(datail_page_text, 'lxml')
            div_content = detail_soup.find('div', class_='grap')
            # 解析章节的内容
            content = div_content.text
            fp.write(title + ':' + content + '\n')
            print(title, '爬取成功')
            fp.close()
        print('Done!')
