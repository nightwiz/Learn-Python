import os


# 修改文件名
os.rename("newfile.txt", "newerfile.txt")

# 删除文件
os.remove("newerfile.txt")

# 创建文件夹
os.mkdir("test")

# 删除文件夹
os.rmdir("test")

# 返回当前路径的绝对路径
os.getcwd()

# 切换目录
os.chdir("../")

# 获取目录列表
os.listdir("./")

# 删除文件夹
os.rmdir("新建文件夹")



