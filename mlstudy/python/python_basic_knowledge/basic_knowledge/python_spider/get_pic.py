import requests
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
download_links = []
path = r'C:\Users\Administrator\Desktop\da\photos\pic'
link = 'https://www.pexels.com/search/love'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/63.0.3239.132 Safari/537.36'
}
res = requests.get(link, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
imgs = soup.select('article > a >img')

for img in imgs:
    photo = img.get('src')
    download_links.append(photo)


for item in download_links:
    print(item)
    data = requests.get(item, headers=headers)
    fp = open(path+item.split('?')[0][-10:], 'wb')
    fp.write(data.content)
    fp.close()

