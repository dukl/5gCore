# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import \
     BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
     DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
     LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
     NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
     TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 定义User对象:
class Users(Base):
	# 表的名字:
	__tablename__ = 'users'

	# 表的结构:
	#OPc =  Column(VARBINARY(16))
	#key = Column(VARBINARY(16))
	#imei = Column(VARCHAR(15))
	imsi = Column(VARCHAR(15),primary_key = True)
	msisdn = Column(VARCHAR(46))
	imei = Column(VARCHAR(15))
	rau_tau_timer = Column(INTEGER(10))
	ue_ambr_ul = Column(BIGINT(20))
	ue_ambr_dl = Column(BIGINT(20))
	access_restriction = Column(INTEGER(10))
	mmeidentity_idmmeidentity = Column(INTEGER(11))
	key = Column(VARBINARY(16))
	rand = Column(VARBINARY(16))
	OPc = Column(VARBINARY(16))

class mmeidentity(Base):

	__tablename__ = 'mmeidentity'

	idmmeidentity = Column(INTEGER(11),primary_key = True)
	mmehost = Column(VARCHAR(255))
	mmerealm = Column(VARCHAR(200))

