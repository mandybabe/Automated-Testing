from selenium import webdriver
import unittest
import time


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys("webdriver")
        driver.find_element_by_id("qb").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "webdriver - 有道搜索")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
