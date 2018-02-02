f = open("test.txt","r")    # 默认为读，所以r可以省略

content = f.read()
print(content)

f.close()


