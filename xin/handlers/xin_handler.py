from tornado import web
from tornado.web import RequestHandler
from xin.sessionchuli import xinwebsession

__author__ = 'Administrator'
class JiChuHandler(RequestHandler):
    def render_string(self, template_name, **kwargs):
        if self.jinja2_env:
            template_path = self.get_template_path()
            if template_path not in web.RequestHandler._template_loaders:
                web.RequestHandler._template_loaders[template_path]=self.jinja2_env
        return web.RequestHandler.render_string(self,template_name,**kwargs)
class XinSessionHandler(JiChuHandler):
    def __init__(self,*args,**kwargs):
        super.XinSeesionHandler(XinSessionHandler,self).__init__(*args,**kwargs)
        self.session = xinwebsession.Session(self.application.session_manager,self)
    def get_current_user(self):
        return self.session.get("user_name")