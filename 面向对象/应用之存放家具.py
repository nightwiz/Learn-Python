# 把一个对象放到另外一个对象中
class Home:
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr

    def __str__(self):
        return "房子的面积是：%d,户型是：%s,地址是：%s"%(self.area, self.info, self.addr)

    def add_item(self,item):
        pass

class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是：%d" % (self.name, self.area)


fangzi = Home(129, "三室一厅", "广州市 天河区 天河路 888号")
print(fangzi)

bed1 = Bed("席梦思", 4)
print(bed1)