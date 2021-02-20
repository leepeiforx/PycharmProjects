# 模拟登录:
# 爬取基于需要用户登录才能获取的信息
# 需求:模拟人人网登录
import requests
from lxml import etree
import common.cloud_auth_code as cac

# %%
url = 'http://www.renren.com/SysHome.do'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)

# 该论坛使用了asp.net来提交验证,所以需要将get网页的__VIEWSTATE数据事先保存下来,
# 然后再post的关键字中提交

auto_code_address = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
img_data = requests.get(auto_code_address, headers=headers).content
with open('./auto_code.jpg', 'wb') as fp:
    fp.write(img_data)
    print('Done')
    fp.close()

# 调用打码平台的示例程序进行验证码图片数据识别
file_path = r'C:\Users\bolat\PycharmProjects\pythonProject\auto_code.jpg'

# # 实例化验证码识别对象,状态各参数
# auto_code_identify = cac.FateadmApi(cac.app_id, cac.app_key, cac.pd_id, cac.pd_key)
# # 调用里面的识别PredictFromFile()方法
# res = auto_code_identify.PredictFromFile(file_name=file_path, pred_type='30600')
# auth_code = res.pred_rsp.value
#%%
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202104178899'
data = {
    'email': 'babilun9.19@163.com',
    'icode': 'hvukm',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '8a3218baf01a63248f7aae3836621f64caa039df0e92e10876893b3e1993ade6',
    'rkey': '8a1483087e0621d533428856ee95fc7a',
    'f': '',
}
response = requests.post(login_url, data=data, headers=headers).text
print(response)

# 这部分没法实现,直接跳到selenuim来实现