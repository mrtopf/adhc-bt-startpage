from framework import Handler, Application
from framework.decorators import html
from logbook import Logger
from logbook import FileHandler
import uuid
import werkzeug
import datetime
import pkg_resources
from jinja2 import Environment, PackageLoader, TemplateNotFound


import setup

class StaticHandler(Handler):
    def get(self, path_info):
        return self.settings.staticapp

class CSSResourceHandler(Handler):
    def get(self, path_info):
        return self.settings['css'].render_wsgi

class JSResourceHandler(Handler):
    def get(self, path_info):
        return self.settings['js'].render_wsgi

class Page(Handler):
    """show a page"""

    @html
    def get(self, page=None):
        if page is None:
            page = "index.html"
        try:
            tmpl = self.app.pts.get_template(page)
        except TemplateNotFound:
            raise werkzeug.exceptions.NotFound()
        out = tmpl.render(
            css = self.settings.css(),
            js = self.settings.js(),
            )
        return out
        

class App(Application):

    logfilename = "/tmp/frontend.log"
    
    def setup_handlers(self, map):
        """setup the mapper"""
        map.connect(None, "/css/{path_info:.*}", handler=CSSResourceHandler)
        map.connect(None, "/js/{path_info:.*}", handler=JSResourceHandler)
        map.connect(None, "/img/{path_info:.*}", handler=StaticHandler)
        map.connect(None, "/extensions/{path_info:.*}", handler=StaticHandler)
        map.connect(None, "/", handler=Page)
        map.connect(None, "/{page}", handler=Page)
        self.logger = Logger('app')

        self.pts = Environment(loader=PackageLoader("startpage","templates"))

def main():
    port = 7652
    app = App(setup.setup())
    return webserver(app, port)

def frontend_factory(global_config, **local_conf):
    settings = setup.setup(**local_conf)
    return App(settings)

def webserver(app, port):
    import wsgiref.simple_server
    wsgiref.simple_server.make_server('', port, app).serve_forever()

if __name__=="__main__":
    main()
else:
    settings = setup.setup()
    app = App(settings)
