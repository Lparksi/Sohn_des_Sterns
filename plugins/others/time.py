from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from plugins.plugins_config.core import GROUPS


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        for group in GROUPS:
            await bot.send_group_msg(group_id=group,
                                     message=f'现在{now.hour}点整啦！')
    except CQHttpError:
        pass
