import threading

__author__ = "clz"
from tornado import web,template,ioloop
import os
from jinja2 import Environment, FileSystemLoader
#####不重写render_string
class TTemplate(object):
    def __init__(self,template_instance):
        self.template_instance=template_instance
    def generate(self,**kwargs):
        return self.template_instance.render(**kwargs)

class JinjaLoader(template.BaseLoader):
    def __init__(self,root_dictionary,**kwargs):
        self.root = os.path.abspath(root_dictionary)
        self.jinja2_env=Environment(loader=FileSystemLoader(self.root),**kwargs)
        self.templates={}
        self.lock = threading.RLock()
    def resolve_path(self, name, parent_path=None):
        return name
    def _create_template(self, name):
        template_instance=TTemplate(self.jinja2_env.get_template(name))
        return template_instance

class IndexHandler(web.RequestHandler):
    def get(self):
        greetings=self.get_argument("greeting","hello")
        self.render("index.html",greetings=greetings)
if __name__ == "__main__":
    template_loader = JinjaLoader("./templates/")
    jinja_settings={
        "template_loader":template_loader,
        "auto_reload":True,
        "autoescape":True,
        "cache_size":100
    }
    # options.parse_command_line()
    app = web.Application(handlers=[(r"/",IndexHandler)],**jinja_settings)
    # http_server = httpserver.HTTPServer(app)
    # http_server.listen(options.port)
    app.listen(1212)
    ioloop.IOLoop.instance().start()
