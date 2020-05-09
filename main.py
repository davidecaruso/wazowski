import os

from aiohttp import web
from dotenv import load_dotenv, find_dotenv

from src.controller import resolve
from src.wazowski import Wazowski

load_dotenv(find_dotenv())

app = web.Application()
app.add_routes([web.post('/graphql', resolve)])

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    web.run_app(app, port=port if Wazowski.is_port_free(port) else Wazowski.next_free_port(port))
