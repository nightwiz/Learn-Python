class Dog(object):
    def __init__(self):
        print("---init---方法")

    def __del__(self):
        print("---del---方法")

    def __str__(self):
        print("---str---方法")
        return "对象的描述信息"

    def __new__(cls):   # cls此时是Dog指向那个的类对象
        print("---new---方法")
        # print(id(cls))
        return object.__new__(cls)


# print(id(Dog))

xtq = Dog()


# Dog() 相当于要做 3 件事情：
# 1，调用__new__方法来创建对象，然后找了一个变量来接收__new__的返回值，这个返回值表示创建出来的对象的引用。
# 2，__inti__(刚刚创建出来的对象的应用)
# 3，返回对象的引用


# __new__方法负责创建，__init__方法负责初始化


# 创建一个对象的一般步骤：
# 1，创建一个对象
# 2，调用__init__方法
# 3，返回对象的引用
