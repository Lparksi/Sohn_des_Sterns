import time

from nonebot import on_command, CommandSession

from plugins.core.log import info
from plugins.core.mongo import get_clo_teach


@on_command('teach', only_to_me=False)
async def teach(session: CommandSession):
    test = str(session.get('text')).split(" ")
    if len(test) != 2:
        await session.finish("请输入正确格式。\n.teach <问题> <答案>")
    question = test[0]
    answer = test[1]
    if check_question_in_db(question=question):
        await session.finish("问题已存在于数据库中。")
    if question == answer:
        await session.finish("问题不能与答案相同。")
    if len(question) <= 4:
        await session.finish("问题长度不得小于5字符。")

    if session.event.sub_type != 'group':
        group_id = None
    else:
        group_id = session.event.group_id
    que = {
        "question": question,
        "answer": answer,
        "group": group_id,
        "asker": {
            "id": session.event.user_id,
            "time": float(time.time())
        }
    }
    info(log=f"插入一个文档：{que}", save=True, module="MongoDB")
    clo_teach = get_clo_teach()
    id = clo_teach.insert_one(que).inserted_id
    await session.finish(f"问答创建成功！ID为{id}")


@teach.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg.strip()
    if stripped_arg:
        session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.finish("请输入正确格式。\n.teach <问题> <答案>")

    session.state[session.current_arg_text] = stripped_arg


def check_question_in_db(question: str) -> bool:
    """
    检查问题是否已在数据库中
    :param question: 问题
    :return: 在 True 否 False
    """
    clo_teach = get_clo_teach()
    if clo_teach.find_one({'question': question}) is None:
        return False
    return True
