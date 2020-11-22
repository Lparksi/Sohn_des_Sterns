from nonebot import on_startup
from nonebot.log import logger
from pluginsConfig import SdS_Version, pre_release


@on_startup
def _():
    logger.info(f"当前星之子版本为：{SdS_Version}")
    if not pre_release:
        logger.warning("你正在使用测试版本的星之子！")
