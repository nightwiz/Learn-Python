import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.21.128', port=3306, user='root', passwd='123456', db='test')

# 创建游标
cursor = conn.cursor()

data = [
    ('N1', 23, 'M'),
    ('N2', 24, 'F'),
    ('N3', 25, 'M'),
]

cursor.executemany('insert into student (name,age,gender) values(%s,%s,%s)', data)

# 默认开启事务，需要commit
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

