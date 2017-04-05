from jinja2 import FileSystemLoader, Environment
from tornado import ioloop
from tornado.options import parse_command_line
from tornado.web import RequestHandler, Application

__author__ = 'clz'

class MyHandler(RequestHandler):
    _path_to_env = {}
    def get_template_path(self):
        return "./templates/"
    def create_template_loader(self, template_path):
        temp_path = template_path
        if isinstance(template_path,(list,tuple)):
            temp_path = template_path[0]
        env = MyHandler._path_to_env.get(temp_path)
        if not env:
            _loader = FileSystemLoader(temp_path)
            env = Environment(loader = _loader)
            MyHandler._path_to_env[temp_path] = env
        return env
    def render_string(self, template_name, **kwargs):
        env = self.create_template_loader(self.get_template_path())
        t = env.get_template(template_name)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.render(**namespace)

class IndexHandler(MyHandler):
    def get(self):
        greetings = self.get_argument("greetings","hello")
        self.render("index.html",greetings = greetings)

if __name__ == "__main__":
    parse_command_line()
    app = Application(handlers=[(r'/',IndexHandler)])
    app.listen(1212)
    ioloop.IOLoop.instance().start()