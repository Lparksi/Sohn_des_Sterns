import nonebot
from os import path
import config
from pathlib import Path
from os.path import isfile
import json

BAN_LIST_PATH = "db/BAN_LIST.json"


def new_list() -> None:
    """
    创建默认list文件
    :param qq: 默认黑名单初始内容
    :return: null
    """
    with open(BAN_LIST_PATH, 'w+') as f:
        f.write(json.dumps({'ban_list': [1, 2, 3]}))
        f.flush()


if __name__ == '__main__':
    if not isfile(BAN_LIST_PATH):
        new_list()
    nonebot.init(config)
    if config.USE_SQLITE3:
        nonebot.load_plugin(r"plugins.core.sqlite")
    nonebot.load_plugin(r"plugins.core.db")
    nonebot.load_plugin(r"plugins.core.auto_ban")
    nonebot.run()
