# -*- coding: utf-8 -*-
from pandas import DataFrame
from xing.xasession import Session
import time
import pythoncom
from xing.logger import LoggerSetting
from xing.logger import Logger
from xing.xaquery import Query

LoggerSetting.FILE = "test_xaquery.log"
log = Logger(__name__)

if __name__ == "__main__":
    try:
        session = Session()
        running = session.login("../config.conf")

        # 테스트를 위한 루프
        while running:
            session.heartbeat()
            xadata = Query("t1101").request({
                "InBlock" : {
                    "shcode" : "122630"
                },
            }, {
                "OutBlock" : ("hname","price", "sign", "change", "diff", "volume", "jnilclose",
                    "offerho1", "bidho1", "offerrem1", "bidrem1", "preoffercha1","prebidcha1",
                    "offerho2", "bidho2", "offerrem2", "bidrem2", "preoffercha2","prebidcha2",
                    "offerho3", "bidho3", "offerrem3", "bidrem3", "preoffercha3","prebidcha3",
                    "offerho4", "bidho4", "offerrem4", "bidrem4", "preoffercha4","prebidcha4",
                    "offerho5", "bidho5", "offerrem5", "bidrem5", "preoffercha5","prebidcha5",
                    "offerho6", "bidho6", "offerrem6", "bidrem6", "preoffercha6","prebidcha6",
                    "offerho7", "bidho7", "offerrem7", "bidrem7", "preoffercha7","prebidcha7",
                    "offerho8", "bidho8", "offerrem8", "bidrem8", "preoffercha8","prebidcha8",
                    "offerho9", "bidho9", "offerrem9", "bidrem9", "preoffercha9","prebidcha9",
                    "offerho10", "bidho10", "offerrem10", "bidrem10", "preoffercha10","prebidcha10",
                    "offer", "bid", "preoffercha", "prebidcha", "uplmtprice", "dnlmtprice", "open", "high", "low", "ho_status", "hotime",
                    "shcode", "hottime", "totofferrem", "totbidrem"
                    )
            })
            ht=xadata["OutBlock"]
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

            pythoncom.PumpWaitingMessages()
            time.sleep(3)
    finally:
        session.logout()
        exit()