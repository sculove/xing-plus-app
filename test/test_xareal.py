# -*- coding: utf-8 -*-
from pandas import DataFrame
from xing.xasession import Session
import time
import pythoncom
from xing.logger import LoggerSetting
from xing.logger import Logger
from xing.xareal import RealManager
from xing import xacom
from modules.information import Information
LoggerSetting.FILE = "test_xareal.log"
log = Logger(__name__)

if __name__ == "__main__":
    try:
        info = Information.load("../config.conf")
        session = Session()
        session.login(info["server"], info["user"])
        running = True

        # manager 등록
        manager = RealManager()
        # 장구분
        manager.addTask("JIF", ("jangubun", "jstatus"), 50).addTarget("1", "jangubun")

        # 주문 체결
        manager.addTask("SC1", ("Isuno", "Isunm", "ordno", "orgordno",
                             "eventid", "ordxctptncode", "ordmktcode",
                             "ordptncode", "mgmtbrnno",  "accno1",
                             "execno", "ordqty", "ordprc", "execqty",
                             "execprc", "ordtrxptncode", "secbalqty",
                             "avrpchsprc", "pchsant"), 50
                        ).addTarget()
        # 코스피 호가
        manager.addTask("H1_", ("shcode", "hottime","totofferrem", "totbidrem",
					"offerho1", "bidho1", "offerrem1", "bidrem1",
					"offerho2", "bidho2", "offerrem2", "bidrem2",
					"offerho3", "bidho3", "offerrem3", "bidrem3",
					"offerho4", "bidho4", "offerrem4", "bidrem4",
					"offerho5", "bidho5", "offerrem5", "bidrem5",
					"offerho6", "bidho6", "offerrem6", "bidrem6",
					"offerho7", "bidho7", "offerrem7", "bidrem7",
					"offerho8", "bidho8", "offerrem8", "bidrem8",
					"offerho9", "bidho9", "offerrem9", "bidrem9",
					"offerho10", "bidho10", "offerrem10", "bidrem10"
				), 100).addTarget(["122630", "114800", "204480"])

        # 코스닥 호가
        manager.addTask("HA_", ("shcode", "hottime","totofferrem", "totbidrem",
					"offerho1", "bidho1", "offerrem1", "bidrem1",
					"offerho2", "bidho2", "offerrem2", "bidrem2",
					"offerho3", "bidho3", "offerrem3", "bidrem3",
					"offerho4", "bidho4", "offerrem4", "bidrem4",
					"offerho5", "bidho5", "offerrem5", "bidrem5",
					"offerho6", "bidho6", "offerrem6", "bidrem6",
					"offerho7", "bidho7", "offerrem7", "bidrem7",
					"offerho8", "bidho8", "offerrem8", "bidrem8",
					"offerho9", "bidho9", "offerrem9", "bidrem9",
					"offerho10", "bidho10", "offerrem10", "bidrem10"
				), 100).addTarget("168330")

        # XARealManager 콜백함수
        def callback(type, data):
            print("[%s] Real 데이터 - %s" % (type, xacom.parseTR(type)) )
            for i in range(len(data)):
                if type == "SC1":
                    print(data[i]["Isunm"])
                elif type == "JIF":
                    print(data[i]["jangubun"], data[i]["jstatus"])
                else:   #H1_, HA_
                    ht = data[i]
                    print("[%s] %s" % (ht["shcode"], ht["hottime"]))
                    print("-------------- + ------- + --------------")
                    print("   매도잔량    |   가격  |   매수잔량")
                    print("-------------- + ------- + --------------")
                    print("%12s | %7s |               " % (ht["offerrem10"],ht["offerho10"]))
                    print("%12s | %7s |               " % (ht["offerrem9"],ht["offerho9"]))
                    print("%12s | %7s |               " % (ht["offerrem8"],ht["offerho8"]))
                    print("%12s | %7s |               " % (ht["offerrem7"],ht["offerho7"]))
                    print("%12s | %7s |               " % (ht["offerrem6"],ht["offerho6"]))
                    print("%12s | %7s |               " % (ht["offerrem5"],ht["offerho5"]))
                    print("%12s | %7s |               " % (ht["offerrem4"],ht["offerho4"]))
                    print("%12s | %7s |               " % (ht["offerrem3"],ht["offerho3"]))
                    print("%12s | %7s |               " % (ht["offerrem2"],ht["offerho2"]))
                    print("%12s | %7s |               " % (ht["offerrem1"],ht["offerho1"]))
                    print("-------------- + ------- + --------------")
                    print("               | %7s |%12s" % (ht["bidho1"],ht["bidrem1"]))
                    print("               | %7s |%12s" % (ht["bidho2"],ht["bidrem2"]))
                    print("               | %7s |%12s" % (ht["bidho3"],ht["bidrem3"]))
                    print("               | %7s |%12s" % (ht["bidho4"],ht["bidrem4"]))
                    print("               | %7s |%12s" % (ht["bidho5"],ht["bidrem5"]))
                    print("               | %7s |%12s" % (ht["bidho6"],ht["bidrem6"]))
                    print("               | %7s |%12s" % (ht["bidho7"],ht["bidrem7"]))
                    print("               | %7s |%12s" % (ht["bidho8"],ht["bidrem8"]))
                    print("               | %7s |%12s" % (ht["bidho9"],ht["bidrem9"]))
                    print("               | %7s |%12s" % (ht["bidho10"],ht["bidrem10"]))
                    print("-------------- + ------- + --------------")
                    print("%14s | 총 잔량 |%14s " % (ht["totofferrem"],ht["totbidrem"]))

        manager.run(callback)

        # 루프가 필요함.
        while running:
            session.heartbeat()
            pythoncom.PumpWaitingMessages()
            time.sleep(3)
    finally:
        session.logout()
        exit()