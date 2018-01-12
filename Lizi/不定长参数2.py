def test(a, b, c=33, *args, **kwargs):  # args以元组的方式保存，kwargs已字典的方式保存。
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


test(11, 22, 33, 44, 55)
test(11, 22)

test(11, 22, 33, task=44, done=55)



