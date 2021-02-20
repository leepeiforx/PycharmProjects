from common import chaojiying as sy
from selenium import webdriver
from time import sleep
from PIL import Image

# %%
# 图片验证码检验
pic_identify = sy.ChaoJiYingClient(username=sy.user_name[0],
                                   password=sy.password[0],
                                   soft_id=sy.soft_id)

# pic = open(r'C:\Users\bolat\Desktop\train.jpg', 'rb').read()
# print(pic_identify.PostPic(pic, 9004)['pic_str'])

# %%
# 12306模拟登陆编码流程
#     使用selenuim打开登陆页码
#     对当前selenuim打开的页面进行截图
#     对验证码所在的的局部区域进行裁剪(好处:将验证码图片和模拟登陆进行一一对应)
#       使用超级鹰识别验证图片(坐标)

driver_exe_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
url = 'https://kyfw.12306.cn/otn/resources/login.html'
chrome = webdriver.Chrome(executable_path=driver_exe_path)
# 窗口最大化
chrome.get(url)
chrome.maximize_window()
login_switch = chrome.find_element_by_xpath('//li[@class="login-hd-account"]')
login_switch.click()

sleep(3)
# 对当前页面进行截图并保存
chrome.save_screenshot('./full_screen.png')
full_screen_png = './full_screen.png'
# 确定验证码图片的左上角,右下角(确认裁剪区域)
# 确定验证码图片对应的左上角
code_img_ele = chrome.find_element_by_class_name('loginImg')
location = code_img_ele.location  # 验证码图片左上角的坐标x,y

# 左上角和右下角的坐标
size = code_img_ele.size  # (验证码标签对应的长和宽)

rangle = ((location['x'], location['y'],
           location['x'] + size['width'], location['y'] + size['height']))

i = Image.open(full_screen_png)
code_img_name = './code_img.png'
# 根据指定区域进行图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)


#%%

# 将验证码提交给超级鹰进行识别
pic_identify = sy.ChaoJiYingClient(username=sy.user_name[0],
                                   password=sy.pass_word[0],
                                   soft_id=sy.soft_id)

pic = open(code_img_name, 'rb').read()
pic_info = pic_identify.PostPic(pic, 9004)
print(pic_info['pic_str'], pic_info['pic_id'])

#%%
pic_identify.ReportError(im_id='8130717345575300011')
