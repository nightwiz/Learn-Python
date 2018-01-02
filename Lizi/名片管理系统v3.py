card_info = [{'name': 'laowang', 'age': 18}, {'name': 'laoli', 'age': 19}, {'name': 'laozhao', 'age': 20}]

find_name = input("请输入要查询的名字：")

for temp in card_info:
    if temp['name'] == find_name:
        print("找到了")
        break
else:
    print("没有找到")
