# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from apps.configs.constants import AppsConf
from apps.utils.common_utils import gen_uuid
from apps.utils.configs_utils import (get_api_conf, get_log_conf, get_jobpool_conf, get_mongodb_conf)


class BaseConfig:

    """Base apps config"""
    DEBUG = False
    TESTING = False
    HOST = AppsConf.API_DEFAULT_HOST
    PORT = AppsConf.API_DEFAULT_PORT
    BASE_PATH = AppsConf.API_DEFAULT_URL
    API_CORS = False
    JSON_AS_ASCII = False  # 支持中文显示
    # JSONIFY_MIMETYPE = "application/json; charset=utf-8"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(DevelopmentConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


class JobConfig:

    """Apps job config"""
    jobpool_conf = get_jobpool_conf()
    CHACHE_DIRNAME = jobpool_conf.get("cache_dir", "/".join([AppsConf.APPS_HOME, "cache_dir"]))
    LOG_DIRNAME = jobpool_conf.get("log_dir", "/".join([AppsConf.APPS_HOME, "log_dir"]))
    WORKER_DIRNAME = jobpool_conf.get("worker_dir", "/".join([AppsConf.APPS_HOME, "worker_dir"]))
    STORE_DIRNAME = jobpool_conf.get("store_dir", "/".join([AppsConf.APPS_HOME, "store_dir"]))


class APIConfig(BaseConfig, JobConfig):

    """Apps api config"""
    api_conf = get_api_conf()
    if "host" in api_conf:
        HOST = api_conf.get("host")
    if "port" in api_conf:
        PORT = api_conf.get("port")
    if api_conf.get("base_path"):
        BASE_PATH = "".join([BaseConfig.BASE_PATH, api_conf.get("base_path"), "/"])
    if "api_cors" in api_conf:
        API_CORS = api_conf.get("api_cors")


class LogConfig(JobConfig):

    """Apps log config"""
    log_conf = get_log_conf()
    LOGNAME = "hemnes"
    LOG_REQUEST_ID = gen_uuid()
    ERROR_LOGNAME = "hemnes_error"
    LEVEL = "DEBUG"
    CONSOLE = True
    if "format" in log_conf:
        FORMAT = log_conf.get("format")
    if "level" in log_conf:
        LEVEL = log_conf.get("level")
    if "console" in log_conf:
        CONSOLE = log_conf.get("console")
    if "rotation" in log_conf:
        ROTATION = log_conf.get("rotation")
    if "retention" in log_conf:
        RETENTION = log_conf.get("retention")


class MongoConfig(AppsConf):

    """Apps mongodb config"""
    mongo_conf = get_mongodb_conf()
    MONGODB_SETTINGS = dict()
    MONGODB_SETTINGS["db"] = mongo_conf.get("db", "test")
    MONGODB_SETTINGS["host"] = mongo_conf.get("host", "mongodb://127.0.0.1:27017/")
    MONGODB_SETTINGS["minpoolsize"] = mongo_conf.get("minpoolsize", 30)
    MONGODB_SETTINGS["maxpoolsize"] = mongo_conf.get("maxpoolsize", 60)
    MONGODB_SETTINGS["alias"] = mongo_conf.get("alias", AppsConf.DEFAULT_SERVICE_NAME)
    MONGODB_SETTINGS["tz_aware"] = mongo_conf.get("tz_aware", False)
    MONGODB_SETTINGS["connect"] = mongo_conf.get("connect", False)
    # default authentication
    if "username" in mongo_conf:
        MONGODB_SETTINGS["username"] = mongo_conf.get("username")
    if "password" in mongo_conf:
        MONGODB_SETTINGS["password"] = mongo_conf.get("password")
    if "authentication_source" in mongo_conf:
        MONGODB_SETTINGS["authentication_source"] = mongo_conf.get("authentication_source")
    if "replicaset" in mongo_conf:
        MONGODB_SETTINGS["replicaset"] = mongo_conf.get("replicaset")
    if "is_mock" in mongo_conf:
        MONGODB_SETTINGS["is_mock"] = mongo_conf.get("is_mock")
