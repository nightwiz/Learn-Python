def sum_2_nums(a, b, *args):    # *args,不定长参数，放在形参的最后一个位置
    print(a)
    print(b)
    print(args)
    result = a + b
    for num in args:
        result += num
    print("result=%d" % result)


sum_2_nums(11, 22, 33, 44, 55, 66, 77)
sum_2_nums(11, 22, 33)
sum_2_nums(11, 22)
