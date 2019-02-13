import pybald
from pybald import context
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

from config import config


# configure our pybald application
pybald.configure(config_object=config)


def map(urls):
    urls.connect('home', r'/', controller='home')


class HomeController(Controller):
    @action
    def index(self, req):
        return "Hello!"


app = Router(routes=map, controllers=[HomeController])

if __name__ == "__main__":
    context.start(app)
