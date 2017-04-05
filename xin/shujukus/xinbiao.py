from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'Administrator'
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    bianma = Column(Integer)
    mingcheng = Column(String(50))
    mima = Column(String(50))
    yan = Column(Integer)


class CeshiYongHu(Base):
    __tablename__ = "ceshi_yonghu"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
