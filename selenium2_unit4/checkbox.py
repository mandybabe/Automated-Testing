from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:/' + os.path.abspath('checkbox.html')
driver.get(file_path)

# 选择页面上所有的tag name 为input的元素
time.sleep(5)

driver.find_element_by_css_selector("#c1").click()
driver.find_element_by_xpath("//input[@id='c2']").click()
driver.find_element_by_id("c3").click()

time.sleep(2)
# 把页面上最后一个checkbox的勾给去掉
driver.find_element_by_css_selector('#c3').click()

