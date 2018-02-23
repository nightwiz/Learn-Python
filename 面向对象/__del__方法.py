class Dog:
    def __del__(self):
        print("----游戏结束----")


dog1 = Dog()    # 引用Dog的值为1（引用计数为1）
dog2 = dog1     # 引用Dog的值为2

# dog1 指向对象 Dog()
# dog2 也指向相同的对象 Dog()，并没有创建一个额外的对象

del dog1    # 引用Dog的值变成1
del dog2    # 引用Dog的值变成0（引用计数为0）
print("===============")

# 当Dog这个类没有引用的时候，python解释器自动调用__del__方法；也就是在最后一次删除引用后__del__会被调用；
# 在程序结束前所有的对象也会调用__del__方法释放；
