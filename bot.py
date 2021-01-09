import nonebot
from os import path
import config

if __name__ == '__main__':
    nonebot.init(config)
    if config.USE_SQLITE3:
        nonebot.load_plugin(r"plugins.core.sqlite")
    nonebot.load_plugin(r"plugins.core.db")
    if config.USE_SMTP_MAIL:
        nonebot.load_plugin(r"plugins.core.mail")
    nonebot.run()
