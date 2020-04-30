# 验证码的处理

from random import randint

# 生成一个1000到9999之间的随机整数
verify = randint(1000, 9999)
print("生成的随机数:%d" % verify)

number = input("请输入随机数：")
print(number)
number = int(number)

if number == verify:
    print("登录成功！！")
elif number == 123456:
    print("登录成功！！")
else:
    print("验证码输入有误！")
