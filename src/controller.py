from aiohttp import web

from src.graphql import schema


async def resolve(request):
    body = await request.json()
    try:
        result = schema.execute(str(body['query']))
        return web.json_response({
            'data': dict(result.data.items()) if result.data else None
        }, status=200)
    except Exception as e:
        return web.json_response({
            'error': e
        }, status=500)
