from nonebot import on_command, CommandSession, on_startup
from nonebot.log import logger


@on_startup
def _():
    logger.info("[插件] help 已启用")


@on_command("help", only_to_me=False)
async def help(session: CommandSession):
    await session.send("""----HELP----
"无限星河之子"
---INFO---
Version:0.1.0
open source url:https://github.com/Lparksi/Sohn_des_Sterns
---实用功能---
help:显示本帮助
info:显示当前群信息
hitokoto:发送一句诗词
TTS:文字转语音
weather:查询天气	
---权限公开---
sudo:获取超级管理员/管理员权限
sudo_list:查询超级管理员列表
admin_list:查询管理员列表
更多信息：https://github.com/Lparksi/Sohn_des_Sterns/blob/master/README.md""")
