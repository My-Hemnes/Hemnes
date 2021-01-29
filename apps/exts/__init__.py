# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from apps.exts.mongodb import db, mongo_config
from apps.exts.schema import ma


def app_ext_register(app):
    """Application init mongoEngine"""
    # mongodb config
    db.init_app(app, config=mongo_config)
    ma.init_app(app)
