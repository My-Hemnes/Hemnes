# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os
import sys
from datetime import timedelta


class AppsConf:
    APPS_HOME = os.path.dirname(os.path.dirname(__file__))  # ../apps
    HEMNES_HOME = os.path.dirname(APPS_HOME)
    sys.path.append(APPS_HOME)
    DEFAULT_SERVICE_NAME = "hemnes"
    API_DEFAULT_HOST = "0.0.0.0"
    API_DEFAULT_PORT = "6060"
    API_DEFAULT_URL = "/"


class CorsConf:
    # Set a time difference between the client and server
    CORS_TIME_MINS = 30
    # Set CORS Header
    CORS_HEADERS = ",".join([
        "Accept", "Accept-Language", "Content-Language", "Remote-Mac-Address", "Remote-Ip", "Content-Type",
        "Authorization", "Content-MD5", "Range", "x-dn-signature-method", "x-dn-api-version", "x-dn-download-size",
        "x-dn-body-raw-size", "x-dn-compress-type", "x-dn-date", "x-sgi-security-token"
    ])
    CORS_RESOURCES = "*"
    CORS_MAX_AGE = timedelta(minutes=CORS_TIME_MINS)


class ConsulConf(AppsConf):
    # Consul endpoint
    CONSUL_HOST = os.environ.get("CONSUL_HOST", "localhost")
    CONSUL_PORT = os.environ.get("CONSUL_PORT", 8500)
    CONSUL_YAML = "consul.yml"
    # Consul Files
    CONSUL_FILES = ("system", )
    # Get the system config file path
    CONF_SYSTEM_FILENAME = "system"


class Register:
    BLUEPRINTS = ("echo", )
