a = 4
b = 5


"""
# 第一种方法，通过一个第三方变量实现a和b的互换
c = 0
c = a
a = b
b = c

print("a=%d,b=%d" % (a,b))

"""


"""
# 没有第三个变量的情况下交换

a = a + b
b = a - b
a = a - b
"""

# 第三方法

a,b = b,a

print("a=%d,b=%d" % (a,b))
