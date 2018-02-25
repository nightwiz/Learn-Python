class Tool(object):
    def __init__(self,new_name):
        self.name = new_name


num = 0
tool1 = Tool("铁锹")
num += 1
print(num)

tool1 = Tool("榔头")
num += 1
print(num)

tool1 = Tool("螺丝刀")
num += 1
print(num)

