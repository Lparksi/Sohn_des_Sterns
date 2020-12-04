from nonebot import on_notice, NoticeSession
from plugins.plugins_config.core import GROUPS


@on_notice('notify')
async def notify(session: NoticeSession):
    if session.event.group_id in GROUPS:
        if session.event.sub_type == 'honor':
            if session.event['honor_type'] == 'talkative':
                await session.send(f"[CQ:at,qq={session.event.user_id}],恭喜成为（水）龙王")
            elif session.event['honor_type'] == 'performer':
                await session.send(f"[CQ:at,qq={session.event.user_id}],恭喜获得[群聊之火]成就")
            elif session.event['honor_type'] == 'emotion':
                await session.send(f"[CQ:at,qq={session.event.user_id}],恭喜获得[快乐源泉]成就")
            else:
                pass
