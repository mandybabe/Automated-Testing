"""
TestLoader ——该类负责根据各种标准加载测试用例，并将它们返回给测试套件。正常情况下，不需要创建这个类的实例。
unittest提供了可以共享的defaultTestLoader类，可以使用其子类和方法创建实例，discover()方法就是其中之一。
  discover(start_dir, pattern='test*.py', top_level_dir=None)
  找到指定目录下所有测试模块，并可递归查到目录下的测试模块，只有匹配到文件名才能被加载。如果启动的不是顶层目录，
那么顶层目录必须单独指定。
   start_dir ：要测试的模块名或测试用例目录。
   pattern='test*.py' ：表示用例文件名的匹配原则。此处匹配文件名以“test”开头的“.py”类型的文件，星号“*”表示任意多个字符。
   op_level_dir=None：测试模块的顶层目录，如果没有顶层目录，默认为None。
   现在通过discover()方法实现runtest.py文件的功能。
"""

import unittest

# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')  # 匹配当前目录下“.py”类型的所有测试文件
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配当前目录下以“test”开头的“.py”类型的测试文件
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配当前目录下以“count_test”开头的“.py”类型的测试文件

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)


'''
    discover()方法会自动根据目录(test_dir)匹配查找测试用例文件(test*.py)，并将查找到的用例组装到测试套件中，
因此，可以直接通过run()方法执行discover，大大简化了测试用例的查找与执行。

'''