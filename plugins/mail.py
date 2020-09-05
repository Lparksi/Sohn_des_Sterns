from nonebot import on_command, CommandSession

from tools.mail import sendemail


@on_command("mail", only_to_me=False)
async def mail(session: CommandSession):
    text = session.get("text", prompt="请输入参数 mail [接收者邮箱] [正文]")
    info = str(text).split(" ")
    emailaddr, msg = info[0], info[1]
    ret = sendemail(toEmail=emailaddr,
                    title="SohndesSterns外发邮件",
                    msg=msg + "\n\n\n此服务仅供测试，如被滥用清联系i@parksi.email")
    if ret == 0:
        await session.send("已发送，如被拦截请查看垃圾箱.")
    else:
        await session.send(f"ERROR:{ret}")


@mail.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请输入参数 mail [接收者邮箱] [正文]')
        session.finish()

    session.state[session.current_key] = stripped_arg
