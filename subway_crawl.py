import random
import time

import requests
from common.utils import get_ua
import json
import pandas as pd
import common.utils as ut


# %%
def get_size(city):
    ak = ut.ak
    url = 'http://api.map.baidu.com/place/v2/search?query=地铁&region={0}&output=json\
    &page_size=20&page_num=0&ak={1}'.format(city, ak)
    res = requests.get(url, headers={'User-Agent': get_ua()})
    data = json.loads(res.text)

    if data['total'] is not None:
        return data

    return 0


def get_data(city):
    """

    :param city:
    :return:
    """
    ak = ut.ak
    sizes = get_size(city)
    df = pd.DataFrame()
    page_sizes = range(int(sizes['total'] / 20 + 1))
    for idx in page_sizes:
        print('正在抓取第{}页数据集'.format(idx))
        url = 'https://api.map.baidu.com/place/v2/search?query=地铁&region={0}&output=json\
         &page_size=20&page_num={1}&ak={2}'.format(city, idx, ak)
        res = requests.get(url)
        data = json.loads(res.text)
        if data['total'] > 0:
            df_data = pd.DataFrame(data['results'])
            df_data['lat'] = df_data['location'].apply(lambda x: x['lat'])
            df_data['lng'] = df_data['location'].apply(lambda x: x['lng'])
            df_data['cnts'] = df_data['address'].apply(lambda x: len(x.split(';')))
            df_data.drop(columns='location', inplace=True)
            df = df.append(df_data)
            time.sleep(random.randint(3, 5))

    return df



if __name__ == '__main__':
    city_list =['']
    df_all = pd.DataFrame
    for city in city_list:
        df = get_data(city)
        df_all.apply(df)
    df_all.to_csv('subway.csv')

