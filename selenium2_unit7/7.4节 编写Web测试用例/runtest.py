import unittest
# 项目集成测试
# 定义测试用例的目录
test_dir = './test_project/test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')  # 匹配当前目录下“.py”类型的所有测试文件
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配当前目录下以“test”开头的“.py”类型的测试文件
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配当前目录下以“count_test”开头的“.py”类型的测试文件

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)