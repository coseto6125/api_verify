# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 12:39:39
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-02 09:51:15
from contextlib import suppress
from hashlib import md5
from os.path import isfile

from aiohttp import ClientSession
from aiohttp_retry import ExponentialRetry, RetryClient

from lib.local_redis import BACKEND_CONFIG


class AioConnection:

    def __init__(self, platform) -> None:
        # with open(f"sw_{platform}.json", "rb") as f:
        #     self.parse_money = loads(f.read())
        self.is_session_tmp = False
        self.platform = platform
        self.cookies = None
        self.url = BACKEND_CONFIG[platform]["url"]
        self.pl_info = BACKEND_CONFIG[platform]

    def session(self) -> RetryClient:
        retry_options = ExponentialRetry(attempts=50)
        client_session = ClientSession(base_url=self.url)
        if isfile(session_file := f".temp/{self.platform}/session_aio.tmp"):
            self.is_session_tmp = True
            client_session.cookie_jar.load(session_file)
        return RetryClient(
            client_session=client_session,
            raise_for_status=False,
            retry_options=retry_options,
        )

    async def _login(self) -> tuple[str, str] | None:
        if self.is_session_tmp and self.cookies:
            return
        LOGIN_URL, LOGIN_URL2 = "/default", "/login"
        NAME = self.pl_info["acc"]
        PASSWORD = md5(self.pl_info["pw"].encode("utf-8")).hexdigest()
        async with self.session() as session:
            async with session.get(LOGIN_URL) as resp:
                result = await resp.text()
                self.cookies = resp.cookies
            csrf_token = result[result.find('{"CSRF-Token": ') + 16 : result.find('{"CSRF-Token": ') + 52]
            if "<html>" in csrf_token:
                csrf_token = result[result.find("var csrf = '") + 12 : result.find("var csrf = '") + 48]
            payload = {
                "name": NAME,
                "password": PASSWORD,
                "validateCode": "",
                "count": "0",
                "isStrongPassword": "true",
                "isPwdOutdated": "true",
            }
            if "html" not in csrf_token:
                payload["_csrf"] = csrf_token
            # if "html" in csrf_token:
            #     with suppress(IndexError):
            #         headers = literal_eval(findall("headers: ({ \"CSRF-Token\": '.*' })", result)[0])
            async with session.post(LOGIN_URL2, cookies=resp.cookies, data=payload) as rep:
                resp2 = await rep.text()
                if '{"code":0' not in resp2:
                    print(resp2)
                    raise ConnectionError(resp2)
                a = "; ".join(f"{v.value}" for k, v in resp.cookies.items())

                # session._client.cookie_jar.save(f".temp/{self.platform}/session_aio.tmp")
                # register(self._last_work)

            with suppress(Exception):
                async with session.post("/2fa/status") as fa:
                    await fa.text()
            # url = '/winAndLoseReport/InitData?beginDate=&endDate=&kindId=&accounts=&serverId=&limit=20&offset=0&total=0&GameUserNO=&RoomType=&_=1674103582922'
            # async with session.get(url,cookies=resp.cookies,) as rep:
            #     resp2 = await rep.text()
            # async with session.get("/default") as r2:
            #     await r2.text()
            #     a = r2.cookies['connect.sid'].value
            # async with session.get("/CheckLogin") as r2:
            #     await r2.text()
            #     b = next(i[1] for i in r2.raw_headers if i[0] == b'Set-Cookie').decode("utf-8")
        with suppress(Exception):
            await session.close()
        return a


# if __name__ == '__main__':
#     m = asyncio.run(AioConnection('YL')._login())
#     print(m)
