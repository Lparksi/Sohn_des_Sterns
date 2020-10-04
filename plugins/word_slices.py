import requests
from nonebot import on_startup, on_command, CommandSession
from nonebot.log import logger

from pluginsConfig import HTTP_HOST, HTTP_PORT


@on_startup
def _():
    logger.info("[插件] word_slices 已启用")
    logger.warn("此功能仅支持GO-CQHTTP")


def get_word_slices(content):
    URL = f"http://{HTTP_HOST}:{HTTP_PORT}/.get_word_slices"
    r = requests.post(url=URL,
                      data={
                          "content": content
                      })
    date = r.json()
    return date["data"]["slices"]


@on_command('word_slices', aliases="分词", only_to_me=False)
async def word_slices(session: CommandSession):
    content = session.get("content")
    date = get_word_slices(content=content)
    msg = '分词的结果是；\n'
    for word in date:
        msg += word + " "
    await session.send(message=msg)


@word_slices.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['content'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要分词的文字不能为空！')
        session.finish()
    session.state[session.current_arg_text] = stripped_arg
