import aiohttp
import pika

fhost = "127.0.0.1"
#fhost = "172.17.0.2"
fport = 8000
chost = "127.0.0.1"
#chost = "172.17.0.2"
cport = 8001


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def post(url, data):
    if isinstance(data, list):
        data = [item.dict() for item in data]
    elif isinstance(data, dict | int | str | float):
        data = data
    else:
        data = data.dict()
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.text()
