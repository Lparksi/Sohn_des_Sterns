from nonebot import on_command, CommandSession

from tools.mail import sendemail


@on_command("mailme", only_to_me=False)
async def mailme(session: CommandSession):
    message = session.get("msg", prompt="你要发送什么？")
    ret = sendemail(toEmail=f"{session.event.user_id}@qq.com",
                    title="Parksi-Bot 测试邮件",
                    msg=message + "\n\n\n由Liu Parksi维护，如被骚扰请联系i@parksi.email,谢谢合作！")
    if ret == 0:
        await session.send("已发送，如被拦截请查看垃圾箱.")
    else:
        await session.send(f"ERROR:{ret}")


@mailme.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['msg'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请输入邮件正文')
