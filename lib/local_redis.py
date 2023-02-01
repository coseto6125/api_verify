# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-12-19 16:05:21
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-02-01 17:52:33
from functools import lru_cache
from platform import uname

from orjson import JSONDecodeError, loads
from redis import ConnectionPool, Redis

try:
    from tomllib import TOMLDecodeError
    from tomllib import loads as tomlLoads
except ImportError:
    from tomli import TOMLDecodeError
    from tomli import loads as tomlLoads


def _parse(data, raw=False):
    """
    > 如果数据是有效的 JSON，则返回解析后的 JSON。
    > 如果数据是有效的 TOML，则返回解析的 TOML。
    > 如果数据既不是有效的 JSON 也不是有效的 TOML，则引发错误

    Args:
      data: 要解析的数据。

    Returns:
      Dict[str:Any]
    """
    if raw:
        return data
    try:
        return loads(data)
    except JSONDecodeError:
        try:
            return tomlLoads(data)
        except TOMLDecodeError as e:
            raise TOMLDecodeError("解析失敗，請確認格式符合json或toml") from e


data = {"host": "192.168.17.71", "port": 6379, "db": 1, "password": "qatest666", "decode_responses": True}


def local_redis() -> ConnectionPool:
    return ConnectionPool(**data)


def redis_set(key, value, timedelta=None):
    with Redis(**data) as r:
        return r.set(key, value, timedelta)


@lru_cache(maxsize=128)
def redis_get(key, raw=False):
    with Redis(**data) as r:
        return r.get(key) if raw else _parse(r.get(key))


def redis_mget_all(key_list):  #
    with Redis(**data) as r:
        return [_parse(i) for i in r.mget(key_list)]


def redis_mset_all(key_list):  #
    with Redis(**data) as r:
        return r.mset(key_list)


GAME_CONFIG, BACKEND_CONFIG, DEVICE_CONFIG = redis_mget_all(["game_setting", "backend_config", "device_config"])
# IS_DEV = uname().node in DEVICE_CONFIG["development"]["device_name"]
# HTTP_HEADER = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# }
