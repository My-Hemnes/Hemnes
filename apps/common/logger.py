# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import sys
import time

from loguru import logger as logtool

from apps.configs.settings import LogConfig

TIME = time.strftime("%Y_%m_%d")


class LOGGER(LogConfig):

    """Logger initial"""

    def __init__(self, module=LogConfig.LOGNAME, request_id=LogConfig.LOG_REQUEST_ID, console=LogConfig.CONSOLE):
        """init logger
          These input parameters are optional:
            - name  日志输出模块名称
            - console  是否输出到终端
        """
        self.log_dir = LogConfig.LOG_DIRNAME
        self.log = logtool

        if not console:
            self.log.remove(handler_id=None)

        self.log.opt(exception=True)
        # # 终端格式初始化
        # self.log.add(
        #     sys.stderr,
        #     format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {function} | {line} | {message}",
        #     filter="", enqueue=True, level=LogConfig.LEVEL)
        # 文件格式初始化
        self.log.add(
            f"{self.log_dir}/{LogConfig.LOGNAME}_{TIME}.log",
            format=LogConfig.FORMAT % (module, request_id),
            filter="",
            encoding="utf-8",
            enqueue=False,  # 启用导致gevent异常
            level=LogConfig.LEVEL,
            rotation=LogConfig.ROTATION,
            retention=LogConfig.RETENTION)
        # 异常日志过滤转存
        self.log.add(f"{self.log_dir}/{LogConfig.ERROR_LOGNAME}_{TIME}.log",
                     format=LogConfig.FORMAT % (module, request_id),
                     filter=lambda record: "ERROR" in record['level'].name,
                     encoding="utf-8",
                     enqueue=False,
                     level=LogConfig.LEVEL,
                     rotation=LogConfig.ROTATION,
                     retention=LogConfig.RETENTION)


def logger_put(module=None, request_id=None):
    """Logger message file put"""
    if not module:
        if not request_id:
            return LOGGER().log
        return LOGGER(request_id=request_id).log
    else:
        return LOGGER(module).log
