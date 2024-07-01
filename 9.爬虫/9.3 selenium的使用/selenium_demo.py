import time
from selenium import webdriver
from lxml import etree

#创建浏览器对象
driver = webdriver.Chrome()

# # 设置浏览器参数
# option = webdriver.ChromeOptions()
# #不弹窗口
# option.add_argument('--headless')
# #禁用gpu 渲染
# option.add_argument('--disable-gpu')
#
# #代理地址
# # option.add_argument('--proxy-server=http://202.20.16.82:9527')
#
# #添加消息头 agent
# option.add_argument('--user-agent=Mozilla/5.0 HAHA')
#
# driver = webdriver.Chrome(chrome_options=option)

#调用浏览器驱动发送请求
driver.get('https://www.baidu.com')


#获取cookie
# cookies = driver.get_cookies()
# cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
#
# print(cookies_dict)

#模拟登录
# element = driver.find_element_by_id('s-top-loginbtn')
# element.click()
#
# time.sleep(8)
# element = driver.find_element_by_id('TANGRAM__PSP_11__userName')
#
# element.send_keys("zhanghao")
# time.sleep(8)
#
# element = driver.find_element_by_id('TANGRAM__PSP_11__password')
# element.send_keys('密码')
#
# element = driver.find_element_by_id('TANGRAM__PSP_11__isAgree')
# element.click()
#
# element = driver.find_element_by_id('TANGRAM__PSP_11__submit')
# element.click()
#
# time.sleep(20)

#获取浏览器数据  --str 类型
data = driver.page_source

#print(data)
#print(type(data))

# 5.保存浏览器上面的数据
# with open('baidu.html', 'w', encoding='utf-8') as f:
#     f.write(data)

#lxml xpath 提取html 数据
# html = etree.HTML(data)
# text = html.xpath('//title/text()')
# img_url = html.xpath('//img/@src')
# print(text)
# print(img_url)


#截图
# driver.save_screenshot('02baidu.png')


#查找html 输入框 和 点击按钮
# driver.find_element_by_id('kw').send_keys('江西理工大学')
# driver.find_element_by_id('su').click()

# #切换下一页
# time.sleep(8)
# element = driver.find_element_by_xpath('//*[@id="page"]/div/a[10]')
# element.click()
#
#
# #网页往前翻一页
# driver.forward()
# print('当前页面的网址:', driver.current_url)
#
# #网页往后翻一页
# time.sleep(8)
# driver.back()
# print('当前页面的网址:', driver.current_url)

# 点击百度第一条新闻
# driver.get('http://news.baidu.com/')
# element = driver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a')
# element.click()
#
# # 获取当前浏览器的所有窗口
# windows = driver.window_handles
# print(windows)
#
# # 切换到第一个浏览器的页面
# time.sleep(2)
# driver.switch_to.window(windows[0])


# 查找元素
# id
# # xpath
# result_el = driver.find_element_by_xpath('//*[@id="kw"]')
# print(result_el)

# class_name 类名称
#result_el = driver.find_element_by_class_name('s_ipt')


# # tag  标签名称
# result_el = driver.find_element_by_tag_name('input')
# # name属性名称
# result_el = driver.find_element_by_name('wd')

# # css selector 选择
# result_el = driver.find_element_by_css_selector('#kw')
#
# # link_text 根据链接的内容找链接标签 href
# result_el = driver.find_element_by_link_text('关于百度')
#
# # partial_link_text 模糊根据链接的内容找链接标签 href
# result_el = driver.find_elements_by_partial_link_text('汉字')
#
# #  使用获取一个标签的方法 --如果标签不存在 会报错
#
# #  使用获取多个个标签的方法 --如果标签不存在 返回的是空list, 不会报错
# result_el = driver.find_elements_by_tag_name('a')

#time.sleep(5)

#执行js 方法
# driver.get("http://www.itcast.cn/")
# time.sleep(1)
#
# js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句
# driver.execute_script(js) # 执行js的方法
#
# time.sleep(5)

#关闭
#driver.quit()
