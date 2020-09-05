from nonebot import on_notice, NoticeSession


@on_notice("group_increase")
async def _(session: NoticeSession):
    if session.event.group_id == 866912510:
        await session.bot.send_group_msg(message=f"欢迎新大佬[CQ:at,qq={session.event.user_id}]",
                                         group_id=session.event.group_id)
        await session.bot.send_group_msg(message="博客：https://parksi.top\n导航：https://shendang.top",
                                         group_id=session.event.group_id)
