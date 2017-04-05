import tornado
from xin.handlers.yemian_handler import MainHandler, LoginHandler
from xin.sessionchuli import xinwebsession

__author__ = 'Administrator'


def login_required(f):
    def _wrapper(self, *args, **kwargs):
        print(self.get_current_user())
        logged = self.get_current_user()
        if None == logged:
            self.write("no login")
            self.finish()
        else:
            ret = f(self, *args, **kwargs)

    return _wrapper


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f",
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=60,
            store_options={
                "redis_host": "localhost",
                "redis_port": 6379,
                "redis_pass": ""
            }
        )
        handlers = [
            (r"", MainHandler),
            (r"/", MainHandler),
            (r"/login", LoginHandler)

        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = xinwebsession.SessionManager(
            settings["session_secret"], settings["store_options"], settings["session_timeout"]
        )

if __name__ == "__main__":
    app = Application()
    app.listen(1212)
    print("start on 1212..")
    tornado.ioloop.IOLoop.instance().start()