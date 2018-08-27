from aiohttp import web
import jinja2
import aiohttp_jinja2

from project import settings
from project.routes import setup_routes


async def init_app(loop=None):
    """Initialize application"""
    app = web.Application(
        middlewares=[],
        loop=loop
    )

    # Setup templates
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(settings.TEMPLATES_PATH.iterdir()))

    # Setup routes
    setup_routes(app)

    if settings.DEBUG:
        app.router.add_static(settings.STATIC_URL, settings.STATIC_PATH)

    return app
