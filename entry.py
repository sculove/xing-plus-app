# -*- coding: utf-8 -*-
from pandas import DataFrame
from xing.xasession import Session
import time
import pythoncom
from xing.logger import LoggerSetting
from xing.logger import Logger
from modules.information import Information
LoggerSetting.FILE = "xing-plus-app.log"
log = Logger(__name__)

if __name__ == "__main__":
    try:
        info = Information.load("config.conf");
        session = Session()
        session.login(info["server"], info["user"])
        running = True

        # 루프가 필요함.
        while running:
            session.heartbeat()
            # @todo
            pythoncom.PumpWaitingMessages()
            time.sleep(3)
    finally:
        session.logout()
        exit()