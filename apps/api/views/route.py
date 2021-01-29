# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from apps.api.views import echo


class AppsUrlsRegister:

    """Apps urls register"""
    ECHO = (dict(interface=echo.EchoHelloView, uri="/hello/<string:username>"), )

    API_INTERFACE = dict(echo=ECHO)

    def __init__(self, module_name, api):
        for route_url in self.API_INTERFACE.get(module_name):
            api.add_resource(route_url.get("interface"), route_url.get("uri"))
