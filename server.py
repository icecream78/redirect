from aiohttp import web
from views import redirect


app = web.Application()

app.add_routes([
    web.post('/save', redirect.Handler().save_redirect),
    web.get('/r/*', redirect.Handler().redirect)
])

if __name__ == '__main__':
    web.run_app(app, port=8889)
