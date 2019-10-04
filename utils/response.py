#!/usr/bin/python
import sys
import traceback


class Response:

    def __init__(self, is_success, response=None, error_message=None):
        self.is_success = is_success
        self.response = response
        self.error_message = error_message


class ErrorResponse:

    def __init__(self, message=''):
        if not message:
            message = 'System Error'
        self.is_success = False
        self.response = []
        self.error_message = message
        self.error_info = ''

    @staticmethod
    def get_error_message():
        exc_type, exc_value, exc_traceback = sys.exc_info()
        value = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
        return value
