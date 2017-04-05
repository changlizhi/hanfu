from jinja2 import FileSystemLoader
from tornado import ioloop
from tornado.options import parse_command_line
from tornado.web import Application, os
from xin.environments.xin_envs import XinJinja2Env
from xin.handlers.xin_handler import JiChuHandler

__author__ = "clz"
class HanFuXinHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("hanfuxin.html",greetings=greetings)

class FuXingZheMenHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("fuxingzhemen.html",greetings=greetings)

class KuanShiXingZhiHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("kuanshixingzhi.html",greetings=greetings)
class HanJiaJieRiHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("hanjiajieri.html",greetings=greetings)
class TieBaHuaTiHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("tiebahuati.html",greetings=greetings)

class DengLuZhuCeHandler(JiChuHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("dengluzhuce.html",greetings=greetings)
    def post(self):
        greetings = self.get_argument("greetings","hello")
        denglu_email = self.get_argument("inputEmail4","default")
        denglu_mima = self.get_argument("inputPassword4","default")
        # zhuce_email = self.get_argument("inputEmail5","default")
        # zhuce_mima = self.get_argument("inputPassword5","default")
        # zhuce_chongfu_mima = self.get_argument("inputPassword6","default")
        print(denglu_email)
        print(denglu_mima)
        jinja_settings={
            "auto_reload":True,
            "autoescape":True,
            "cache_size":100
        }
        self.jinja2_env=XinJinja2Env(loader=FileSystemLoader("templates"),**jinja_settings)
        self.render("dengluzhuce.html",greetings=greetings)


if __name__ == "__main__":
    parse_command_line()
    app = Application(handlers=[(r"/",DengLuZhuCeHandler),
                                (r"/hanfuxin",HanFuXinHandler),
                                (r"/tiebahuati",TieBaHuaTiHandler),
                                (r"/kuanshixingzhi",KuanShiXingZhiHandler),
                                (r"/dengluzhuce",DengLuZhuCeHandler),
                                (r"/hanjiajieri",HanJiaJieRiHandler),
                                (r"/fuxingzhemen",FuXingZheMenHandler)],
                      template_path=os.path.dirname(__file__),
                      static_path=os.path.join(os.path.dirname(__file__), "static"))
    app.listen(1212)
    ioloop.IOLoop.instance().start()







