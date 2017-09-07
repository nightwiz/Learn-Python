from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum, DATE, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@192.168.184.138/testdb",encoding='utf-8')

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # 关联两个外键
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    # 通过billing_address和shipping_address去查address的表数据
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return self.street
# 创建表结构
# Base.metadata.create_all(engine)



