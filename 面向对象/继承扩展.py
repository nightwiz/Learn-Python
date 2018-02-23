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
    def bark(self):
        print("----旺旺----")


class Xiaotianquan(Dog):
    def fly(self):
        print("----识飞----")


xiaotq = Xiaotianquan()
xiaotq.fly()

# 继承父类的bark方法
xiaotq.bark()

# 继承父类的父类的eat方法
xiaotq.eat()
