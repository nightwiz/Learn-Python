"""
1，获取用户要复制的文件名称
2，打开要复制的文件
3，新建一个文件
4，从旧文件读取数据，并且写入到新文件中

"""

# 获取用户要复制的文件名
old_file_name = input("请输入要复制的文件名：")

# 打开要复制的文件名
old_file = open(old_file_name,"r")


# 拼接文件名,从文件名的右边查找"."字符串并且截取字符串拼接。
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]

# 新建文件
new_file = open(new_file_name,"w")


# 从旧文件中读取数据，写入到新文件中
while True:
    content = old_file.read(1024)   # 循环去 读取1024字节

    if len(content) == 0:           # 当长度为0时，即读取完毕跳出退出循环
        break

    new_file.write(content)         # 写入循环读取的数据


# 关闭两个文件
old_file.close()
new_file.close()
