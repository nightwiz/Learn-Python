# 定义一个Cat的类class
class Cat:
    # 属性

    # 方法，定义方法的时候，第一个参数需要写上self
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水...")


# 创建一个对象tom，指向Cat这个类的引用
tom = Cat()

# tom具有cat的方法，所以可以调用Cat的方法
tom.eat()       # ---> 调用了Cat这个class里面的def eat() 方法
tom.drink()     # ---> 调用了Cat这个class里面的def drink() 方法

