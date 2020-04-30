import unittest


def setUpModule():
    print("test module start >>>>>>>>>")


def tearDownModule():
    print("test module end >>>>>>>>>>>")


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start =======>")

    @classmethod
    def tearDownClass(cls):
        print("test class end =========>")

    def setUp(self):
        print("test case start -->")

    def tearDown(self):
        print("test case end -->")

    def test_case(self):
        print("test case1")

    def test_case2(self):
        print("test case2")


if __name__ == '__main__':
    unittest.main()

'''
setUpModule/tearDownModule ：     在整个模块开始与结束时被执行。
setUpClass/tearDownClass ：       在测试类的开始与结束时被执行。
setUp/tearDown ：                 在测试用例的开始与结束时被执行。

  需要注意的是，setUpClass/tearDownClass 的写法稍微有些不同。首先，需要通过@classmethod进行装饰，其次方法的参数为cls。
其实，cls与self并没有什么特别之处，都只表示类方法的第一个参数，只是大家约定俗成，习惯于这样来命名，当然也可以用abc来代替。
'''