import leancloud
import requests
import uuid
from nonebot import CommandSession
import hashlib
from config import OWNER
from nonebot.log import logger

_MODEL_NAME = 'FeedBack'


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


class FeedBack(object):
    def __init__(self):
        # init
        leancloud.init(app_id='CDhsl3xYSgOtBsa7h4FRi95J-MdYXbMMI',
                       app_key='9kSvJ9zY34bH1RY7oMbgCb7B')

        # EnvInfo
        EnvInfo = leancloud.Object.extend('EnvInfo')
        env_info = EnvInfo()

        #   地理位置及运营商
        local_addr = requests.get('http://myip.ipip.net/').text[24:]
        env_info.set('local_addr', local_addr)

        #   Mac码
        env_info.set('mac', get_mac_address())

        #   星之子唯一编号
        with open('sds_id', "r", encoding='utf-8') as f:
            sds_id = f.read()
        self.sds_id = sds_id
        env_info.set('sds_id', sds_id)

        #   星之子版本
        with open('.version', 'r', encoding='utf-8') as f:
            sds_ver = f.read()
        env_info.set('sds_ver', sds_ver)

        env_info.save()
        logger.info(f"[{_MODEL_NAME}] 硬件设备上传成功")

        # Other Objects
        #   Teach
        Teach = leancloud.Object.extend('Teach')
        self.teach = Teach()
        # todo More other objects for feedback

    def teach_add(self, session: CommandSession):
        _FUN_NAME = 'teach_add'
        teach = self.teach()
        teach.set('type', 'add')
        teach.set('group', hashlib.md5(session.event.group_id).hexdigest())
        teach.set('user_id', hashlib.md5(session.event.user_id).hexdigest())
        teach.set('sds_id', self.sds_id)

        teach.save()
        logger.info(f"[{_MODEL_NAME}] Teach模块 {_FUN_NAME} 事件上传成功")

    def teach_del(self, session: CommandSession):
        _FUN_NAME = 'teach_del'
        teach = self.teach()
        teach.set('type', 'del')
        teach.set('group', hashlib.md5(session.event.group_id).hexdigest())
        teach.set('user_id', hashlib.md5(session.event.user_id).hexdigest())
        teach.set('sds_id', self.sds_id)

        teach.save()
        logger.info(f"[{_MODEL_NAME}] Teach模块 {_FUN_NAME} 事件上传成功")


feedback = FeedBack()
