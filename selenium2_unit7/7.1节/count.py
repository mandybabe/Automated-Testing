# 用于判断质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


'''
   创建is_prime()函数用于实现对质数的判断。当得到一个数字n后，首先判断它是否小于或等于1，如果小于或等于1，则直接返回False；
如果大于1，则对其进行循环判断；若能整除2到其自身之间的任意一个数，则不为质数，返回False，否则返回True。
'''
