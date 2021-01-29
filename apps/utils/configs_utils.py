# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os

import yaml

from apps.common.consul import consul
from apps.configs.constants import ConsulConf
from apps.errors.base_error import NoFileFound, FileReadFailed, FileArgsGetFailed


class Configuration(object):

    """Initial the config file and parser sections."""

    def __init__(self, filename=None):
        """Set initial parameters.

        The parameter `filename` point to the configuration file.
        """
        _filename = filename or ConsulConf.CONF_SYSTEM_FILENAME
        if _filename not in ConsulConf.CONSUL_FILES:
            raise NoFileFound(filename)
        config = consul.sys_config
        self._contents = config.get(filename) or dict()

    def _read(self, filename):
        """Read sections from config file."""
        try:
            with open(filename, "r", encoding="utf-8") as r:
                return yaml.full_load(r)
        except Exception as error:
            raise FileReadFailed(filename)

    def get(self, *args):
        """Get section from conf content."""
        if not args:
            return self._contents
        firstly = True
        section = None
        try:
            for item in args:
                if firstly:
                    section = self._contents.get(item)
                    firstly = False
                else:
                    section = section.get(item)
        except Exception as error:
            raise FileArgsGetFailed(*args)
        return section


def get_system_conf():
    """获取系统配置"""
    return Configuration(ConsulConf.CONF_SYSTEM_FILENAME).get()


def get_api_conf():
    """获取API配置"""
    return Configuration(ConsulConf.CONF_SYSTEM_FILENAME).get("api")


def get_jobpool_conf():
    """获取工作区配置"""
    jobpool_conf = Configuration(ConsulConf.CONF_SYSTEM_FILENAME).get("jobpool")
    job_dir = jobpool_conf.get("job_dir", "/".join([ConsulConf.HEMNES_HOME]))
    jobpool_conf["cache_dir"] = "/".join([job_dir, jobpool_conf.get("cache_name")])
    jobpool_conf["log_dir"] = "/".join([job_dir, jobpool_conf.get("log_name")])
    jobpool_conf["worker_dir"] = "/".join([job_dir, jobpool_conf.get("worker_name")])
    jobpool_conf["store_dir"] = "/".join([job_dir, jobpool_conf.get("store_name")])
    return jobpool_conf


def get_log_conf():
    """获取日志配置"""
    return Configuration(ConsulConf.CONF_SYSTEM_FILENAME).get("log")


def get_mongodb_conf():
    """获取mongo数据库配置"""
    return Configuration(ConsulConf.CONF_SYSTEM_FILENAME).get("mongodb")
