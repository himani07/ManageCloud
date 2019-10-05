#!/usr/bin/python


class Response:

    def __init__(self, is_success, response=None, error_message=None):
        self.is_success = is_success
        self.response = response
        self.error_message = error_message
