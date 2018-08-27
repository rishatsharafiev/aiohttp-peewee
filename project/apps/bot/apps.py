from aiohttp import web

from .routes import routes

bot_app = web.Application()
bot_app.add_routes(routes)
