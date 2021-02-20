import requests
import json
import pprint

query ='烤鸭'
region ='北京'

par = {
    'query': query,
    'region': region,
    'output': 'json',
    'ak': 'FFSaIYCjGG9fZapPpdvFjgCaR1rUZnhu'
}
url='http://api.map.baidu.com/place/v2/search?'
test_url = 'http://api.map.baidu.com/place/v2/search?&query=烤鸭&region=北京&output=json&ak=FFSaIYCjGG9fZapPpdvFjgCaR1rUZnhu'
res = requests.get(url, params=par)
json_data = json.loads(res.text)
# pprint.pprint(json_data)

for js in json_data['results']:
    print(js['name'])