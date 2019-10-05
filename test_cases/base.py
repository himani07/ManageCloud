from flask_testing import TestCase
from application import application
from utils.utils import Utils


db = Utils.get_db()


class TestingConfig:
    """ TestingConfig class """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = Utils.get_db_uri()
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class BaseTestCase(TestCase):

    def create_app(self):
        application.config.from_object('test_cases.base.TestingConfig')
        return application

    def setUp(self):
        print('setup started')

    def tearDown(self):
        print('teardown')
