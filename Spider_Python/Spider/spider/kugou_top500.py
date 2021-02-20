import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
}

link = r'https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'


def get_info(links):
    for link in links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        titles = soup.select('div.pc_temp_songlist > ul > li >a')
        ranks = soup.select('span.pc_temp_num')
        times = soup.select('span.pc_temp_time')
        for rank, title, time in zip(ranks, titles, times):
            data = {
                'rank': rank.get_text().strip(),
                'singer': title.get_text().strip().split('-')[0],
                'name': title.get_text().strip().split('-')[1],
                'time': time.get_text().strip()
            }
            print(data)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from'.format(str(i)) for i in range(1, 24)]
    get_info(urls)
    time.sleep(2)
    
