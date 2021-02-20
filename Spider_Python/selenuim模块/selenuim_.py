from selenium import webdriver
from time import sleep
from lxml import etree
# 导入动作链对应的类
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


# %%
# 实例化一个浏览器对象(传入浏览器的驱动路径)
chrome = webdriver.Chrome(executable_path='./chromedriver.exe')
# 让浏览器发起一个指定url的对应请求
chrome.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器浏览器当前页面的页面源码数据
page_text = chrome.page_source

tree = etree.HTML(page_text)
corp_name = tree.xpath('//ul[@id="gzlist"]/li/dl/@title')
print(corp_name)
sleep(5)
chrome.quit()

# %%
chrome = webdriver.Chrome(executable_path='./chromedriver.exe')
chrome.get('https://www.taobao.com/')
# 标签定位
search_input = chrome.find_element_by_id('q')

# 执行一组js程序(滚动一个屏幕(y)的位置)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 标签交互
search_input.send_keys('3080显卡')
# btn-search tb-bg 这种只需要选择其中一部分(如btn-search|tb-bg即可)
button = chrome.find_element_by_class_name('btn-search')
button.click()
sleep(5)
chrome.quit()

chrome.get('www.baidu.com')
sleep(2)
# 回退
chrome.back()
# 前进
chrome.forward()
chrome.quit()

# %%
# selsenuim处理iframe
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

chrome = webdriver.Chrome(executable_path='./chromedriver')
chrome.get(url)
# 如果定位的标签是存在与iframe标签之中的,则必须通过如下操作再进行标签定位

chrome.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域
div = chrome.find_element_by_id('draggable')

# 动作链
# 实例化一个动作链对象(传入浏览器对象)
action = ActionChains(chrome)

# 点击并长按指定的标签
action.click_and_hold(div)
for i in range(5):
    action.move_by_offset(17, 0).perform()  # .proform表示立即执行
    sleep(0.3)

# 释放动作链
action.release()
chrome.quit()

# %%
# 模拟登陆QQ空间

url = 'https://qzone.qq.com/'

chrome = webdriver.Chrome(executable_path='./chromedriver')
chrome.get(url)
chrome.switch_to.frame('login_frame')

a_tag = chrome.find_element_by_id('switcher_plogin')
a_tag.click()

sleep(2)
# chrome.switch_to.frame('login_frame')
user_name_tag = chrome.find_element_by_id('u')
user_name_tag.send_keys('407182089')
sleep(1)
user_password_tag = chrome.find_element_by_id('p')

user_password_tag.send_keys('tercent532110')
sleep(2)
login_button = chrome.find_element_by_id('login_button')
login_button.click()
sleep(3)
chrome.quit()

# %%
# 无头浏览器(phantomJs)
url = 'https://www.baidu.com/'

# 实例化Options对象
# chrome_options = Options()
# 这两种方法都可以
chrome_options = webdriver.ChromeOptions()
# 实现无头
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 实现规避检测
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

chrome = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
chrome.get(url)
page_text = chrome.page_source
print(page_text)

# 规避检测(实现让selenuim规避掉被检测的风险)

