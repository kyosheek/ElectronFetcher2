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
    app.listen(443)
        try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

