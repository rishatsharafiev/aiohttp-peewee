from aiohttp import web
import aiomonitor

from project.application import init_app
from project import settings


def app_factory():
    loop = settings.loop

    with aiomonitor.start_monitor(loop=loop, locals={"host": settings.APP_HOST, "port": settings.APP_PORT}):
        app = loop.run_until_complete(init_app(loop))
        web.run_app(app, host=settings.APP_HOST, port=settings.APP_PORT)


if __name__ == '__main__':
    app_factory()
