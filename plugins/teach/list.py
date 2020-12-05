from nonebot import on_command, CommandSession
from plugins.core.mongo import get_clo_teach


@on_command('teach-list', only_to_me=False)
async def _list(session: CommandSession):
    clo_teach = get_clo_teach()
    count = clo_teach.count()
    if count <= 30:
        teaches = clo_teach.find()
        msg = f"""
当前问答数据库共存储{count}条问答。\n\n"""
        for teach in teaches:
            msg += f"Q:{teach['question']}, A:{teach['answer']}, by{teach['asker']['id']}\n\n"
        await session.finish(msg)

    else:
        # todo 对于问答多于30条的情况做分页处理
        msg = f"""
当前问答数据库共存储{count}条问答。当前问答过多，将只显示前三十条记录。\n\n"""
        count = 0
        teaches = clo_teach.find()
        if count <= 30:
            for teach in teaches:
                msg += f"Q:{teach['question']}, A:{teach['answer']}, by{teach['asker']['id']}\n\n"
        await session.finish(msg)
