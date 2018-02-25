# 所谓多态：定义时的类型和运行时的类型不一样，此时就是多态

# 类里面定义的 def 叫方法，需要带上self参数；
# 类外面定义的 def 叫函数，没有参数可以不用写；


class Dog(object):
    def print_self(self):
        print("大家好")


class Xiaotq(Dog):
    def print_self(self):
        print("Hello everyone")


def introduce(temp):
    temp.print_self()   # 多态；只有在真正执行的时候才确定是调用哪个类的哪个方法。


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
