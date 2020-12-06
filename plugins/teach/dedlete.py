from nonebot import on_command, CommandSession
from plugins.core.mongo import get_clo_teach, MongoDB
from nonebot.log import logger
from bson import ObjectId
from plugins.core.log import info
from plugins.feedback.feedback import feedback

if MongoDB:
    @on_command('##', only_to_me=False)
    async def delete(session: CommandSession):
        id = session.get('id')
        clo_teach = get_clo_teach()
        clo_teach.delete_one({"_id": ObjectId(id)})
        info(log=f"{session.event.user_id} 已删除问题 {id}", module="teach", save=True)
        feedback.teach_del(session=session)
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
else:
    logger.warning("[Teach] 删除组件： 未配置MongoDB 数据库，已停止加载。")
