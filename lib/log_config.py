# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-12-29 13:57:52
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-11 09:58:42

from datetime import datetime
from logging import INFO, FileHandler, Filter, Formatter, Logger, getLogger
from platform import node
from typing import Literal

from coloredlogs import install

FILE_NAME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class HostnameFilter(Filter):
    hostname = node()

    def filter(self, record) -> Literal[True]:
        record.hostname = HostnameFilter.hostname
        return True


def set_logger(name) -> Logger:
    import logging

    install(
        level="INFO",
        fmt="%(asctime)s, %(hostname)s: %(name)-8s %(levelname)-8s %(module)-16s %(message)s ",
        milliseconds=False,
    )
    logger = getLogger(name)
    logging.SUCCESS = 25
    logging.addLevelName(logging.SUCCESS, "SUCCESS")
    # setattr(logger, "success", lambda message, *args: logger._log(logging.SUCCESS, message, args))
    logger.success = lambda message, *args: logger._log(logging.SUCCESS, message, args)
    logging.NOTICE = 24
    logging.addLevelName(logging.NOTICE, "NOTICE")
    # setattr(logger, "notice", lambda message, *args: logger._log(logging.NOTICE, message, args))
    logger.notice = lambda message, *args: logger._log(logging.NOTICE, message, args)
    if not logger.handlers:
        fh = FileHandler(f"log/log_{FILE_NAME}.log", encoding="utf-8-sig")
        fh.addFilter(HostnameFilter())
        fh.setLevel(INFO)
        formatter = Formatter("%(asctime)s, %(hostname)s: %(name)-8s %(levelname)-8s %(module)-15s %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger


LOGGER = set_logger('MainTh')