from os import path, mkdir
from os.path import exists
import nonebot
import shutil
import config
import json


def copy_plugins_config():
    shutil.copy(src='pluginsConfigDefault.json',
                dst='pluginsConfig.json')


if __name__ == '__main__':
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
    nonebot.run()
