def get_wendu():
    wendu = 22
    print("当前温度是%d" % wendu)
    return wendu
# 返回温度


def get_wendu_huashi(wendu):
    wendu = wendu + 3
    print("当前华氏摄氏度是 %d" % wendu)


# 如果一个函数有返回值，但是没有在调用函数之前 用一个变量保存的话，那么没有任何意义
result = get_wendu()

get_wendu_huashi(result)

'''
函数的四种形式：

def 函数名():
    pass
    
def 函数名():
    return xxx
    
def 函数名(参数):
    pass
    
def 函数名(参数):
    return xxx
'''