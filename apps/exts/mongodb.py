# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from flask_mongoengine import MongoEngine
from apps.configs.settings import MongoConfig

mongo_config = {"MONGODB_SETTINGS": MongoConfig.MONGODB_SETTINGS}

db = MongoEngine(config=mongo_config)
