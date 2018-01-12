
'''
程序的存放顺序，先放全局变量的定义，再放函数的定义，再放函数的调用
'''


'''
# 局部变量通过return返回，变量接受return的返回值，传给另外一个函数调用
def get_wendu():
    wendu = 33  #局部变量，仅在函数内有效
    return wendu


def print_wendu(wendu):
    print("温度是%d" % wendu)


result = get_wendu()

print_wendu(result)
'''



# 定义一个全局变量wendu
wendu = 0


def get_wendu():
    # 使用global对一个局部变量声明，那么这个函数中的wendu = 33 就不是定义一个局部变量，而是对全局变量wendu进行修改
    global wendu
    wendu = 33


def print_wendu():
    print("温度是 %d" % wendu)


get_wendu()
print_wendu()


