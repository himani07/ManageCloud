from api import api
from flask_restplus import Resource
from services.tag_service import TagService
from utils.flask_models import FlaskModels
from utils.exception import AppException
from utils.response import Response
from utils.constants import exception_message, TAG_CREATE_SUCCESS, TAG_DELETE_SUCCESS
import logging

ns = api.namespace('api/tag',
                   description='Operations related to Machine tags')


@ns.route('')
class TagController(Resource):

    def get(self):
        """
        Fetches all tags
        :return:
        """
        try:
            tags = TagService.get_tags()
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('FETCH_TAG_EXCEPTION'))
        return Response(True, tags).__dict__, 200

    @api.expect(FlaskModels.tag_model, validate=True)
    def post(self):
        """
        Api for creating new tag for machine
        :return:
        """
        try:
            input_data = api.payload
            TagService.create_tag(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('CREATE_TAG_EXCEPTION'))
        return TAG_CREATE_SUCCESS

    @api.expect(FlaskModels.delete_tag, validate=True)
    def delete(self):
        """ Delete tag """
        try:
            input_data = api.payload
            TagService.delete_tag(input_data)
        except AppException:
            logging.exception('hiiihi')
        except Exception:
            raise AppException(exception_message.get('DELETE_TAG_EXCEPTION'))
        return TAG_DELETE_SUCCESS