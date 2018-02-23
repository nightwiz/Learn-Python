class Base(object):     # 写上object称为新式类；不写默认就是继承自object，但是称为经典类
    def test(self):
        print("----Base----")


class A(Base):
    def test1(self):
        print("----test1----")


class B(Base):
    def test2(self):
        print("----test2----")


# C继承A和B
class C(A,B):
    pass


# c继承了Base，A和B类的方法
c = C()
c.test1()
c.test2()
c.test()
