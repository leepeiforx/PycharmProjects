# 实战 识别古诗文网登陆页面中的验证码
# 使用打码平台步骤 (1,将验证码图片下载到本地)
import requests
from lxml import etree

from common import cloud_auth_code as cac


# %%

# 封装识别验证码图片的函数
def getCodeText():
    pass


if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    auto_code_address = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(auto_code_address, headers=headers).content
    with open('./auto_code_img.jpg', 'wb') as fp:
        fp.write(img_data)
        print('Done')
        fp.close()

    # 调用打码平台的示例程序进行验证码图片数据识别
    file_path = r'C:\Users\bolat\PycharmProjects\pythonProject\auto_code_img.jpg'

    # 实例化验证码识别对象,状态各参数
    auto_code_identify = cac.FateadmApi(cac.app_id, cac.app_key, cac.pd_id, cac.pd_key)
    # 调用里面的识别PredictFromFile()方法
    res = auto_code_identify.PredictFromFile(file_name=file_path, pred_type='30400')
    print(res.pred_rsp.value, res.cust_val)
