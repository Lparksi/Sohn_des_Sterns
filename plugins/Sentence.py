import requests
from nonebot import on_command, CommandSession, on_startup
from nonebot.log import logger


@on_startup
async def _():
    logger.info("[插件] 一言 已启用")


@on_command("Sentence", aliases="一言", only_to_me=False)
async def Sentence(session: CommandSession):
    URL = 'https://v1.hitokoto.cn/'
    r = requests.get(URL)
    hitokoto = r.json()['hitokoto']
    await session.send(hitokoto)
