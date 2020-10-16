from nonebot import on_command, on_startup, CommandSession
from nonebot.log import logger


@on_startup
def _():
    logger.info("[插件] TTS 已启用")


@on_command("TTS", aliases="tts", only_to_me=False)
async def tts(session: CommandSession):
    text = session.get("text")
    await session.send(f"[CQ:tts,text={text}]")


@tts.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['text'] = stripped_arg

    if not stripped_arg:
        session.finish("请附带要转换的文本!")

    session.state[session.current_arg_text] = stripped_arg
