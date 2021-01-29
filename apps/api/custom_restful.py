# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
try:
    from collections.abc import MutableSequence
except ImportError:
    from collections import MutableSequence
from flask import request
from flask_restful.reqparse import Argument, RequestParser
from werkzeug import exceptions
from apps.errors.base_error import AppBaseException


class CustomArgument(Argument):

    def handle_validation_error(self, error, bundle_errors):
        """Called when an error is raised while parsing. Aborts the request
        with a 400 status and an error message
        """
        error = self.help
        raise error(self.name)


class CustomReqparse(RequestParser):
    """Custom flask-restful reqparse"""

    def __init__(self):
        RequestParser.__init__(self, argument_class=CustomArgument)

    def parse_args(self, req=None, strict=False, http_error_code=400):
        """Parse all arguments from the provided request and return the results
        as a Namespace

        :param req: Can be used to overwrite request from Flask
        :param strict: if req includes args not in parser, throw 400 BadRequest exception
        :param http_error_code: use custom error code for `flask_restful.abort()`
        """
        if req is None:
            req = request

        namespace = self.namespace_class()

        # A record of arguments not yet parsed; as each is found
        # among self.args, it will be popped out
        req.unparsed_arguments = dict(self.argument_class('').source(req)) if strict else {}
        errors = {}
        for arg in self.args:
            value, found = arg.parse(req, self.bundle_errors)
            if isinstance(value, ValueError):
                errors.update(found)
                found = None
            if found or arg.store_missing:
                namespace[arg.dest or arg.name] = value
        if errors:
            raise AppBaseException()

        if strict and req.unparsed_arguments:
            raise exceptions.BadRequest('Unknown arguments: %s'
                                        % ', '.join(req.unparsed_arguments.keys()))

        return namespace

