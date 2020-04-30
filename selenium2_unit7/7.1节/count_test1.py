from selenium2_unit7 import count
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        self.assertTrue(count.is_prime(7), msg="Is not prime!")

    def tearDown(self):
        print("tear end")


if __name__ == "__main__":
    unittest.main()
