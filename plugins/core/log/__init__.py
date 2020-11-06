from nonebot.log import logger as logger
from plugins.core.log.errer import LogLevelError
from plugins.core.log.saveLog import save as savelog


def info(log, save: bool, module):
    msg = f"[{module}] {log}"
    logger.info(msg=msg)
    if save:
        savelog(msg)


def warning(log, save: bool, module):
    msg = f"[{module}] {log}"
    logger.warning(msg=msg)
    if save:
        savelog(msg)


def debug(log, save: bool, module):
    msg = f"[{module}] {log}"
    logger.debug(msg=msg)
    if save:
        savelog(msg)


def error(log, save: bool, module):
    msg = f"[{module}] {log}"
    logger.error(msg=msg)
    if save:
        savelog(msg)
