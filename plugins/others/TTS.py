from nonebot import on_command, CommandSession


@on_command("TTS", aliases="tts", only_to_me=False)
async def tts(session: CommandSession):
    text = session.get("text")
    await session.send(f"[CQ:tts,text={text}]")


@tts.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.finish("请附带要转换的文本!")

    session.state[session.current_arg_text] = stripped_arg
