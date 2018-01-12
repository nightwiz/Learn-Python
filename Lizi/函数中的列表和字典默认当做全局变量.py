nums = [11, 22, 33]
infor = {"name": "zhang"}


def test():
    nums.append(44)
    infor['age'] = 18


def test2():
    print(nums)
    print(infor)


test()
test2()

# 在test函数中对全局变量nums和infor做修改，没有声明global但是也是修改成功
# 在函数中，列表和字典默认就是当做全局变量
# 如果在函数中对列表和字典修改，不需要加global
