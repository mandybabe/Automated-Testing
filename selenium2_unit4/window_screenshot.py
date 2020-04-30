from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
# 注意，保存时图片选择其他格式Pycharm会报警告，建议选择.png格式
driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\baidu_img.png")
driver.get_screenshot_as_png()
sleep(4)
driver.quit()
