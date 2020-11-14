from nonebot import on_command, CommandSession
from plugins.user.core import up_user, find_user, new_user
from plugins.core.error_code import get_error_msg
from plugins.core.user_level_msg import get_user_level_msg
from nonebot.permission import SUPERUSER


# @on_command('upgrade', only_to_me=False, permission=SUPERUSER)
async def admin_upgrade(session: CommandSession):
    uid = session.get('uid')
    if uid is None:
        uid = session.event.user_id
    if not find_user(uid):
        new_user(session=session,
                 name=session.event.sender['nickname'])
    err = up_user(uid)
    if err is not None:
        await session.finish(get_error_msg(err))
    else:
        date = find_user(uid)
        await session.finish(
            f"[CQ:at,qq={session.event.user_id}],你的等级已提升为 [{date['level']} {get_user_level_msg(date['level'])}]")


# @admin_upgrade.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['uid'] = stripped_arg
    if not stripped_arg:
        session.state['uid'] = None
