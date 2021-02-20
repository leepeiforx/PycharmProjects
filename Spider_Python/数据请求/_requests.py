# 需求:爬取sogou首页的信息
import requests
import json

# %%
if __name__ == '__main__':
    # 指定url
    url = 'https://www.sogou.com/'
    # 发起请求(get方法会返回一个响应对象)
    response = requests.get(url)
    # 获取响应数据,.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('Done')

# %%
# 需求: 爬取搜狗指定词条的搜索结果页面(简易网页采集器)
# 反爬机制:UA伪装:user-agent(请求载体的身份标识)
# UA伪装: 网站会检测对应请求的载体身份标识,如果检测到请求到请求载体的身份标识是某款浏览器
# 则说明该请求是一个正常的请求.如果反之,则表示该请求是一个不正常的(爬虫)请求,则很有可能拒绝.
if __name__ == '__main__':
    # UA伪装:将对应的UA封装到一个字典中
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    #    处理url携带的参数:封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定url发起的请求是携带参数的,并且请求过程中已经处理过了
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    file_name = kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_name, '保存成功!!!')

# %%
# 需求: 破解百度翻译
# --post请求,(携带了参数)
# -- 相应数据是一组json数据
if __name__ == '__main__':
    # 指定Url
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    # post请求参数处理,同get请求一致
    word = input('input a word')
    data = {'kw': word}
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据,json()方法返回的时obj(如果确认响应数据是json,才使用.json()方法)
    dic_obj = response.json()
    print(dic_obj)
    # 持久化存储
    file_name = word + '.json'
    with open(file_name, 'w', encoding='utf-8') as fp:
        # 因为输出的Json中含有中文,所以不应该使用ascii
        json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('Done')

# %%
# 需求:爬取豆瓣电影分类排行榜中的电影详细数据
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': 11,
        'interval_id': '100:90',
        'action': '',
        # 从库中的第几部电影去取
        'start': '0',
        # 一次获取的个数
        'limit': 20
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    response = requests.get(url, params=param, headers=headers)
    list_data = response.json()
    with open('./douban.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp, ensure_ascii=False)
    print('Done!')

# %%
# 需求:爬取肯德基餐厅查询中指定地点的餐厅数量
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    city = input('输入你所在的城市:')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    for i in range(1, 5):
        param = {
            'cname': '',
            'pid': '',
            'keyword': city,
            'pageIndex': i,
            'pageSize': '10'
        }
        response = requests.post(url, data=param, headers=headers)
        page_text = response.text
        with open('.{}.txt'.format(city), 'w+', encoding='utf-8') as fp:
            fp.write(page_text)
    print('Done')

# %%
# 需求: 爬取国家药品监督总局基于中华人民共和国化妆品生成许可证相关数据
if __name__ == '__main__':
    # 批量获取不同企业的ID值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    id_list = []  # 存储企业的ID
    all_data_list = []  # 存储所有企业详情数据
    # 参数的封装
    for page in range(1, 6):
        param = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        page_info = requests.post(url, data=param, headers=headers).json()
        for dic in page_info['list']:
            id_list.append(dic['ID'])

    # 获取企业详情信息

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id_lst in id_list:
        data = {
            'id': id_lst
        }
        detail_json = requests.post(post_url, data=data, headers=headers).json()
        all_data_list.append(detail_json)

    # 持久化存储
    with open('./makeup_corp_detail.json', 'w+', encoding='utf-8') as fp:
        json.dump(all_data_list, fp=fp, ensure_ascii=False)
        print('Done')
