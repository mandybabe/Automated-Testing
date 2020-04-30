from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

'''
# 获得cookie信息
cookie = driver.get_cookies()

# 将获得cookie的信息打印
print(cookie)

driver.quit()
'''

# 向cookie的name和value中添加会话信息
driver.add_cookie({'name': 'key-aaaa', 'value': 'value-bbbb'})
# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息

for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
