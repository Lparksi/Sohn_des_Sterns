from nonebot import on_command, CommandSession
from plugins.core.mongo import get_clo_teach, MongoDB
from nonebot.log import logger
import datetime
from bson import ObjectId

if MongoDB:
    @on_command("#", aliases="inquire", only_to_me=False)
    async def inquire(session: CommandSession):
        clo_teach = get_clo_teach()
        text = session.get('text')
        if len(str(text)) == 24:
            data = clo_teach.find_one({"_id": ObjectId(text)})
        else:
            data = clo_teach.find_one({"question": text})
        if data is None:
            await session.finish(f'未找到与“{text}”相关联的问答数据')
        question_id = data["_id"]
        question = data["question"]
        answer = data["answer"]
        group = data["group"]
        asker_id = data["asker"]["id"]
        asker_time = data["asker"]["time"]
        dataArray = datetime.datetime.fromtimestamp(asker_time)
        asker_time = dataArray.strftime("%Y-%m-%d %H:%M:%S")
        await session.finish(f"""问题ID：{question_id}
问题：{question}
回答：{answer}
提问者：{asker_id}
提问时所在群：{group}
创建时间：{asker_time}""")


    @inquire.args_parser
    async def _(session: CommandSession):
        stripped_arg = session.current_arg_text.strip()
        if stripped_arg:
            session.state['text'] = stripped_arg
            return

        if not stripped_arg:
            session.finish("请输入问题id或问题以查询")

        session.state[session.current_arg_text] = stripped_arg
else:
    logger.warning("[Teach] 查询组件： 未配置MongoDB 数据库，已停止加载。")
