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

a,b = b,a
print("a=%d,b=%d" % (a,b))
