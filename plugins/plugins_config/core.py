import json

with open('pluginsConfig.json') as f:
    plugins_config = dict(json.loads(f.read()))

SdS_Version = plugins_config["SdS_Version"]
pre_release = plugins_config["pre_release"]

GROUPS = plugins_config["GROUPS"]

HEWEATHER_KEY = plugins_config["HEWEATHER_KEY"]
TENCENT_AI_APP_ID = plugins_config["TENCENT_AI_APP_ID"]
TENCENT_AI_APP_KEY = plugins_config["TENCENT_AI_APP_KEY"]

MONGODB_URL = plugins_config["MONGODB_URL"]
MONGODB_SHOW_URL = plugins_config["SHOW_URL"]

Feedback = plugins_config["Feedback"]


def get(key):
    return plugins_config.get(key)
