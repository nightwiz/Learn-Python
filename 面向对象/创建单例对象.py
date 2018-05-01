"""
class Dog(object):
    pass


a = Dog()
print(id(a))
b = Dog()
print(id(b))
# 打印出来的id不一样
"""


class Dog(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # return 上一次创建的对象引用
            return cls.__instance


a = Dog()
print(id(a))

b = Dog()
print(id(b))

# 打印出来的ID一样
