# 用例执行的顺序
import unittest


# @unittest.skip("直接跳过测试该测试类")
class TestBdd(unittest.TestCase):

    def setUp(self):
        print("test TestBdd :")

    def test_ccc(self):
        print("test ccc")

    def test_aaa(self):
        print("test aaa")

    def tearDown(self):
        pass


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test TestAdd :")

    def test_bbb(self):
        print("test bbb")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

'''
   unittest测试框架默认根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0~9,A~Z,a~z。所以，TestAdd类会优先于TestBdd类执行，
test_aaa()方法会优先于test_ccc()被执行，因而它并没有按照用例从上到下的顺序执行。
   对于测试目录与测试文件来说，unittest框架同样是按照这个规则来加载测试用例的。
   那么可不可以让test_ccc()先执行？答案是肯定的，只是不能使用默认的main()方法了，而是需要通过TestSuite()类的addTest()方法按照一定的顺序来加载。
   
注意：以下方法并没有实现这个需求！！！！！！！可能是python版本更新了。

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestBdd("test_ccc"))
    suite.addTest(TestAdd("test_bbb"))
    suite.addTest(TestBdd("test_aaa"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
'''
