import time

from selenium import webdriver

# %%

driver = webdriver.Chrome()
driver.maximize_window()  # 浏览器最大化显示
first_url = 'https://www.baidu.com/'
driver.get(first_url)
driver.find_element_by_id('kw').send_keys('selenuim')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.set_window_size(1900, 1000)  # 自定义浏览器大小
second_url = 'http://news.baidu.com'
driver.get(second_url)
driver.back()  # 返回网页（新闻->百度）
time.sleep(1)
driver.forward()  # 前进网页（百度->新闻）

driver.quit()
# %%
# 简单对象定位
# webdriver提供了一系列的对象定位方法，常用的有以下几种
# · id
# · name
# · class_name
# · link text
# · partial_link_text
# · tag_name
# · xpath
# · css selector
driver = webdriver.Chrome()
driver.get(first_url)
time.sleep(2)
#########百度输入框的定位方式###########
try:
    driver.find_element_by_id('kw').send_keys('selenuim')  # 通过id方式定位
    driver.find_element_by_name('wd').send_keys('selenuim')  # 通过name方式定位
    driver.find_element_by_tag_name('input').send_keys('s_ipt')  # 通过class_name 针对百度输入框无法使用
    driver.find_element_by_class_name('s_ipt').send_keys('444')  # 通过CSS方式定位
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('kw')

except Exception:
    print('定位异常')
time.sleep(3)
driver.quit()

# %%
# xpath:attributer （属性）

# input标签下id =kw的元素
driver = webdriver.Chrome()
driver.get(first_url)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

# xpath:idRelative （id相关性）
# 在/form/span/input 层级标签下有个div标签的id=fm的元素
# id为'check' 的tr ，定位他里面的第2个td
# driver.find_element_by_xpath("//tr[@id='check']/td[2]").click()

# # xpath:position （位置）
# driver.find_element_by_xpath("//input").send_keys("selenium")
# driver.find_element_by_xpath("//tr[7]/td[2]").click()#第7个tr 里面的第2个td
#
# # xpath: href （水平参考）
# #在a标签下有个文本（text）包含（contains）'网页' 的元素
# driver.find_element_by_xpath("//a[contains(text(),'网页')]").click()
#
# # xpath:link
# #有个叫a的标签，他有个链接href='http://www.baidu.com/ 的元素
# driver.find_element_by_xpath("//a[@href='http://www.baidu.com/']").click()

# %%
# link定位
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(2)
browser.find_element_by_link_text('贴吧').click()
time.sleep(2)
browser.quit()

# %%
# Partial Link Text 定位
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_partial_link_text('贴').click()
time.sleep(3)
browser.quit()

# %%
# 层级定位
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
url = r'C:\Users\my_c\PycharmProjects\projects\Spider\Ajax\level_locate.html'
driver.get(url)
driver.find_element_by_link_text('Link1').click()

# 在父亲元件下找到link为Action的子元素
WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_link_text('dropdown1').is_displayed())
meau = driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')

# 鼠标定位到子元素上
webdriver.ActionChains(driver).move_to_element(meau).perform()

time.sleep(2)
driver.quit()

# %%
# 操作对象：
# · click 点击对象
# · send_keys 在对象上模拟按键输入
# · clear 清除对象的内容，如果可以的话
#
# WebElement  另一些常用方法：
# · text  获取该元素的文本
# · submit  提交表单
# · get_attribute  获得属性值

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenuim')
# driver.find_element_by_id('su').click()

# send_keys("XX") 　　用于在一个输入框里输入内容。
# click() 　　用于点击一个按钮。
# clear()　　 用于清除输入框的内容，比如百度输入框里默认有个“请输入关键字”的信息，
# 再比如我们的登陆框一般默认会有“账号”“密码”这样的默认信息。clear可以帮助我们清除这些信息。

# WebElement  另一些常用方法：
# · text  获取该元素的文本
# · submit  提交表单
# · get_attribute  获得属性值

# text
# 用于获取元素的文本信息

driver.find_element_by_id('su').submit()

# WebElement的方法：
# 一般来说，所有有趣的操作与页面进行交互的有趣的操作，都通过WebElement完成
# classselenium.webdriver.remote.webelement.WebElement(parent, id_)
# 这个类代表HTML页面元素

# id_#当前元素的ID
# tag_name#获取元素标签名的属性
# text#获取该元素的文本。
# click()#单击（点击）元素
# submit()#提交表单
# clear()#清除一个文本输入元素的文本
# get_attribute(name)#获得属性值
# s_selected(self)#元素是否被选择Whethertheelementisselected.
#
# is_enabled()#元素是否被启用
# find_element_by_id(id_)

