import time

from nonebot import on_command, CommandSession

start_time = time.ctime()


# todo 对于不在群聊的请求，只显示Bot-info 部分 by:QQ TALK GROUP
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
