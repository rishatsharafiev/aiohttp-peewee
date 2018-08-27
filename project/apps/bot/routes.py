from aiohttp import web

from .views import WebhookView

routes = [
    web.view('/webhook', WebhookView, name='webhook')
]