# find_ element_ by_ css _ selector ：
# 通过元素的 class 选择，
# 如＜div class='bdy­inner'>test</div＞可以使用 find_element_ by_ css _ selector （’div.bdy-inner’）。
# find_ element_ by_ xpath ：通过 xpa也选择，
# 如＜fonn id＝”loginFonn与可以使用driver. find_ element_ by_ xpath（”／／form[@id＝’loginForm’］”）。
# id_element_ by _id：通过元素的 id 选择，
# 如＜div id＝’ bdy-inner'>test</div＞可以使用 driver.find_ element_ by一id（’ bdy-inner＇）。
# find_ element_ by_ name：通过元素的 name 选择，
# 如＜input name＝”usemame” type＝”text” ／＞可以使用 driver.find一element一by一＿name（’password’）
# find element_by_link_text： 通过链接地址选择，
# 如<a href=”continue.html”>Continue</a> 可以使用 driver.find_element_ by一link_text（℃ontinue＇）。
# find_ element_ by _partial_ link_text ：通过链接的部分地址选择，
# 如 q href=”continue.html”>Continue</a>可以使用 driver.find_ element_ by _partial_ link_ text（’Continue＇）。
# find_ element_ by_ tag_ name：通过元素的名称选择，
# 如＜h1> Welcome＜H1＞可以使用 driver.find_ element_ by_ tag_ name（’hl)
# find_ element_ by_ class_ name：通过元素的 class 选择，
# 如＜p class＝content”＞ Site content goes here.</p＞可以使用 driver.find_element_ by_ class_name（’content’）。
# 有时， 我们需要查找多个元素。 上述例子就查找了所有的评论。
# 因此,也有对应的元素选择方法，就是在上述的 element 后加上 s，变成 elements。

# %%
# 控制滚动条到底部
driver = webdriver.Chrome()
driver.get('https://www.gamersky.com/')
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys('selenuim')
# driver.find_element_by_id('su').click()
time.sleep(1)
# js="var q=document.getElementById('id').scrollTop=10000"
# driver.execute_script(js)

# 页面包含滚动条使用如下代码
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(3)
js = 'var q=document.documentElement.scrollTop=0'
driver.execute_script(js)
time.sleep(3)

driver.quit()

# %%
# 本节重点：
#
# l 键盘按键用法
# l 键盘组合键用法
# l send_keys() 输入中文运行报错问题

driver = webdriver.Chrome()
driver.get('https://music.163.com/')
driver.find_element_by_id('lbNormal').click()
time.sleep(2)
driver.find_element_by_name('email').send_keys('babilun9.19')
driver.find_element_by_name('password').send_keys('babilun9.19')

# 要想调用键盘按键操作需要引入keys包：
# from selenium.webdriver.common.keys import Keys
# 通过send_keys()调用按键：
# send_keys(Keys.TAB)        # TAB
# send_keys(Keys.ENTER)    # 回车

# %%
# 本节重点:

# driver.get_cookies（） 获得cookie信息
# # add_cookie(cookie_dict)  向cookie添加会话信息
# # delete_cookie(name)   删除特定(部分)的cookie
# # delete_all_co okies()    删除所有cookie

driver = webdriver.Chrome()
driver.get('http://www.youdao.com/')

cookies = driver.get_cookies()

# 向cookie的name 和value添加会话信息。
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbb'})
# 遍历cookies中的name和value信息打印，当然还有上面添加的信息
for cookie in cookies:
    print('{} -> {}'.format(cookie['name'], cookie['value']))
driver.delete_cookie('CookieName')

time.sleep(3)
driver.quit()
print(cookies)

# %%
# 本节重点：
#
# ActionChains 类
# context_click()  右击
# double_click()   双击
# drag_and_drop()  拖动
#
#
#
# 测试的产品中有一个操作是右键点击文件列表会弹出一个快捷菜单，可以方便的选择快捷菜单中的选择对文件进行操作（删除、移动、重命名），之前学习元素的点击非常简单：
#
# driver.find_element_by_id(“xxx”).click()
# 那么鼠标的双击、右击、拖动等是否也是这样的写法呢？例如右击：
#
# driver.find_element_by_id(“xxx”).context_click()

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
news = driver.find_element_by_link_text('新闻')
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(news).perform()
time.sleep(3)
# 对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(news).perform()
time.sleep(3)
# 对定位到的元素执行鼠标拖拽操作
ActionChains(driver).drag_and_drop(news).perform()
