import os
from aiohttp import web
from models import Database


class Handler(Database):
    def __init__(self, use_external_db=False, db_path=os.path.join(os.curdir, 'record.db')):
        Database.__init__(self, use_external_db, db_path)

    async def redirect(self, request):
        code = request.match_info.get('code', None)
        if code is None:
            return web.json_response({
                'ok': False,
                'result': 'No redirect code specified'
            })
        redirect_url = self.get_url(code)
        if redirect_url is None:
            return web.json_response({
                'ok': False,
                'result': 'No redirect url was found by code'
            })

        return web.HTTPFound(redirect_url)

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
