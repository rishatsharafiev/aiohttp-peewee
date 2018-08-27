from aiohttp import web


class ResourceView(web.View):
    """Resource View Class"""

    async def get(self):
        """Get method"""
        return web.Response(text=f'Hello')
