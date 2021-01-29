# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""APPS Manage start"""

import os
from apps.api.application import app


def main():
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))


if __name__ == '__main__':
    main()
