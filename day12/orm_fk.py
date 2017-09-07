import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum, DATE, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine("mysql+pymysql://root:123456@192.168.184.138/testdb",
                       encoding='utf-8')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<id:%s day:%s status:%s>" % (self.id, self.name, self.register_date)


class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    # 外键关联
    stu_id = Column(Integer, ForeignKey("student.id"))

    # 添加关系，互相关联
    student = relationship("Student", backref="my_study_record")

    def __repr__(self):
        return "<%s day:%s status:%s>" % (self.student.name, self.day,self.status)


# 创建表结构
Base.metadata.create_all(engine)


# 创建与数据库的会话session
Session_class = sessionmaker(bind=engine)

# 生成session实例
session = Session_class()

# Session_classs1 = Student(name="zhangsan", register_date="2017-07-07")
# s2 = Student(name="lisi", register_date="2017-08-08")
# s3 = Student(name="wangwu", register_date="2017-09-09")
# s4 = Student(name="zhaoliu", register_date="2017-10-10")
#
#
# study_obj1 = StudyRecord(day=1, status="YES", stu_id=1)
# study_obj2 = StudyRecord(day=2, status="YES", stu_id=1)
# study_obj3 = StudyRecord(day=3, status="YES", stu_id=1)
# study_obj4 = StudyRecord(day=1, status="YES", stu_id=2)

# 一次性提交
# session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

stu_obj = session.query(Student).filter(Student.name=="zhangsan").first()

print(stu_obj.my_study_record)

session.commit()
