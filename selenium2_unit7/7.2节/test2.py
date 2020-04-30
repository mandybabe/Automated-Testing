import unittest


# @unittest.skip("直接跳过测试测试类")
class MyTest(unittest.TestCase):

    def setUp(self):
        pass  # 该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。

    def tearDown(self):
        pass

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2, "当条件为True时跳过测试")
    def test_skip_if(self):
        print("test bbb")

    @unittest.skipUnless(3 > 2, "当条件为True时执行测试")
    def test_skip_unless(self):
        print("test ccc")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2, 3)


if __name__ == '__main__':
    unittest.main()

'''
   以上共创建了4条测试用例。
   第一条测试用例通过@unittest.skip()装饰，直接跳过不执行。
   第二条用例通过 @unittest.skipIf()装饰，当条件为真时不执行，3>2条件为真(True)，跳过不执行。
   第三条用例通过@unittest.skipUnless()装饰，当条件为真时执行，判断3>2条件为真(True)，第三条用例执行。
   第四条用例通过@unittest.expectedFailure装饰，不管执行结果是否失败，统一标记为失败，但不会抛出异常信息。
   
   当然，这些方法同样可以作用于测试类，只需将它们定义在测试类上面即可。
   
'''
