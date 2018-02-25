class Tool(object):

    # 另外一种属性定义；定义在class里面，def外面，只写变量名，没有self；这样的属性称为 类属性
    num = 0

    # 类的方法
    def __init__(self,new_name):
        # 实例属性
        self.name = new_name
        # 对类属+1
        Tool.num += 1



tool1 = Tool("铁锹")

tool2 = Tool("榔头")

tool3 = Tool("螺丝刀")

print(Tool.num)



# Tool 类对象；类对象里面的属性称为类属性
# tool1 实例对象；实例对象里面的属性称为实例属性

# 实例属性：和具体的某个实例对象有关系，并且一个实例对象 和 另外一个实例对象是不共享属性的
# 类属性：类属性所属于类对象，并且多个实例对象之间共享同一个 类属性
