# MongoDB 数据库操作

from pymongo import MongoClient
from pluginsConfig import MONGODB_URL
from nonebot.log import logger

if MONGODB_URL is not None:
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
else:
    logger.warning("[MongoDB] 数据库URL 未配置")
