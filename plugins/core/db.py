from nonebot.log import logger

import config
import time

signed_user_list = []
# Sqlite3 模式
if config.USE_SQLITE3:
    from plugins.core.sqlite import Sohn_des_Sterns

    db = Sohn_des_Sterns

    users = db.cursor().execute('select * from user').fetchall()
    for user in users:
        signed_user_list.append(user[1])
    logger.info(f"[SQLITE3]:数据库加载并缓冲完毕，现有用户 {len(signed_user_list)} 个！")


    def create_user(qq: int, nick_name: str = 'Undefined', sign_time: float = time.time()) -> None:
        """
        创建一个用户
        :param qq:QQ号
        :param nick_name:昵称
        :param sign_time: 注册时间
        :return: None
        """
        db.cursor().execute('insert into user (qq, nick_name, sign_time) VALUES (?,?,?)', (
            qq, f'"{nick_name}"', sign_time
        ))
        db.commit()
        signed_user_list.append(qq)


    def rename_user(nick_name: str, qq: int = 0, uid: int = 0) -> None:
        """
        重命名一个用户，两个参数二选一。
        :param nick_name:昵称
        :param qq: QQ号
        :param uid: Uid
        :return:None
        """
        if qq:
            db.execute('update user set nick_name=? where qq=?', (f'"{nick_name}"', qq))
            db.commit()
        elif uid:
            db.execute('update user set nick_name=? where uid=?', (f'"{nick_name}"', uid))
            db.commit()
        else:
            raise Exception("缺少参数qq或uid！")


    def is_signed(qq: int) -> bool:
        """
        检查是否已注册
        :param qq: QQ号
        :return: Bool
        """
        if qq in signed_user_list:
            return True
        else:
            return False
