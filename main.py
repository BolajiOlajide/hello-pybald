import pybald
from pybald import context
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

from config import config


# configure our pybald application
pybald.configure(config_object=config)


def map(urls):
    urls.connect('home', r'/', controller='home')
    urls.connect('show_blog', r'/blog', controller='home',
                 action='showBlog')
    urls.connect('show_post', r'/blog/posts/{id}', controller='post',
                 action='show', conditions={"method": ["GET", "HEAD"]})


class PostController(Controller):
    @action
    def show(self, req):
        return "Posting a new blog post"


class HomeController(Controller):
    @action
    def index(self, req):
        return "Hello!"

    @action
    def showBlog(self, req):
        return "Welcome to my blog!"


app = Router(routes=map, controllers=[HomeController])

if __name__ == "__main__":
    context.start(app)
