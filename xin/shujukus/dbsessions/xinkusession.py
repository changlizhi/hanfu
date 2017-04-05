from xin.shujukus.dbengins.xinengin import get_mysql_engin

__author__ = 'Administrator'
from sqlalchemy.orm import sessionmaker


def get_mysql_session():
    DBSession = sessionmaker(bind=get_mysql_engin())
    return DBSession()