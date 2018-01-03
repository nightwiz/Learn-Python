a = [11, 22, 33]
b = [44, 55]


# append，作为一个整体添加（例如添加了一个元素，一个列表，一个字典）a = [11,22] b=[33,44] a.append(b) = [11,22,[33,44]]
# a.append(b)
# print(a)


# extend, 打散了加入，相当于合并 a = [11,22] b=[33,44] a.extend(b) = [11,22,33,44]
a.extend(b)
print(a)

