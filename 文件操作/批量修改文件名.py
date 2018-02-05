import os

# 获取要重命名的文件夹名字
folder_name = input("请输入要批量重命名的文件夹：")

# 获取指定文件夹中所有的文件名字
file_names = os.listdir(folder_name)

os.chdir(folder_name)

# 重命名
for name in file_names:
    print(name)
    old_file_name = folder_name + "/" + name
    new_file_name = folder_name + "/" + "[高清无码]" + name
    os.rename(old_file_name, new_file_name)

