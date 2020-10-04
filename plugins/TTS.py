from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger


@on_startup
def _():
    logger.info("[插件] TTS语音转文字 已启用")
    logger.warn("此功能仅支持GO-CQHTTP！")


@on_command("tts", only_to_me=False)
async def tts(session: CommandSession):
    text = session.get('text')
    await session.send(f"[CQ:tts,text={text}]")


@tts.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要转换语音的文字不能为空！')
        session.finish()
    session.state[session.current_arg_text] = stripped_arg
