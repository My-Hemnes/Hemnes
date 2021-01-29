# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os
import subprocess

HOME = os.path.dirname(os.path.abspath(__file__))


def sub_run(cmd):
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def isort_normalization():
    cmd = "isort -ls -y"
    sub_run(cmd)
    print("执行isort导入格式规范")


def yapf_normalization():
    cmd = "yapf -i -r {} --style {}".format(HOME, get_yapf_conf())
    sub_run(cmd)
    print("执行yapf代码格式规范")


def get_yapf_conf():
    yapf_conf = "/".join([HOME, "yapf_style.cfg"])
    return yapf_conf


def main():
    isort_normalization()
    yapf_normalization()


if __name__ == '__main__':
    main()
