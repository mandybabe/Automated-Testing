from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_css_selector("a.pf:nth-child(9)")
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text('搜索设置').click()

# 保存设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert().accept()

time.sleep(5)

driver.quit()
