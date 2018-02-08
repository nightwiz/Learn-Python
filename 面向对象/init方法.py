class Cat:
    """定义了一个Cat类"""
    # 方法，定义方法的时候，第一个参数需要写上self（也可以是其他单词），用来接收当前这个对象。
    # self的作用是:你通过哪个对象去调用这个方法，self就指向该对象。
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水...")

    def introduce(self):

        # 改用self，谁调用就是执行谁的，self
        print("%s的年龄是%d" % (self.name, self.age))


# 创建一个对象tom，指向Cat这个类的引用
tom = Cat()

tom.eat()
tom.drink()
tom.name = "汤姆"
tom.age = 40


# 获取属性的第2种方式
tom.introduce()     # 相当于tom.introduce(tom)

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10

lanmao.introduce()
