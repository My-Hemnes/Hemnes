# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from werkzeug.routing import Rule, Map
from werkzeug.serving import run_simple
from werkzeug.exceptions import HTTPException

rules = [Rule('/', endpoint='index'), Rule('/message/<mobile_number>', endpoint='mobile')]
url_map = Map(rules)


def application(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except HTTPException as ex:
        return ex(environ, start_response)

    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)

    body = 'Rule points to {} with arguments {}' \
        .format(endpoint, args).encode('utf-8')
    return [body]


if __name__ == "__main__":
    run_simple('localhost', 5000, application)
