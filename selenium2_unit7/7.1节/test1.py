from selenium2_unit7 import calculator
import unittest


class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = calculator.Count(2, 3)
        self.assertEqual(j.add(), 5)  # 比较相等

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    unittest.main()

'''
  分析上面的代码，首先引入unittest模块，创建TestCount类继承unittest的TestCase类，
我们可以将TestCase类看成是对特定类进行测试的集合。
  setUp()方法用于测试用例执行前的初始化工作，这里只简单打印"test start"信息。
tearDown()方法与 setUp()方法相呼应，用于测试用例执行之后的善后工作，这里打印"test end"信息。
  在test_add()中首先调用Count类并传入要计算的数，通过调用add()方法得到两数相加的返回值。
这里不再使用繁琐的异常处理，而是调用unittest框架所提供的assertEqual()方法对add()的返回值进行断言，
判断两者是否相等，assertEqual()方法由TestCase类继承而来。
  unittest提供了全局的main()方法使用TestLoader类来搜索所有包含在该模块中以"test"命名开头的测试方法，
并自动执行它们。

'''
'''
Python知识补充
    if __name__ == "__main__": 语句说明
    在后面实例中我们会经常用到这个语句，在解释它之前先补充点Python知识：
    1. Python文件的后缀为.py。
    2. .py文件既可以用来直接执行，就像一个小程序一样，也可以用来作为模块被导入。
    3. 在Python中导入模块一般使用的是import。
    顾名思义，if就是如果的意思，在句子开始处加上if，就说明这个句子是一个条件语句。接着是__name__，
__name__作为模块的内置属性，简单地说，就是.py文件的调用方式。最后是__main__，如上所述，
.py文件有两种使用方式：作为模块被调用和直接使用，如果它等于“__main__”就表示直接使用。
    

'''