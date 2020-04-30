from selenium import webdriver
from selenium2_unit5 import Public


class LoginTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.126.com")

    # admin用户登录
    def test_admin_login(self):
        username = 'admin'
        password = '123'
        Public.Login.user_login(self.driver, username, password)
        self.driver.quit()

    # guest 用户登录
    def test_guest_login(self):
        username = 'guest'
        password = '321'
        Public.Login.user_login(self.driver, username, password)
        self.driver.quit()


LoginTest.test_admin_login()
LoginTest.test_guest_login()
