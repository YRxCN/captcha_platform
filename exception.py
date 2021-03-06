#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kerlomz <kerlomz@gmail.com>


class InvalidUsage(Exception):

    def __init__(self, message, code=None):
        Exception.__init__(self)
        self.message = message
        self.success = False
        self.code = code

    def to_dict(self):
        rv = {'code': self.code, 'message': self.message, 'success': self.success}
        return rv


class SystemException(RuntimeError):
    def __init__(self, message, code=-1):
        self.message = message
        self.code = code


def exception(text, code=-1):
    raise SystemException(text, code)


class ConfigException:
    MODEL_CONFIG_PATH_NOT_EXIST = -4042
    CHAR_SET_NOT_EXIST = -4043
    CHAR_SET_INCORRECT = -4043


