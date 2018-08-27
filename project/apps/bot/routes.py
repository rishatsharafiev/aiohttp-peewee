from aiohttp import web

from .views import ResourceView

routes = [
    web.view('/resources', ResourceView, name='resource')
]
