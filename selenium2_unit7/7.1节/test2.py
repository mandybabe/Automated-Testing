from selenium2_unit7 import calculator
import unittest


class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = calculator.Count(2, 3)
        self.assertEqual(j.add(), 5)  # 比较相等

    def test_add2(self):
        j = calculator.Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

'''
   在代码的最后，我们去掉了main()方法，采用构造测试集的方法来加载与运行测试用例，实现了有选择地执行测试用例。
   首先，调用unittest框架的TestSuite()类来创建测试套件，通过它所提供的addTest()方法来添加测试用例test_add2()。
接着调用unittest框架的TextTestRunner()类，通过它下面的run()方法来运行suite所组装的测试用例。
   
'''