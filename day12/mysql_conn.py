import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.21.128', port=3306, user='root', passwd='123456', db='python')

# 创建游标
cursor = conn.cursor()

# 执行SQL，返回受影响行数
effect_row = cursor.execute("select * from A")

# 打印受影响函数
print(effect_row)

# 获取第一行结果
print(cursor.fetchone())

# 获取前3行数据
print(cursor.fetchmany(3))

# 打印全部结果
print(cursor.fetchall())
