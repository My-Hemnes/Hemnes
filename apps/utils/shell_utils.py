# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os
import signal
import subprocess


class Shell(object):

    """
    完成Shell脚本的包装。
    执行结果存放在Shell.ret_code, Shell.ret_info, Shell.err_info中
    run()为普通调用，会等待shell命令返回。
    run_background()为异步调用，会立刻返回，不等待shell命令完成
    异步调用时，可以使用get_status()查询状态，或使用wait()进入阻塞状态，
    等待shell执行完成。
    异步调用时，使用kill()强行停止脚本后，仍然需要使用wait()等待真正退出。"""

    def __init__(self):
        """Initial shell tools"""
        self.ret_code = None
        self.ret_info = None
        self.err_info = None

    def run_background(self, cmd):
        """以非阻塞方式执行shell命令（Popen的默认方式）。"""
        self._process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def run(self, cmd):
        """以阻塞方式执行shell命令。"""
        self.run_background(cmd)
        self.wait()

    def wait(self):
        """等待shell执行完成。"""
        self.ret_info, self.err_info = self._process.communicate()  # 阻塞
        self.ret_code = self._process.returncode

    def get_status(self):
        """获取shell运行状态(RUNNING|FINISHED)"""
        retcode = self._process.poll()
        if not retcode:
            status = "RUNNING"
        else:
            status = "FINISHED"
        return status

    def kill_signal(self, sig):
        os.kill(self._process.pid, sig)

    def kill(self):
        self.kill_signal(signal.SIGKILL)
