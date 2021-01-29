# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import pytest

from apps.tests import log

log.info("wdawawdawdad")
log.error("wdawawdawdad")
log.critical("sdasdasd")


@log.catch()
def test_abc(x, y, z):
    return x / y + z


test_abc(1, 0, 0)

# from functools import partial
#
# logger = log.opt(colors=True)
# logger.opt = partial(logger.opt, colors=True)
#
# logger.opt(raw=True).info("It <green>still</> works!\n")
