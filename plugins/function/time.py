from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.log import logger
from config import FUNC_TIME_GROUPS


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    for group in FUNC_TIME_GROUPS:
        try:
            await bot.send_group_msg(group_id=group,
                                     message=f'现在{now.hour}点整啦！')
        except CQHttpError:
            logger.warn(f"[Function.time] 向{group}发送报时消息失败！")
