from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner


class Baidu(unittest.TestCase):
    """百度搜索测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"

    def test_baidu_search(self):
        """搜索关键字：HTMLTestRunner"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 定义报告存放路径
    fp = open('./result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况：')

    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件


'''
   在类或方法的下方，通过三引号（""" """或''' '''）来添加doc string类型的注释，这类注释在平时调用的时候不显示，
可以通过help()方法来查看类或方法的这种注释。
   回到问题的原点，HTMLTestRunner可以读取doc string类型的注释，所以，我们只需给测试类或方法添加这种类型的注释即可。
'''

'''
注意：一定要直接使用“Run按钮，运行。如果点击“Run unittests in ...”,会出现无法生成测试报告的情况。'''