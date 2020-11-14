from nonebot import CommandSession
from plugins.core.log import warning, info, debug
from plugins.core.mongo import get_clo_users

clo_users = get_clo_users()


# todo 优化查询逻辑，减少数据库开销
# todo 提供更多接口，减少逻辑混乱
# todo 将字典转为属性，提供自动补全，减少逻辑错误
# todo func: Inquire_level 查询等级


def new_user(session: CommandSession, name: str = None, level: int = 1, agent: bool = False) -> None:
    """
    创建一个新用户
    :param session: 会话
    :param name: 昵称
    :param level: 等级
    :param agent: 代理者
    :return: None
    """
    user = {
        'uid': int(session.event.user_id),
        'from_group_id': int(session.event.group_id),
        'name': name,
        'level': level,
        'agent': agent
    }
    clo_users.insert_one(user)
    info(log=f"创建了一位用户:{user}", save=True, module="Auth")


def find_user(uid: int):
    """
    查询一个用户
    :param uid: 用户ID
    :return: 未找到返回False，找到返回数据
    """
    date = clo_users.find_one({'uid': uid})
    debug(log=f"查询了一位用户:{date}", save=True, module="Auth")
    if date is None:
        return False
    return date


def del_user(uid: int):
    """
    删除一个用户
    :param uid: 用户ID
    :return:
    """
    date = clo_users.delete_one({'uid': uid})
    warning(log=f"删除了一位用户:{date}", save=True, module="Auth")


def up_user(uid: int):
    """
    升级一位用户
    :param uid: 用户ID
    :return: None or Error code

    :Error code:
    -1001: 用户在黑名单
    -1011: 用户已为普通用户组最高
    """
    date = find_user(uid)
    if date['level'] == 0:
        return -1001
    elif date['level'] >= 3:
        return -1011
    date['level'] = date['level'] + 1
    clo_users.save(date)


def super_user(uid: int):
    """
    提权一位用户
    :param uid: 用户ID
    :return: None or Error code

    :Error code:
    -1001: 用户在黑名单
    -1012: 用户已为管理用户组最高
    """
    date = find_user(uid)
    if date['level'] < 7 and date['level'] != 0:
        if date["level"] <= 3:
            date['level'] = 3
        date["level"] = date['level'] + 1
        clo_users.save(date)
    if date['level'] == 0:
        return -1001
    if date['level'] >= 7:
        return -1012


__doc__ = """
'uid': session.event.user_id,   用户id
'from_group_id': session.event.group_id,  用户来自的群聊  
'name': name,  用户昵称
'level': level,  用户等级
    1 普通用户
    2 资深用户
    3 骨灰级用户
    4 管理员
    5 超级管理员
    6 权力代行者
    0 黑名单用户
'agent': agent 权力代行者，能够行使全部的权力
    True or False
"""
