import time

from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger

from config import ADMINS
from config import SUPERUSERS as SPRS
from tools.savelogger import logger as slogger

SUPERS = {}
ADMINS = {}


@on_startup
def _():
    logger.info("[插件] Authority 已启用")


@on_command("sudo", aliases="以神之名", only_to_me=False)
async def sudo(session: CommandSession):
    if session.event.user_id in SPRS:
        SUPERS[session.event.user_id] = time.time()
        await session.send(
            f"[CQ:at,qq={session.event.user_id}]已提升为超级管理员，时效10分钟，请注意：权力越大责任越大，切勿滥用权限！(超级管理员的每一条指令都将被存储在日志文件中)")
        slogger.info(f"[授权] {session.event.user_id} 成功申请超级管理员")
    elif session.event.user_id in ADMINS:
        ADMINS[session.event.user_id] = time.time()
        await session.send(
            f"[CQ:at,qq={session.event.user_id}]已提升为管理员，时效10分钟，请注意：权力越大责任越大，切勿滥用权限！(管理员的每一条指令都将被存储在日志文件中)")
        slogger.info(f"[授权] {session.event.user_id} 成功申请管理员")
    else:
        await session.send("管理员指令，请勿触发")
        slogger.info(f"[授权] {session.event.user_id} 尝试申请管理员，但并未获得权限")


def checkSupers(user_id):
    try:
        authtime = SUPERS[user_id]
        if time.time() - authtime <= 10 * 60:
            return True
        else:
            return False
    except KeyError:
        return False


def checkAdmins(user_id):
    try:
        authtime = ADMINS[user_id]
        if time.time() - authtime <= 10 * 60:
            return True
        else:
            return False
    except KeyError:
        return False


@on_command("sudo_list", aliases="超级管理员列表", only_to_me=False)
async def sudo_list(session: CommandSession):
    msg = "---超级管理员列表---\n"
    for super in SUPERS:
        if checkSupers(super):
            auth_time = SUPERS[super]
            name = await session.bot.get_stranger_info(user_id=super)
            name = name['nickname']
            msg += f"{name} {super} {time.ctime(auth_time)}\n"
    await session.send(msg)


@on_command("admin_list", aliases="管理员列表", only_to_me=False)
async def admin_list(session: CommandSession):
    msg = "---管理员列表---\n"
    for admin in ADMINS:
        if checkAdmins(admin):
            auth_time = SUPERS[admin]
            name = await session.bot.get_stranger_info(user_id=admin)
            name = name['nickname']
            msg += f"{name} {admin} {time.ctime(auth_time)}\n"
    await session.send(msg)
