import orm_mul_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_mul_fk.engine)
session = Session_class()

# addr1 = orm_mul_fk.Address(street="Tiantongyuan", city="ChangPing", state="BJ")
# addr2 = orm_mul_fk.Address(street="WuDaoKou", city="HaiDian", state="BJ")
# addr3 = orm_mul_fk.Address(street="Yanjiao", city="LangFang", state="HB")

# session.add_all([addr1,addr2,addr3])


# c1 = orm_mul_fk.Customer(name="zhangsan", billing_address=addr1, shipping_address=addr2)
# c2 = orm_mul_fk.Customer(name="Jack", billing_address=addr3, shipping_address=addr3)


# session.add_all([c1,c2])

obj = session.query(orm_mul_fk.Customer).filter(orm_mul_fk.Customer.name=="zhangsan").first()

print(obj.name, obj.billing_address, obj.shipping_address)

session.commit()