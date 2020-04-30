from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file://' + os.path.abspath('frame.html')
driver.get(file_path)

# 切换到iframe（id='if'）
xf = driver.find_element_by_xpath('//*[@class="if"]')
driver.switch_to.frame(xf)

# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
