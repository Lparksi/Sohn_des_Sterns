import requests
from nonebot import on_command, CommandSession


@on_command("Sentence", aliases="一言", only_to_me=False)
async def Sentence(session: CommandSession):
    URL = 'https://v1.hitokoto.cn/'
    r = requests.get(URL)
    hitokoto = r.json()['hitokoto']
    await session.send(hitokoto)
