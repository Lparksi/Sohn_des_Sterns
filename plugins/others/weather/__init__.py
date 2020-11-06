from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger

from plugins.others.weather.getWeather import getWeather


@on_startup
def _():
    logger.info("[插件] 天气 已启用")


@on_command('weather', aliases="天气", only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt="你要查询哪个城市的天气？")
    await session.send(getWeather(city=city))


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的城市名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg
