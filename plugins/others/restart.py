from nonebot import on_command, CommandSession


@on_command("restart", only_to_me=False)
async def _(session: CommandSession):
    if checkSupers(session.event.user_id) or checkAdmins(session.event.user_id):
        await session.send("收到指令，正在重启.")
        await session.bot.set_restart_plugin()
    else:
        await session.send("请先行提权！")
