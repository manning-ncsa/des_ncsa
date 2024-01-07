""" Main application for public release"""
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.log
import Settings
from tornado.options import define, options
import os
from global_vars import log

define("port", default=8080, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(tornado.web.RequestHandler):
    """
    Class that handle most of the request, all the rest of the handling is done
    by page.js
    """
    @tornado.web.asynchronous
    def get(self, path = ''):
        self.render('index.html', rootPath = r'{}/'.format(Settings.APP_ROOT))

        #passwords = read_passwd_file()
        #if verify_password(passwords, basicauth_user, basicauth_pass):
            #self.render('index.html')

class My404Handler(tornado.web.RequestHandler):
    """
    Handles 404 requests, basically bust just changin the status to 404
    """
    def get(self):
        self.set_status(404)
        self.render('index.html', chichi=False)
    def post(self):
        self.set_status(404)
        self.render('index.html', chichi=False)

class Application(tornado.web.Application):
    """
    The tornado application  class
    """
    def __init__(self):
        # The order of the route handlers matters!
        handlers = [
            (r"{}".format(Settings.APP_ROOT), MainHandler),
            (r"{}/static/(.*)".format(Settings.APP_ROOT), tornado.web.StaticFileHandler, {'path':Settings.STATIC_PATH}),
            (r"{}/(.*)".format(Settings.APP_ROOT), MainHandler),
            ]
        settings = {
            "template_path":Settings.TEMPLATE_PATH,
            "debug":Settings.DEBUG_ENABLED,
            "default_handler_class": My404Handler,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    """
    The main function
    """
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    #http_server = tornado.httpserver.HTTPServer(Application(), ssl_options={"certfile": "/etc/httpd/ssl/des.crt", "keyfile": "/etc/httpd/ssl/des.key",})
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
