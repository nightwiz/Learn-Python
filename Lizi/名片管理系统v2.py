print("=" * 30)
print("名片管理系统V 0.1")
print("=" * 30)

# 打印功能
print("1，添加一个新名片")
print("2，删除一个名片")
print("3，修改一个名片")
print("4，查询一个名片")
print("5，查询所有名片")
print("6，退出系统")


# 定义一个空列表来存储名片
card_info = []

while True:

    # 获取用户输入
    num = int(input("请输入操作序号："))

    # 根据用户的输入执行相应的功能
    if num == 1:
        new_name = input("请输入新的名字：")
        new_qq = input("请输入新的QQ：")
        new_weixin = input("请输入新的微信：")
        new_addr = input("请输入新的住址")

        # 定义一个字典，添加到列表中
        new_info = {}
        new_info['name'] = new_name
        new_info['qq'] = new_qq
        new_info['weixin'] = new_weixin
        new_info['addr'] = new_addr

        # 将字典添加到列表
        card_info.append(new_info)

        # 测试打印
        # print(card_info)
    elif num == 2:
        pass
    elif num == 3:
        pass
