# Check & Import Config
try:
    from plugins.plugins_config.core import HEWEATHER_KEY

    noConfig = False
except ImportError:
    noConfig = True

import requests
from nonebot.log import logger


def getWeather(city):
    if noConfig:
        return '未找到配置文件,详见README说明'
    if HEWEATHER_KEY is None:
        return '未配置和风天气Key,详见README说明'
    cityIdInfo = getCityId(city=city)
    cityId = cityIdInfo[0]
    cityName = cityIdInfo[1]
    URL = 'https://devapi.heweather.net/v7/weather/3d'
    payload = {
        'key': HEWEATHER_KEY,
        'location': cityId
    }
    r = requests.get(URL, params=payload)
    date = r.json()
    if date['code'] != '200':
        logger.info(f"[插件] [Weather]> 获取城市天气信息失败，原始消息：{city}")
        logger.debug(f"[插件] [Weather]> Can not get weather info, Original message:{city}")
        return "获取城市信息失败"
    msg = f"{cityName}的近三日天气为\n"
    daily_date = date['daily']
    for daily in daily_date:
        msg += f"{daily['fxDate']}:\n"
        msg += f"白天:{daily['textDay']}\n"
        msg += f"夜晚:{daily['textNight']}\n"
        msg += f"日出时间:{daily['sunrise']}\n"
        msg += f"日落时间:{daily['sunset']}\n"
        msg += f"月升时间:{daily['moonrise']}\n"
        msg += f"月落时间:{daily['moonset']}\n"
        msg += f"月相:{daily['moonPhase']}\n"
        msg += f"最高温度{daily['tempMax']}\n"
        msg += f"最低温度{daily['tempMin']}\n"
    msg += "数据由和风天气提供"
    return msg


def getCityId(city):
    URL = r'https://geoapi.heweather.net/v2/city/lookup?'
    payload = {
        'location': city,
        'key': HEWEATHER_KEY
    }
    r = requests.get(url=URL, params=payload)
    print(r.text)
    date = r.json()
    if date['code'] != '200':
        logger.info(f"[插件] [Weather]> 获取城市ID失败，原始消息：{city}")
        logger.debug(f"[插件] [Weather]> Can not get weatherId, Original message:{city}")
        return "获取城市ID错误"
    else:
        return date['location'][0]['id'], date['location'][0]['name'] + '-' + date['location'][0]['adm2'] + '-' + \
               date['location'][0]['adm1'] + '-' + date['location'][0]['country']
