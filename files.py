from ujson import dumps, loads
from aiofiles import open
from typing import Any

type DATA = dict[str, Any]


async def load(file: str = 'data.json') -> DATA:
    async with open(file, 'r', encoding='utf-8') as file:
        return loads(await file.read())


async def write[I: DATA](data: I, file: str = 'data.json') -> I:
    async with open(file, 'w', encoding='utf-8') as file:
        await file.write(dumps((await file.read())))
        return data
