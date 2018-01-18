# 阶乘
# 4! = 4*3*2*1
# 5! = 5*4*3*2*1

"""

i = 1
result = 1
while i <= 4:
    result = result * i
    i += 1
    # i = 1
    # result = 1 * 1
    # i = 2
    # result = 1 * 2
    # i = 3
    # result = 2 * 3
    # i = 4
    # result = 6 * 4

    # result = 1 * 2 * 3 * 4

print(result)

"""

# 递归，函数在函数内部调用自己
# 5的阶乘可以拆分为 5 * 4! 即 5 乘以 4 的阶乘得到 5 的阶乘
# 4的阶乘可以拆分为 4 * 3! 即 4 乘以 3 的阶乘得到 4 的阶乘


def getnums(num):
    if num > 1:
        return num * getnums(num - 1)
    else:
        return num


result = getnums(4)
print(result)
