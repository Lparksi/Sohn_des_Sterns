from nonebot import on_startup
from plugins.feedback.core.main import upload
from nonebot.log import logger
from pluginsConfig import Feedback


@on_startup
def _():
    try:
        if Feedback:
            upload()
            logger.info("根据你的配置文件，现已将你的电脑/服务器信息与IP地址信息上传至我们的反馈服务器。\n详情见README.md\n谢谢合作！")
        else:
            logger.info("根据你的配置文件，自动跳过反馈。")
    finally:
        logger.info("反馈阶段已完成。")
