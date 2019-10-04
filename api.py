#!/usr/bin/python
"""
__version__     = "0.1"
__author__      = "Himani Jain"
"""
import traceback
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from utils.constants import APP_VERSION, APP_TITLE, APP_DESCRIPTION
from utils.utils import Utils
from utils.response import Response
from utils.exception import AppException


logger = Utils.get_logger(__name__)

"""
Defining the RESTPlus instance
"""

api = Api(
          None,
          version=APP_VERSION,
          title=APP_TITLE,
          description=APP_DESCRIPTION,
      )


@api.errorhandler
def default_error_handler(e):
    if type(e) in (AppException, ):
        message = str(e)
    else:
        message = "Oops! Something went wrong"
    logger.error(message, exc_info=True)
    response = Response(False, error_message=message)
    return response.__dict__


@api.errorhandler(NoResultFound)
def database_not_found_error_handler():
    logger.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404



