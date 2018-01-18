def sum_3_nums(a, b, c):                # 传入的参数，形参
    result = a + b + c
    return result


def average_3_nums(a1, a2, a3):         # 传入的参数，形参
    result = sum_3_nums(a1, a2, a3)     # 接收的参数，实参
    result = result/3  # result/=3
    print("平均值是: %d" % result)


num1 = int(input("请输入第1个数:"))
num2 = int(input("请输入第2个数:"))
num3 = int(input("请输入第3个数:"))


# sum_3_nums(num1, num2, num3)
average_3_nums(num1, num2, num3)        # 接收的参数，实参
