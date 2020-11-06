import time

from nonebot import on_command, CommandSession, on_startup
from nonebot.log import logger


@on_startup
def _():
    logger.info("[插件] INFO 已启用")


start_time = time.ctime()


@on_command('info', only_to_me=False)
async def info(session: CommandSession):
    data = await session.bot.get_group_info(group_id=session.event.group_id)
    group_name, member_cont, max_member_count = data["group_name"], data["member_count"], data["max_member_count"]
    await session.send(f"""---GROUP INFO---
{group_name}({session.event.group_id})
目前群人数：{member_cont}
最大群人数：{max_member_count}
---BOT INFO---
启动时间：{start_time}""")
    logger.info(f"[插件 INFO] 向群 {group_name}/{session.event.group_id} 发送了信息")
