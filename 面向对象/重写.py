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

    def bark(self):     # 重写方法；当自己的方法中有bark方法，就不再调用父类Dog中的bark方法
        print("---嗷呜---")


xiaotq = Xiaotianquan()
xiaotq.fly()

xiaotq.bark()

xiaotq.eat()
