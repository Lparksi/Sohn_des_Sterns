from os import path, mkdir

import nonebot

import config

if __name__ == '__main__':
    if not path.isdir("logs"):
        mkdir("logs")
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'core'),
        'plugins.core'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'others'),
        'plugins.others'
    )
    nonebot.run()
