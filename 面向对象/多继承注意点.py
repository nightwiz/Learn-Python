class Base(object):
    def test(self):
        print("----Base----")


class A(Base):
    def test(self):
        print("----A----")


class B(Base):
    def test(self):
        print("----B----")


# C继承A和B
class C(A,B):
    pass
    # def test(self):
    #     print("----C----")


# c继承了Base，A和B类的方法
c = C()
c.test()


# 查看调用方法的时候搜索的顺序；如果在某个类中找到了方法，就停止搜索
print(C.__mro__)
