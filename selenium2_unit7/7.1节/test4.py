from selenium2_unit7 import calculator
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test add start")

    def test_add(self):
        j = calculator.Count(2, 3)
        self.assertEqual(j.add(), 5)  # 比较相等

    def test_add2(self):
        j = calculator.Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print("test add end")


class TestSub(unittest.TestCase):
    def setUp(self):
        print("test sub start")

    def test_sub(self):
        j = calculator.Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = calculator.Count(71, 46)
        self.assertEqual(j.sub(), 25)

    def tearDown(self):
        print("test sub end")


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

'''
   上面创建了TestAdd()和TestSub()两个测试类，分别测试calculator.py文件中的add()和sub()两个功能。
通过TestSuite类的addTest()方法把不同测试类中的测试方法组装到测试套件中。
   
'''