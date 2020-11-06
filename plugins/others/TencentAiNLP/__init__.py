import plugins.others.TencentAiNLP.api
from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger


@on_startup
def _():
    logger.info("[插件] 智能闲聊 已启用")


@on_command("ask", aliases="#", only_to_me=False)
async def ask(session: CommandSession):
    text = session.get('text')
    await session.send(api.TextChat.ask(text))


@ask.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.finish()

    session.state[session.current_arg_text] = stripped_arg
