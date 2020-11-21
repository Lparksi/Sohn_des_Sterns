import leancloud
from plugins.feedback.core.get import get_ip, get_mac_address
from time import time
import platform


# todo 对于每项功能的独立计数


def upload():
    leancloud.init(app_id="CDhsl3xYSgOtBsa7h4FRi95J-MdYXbMMI",
                   app_key="9kSvJ9zY34bH1RY7oMbgCb7B")

    EnvInfo = leancloud.Object.extend('EnvInfo')
    env_info = EnvInfo()

    # 运行环境信息
    env_info.set('ip', get_ip())
    env_info.set('mac', get_mac_address())
    env_info.set('time', time())
    env_info.set('python_version', platform.python_version())
    env_info.set('architecture', platform.architecture()[0])
    env_info.set('os', platform.platform())
    env_info.set('full_info', platform.uname())

    env_info.save()
