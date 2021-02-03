# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
from apps.configs.api_status import StatusCodes
from apps.common.Internationalization import International


class AppBaseException(Exception):

    """This exception is a global base of all exception in apps."""

    def __init__(self, *args, **kwargs):
        """Initialize error info.

        :arg string message: error message
        :arg string message: error message(ch)
        """
        Exception.__init__(self, *args, **kwargs)

        self.error = StatusCodes.ERROR_APP_BASE_EXCEPTION
        self.content = kwargs.get("content", dict())

    def __dict__(self):
        """Gen string info."""
        return {
            "code": self.error.get("code"),
            "message": self.error.get("message"),
            "message_chs": self.error.get("message_chs"),
            "content": self.content
        }


class ApplicationError(AppBaseException):

    """This exception indicates that application error."""

    def __init__(self, *args, **kwargs):
        """Initialize error info."""
        AppBaseException.__init__(self, *args, **kwargs)
        self.error = StatusCodes.ERROR_APP_BASE_EXCEPTION


class AppClientError(AppBaseException):

    """This exception indicates that application error."""

    def __init__(self, *args, **kwargs):
        """Initialize error info."""
        AppBaseException.__init__(self, *args, **kwargs)
        self.error = StatusCodes.ERROR_APP_CLIENT_EXCEPTION
        self.error["message"] = self.error.get("message").format(args)
        self.error["message_chs"] = self.error.get("message_chs").format(args)


class NoFileFound(AppBaseException):

    """This exception indicates that application error."""

    def __init__(self, *args, **kwargs):
        """Initialize error info."""
        AppBaseException.__init__(self, *args, **kwargs)
        self.error = StatusCodes.ERROR_NO_FILE_FOUND
        self.error["message"] = self.error.get("message").format(args)
        self.error["message_chs"] = self.error.get("message_chs").format(args)


class FileReadFailed(AppBaseException):

    """This exception indicates that application error."""

    def __init__(self, *args, **kwargs):
        """Initialize error info."""
        AppBaseException.__init__(self, *args, **kwargs)
        self.error = StatusCodes.ERROR_FILE_READ_FAILED
        self.error["message"] = self.error.get("message").format(args)
        self.error["message_chs"] = self.error.get("message_chs").format(args)


class FileArgsGetFailed(AppBaseException):

    """This exception indicates that application error."""

    def __init__(self, *args, **kwargs):
        """Initialize error info."""
        AppBaseException.__init__(self, *args, **kwargs)
        self.error = StatusCodes.ERROR_FILE_ARGUMENT_GET_FAILED
        self.error["message"] = self.error.get("message").format(args)
        self.error["message_chs"] = self.error.get("message_chs").format(args)
