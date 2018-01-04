def get_wendu():
    wendu = 22
    print("当前温度是%d" % wendu)
    return wendu
# 返回温度


def get_wendu_huashi(wendu):
    wendu = wendu + 3
    print("当前华氏摄氏度是 %d" % wendu)


result = get_wendu()

get_wendu_huashi(result)
