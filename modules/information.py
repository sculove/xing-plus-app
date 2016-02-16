# -*- coding: utf-8 -*-
import os
import configparser

class Information:
    @staticmethod
    def load(configfile):
        if os.path.isfile(configfile):
            config = configparser.ConfigParser()
            config.read(configfile)
            server = {
                "address": config.get("SERVER", "address"),
                "port": config.get("SERVER", "port")
            }
            user = {
                "id": config.get("USER", "id"),
                "passwd": config.get("USER", "passwd"),
                "account_passwd": config.get("USER", "account_passwd"),
                "certificate_passwd": config.get("USER", "certificate_passwd")
            }
        else:
            server = {
                "address": input("접속할 서버(hts.ebestsec.co.kr)가 맞나요?[y:엔터] :"),
                "port": input("접속할 서버 포트(20001)가 맞나요?[y:엔터] :")
            }
            user = {
                "id": input("계정(id)을 입력해주세요 > "),
                "passwd": input("계정 암호(passwd)를 입력해주세요 > "),
                "account_passwd": input("계좌 암호(account_passwd)를 입력해주세요 > "),
                "certificate_passwd": input("인증서 암호(account_passwd)를 입력해주세요 > ")
            }
        # @todo y/Y/엔터 인경우 처리 필요.
        server["address"] = server["address"] or "hts.ebestsec.co.kr"
        server["port"] = server["port"] or 20001
        server["type"] = 0

        return {
            "server": server,
            "user": user
        }
