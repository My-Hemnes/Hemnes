# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import json
from flask import request
from flask_restful import marshal_with
from apps.api.encapsulation import APILOG, parser
from apps.api.encapsulation import APIMethodUnauthView, api_standard_response_handler
from apps.api.verify import echo_args_parser, echo_args_filed


# 测试接口
class EchoHelloView(APIMethodUnauthView):

    """Define HTTP method for hello world."""

    def get(self, username):
        """GET hello world."""
        APILOG.debug("GET hello world for %s request" % username)
        response = {"echo": "Hi, %s, welcome to hemnes" % username, "method": "GET"}
        APILOG.info("GET hello world for %s succeed" % username)
        return api_standard_response_handler(200, response)

    def post(self, username):
        """POST hello world."""
        # 定义当前接口参数格式
        echo_args_parser(parser)
        data = parser.parse_args()
        APILOG.debug("POST hello world for %s request" % username)
        response = {"data": data, "method": "POST"}
        APILOG.info("POST hello world for %s succeed" % username)
        return api_standard_response_handler(201, response)
