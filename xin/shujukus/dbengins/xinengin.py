__author__ = 'Administrator'
from sqlalchemy import create_engine


def get_mysql_engin():
    return create_engine("mysql+pymysql://root:root@localhost:3306/hanfuxin?charset=utf8")