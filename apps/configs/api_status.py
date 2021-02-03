# !/usr/bin/env python
# -*- coding=utf-8 -*-
#


class StatusCodes:

    ERROR_APP_CLIENT_EXCEPTION = dict(  # 客户端参数异常
        code="40004", message="Request arguments {} error or not found.", message_chs=u"请求参数 {} 异常或不存在。")
    ERROR_APP_BASE_EXCEPTION = dict(  # 服务异常
        code="50000", message="InternalServerError.", message_chs=u"服务器内部错误。")
    ERROR_NO_FILE_FOUND = dict(  # 文件丢失或缺失
        code="50001", message="The configuration file '{}' not found.", message_chs=u"配置文件 '{}' 不存在。")
    ERROR_FILE_READ_FAILED = dict(  # 文件读取异常
        code="50002", message="Config field read error: {}.", message_chs=u"读取 {} 配置项失败。")
    ERROR_FILE_ARGUMENT_GET_FAILED = dict(  # 文件参数获取异常
        code="50003", message="Config argument get error: {}.", message_chs=u"{} 配置参数获取失败。")
