# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
'''
# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
# text = driver.find_element_by_id('cp').text
# print(text)

# 返回元素的属性值，可以是id、name、type或其他任意属性
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

# 返回元素的结果是否可见，返回结果为True or False
result = driver.find_element_by_id('kw').is_displayed()
print(result)
'''
driver.set_window_size(600, 600)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scroll(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
