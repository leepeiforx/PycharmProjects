import requests
import re
import time
from multiprocessing import Pool

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/63.0.3239.132 Safari/537.36'
}

def re_scraper(url):
    res  = requests.get(url, headers=headers)

    ids = re.findall('<h2>\s+(.*?)\s+</h2>',res.text)
    contents = re.findall('<div class="content">\s+<span>\s+(.*?)\s+</span>',res.text)

    for qiubai_id, content in zip(ids, contents):
        data = {
            'qiubai_id': qiubai_id.strip(),
            'content': content.strip()
        }
        return data

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
            for i in range(1,14)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print('串行爬虫:', end_1-start_1)

    start_2 = time.time()
    pool = Pool(processes=2)            #2个线程
    pool.map(re_scraper, urls)
    end_2 = time.time()
    print('双线程:',end_2-start_2)

    start_4 = time.time()
    pool = Pool(processes=4)            #4个线程
    pool.map(re_scraper, urls)
    end_4 = time.time()
    print('四线程:', end_4 - start_4)
