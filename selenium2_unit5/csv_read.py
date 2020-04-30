import csv  # 导入csv包

# 读取本地csv文件
date = csv.reader(open('info.csv', 'r'))
'''

# 循环输出每一行信息
for user in date:
    print(user)
'''

# 取用户的邮箱地址
for user in date:
    print(user[1])