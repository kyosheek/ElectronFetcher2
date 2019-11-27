import tornado.ioloop
import tornado.web
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('This data was recieved by GET request to localhost on 443')

def make_app():
    return tornado.web.Application([
                                    (r"/", MainHandler),
                                    ])

if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    app.listen(443)
    tornado.ioloop.IOLoop.current().start()
