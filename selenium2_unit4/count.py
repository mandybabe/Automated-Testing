###类与方法
"""
class A(object):
    def add(self, a, b):
        return a + b
count=A()
print(count.add(3, 5))

class A():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b
count = A('4', 5)
print(count.add())



class A:
    def add(self, a, b):
        return a + b


class B(A):
    def sub(self, a, b):
        return a - b


print(B().add(1, 5))


###模组
import time
from time import ctime
from time import *
print(ctime())
print("休眠两秒")
sleep(2)
print(ctime())

"""

#


try:
    a = "异常测试：\n"
    print(a)
except BaseException as msg:
    print(msg)
finally:
    print("不管是否异常，我都会被执行。")
