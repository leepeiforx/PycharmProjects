import requests

# %%
url = 'https://www.sogou.com/web?query=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
# ip代理
proxies = {
    'http': '49.89.143.39:3000'
}

p = requests.get('http://icanhazip.com', headers=headers, proxies=proxies)
print(p.text)
