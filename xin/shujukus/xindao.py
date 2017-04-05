from xin.shujukus.dbsessions.xinkusession import get_mysql_session
from xin.shujukus.xinbiao import User, CeshiYongHu

__author__ = 'Administrator'


class UserDao():
    session = get_mysql_session()

    def insert_user(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def select_all(self):
        users = self.session.query(User).filter(User.id.in_([2, 3])).order_by("id").all()
        return users


class CeshiYongHuDao():
    session = get_mysql_session()

    def insert_ceshi_yonghu(self, ceshi_yonghu):
        self.session.add(ceshi_yonghu)
        self.session.commit()
        self.session.close()

    def select_all(self):
        ceshi_yonghus = self.session.query(CeshiYongHu).filter(CeshiYongHu.id.in_([2, 1])).order_by("id").all()
        return ceshi_yonghus