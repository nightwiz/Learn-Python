import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine("mysql+pymysql://root:123456@192.168.21.128/test",
                       encoding='utf-8', echo=True)

# 生成orm基类，给下面的class继承
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# 创建表结构
Base.metadata.create_all(engine)

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)

# 生成session实例,类似于cursor
Session = Session_class()

# 生成你要创建的数据对象
user_obj1 = User(name="alex", password="alex3714")
user_obj2 = User(name="zhangxt", password="123456")

# 此时还没创建对象呢，打印id发现还是None
print(user_obj1.name, user_obj1.id)

# 把要创建的数据对象添加到这个session里，一会统一创建
Session.add(user_obj1)
Session.add(user_obj2)

# 此时也依然还没创建
print(user_obj1.name, user_obj1.id)

# 现在统一提交，创建数据
Session.commit()
