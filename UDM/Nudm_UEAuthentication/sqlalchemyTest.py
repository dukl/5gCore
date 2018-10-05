# coding: utf-8
# 导入:
from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
from sqlalchemy.dialects.mysql import \
     BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
     DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
     LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
     NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
     TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

import os  
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 定义User对象:
class Users(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    #id = Column(String(20), primary_key=True)
    #name = Column(String(20))
    #sqn = Column(BigInteger(20))
    OPc =  Column(VARBINARY(160))
    imei = Column(VARCHAR(15))
    imsi = Column(String(15),primary_key = True)

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:linux@localhost:3306/oai_db?charset=utf8')
print(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建session对象:
session = DBSession()
user = session.query(Users).filter(Users.imsi=='208930000000001').one()
print('type:',type(user))
print('imei:',type(user.imei))
print('OPc:',type(user.OPc))
opc = bytes().fromhex('e734f8734007d6c5ce7a0508809e7e9c')
print((opc))
if user.OPc == opc:
	print('hhhhhh')
else:
	print('eeeeee');
# 创建新User对象:
#new_user = Users(imsi = '111111111111111',sqn=00000281454575616225)
# 添加到session:
#session.add(new_user)
# 提交即保存到数据库:
#session.commit()
# 关闭session:
#session.close()

