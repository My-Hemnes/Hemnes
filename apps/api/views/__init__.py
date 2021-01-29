# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from flask import Blueprint
from apps.configs.constants import Register
from apps.api.views.route import AppsUrlsRegister
from apps.api.encapsulation import CustomApi


def register_blueprint(app, base_path):
    """Register Flask blueprint."""
    for module in Register.BLUEPRINTS:
        # 蓝图及接口路由注册
        blue_module = Blueprint(module, __name__)
        api = CustomApi(blue_module)
        AppsUrlsRegister(module, api)
        app.register_blueprint(blue_module, url_prefix="".join((base_path, module)))
