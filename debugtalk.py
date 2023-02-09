# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-19 09:49:28
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-09 16:51:16
import asyncio
import logging
from os.path import isfile

from loguru import logger

from lib.basic_aiohttp import AioConnection
from lib.local_redis import redis_get, redis_set

# # commented out function will be filtered
# # def get_headers():
# #     return {"User-Agent": "hrp"}


# platform = "YL"
@logger.catch
def get_backend_info(platform: str) -> 1:
    file_path = f'.temp/{platform}_acc.tmp'
    if isfile(file_path):
        return 0
    session = asyncio.run(AioConnection(platform)._login())
    with open(file_path,'w',encoding='utf8') as f:
        f.write(session)
    return 1

@logger.catch
def get_tt_backend_info(platform: str) -> 1:
    file_path = f'.temp/{platform}_acc.tmp'
    if isfile(file_path):
        return 'ok'
    session = asyncio.run(AioConnection(platform)._login_tt())
    with open(file_path,'w',encoding='utf8') as f:
        f.write(f'{session}')
    return 1


@logger.catch
def get_connect_sid(platform: str) -> str:
    file_path = f'.temp/{platform}_acc.tmp'
    with open(file_path,'r',encoding='utf8') as f:
        return f.read()

@logger.catch
def get_headers_cookie(platform: str) -> str:
    return '1'

@logger.catch
def setup_hook_example(name) -> str:
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"

@logger.catch
def teardown_hook_example(name) -> str:
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"
