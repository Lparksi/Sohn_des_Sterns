import sys
import time


class logger:
    def __init__(self):
        t = time.localtime()

        self.log_file = sys.path[0] + f'/logs/{t.tm_year}-{t.tm_mon}-{t.tm_mday}-{t.tm_hour}-{t.tm_min}-{t.tm_sec}.log'
        self.bot_name = "Sohn des Sterns"

    def _saveLog(self, log):
        with open(self.log_file, "w+") as f:
            f.write(log)

    def info(self, msg):
        message = f"[{time.ctime()}] [{self.bot_name}] INFO: {msg}\n"
        self._saveLog(message)

    def debug(self, msg):
        message = f"[{time.ctime()}] [{self.bot_name}] DEBUG: {msg}\n"
        self._saveLog(message)

    def wrong(self, msg):
        message = f"[{time.ctime()}] [{self.bot_name}] WRONG: {msg}\n"
        self._saveLog(message)

    def error(self, msg):
        message = f"[{time.ctime()}] [{self.bot_name}] ERROR: {msg}\n"
        self._saveLog(message)


logger = logger()
