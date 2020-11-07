from nonebot import on_command, CommandSession
from plugins.core.mongo import get_clo_teach
from bson import ObjectId


@on_command('##', only_to_me=False)
async def delete(session: CommandSession):
    id = session.get('id')
    clo_teach = get_clo_teach()
    clo_teach.delete_one({"_id": ObjectId(id)})
    await session.send("已执行删除，")


@delete.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['id'] = stripped_arg
        return

    if not stripped_arg:
        session.finish("请输入问题id以删除")

    session.state[session.current_arg_text] = stripped_arg
