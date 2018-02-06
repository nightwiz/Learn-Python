# 定义一个Cat的类class
class Cat:
    # 属性

    # 方法，定义方法的时候，第一个参数需要写上self
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水...")

    def introduce(self):
        print("%s的年龄是%d" % (tom.name, tom.age))


# 创建一个对象tom，指向Cat这个类的引用
tom = Cat()


# 调用tom指向的对象中的 方法
tom.eat()       # ---> 调用了Cat这个class里面的def eat() 方法
tom.drink()     # ---> 调用了Cat这个class里面的def drink() 方法


# 给tom指向的对象Cat 添加 name 和 age 这两个属性
tom.name = "汤姆"
tom.age = 40


# 获取属性的第1种方式
# print("%s的年龄是%d" % (tom.name,tom.age))


# 获取属性的第2种方式
tom.introduce()

