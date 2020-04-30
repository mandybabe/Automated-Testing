from selenium import webdriver
# 以数组的形式对搜索的关键字进行参数化
search_text = ['python', '中文', 'text']

for text in search_text:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id('su').click()
    driver.quit()
