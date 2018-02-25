class Tool(object):

    # 另外一种属性定义；定义在class里面，def外面，只写变量名，没有self；这样的属性称为类属性
    num = 0

    # 类的方法
    def __init__(self,new_name):
        self.name = new_name


tool1 = Tool("铁锹")

tool1 = Tool("榔头")

tool1 = Tool("螺丝刀")
