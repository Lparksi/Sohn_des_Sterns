from nonebot import on_command, CommandSession


@on_command('help', only_to_me=False)
async def help_img(session: CommandSession):
    # 2020/11/21
    # https://s3.ax1x.com/2020/11/21/D1aPpR.jpg
    await session.send("[CQ:image,file=https://s3.ax1x.com/2020/11/21/D1aPpR.jpg]")
