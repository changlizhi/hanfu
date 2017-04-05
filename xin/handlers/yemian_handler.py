from xin.applications.session_useone import login_required
from xin.handlers.xin_handler import XinSessionHandler

__author__ = 'Administrator'

class MainHandler(XinSessionHandler):
    @login_required
    def get(self):
        username = self.get_current_user()
        print("start...")
        print(username)
        print(self.session["yannuo"])
        if None == username:
            self.write("yannuo")
        else:
            self.write("登录：" + username + "？")
class LoginHandler(XinSessionHandler):
    def get(self):
        self.session["username"] = self.get_argument("name")
        self.session["yannuo"] = "言诺"
        self.session.save()
        self.write("创建session成功！")