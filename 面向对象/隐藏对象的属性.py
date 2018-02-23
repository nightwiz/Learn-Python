class Dog:
    def set_age(self, new_age):
        if new_age>0 and new_age<=100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age


dog = Dog()

# dog.age = -10
# dog.name = "小白"
# print(dog.age)

# 用方法来替代 直接获取属性的值
# 定义属性的时候不要让外部直接调用，而是通过方法去获取，例如get_age,get_name.

dog.set_age(-10)    # 设置一个不合理的年龄 -10
age = dog.get_age()
print(age)


# age 输出为 0
