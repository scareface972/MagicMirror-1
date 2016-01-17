import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado import autoreload
from tornado.options import define, options

define("port", default=8000, help="")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop = tornado.ioloop.IOLoop().instance()
    autoreload.start(ioloop)
    ioloop.start()
