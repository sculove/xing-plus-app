# -*- coding: utf-8 -*-
from pandas import DataFrame
from xing.xasession import Session
import time
import pythoncom
from xing.logger import LoggerSetting
from xing.logger import Logger
from xing.xachartdata import Chartdata

LoggerSetting.FILE = "test_xachartdata.log"
log = Logger(__name__)

if __name__ == "__main__":
    try:
        session = Session()
        running = session.login("../config.conf")
        chart = Chartdata("012510")
        chart.load({
            Chartdata.DAY : [ "20150101" ],
            Chartdata.WEEK : [ "20070101" ],
            Chartdata.MONTH : ("20100101", "20161231")
        })

        # 테스트를 위한 루프
        while running:
            session.heartbeat()
            chart.load({
                5 : ["20151202"]
            }).process({
                "SMA" : [ 5, 10, 20, 60],   # 이동평균선
                "BBANDS" : [20, 2], #볼랜져 밴드 period, 승수
                "ATR" : 14, #ATR 지표 period
                "STOCH" : [ 5, 3, 0],   #스토케스틱 K period, D period, D type
                "MACD" : [12, 26, 9],  # short, long, signal
                "RSI" : 14,  # period
            })
            _5df = chart.get(5)
            _dayDf = chart.get(Chartdata.DAY)
            _weekDf = chart.get(Chartdata.WEEK)
            _monthDf = chart.get(Chartdata.MONTH)
            print("5분 데이터 : %s ~ %s" % (_5df.iloc[0]["date"], _5df.iloc[len(_5df)-1]["date"]) )
            print("일 데이터 : %s ~ %s" % (_dayDf.iloc[0]["date"], _dayDf.iloc[len(_dayDf)-1]["date"]) )
            print("주 데이터 : %s ~ %s" % (_weekDf.iloc[0]["date"], _weekDf.iloc[len(_weekDf)-1]["date"]) )
            print("월 데이터 : %s ~ %s" % (_monthDf.iloc[0]["date"], _monthDf.iloc[len(_monthDf)-1]["date"]) )

            pythoncom.PumpWaitingMessages()
            time.sleep(1)
    finally:
        session.logout()
        exit()