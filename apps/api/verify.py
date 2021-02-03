# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""
:param name: - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo
:param location: request指定从哪里获取参数; json, args, form
:param default: 默认值，若没有传入此次参数，则使用此默认值
:param type: 入参被转换的格式; 提供url，正则，natural 自然数，positive 正整数， int_range(low, high) 整数范围，boolean
:param choices: 参数可允许的值的一个容器
:param required: 可选参数是否可以省略
:param help: 参数检验错误时返回的错误描述信息
:param action: 描述对于请求参数中出现多个同名参数时的处理方式 ;
  action='store' 保留出现的第一个，默认|action="append" 以列表追加保存所有同名参数的值
:param trim：是否去掉前后空格

"""
from flask_restful import fields
from apps.errors.base_error import AppClientError


def echo_args_parser(cls):
    cls.add_argument("password", location='json', type=str, required=True, help=AppClientError)
    cls.add_argument("task_ids", location='json', type=list, required=True, help=AppClientError)
    cls.add_argument("atime", location='json', type=int, required=True, help=AppClientError)
    cls.add_argument("pay_number", location='json', type=float, required=True, help=AppClientError)


def echo_args_filed(**kwargs):
    resource_fields = {
        "pay_number": fields.Float,
        "follow_id": fields.String(attribute="assn_follow_id"),  # 以新的字段名 ‘follow_id’ 返回
        "age": fields.Integer(default=18),  # 未定义时的默认值
        "task_ids": fields.List(fields.String),
        "more": fields.Nested({"signature": fields.String})
    }
    return resource_fields
