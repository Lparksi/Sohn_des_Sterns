def get_error_msg(error_code: int):
    if error_code == -1001:
        return "用户在黑名单"
    elif error_code == -1011:
        return "用户已为普通用户组最高"
    elif error_code == -1012:
        return "用户已为管理用户组最高"
    elif error_code is None:
        return None
    else:
        return "未定义的错误码"
