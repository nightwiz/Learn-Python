def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


A = (44, 55, 66)
B = {"name": "laowang", "age": 18}


test(11, 22, 33, A, B)      # A 和 B 会作为一个整体保存在args，kwargs为空字典

test(11, 22, 33, *A, **B)   # 拆包；A作为一个元组保存在args，B作为一个字典保存在kwargs



