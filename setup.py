# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
"""The Hemnes package setup by linux."""

import os
import sys
import traceback
import subprocess

try:
    import setuptools
except ImportError:
    import distutils.core as setuptools

DOUBAN_SOURCE = {
    'index_url': 'https://pypi.douban.com/simple/',
    'trusted_host': 'pypi.douban.com '
}
LOCAL_SOURCE = {
    'index_url': 'https://nexus.diannei-ai.com/repository/group-pypi/simple'
}

HEMNES_DIR = os.path.dirname(__file__)

__verison__ = "0.0.9"

try:
    # Read and pip install package requires
    REQUIREMENTS = "/".join([HEMNES_DIR, "requirements.txt"])
    if os.path.exists(REQUIREMENTS):
        try:
            subprocess.check_call(
                "sudo -H pip3 --default-timeout=6000 install -r {0} -i {1} --force-reinstall"
                .format(REQUIREMENTS, LOCAL_SOURCE["index_url"]),
                shell=True)
        except Exception as e:
            try:
                subprocess.check_call(
                    "sudo -H pip3 --default-timeout=6000 install -r {0} -i {1} --trusted-host {2} --force-reinstall"
                    .format(REQUIREMENTS, DOUBAN_SOURCE["index_url"],
                            DOUBAN_SOURCE['trusted_host']),
                    shell=True)
            except Exception as e:
                subprocess.check_call(
                    "sudo -H pip3 --default-timeout=6000 install -r {0}".
                    format(REQUIREMENTS),
                    shell=True)
    else:
        print(sys.stderr,
              "Can't find the requirements.txt in {0}".format(REQUIREMENTS))
except Exception as error:
    print(sys.stderr,
          "Some error for pip with {}".format(str(traceback.format_exc())))
    sys.exit(1)

# 打包
setuptools.setup(
    name="hemnes",
    version=__verison__,
    package_dir={"": "apps"},
    packages=setuptools.find_packages("apps", exclude=["tests", "test_*", "scripts"]),
    package_data={"": ["*.yml", "*.sh", "*.bat", "*.dic", "*.png", "*.html"]},
    install_requires=[
        "isort",
        "yapf"
    ],
    entry_points={
        "console_scripts": ["normalization=normalization:main",
                            "pid_fire=tests.test_pid_fire:main"]
    },
)
