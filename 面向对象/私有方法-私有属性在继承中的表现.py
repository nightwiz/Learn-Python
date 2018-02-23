class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("----test1----")

    def __test2(self):
        print("----test2----")

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    pass


"""
# B继承了A，在B类中定义了公有方法test4并在公有方法中调用A类的私有方法和私有属性，是不行的！
class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)
"""


b = B()
b.test1()
# b.__test2()   # 私有方法并不会被继承
print(b.num1)
# print(b.__num2)   # 私有属性并不会被继承

b.test3()   # 调用父类的公用方法test3，再通过test3方法去调用私有方法和私有属性，是可以调用到__test2方法和__num2属性的。


# 总结
# 如果调用的是 继承父类中的 公有方法，可以在这个公有方法中访问父类中的私有属性和私有方法
# 但是 如果在子类中实现了一个 公有方法，那么这个方法是不能够调用继承的父类中的私有方法和私有属性的
