import logging
from db import DatabaseServer
from .constants import  SQLALCHEMY_TRACK_MODIFICATIONS, SWAGGER_UI_DOC_EXPANSION,\
    SWAGGER_UI_OPERATION_ID, ERROR_INCLUDE_MESSAGE, BUNDLE_ERRORS
import os


class Utils:

    @staticmethod
    def get_db_uri():
        base_dir = os.getcwd()
        _uri = 'sqlite:///' + base_dir + '/test.db'
        return _uri

    @staticmethod
    def get_application_config():
        """
        Function helps to load the application configuration
        """

        return {
            'SQLALCHEMY_TRACK_MODIFICATIONS': SQLALCHEMY_TRACK_MODIFICATIONS,
            'SQLALCHEMY_DATABASE_URI': Utils.get_db_uri(),
            'SWAGGER_UI_DOC_EXPANSION': SWAGGER_UI_DOC_EXPANSION,
            'SWAGGER_UI_OPERATION_ID': SWAGGER_UI_OPERATION_ID,
            'ERROR_INCLUDE_MESSAGE': ERROR_INCLUDE_MESSAGE,
            'BUNDLE_ERRORS': BUNDLE_ERRORS
        }

    @staticmethod
    def get_logger(name=''):
        if not name:
            name = 'root'
        return logging.getLogger(name)

    @staticmethod
    def get_db():
        """
        Func helps return the DB Instance
        :return:
        """
        return DatabaseServer.get_instance()