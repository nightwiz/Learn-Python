"""

在python num += num 并不等价于 num = num + num

如果是数字答案是一样的，但是并不是那么一回事

python中并不是 值 赋值，而是值 引用

"""

a = [100]


def test(num):  # num 指向 a 的引用 100
    num = num+num  # ---> [100] + [100] ===> [100,100]  num 指向 新的引用 [100,100]
    print(num)  # 打印 num 的 引用


test(a)

print(a)

# 输出：
# [100,100]
# [100]
