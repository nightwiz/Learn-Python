info = {'name': 'laowang', 'age': 30}

print(info.keys())  # python2返回一个列表，python3返回一个对象

print(info.values())

print(info.items())

print(info.get('name'))


for temp in info.keys():
    print(temp)

for temp in info.values():
    print(temp)

for temp in info.items():
    print('key = %s,value = %s' % (temp[0], temp[1]))


for A, B in info.items():
    print('key = %s,value = %s' % (A, B))



''' 元组拆包'''

a = (11, 22)
b = a
print(b)

c, d = a    # 元组拆包

print(c)
print(d)
