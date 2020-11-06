from nonebot import on_startup, on_command, CommandSession

from plugins.others.bingImage.getImage import getDailyImage, getBingImage


@on_startup
def _():
    pass


@on_command('daliimg', aliases=("每日一图", "每日图片"), only_to_me=False)
async def daliimg(session: CommandSession):
    url = getDailyImage()
    await session.send(f'[CQ:image,file={url}]')


@on_command('image', aliases="一图", only_to_me=False)
async def image(session: CommandSession):
    url = getBingImage()
    await session.send(f"[CQ:image,cache=0,file={url}]")
