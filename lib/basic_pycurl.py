# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-03-15 17:39:24
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-19 12:42:08
import sys

sys.path.append("C:\Python311\Scripts")
sys.path.append("C:\Python311\lib\site-packages")
import logging
from contextlib import suppress
from hashlib import md5
from re import findall
from urllib.parse import urlencode

from dotenv import dotenv_values
from pycurl import Curl


class BackendSession:

    def __init__(self, platform) -> None:
        self.platform = platform
        self.C = self.set_curl()
        self.pl_info = dotenv_values(".env")
        self.url = self.pl_info["base_url"][:-1]
        # self._close = self.C.close

    def set_curl(self) -> Curl:
        C = Curl()
        C.setopt(C.TIMEOUT, 60)
        C.setopt(C.CONNECTTIMEOUT, 0)
        C.setopt(C.COOKIEFILE, f"session.tmp")
        C.setopt(C.COOKIEJAR, f"session.tmp")
        C.setopt(C.FOLLOWLOCATION, True)
        C.setopt(C.SSL_VERIFYPEER, 0)
        C.setopt(C.SSL_VERIFYHOST, 0)
        # C.setopt(C.CAINFO, where())
        C.setopt(C.VERBOSE, 0)
        C.setopt(C.IPRESOLVE, C.IPRESOLVE_V4)
        C.setopt(
            C.HTTPHEADER,
            [
                "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
            ],
        )
        C.setopt(C.HEADERFUNCTION, self._header_function)
        self.headers = {}
        return C

    def login(self) -> Curl | str:
        self.C.setopt(self.C.URL, f"{self.url}/default")
        result = self.C.perform_rs()
        csrf_token = result[result.find('{"CSRF-Token": ') + 16 : result.find('{"CSRF-Token": ') + 52]
        if "<html>" in csrf_token or len(csrf_token) < 10:
            csrf_token = result[result.find("var csrf = '") + 12 : result.find("var csrf = '") + 48]
        if "开发商后台" in result:
            return self.C
        if "html" in csrf_token:
            with suppress(Exception):
                csrf_token = findall("headers: { \"CSRF-Token\": '(.*)' }", result)[0]
        headers = [f"CSRF-Token: {csrf_token}"]
        payload = urlencode({
            "name": self.pl_info["USERNAME"],
            "password": md5(self.pl_info["PASSWORD"].encode("utf-8")).hexdigest(),
            "validateCode": "",
            "count": "0",
            "isStrongPassword": "true",
            "isPwdOutdated": "true",
        })

        if "html" not in csrf_token and "<head>" not in csrf_token:
            self.C.setopt(self.C.HTTPHEADER, headers)
        self.C.setopt(self.C.POSTFIELDS, payload)
        self.C.setopt(self.C.URL, f"{self.url}/login")
        resp = self.C.perform_rs()
        if self.platform not in {"BY", "YL"}:
            self.C.setopt(self.C.URL, f"{self.url}/2fa/status")
            self.C.perform()
        assert '"code":0' in resp , '平台入口登入'
        self.C.setopt(self.C.URL, f"{self.url}/default")
        self.C.perform()
        self.headers
        return self.headers
    
    def _header_function(self,header_line):
        header_line = header_line.decode('iso-8859-1')
        if ':' not in header_line:
            return

        name, value = header_line.split(':', 1)
        name = name.strip()
        value = value.strip()
        name = name.lower()
        self.headers[name] = value