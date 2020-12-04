from nonebot import on_notice, NoticeSession
from plugins.plugins_config.core import GROUPS


@on_notice('group_increase')
async def group_increase(session: NoticeSession):
    if session.event.group_id in GROUPS:
        await session.send(f"""[CQ:at,qq={session.event.user_id}],欢迎新大佬加入！
操作者：{session.event.operator_id}""")


@on_notice('group_decrease')
async def group_decrease(session: NoticeSession):
    if session.event.group_id in GROUPS:
        if session.event.sub_type == 'leave':
            await session.send(f"""用户 [{session.event.user_id}] 已退出本群。
珍惜在一起的一分一秒。""")
        elif session.event.sub_type == 'kick':
            await session.send(f"""用户 [{session.event.user_id}] 被 [CQ:at,qq={session.event.operator_id}]移除群聊，
请遵守本群群规！""")
        else:
            pass


@on_notice('group_ban')
async def group_ban(session: NoticeSession):
    if session.event.group_id in GROUPS:
        if session.event.sub_type == 'ban':
            await session.send(
                f"""[CQ:at,qq={session.event.user_id}] 被 [CQ:at,qq={session.event.operator_id}] 禁言 {session.event['duration'] / 60}分钟""")
        elif session.event.sub_type == 'lift_ban':
            await session.send(f"""[CQ:at,qq={session.event.user_id}] 被 [CQ:at,qq={session.event.operator_id}] 解除禁言。""")
