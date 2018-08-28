from aiohttp import web
import aiomonitor

from project.application import init_app
from project import settings

import logging
import logging.config


def app_factory():
    """Application factory"""
    # Initialize logging config
    logging.config.dictConfig(settings.LOGGING)

    # Get loop
    loop = settings.loop

    # Set up monitoring tool
    with aiomonitor.start_monitor(loop=loop, locals={"host": settings.APP_HOST, "port": settings.APP_PORT}):
        # Run application
        app = loop.run_until_complete(init_app(loop))
        web.run_app(app, host=settings.APP_HOST, port=settings.APP_PORT)


if __name__ == '__main__':
    app_factory()
