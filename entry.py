# -*- coding: utf-8 -*-
from pandas import DataFrame
from xing.xasession import Session
import time
import pythoncom
from xing.logger import LoggerSetting
from xing.logger import Logger
LoggerSetting.FILE = "xing-plus-app.log"
log = Logger(__name__)

if __name__ == "__main__":
    try:
        session = Session()
        running = session.login("config.conf")

        # 루프가 필요함.
        while running:
            session.heartbeat()
            # @todo
            pythoncom.PumpWaitingMessages()
            time.sleep(3)
    finally:
        session.logout()
        exit()