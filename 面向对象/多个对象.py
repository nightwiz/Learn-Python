# 定义一个Cat的类class
class Cat:
    # 属性

    # 方法，定义方法的时候，第一个参数需要写上self。
    # self的作用是:你通过哪个对象去调用这个方法，self就指向该对象。
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水...")

    def introduce(self):
        # print("%s的年龄是%d" % (tom.name, tom.age))

        # 改用self，谁调用就是执行谁的，self
        print("%s的年龄是%d" % (self.name, self.age))


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
tom.introduce()     # tom去调用introduce的时候，self就是tom


lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10

lanmao.introduce()  # lanmao去调用introduce的时候，self就是lanmao
