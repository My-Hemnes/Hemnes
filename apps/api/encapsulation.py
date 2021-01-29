# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import traceback
try:
    from collections.abc import MutableSequence
except ImportError:
    from collections import MutableSequence
from flask import make_response, g
from flask import request, jsonify
from flask_restful import Resource, Api
from functools import wraps
from apps.common.logger import logger_put
from apps.api.custom_restful import CustomReqparse
from apps.utils.common_utils import get_gmttime, gen_uuid
from apps.errors.base_error import AppBaseException


APILOG = logger_put()
parser = CustomReqparse()  # 创建RequestParser实例


class DefaultApiResponse:
    # Default api response
    HEADERS = {
        "Date": get_gmttime(),
        "Content-Type": "application/json; charset=utf-8"
    }


def api_standard_response_handler(code, data, new_headers=None):
    """Define handle for standard response."""
    headers = DefaultApiResponse.HEADERS
    headers.update(new_headers if new_headers else dict())
    if isinstance(data, dict) or isinstance(data, list):
        headers["ResponseID"] = g.request_id or ""
        return make_response(jsonify(data), code, headers)
    else:
        headers["Content-Type"] = "application/octet-stream"
        return make_response(data, code, headers)


def api_info_verify_handler(func):
    """Define wrap for verify API info whether if valid."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Verify whether if API info valid."""
        g.request_id = request.headers.get("RequestID", gen_uuid())
        APILOG = logger_put(request_id=g.request_id)
        return func(*args, **kwargs)

    return wrapper


class CustomApi(Api):
    """Custom flask-restful api"""

    # 自定义异常处理
    def handle_error(self, error):
        headers = DefaultApiResponse.HEADERS
        headers["ResponseID"] = g.request_id or ""
        if hasattr(error, "__dict__"):
            response = error.__dict__()
        else:
            response = AppBaseException().__dict__()
        APILOG.error("Hemnes api ERROR: %s" % response)
        APILOG.error("Hemnes api TRACEBACK: %s" % traceback.format_exc())
        return make_response(jsonify(response), 500, headers)


class APIMethodUnauthView(Resource):

    """Define request functions without authorize for HTTP RESTful API."""
    decorators = (api_info_verify_handler,)


class APIMethodView(Resource):

    """Define request functions without authorize for HTTP RESTful API."""
    decorators = (api_info_verify_handler,)
