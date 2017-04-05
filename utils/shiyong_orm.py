from xin.shujukus.xinbiao import User
from xin.shujukus.xindao import UserDao, CeshiYongHuDao

__author__ = "clz"
if __name__ == "__main__":
    new_user = User(id = 1003,bianma=3333,mingcheng="clztest",mima="bbb333cccaaa",yan=4713)
    user_dao = UserDao()
    ceshi_yonghu_dao = CeshiYongHuDao()
    # user_dao.insert_user(new_user)
    print(user_dao.select_all())
    print(ceshi_yonghu_dao.select_all())
    #增加
    # session.add(new_user)
    # session.commit()
    #查询
    # users = session.query(User).filter(User.id.in_([2,3])).order_by("id").all()
    # print(users[1].mingcheng)
    #like查询打印sql
    # users = session.query(User).filter(User.id.like("100%")).order_by("id")
    # print(users)
    # print(users.all()[1].mingcheng,len(users.all()))
    #
    # ceshis = session.query(CeshiYongHu).filter(CeshiYongHu.id.in_([1,2])).order_by("id").all()
    # print(ceshis)
    #更新
    # session.query(User).filter(User.id == 1002).update({User.mingcheng:"mingchengclz"})
    # session.commit()
    #计数
    # userscount = session.query(func.count("*")).select_from(User).filter(User.id.in_("3")).scalar()
    # print(userscount)
    #删除
    # session.query(User).filter(User.id == 1002).delete()
    # session.commit()
    #执行原生sql
    # sql = session.query("id","mingcheng").from_statement("select id,mingcheng from user where id like '100%'")
    # print(sql.all())
    # sql = session.query("id","mingcheng").from_statement("select id,mingcheng from user where id =:id").params(id=12)
    # print(sql.all())
    # session.close()