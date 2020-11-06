import sys
import datetime
import time as time

date = datetime.date.today()
path = sys.path[0] + r"/logs/" + f"{date.year}_{date.month}_{date.day}.log"


def save(text: str):
    with open(path, "a+") as f:
        localtime = time.asctime(time.localtime(time.time()))
        log = f'[{date.year}-{date.month}-{date.day} {localtime}]' + text + '\n'
        f.write(log)
