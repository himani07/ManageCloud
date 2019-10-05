from api import api
from flask_restplus import Resource
from services.tag_service import TagService
from utils.flask_models import FlaskModels
from utils.exception import AppException


ns = api.namespace('api/tag',
                   description='Operations related to Machine tags')


@ns.route('')
class TagController(Resource):
    @api.expect(FlaskModels.machine_model, validate=True)
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
            raise AppException('Error in creating tag')
        return "OK"

    @api.expect(FlaskModels.delete_machine, validate=True)
    def delete(self):
        try:
            input_data = api.payload
            TagService.delete_tag(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in deleting tag')
        return "OK"