# 定义一个空列表来存储名片
card_infors = []


def print_menu():
    """这是用来完成打印功能"""
    print("=" * 30)
    print("名片管理系统V 0.1")
    print("=" * 30)
    print("1，添加一个新名片")
    print("2，删除一个名片")
    print("3，修改一个名片")
    print("4，查询一个名片")
    print("5，查询所有名片")
    print("6，退出系统")


def add_new_card_infor():
    """完成添加一个新的名片"""
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的QQ：")
    new_weixin = input("请输入新的微信：")
    new_addr = input("请输入新的住址：")

    # 定义一个字典，添加到列表中
    new_info = {}
    new_info['name'] = new_name
    new_info['qq'] = new_qq
    new_info['weixin'] = new_weixin
    new_info['addr'] = new_addr

    # 将字典添加到列表
    global card_infors
    card_infors.append(new_info)

    # 测试打印
    # print(card_info)


def find_card_infor():
    """查询名片"""

    global card_infors

    find_name = input("请输入要查找的姓名：")
    find_flag = 0  # 默认表示没找到
    for temp in card_infors:
        if find_name == temp["name"]:
            print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
            find_flag = 1  # 表示找到了
            break
    if find_flag == 0:
        print("查无此人")


def show_all_infor():
    """显示所有的名片信息"""

    global card_infors

    print("姓名\tQQ\t微信\t住址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))


# 1，打印功能提示
print_menu()


def main():
    """完成对整个程序的控制"""

    while True:

        # 获取用户输入
        num = int(input("请输入操作序号："))

        # 根据用户的输入执行相应的功能
        if num == 1:
            add_new_card_infor()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_card_infor()
        elif num == 5:
            show_all_infor()
        elif num == 6:
            break
        else:
            print("输入有误，请重新输入")


# 调用主函数
main()
