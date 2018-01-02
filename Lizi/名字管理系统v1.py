print("=" * 30)
print("名字管理系统V 0.1")
print("=" * 30)

# 打印功能
print("1，添加一个名字")
print("2，删除一个名字")
print("3，修改一个名字")
print("4，查询一个名字")
print("5，退出系统")


# 定义一个空列表来存储姓名
names = []

# 开始循环

while True:

    # 获取用户输入
    num = int(input("请输入你的选择："))

    # 根据用户输入，判断
    if num == 1:
        new_name = input("请输入名字：")
        names.append(new_name)
        print(names)

    elif num == 2:
        rm_name = input("请输入要删除的名字：")
        if rm_name in names:
            names.remove(rm_name)
            print(names)
        else:
            print("找不到这个名字 %s" % rm_name)
    elif num == 3:
        change_name = input("请输入要修改的名字：")
        if change_name in names:
            changed_name = input("请输入修改后的名字：")
            names[names.index(change_name)] = changed_name
            print(names)
        else:
            print("没有找到这个名字")

    elif num == 4:
        find_name = input("请输入要查询的名字：")
        if find_name in names:
            print("找到了你要找的人")
        else:
            print("查无此人")
    elif num == 5:
        break
    else:
        print("输入有误，请重新输入")
