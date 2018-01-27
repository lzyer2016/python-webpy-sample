#encoding: utf-8

#   入口

from urls import urls
from handlers import *
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()