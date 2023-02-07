# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 09:49:28
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-02 10:00:25
import asyncio
import logging
from loguru import logger

from lib.basic_aiohttp import AioConnection
from lib.local_redis import redis_get, redis_set

# # commented out function will be filtered
# # def get_headers():
# #     return {"User-Agent": "hrp"}


# platform = "YL"
@logger.catch
def get_backend_info(platform: str) -> 1:
    if redis_get(f"{platform}_connect_sid", True) is not None:
        return 0
    session = asyncio.run(AioConnection(platform)._login())
    redis_set(f"{platform}_connect_sid", session,600000)
    return 1

@logger.catch
def get_connect_sid(platform: str) -> str:
    return redis_get(f"{platform}_connect_sid", True)

@logger.catch
def get_headers_cookie(platform: str) -> str:
    return redis_get(f"{platform}_headers_cookie", True)

@logger.catch
def setup_hook_example(name) -> str:
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"

@logger.catch
def teardown_hook_example(name) -> str:
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"
