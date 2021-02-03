# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os

import yaml
from six import iteritems
from flask_consulate import Consul as BaseConsul

from apps.configs.constants import ConsulConf
from apps.utils.common_utils import read_yml, jobpool_init


def get_consul_config():
    """Initialize api consul."""
    consul_file = os.path.join(ConsulConf.APPS_HOME, "configs", ConsulConf.CONSUL_YAML)
    return read_yml(consul_file)


class Consul(BaseConsul):

    """The Consul flask.ext object is responsible for connecting and querying
    consul (using gmr/consulate as the underlying client library)."""

    def __init__(self, consul_conf=None):
        """Initialize consul."""
        self.host = ConsulConf.CONSUL_HOST
        self.port = ConsulConf.CONSUL_PORT
        self.kwargs = consul_conf if consul_conf else {}
        self.prefix = self.kwargs.get("prefix")
        self.templates = self.kwargs.get("templates")
        self.max_tries = self.kwargs.get('max_tries', 3)
        self.session = self._create_session(test_connection=self.kwargs.get('test_connection', False), )
        self.sys_config = self.apply_remote_configs()

    def apply_remote_config(self, namespace=None):

        if namespace is None:
            namespace = "config/{service}/{environment}/".format(service=os.environ.get('SERVICE', 'generic_service'),
                                                                 environment=os.environ.get(
                                                                     'ENVIRONMENT', 'generic_environment'))
        config = self.session.kv.find(namespace)
        if not config:
            raise KeyError("请检查consul中是否存在namespace:{}".format(namespace))
        for k, v in iteritems(config):
            k = k.replace(namespace, namespace.split('/')[-1])
            try:
                conf = yaml.full_load(v)
                content = {k: conf}
                return content
            except (TypeError, ValueError):
                raise KeyError("Couldn't to parse and import configuration file in consul (namespace=%s)" % namespace,
                               u"不能从consul中解析并导入配置文件 (namespace=%s)" % namespace)

    def apply_remote_configs(self):
        """apply remotes all templates"""
        configs = dict()
        for template in self.templates:
            configs.update(self.apply_remote_config(namespace='/'.join([self.prefix, template])))

        # initial system jobpool
        if configs.get("system"):
            jobpool_init(configs["system"].get("jobpool"))

        return configs


consul = Consul(consul_conf=get_consul_config())
