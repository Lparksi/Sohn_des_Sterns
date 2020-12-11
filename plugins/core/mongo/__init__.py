# MongoDB 数据库操作

from pymongo import MongoClient
from plugins.plugins_config.core import MONGODB_URL, MONGODB_SHOW_URL
from nonebot.log import logger

MongoDB = False
if MONGODB_URL is not None:
    if MONGODB_SHOW_URL:
        logger.debug(f"[MongoDB] 正在尝试连接：{MONGODB_URL}")
        client = MongoClient(MONGODB_URL)
        db = client['bot']
        clo_groups = db['groups']
        clo_users = db['users']
        clo_teach = db['teach']


        def get_db_bot():
            return db


        def get_clo_groups():
            return clo_groups


        def get_clo_users():
            return clo_users


        def get_clo_teach():
            return clo_teach


    MongoDB = True
else:
    logger.warning("[MongoDB] 数据库URL 未配置")
    logger.warning("[MongoDB] 基于 MongoDB 的插件将不可用！")
    def get_db_bot():
        return 0


    def get_clo_groups():
        return 0


    def get_clo_users():
        return 0


    def get_clo_teach():
        return 0
