import orm_m2m
from sqlalchemy.orm import sessionmaker

# 创建与数据库的会话session
Session_class = sessionmaker(bind=orm_m2m.engine)

# 生成session实例
session = Session_class()

# b1 = orm_m2m.Book(name="learn Python with me", pub_date="2011-01-01")
# b2 = orm_m2m.Book(name="learn Java with me", pub_date="2012-02-02")
# b3 = orm_m2m.Book(name="learn Go with me", pub_date="2013-03-03")
#
# a1 = orm_m2m.Author(name="zhangsan")
# a2 = orm_m2m.Author(name="lisi")
# a3 = orm_m2m.Author(name="wangwu")
#
# b1.authors = [a1,a3]
# b3.authors = [a1,a2,a3]
#
# session.add_all([b1,b2,b3,a1,a2,a3])

author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="zhangsan").first()

# 通过relationship中定义的books反查

# 查作者是zhangsan的书名
print(author_obj.books)

# 查作者是张三的第一本书的pub_date
print(print(author_obj.books[1].pub_date))

book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.id==2).first()

# 查ID为2的书名
print(book_obj)

# # 查ID为2的书的作者
print(book_obj.authors)

# 删除作者为zhangsan的书，删除完之后会orm会自动删除book_m2m_author的记录
book_obj.authors.remove(author_obj)

session.commit()