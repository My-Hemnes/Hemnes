# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""Initialize hemnes API in gunicorn."""
#
import os
import multiprocessing
import gevent.monkey
gevent.monkey.patch_all()

from apps.configs.settings import APIConfig, LogConfig

bind = "{}:{}".format(APIConfig.HOST, APIConfig.PORT)
workers = multiprocessing.cpu_count()
threads = 1
timeout = 600
backlog = 2048
# daemon = True
debug = False
#
worker_class = "gevent"
worker_connections = 1000
proc_name = "gunicorn"
loglevel = "error"

pidfile = "/".join([LogConfig.LOG_DIRNAME, "gunicorn.pid"])
if os.path.exists(pidfile):
    os.remove(pidfile)
logfile = "/".join([LogConfig.LOG_DIRNAME, "gunicorn.log"])

accesslog = "/".join([LogConfig.LOG_DIRNAME, "gun_access.log"])
errorlog = "/".join([LogConfig.LOG_DIRNAME, "gun_error.log"])
x_forwarded_for_header = 'X-FORWARDED-FOR'

preload_app = True

# forwarded_allow_ips = "127.0.0.1"
