def test(a, b=22):  # 缺省参数
    result = a + b
    print("result=%d" % result)


test(11)
test(33, 33)
test(44)

# 缺省参数不能是第一个参数


def test2(a, b=22, c=33):   # 缺省参数
    print(a)
    print(b)
    print(c)


test2(11, 44)


def test3(a, b=22, c=33):   # 缺省参数
    print(a)
    print(b)
    print(c)


test3(11, c=44)  # 命名参数


def test4(a, d, b=22, c=33):
    print(a, b, c, d)


test4(d=11, a=22, c=44)  # 命名参数
