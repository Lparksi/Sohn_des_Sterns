from nonebot import on_command, CommandSession


@on_command('info', only_to_me=False)
async def info(session: CommandSession):
    if session.event.sub_type == "group":
        data = await session.bot.get_group_info(group_id=session.event.group_id)
        group_id = data["group_id"]
        group_name = data["group_name"]
        member_count = data["member_count"]
        max_member_count = data["max_member_count"]
        await session.send(f"""--Group Info--
Id:{group_id}
Name:{group_name}
Member Count:{member_count}
Max Member Count:{max_member_count}""")
