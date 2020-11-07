from nonebot import on_startup, on_command, CommandSession
from plugins.core.log import logger, warning, info, debug, error
import json, time
from plugins.core.mongo import get_clo_teach


@on_startup
def _():
    logger.info("[插件] 教学 已启用")


@on_command('teach', only_to_me=False)
async def teach(session: CommandSession):
    test = str(session.get('text')).split(" ")
    if len(test) != 2:
        await session.finish("请输入正确格式。\n.teach <问题> <答案>")
    question = test[0]
    answer = test[1]
    que = {
        "question": question,
        "answer": answer,
        "group": session.event.group_id,
        "asker": {
            "id": session.event.user_id,
            "time": float(time.time())
        }
    }
    debug(log=f"插入一个文档：{que}", save=True, module="MongoDB")
    clo_teach = get_clo_teach()
    id = clo_teach.insert_one(que).inserted_id
    await session.finish(f"问答创建成功！ID为{id}")


@teach.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.finish("请输入正确格式。\n.teach <问题> <答案>")

    session.state[session.current_arg_text] = stripped_arg
