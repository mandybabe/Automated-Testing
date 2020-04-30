import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        a = "hello"
        b = "hello world"
        self.assertIn(a, b, msg="a is not in b")

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    unittest.main()
