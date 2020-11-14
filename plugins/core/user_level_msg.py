def get_user_level_msg(level: int):
    if level == 0:
        return "黑名单用户"
    elif level == 1:
        return "普通用户"
    elif level == 2:
        return "资深用户"
    elif level == 3:
        return "骨灰级用户"
    elif level == 4:
        return "管理员"
    elif level == 5:
        return "超级管理员"
    elif level == 6:
        return "权力代行者"
    else:
        return "未定义等级"
