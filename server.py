import os
from aiohttp import web
from views import redirect

PORT = os.getenv('PORT', 8080)
USE_DB = os.getenv('USE_DB', 'true') == 'true'
DB_PATH = os.getenv('DB_PATH', os.path.join(os.curdir, 'record.db'))

app = web.Application()
redirect_handler = redirect.Handler(USE_DB, DB_PATH)

app.add_routes([
    web.post('/save', redirect_handler.save_redirect),
    web.get('/r/{code}', redirect_handler.redirect)
])

if __name__ == '__main__':
    web.run_app(app, port=PORT)
