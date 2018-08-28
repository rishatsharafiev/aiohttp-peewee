from aiohttp import web


class WebhookView(web.View):
    """Webhook View Class"""

    async def get(self):
        """Get method"""
        return web.Response(text=f'Hello')
