from flask_testing import TestCase
from application import app
from common.utils import Utils
import os


mod_by = "kapil.babani@thepsi.com"

db = Utils.get_db()


class TestingConfig():
    """ TestingConfig class """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://{user}:{password}@{host}/{dbname}'.format(
        user=os.environ['username_test'], password=os.environ['password_test'], host=os.environ['host'],
        dbname=os.environ['dbname_test'])
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('test_cases.base.TestingConfig')
        return app

    def setUp(self):
        print('setup started')


    def tearDown(self):
        print('teardown')
