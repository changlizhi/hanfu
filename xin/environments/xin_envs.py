from jinja2 import Environment

__author__ = 'Administrator'
class XinJinja2Env(Environment):
    def load(self,template_name):
        templ = self.get_template(template_name)
        if templ:
            setattr(templ,"generate",templ.render)
        return templ
    def reset(self):
        if hasattr(self,"bytecode_cache") and self.bytecode_cache:
            self .bytecode_cache.clear()