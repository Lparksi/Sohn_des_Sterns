from os import path, mkdir
from os.path import exists
import nonebot
import shutil
import config
import uuid


def copy_plugins_config():
    shutil.copy(src='pluginsConfigDefault.json',
                dst='pluginsConfig.json')


if __name__ == '__main__':
    if not exists('sds_id'):
        sds_id = str(uuid.uuid1())
        with open('sds_id', 'w+', encoding='utf-8') as f:
            f.write(sds_id)
        nonebot.log.logger.info(f"未检测出星之子唯一Id，已创建，Id为{sds_id}")

    if not exists('pluginsConfig.json'):
        copy_plugins_config()

    if not path.isdir("logs"):
        mkdir("logs")

    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'plugins_config'),
        'plugins.plugins_config'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'core'),
        'plugins.core'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'feedback'),
        'plugins.feedback'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'others'),
        'plugins.others'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'teach'),
        'plugins.teach'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'user'),
        'plugins.user'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'group_manger'),
        'plugins.group_manger'
    )
    nonebot.log.logger.info("星之子插件加载完毕。https://sds.parksi.top")
    nonebot.run()
