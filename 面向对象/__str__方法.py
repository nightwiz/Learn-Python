class Cat:
    """定义了一个Cat类"""
    # 方法，定义方法的时候，第一个参数需要写上self（也可以是其他单词），用来接收当前这个对象。
    # self的作用是:你通过哪个对象去调用这个方法，self就指向该对象。

    # 初始化对象
    # init方法又叫魔法方法
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age


    # 对象描述信息
    def __str__(self):
        return "%s的年龄是%d" % (self.name, self.age)

    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水...")

    def introduce(self):

        # 改用self，谁调用就是执行谁的，self
        print("%s的年龄是%d" % (self.name, self.age))


# 创建一个对象tom，指向Cat这个类的引用，并传入name和age参数
tom = Cat("tom", 40)

lanmao = Cat("蓝猫", 10)

print(tom)
print(lanmao)
