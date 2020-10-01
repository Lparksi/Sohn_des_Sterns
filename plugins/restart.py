from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger

from plugins.Authority import checkAdmins, checkSupers


@on_startup
def _():
    logger.info("[插件] 重启 已启用")


@on_command("restart", only_to_me=False)
async def _(session: CommandSession):
    if checkSupers(session.event.user_id) or checkAdmins(session.event.user_id):
        await session.send("收到指令，正在重启.")
        await session.bot.set_restart_plugin()
    else:
        await session.send("请先行提权！")
