from aiocqhttp import Event
from nonebot import get_bot
from plugins.core.mongo import get_clo_teach

bot = get_bot()
clo_teach = get_clo_teach()


@bot.on_message
async def resp(event: Event):
    text = event.message
    date = clo_teach.find_one({"question": str(text)})
    if date is not None:
        return {'reply': date["answer"]}
    return
