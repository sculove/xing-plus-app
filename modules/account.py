# -*- coding: utf-8 -*-
from pandas.core.frame import DataFrame
from xing.logger import Logger
from xing.xaquery import Query
log = Logger(__name__)

class AccountManager:
    ALL = 0
    SING = 1
    OUTSTANDING = 2
    BUY = 2
    SELL = 1
    def __init__(self, acc, passwd):
        self._acc = acc
        self._passwd = passwd
    
    # 잔고 조회
    def blance(self):
        return Query("t0424").request({
            "InBlock" : {
                "accno" : self._acc,
                "passwd" : self._passwd
            }
        },{
            "OutBlock" : ("sunamt","dtsunik","mamt","sunamt1","tappamt", "tdtsunik"),
            "OutBlock1" : DataFrame(columns=("expcode", "janqty","janqty",
                                             "mdposqt", "pamt", "mamt",
                                             "hname", "marketgb", "jonggb",
                                             "janrt","price","appamt",
                                             "dtsunik","sunikrt","fee","tax","janrt"))
        });
        
    # 체결, 미체결 내역 조회        
    def orders(self, gubun = ALL):
        return Query("t0425").request({
                "InBlock" : {
                    "accno" : self._acc,
                    "passwd" : self._passwd,
                    "chegb" : gubun #전체0, 체결 1, 미체결 2
                }
            }, {
                "OutBlock1" : DataFrame(columns=("ordno", "expcode", "medosu", 
                                                 "qty", "price", "cheqty", "cheprice", "ordrem",
                                                 "status","ordtime","ordermtd",
                                                 "price1", "orggb", "singb"))
        });

    # 예수금 조회
    def deposit(self):
        return Query("CSPAQ12200").request({
                "InBlock1" : {
                    "RecCnt" : 1,
                    "AcntNo" : self._acc,
                    "Pwd" : self._passwd,
                    "BalCreTp" : "0" #잔고생성구분: 0-주식잔고
                }
            }, {
                "OutBlock2" : ("AcntNm","MnyOrdAbleAmt","RcvblAmt",
                               "Dps","D1Dps","D2Dps","MnyrclAmt"),
        });
        
    # 주문하기 
    def trade(self, shcode, type, count, price):
        return Query("CSPAT00600").request({
                "InBlock1" : {
                    "AcntNo" : self._acc,
                    "InptPwd" : self._passwd,
                    "BnsTpCode" : type,  # 1:매도, 2:매수
                    "IsuNo" : shcode,
                    "OrdQty" : count,
                    "OrdPrc" : price,
                    "MgntrnCode" : "0000", # 신용거래코드:0000-보통
                    "LoanDt" : " ",   # 신용거래가 아닐 경우 space
                    "OrdCndiTpCode" : "0", # 주문조건구분 : 0-없음
                    "OrdprcPtnCode" : "00" # 호가유형코드: 00-지정가, 05-조건부지정가, 06-최유리지정가, 07-최우선지정가
                }
            }, {
                "OutBlock1" : ("RecCnt","MgntrnCode", "LoanDt"),
                "OutBlock2" : ("OrdNo","SpareOrdNo", "OrdTime","OrdMktCode",
                               "OrdPtnCode","ShtnIsuNo","OrdAmt")                    
        });