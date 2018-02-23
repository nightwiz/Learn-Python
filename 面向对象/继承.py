# 子类（派生类） 继承 父类（基类）
class Animal:
    def eat(self):
        print("----吃----")

    def drink(self):
        print("----喝----")

    def sleep(self):
        print("----睡----")

    def run(self):
        print("----跑----")


class Dog(Animal):
    """
    def eat(self):
        print("----吃----")

    def drink(self):
        print("----喝----")

    def sleep(self):
        print("----睡----")

    def run(self):
        print("----跑----")
    """
    def bark(self):
        print("----旺旺----")


class Cat(Animal):
    def catch(self):
        print("----抓老鼠----")


# a = Animal()
# a.eat()

wangcai = Dog()
wangcai.eat()
wangcai.bark()


tom = Cat()
tom.eat()
tom.catch()

# wangcai只能使用Dog或者Animal类中的方法
# tom只能使用Cat或者Animal类中的方法
# 不允许出现tom使用Dog中的方法或者wangcai使用Cat中的方法
