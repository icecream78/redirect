from aiohttp import web
from models import Database


class Handler(Database):
    def __init__(self):
        Database.__init__(self)

    async def redirect(self, request):
        query = request.query
        print(query)

    async def save_redirect(self, request):
        try:
            data = await request.json()
        except:
            return web.json_response({
                'ok': False,
                'result': 'Error while decode request. Fix data and try again'
            })

        if not ('url' in data or len(data['url']) > 0):
            return web.json_response({
                'ok': False,
                'url': 'Please specify link and try again',
            })

        saveStatus, code = self.save_url(data['url'])
        return web.json_response({
            'ok': saveStatus,
            'result': code
        })
