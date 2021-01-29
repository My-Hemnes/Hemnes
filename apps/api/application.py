# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""Define application for API."""

from flask import Flask
from flask_cors import CORS

from apps.configs.settings import APIConfig
from apps.configs.constants import AppsConf, CorsConf
from apps.exts import app_ext_register
from apps.api.views import register_blueprint


def create_app_instance():
    """Create Flask application object."""
    app = Flask(AppsConf.DEFAULT_SERVICE_NAME)
    # api init
    api = APIConfig()
    app.config.from_object(api)
    # app ext init
    app_ext_register(app)
    # 蓝图
    register_blueprint(app, api.BASE_PATH)
    # 跨域
    if api.API_CORS:
        CORS(app,
             resources=CorsConf.CORS_RESOURCES,
             expose_headers=CorsConf.CORS_HEADERS,
             max_age=CorsConf.CORS_MAX_AGE,
             send_wildcard=True)
    # # 中间件
    # register_middleware(app=app)
    return app


app = create_app_instance()
