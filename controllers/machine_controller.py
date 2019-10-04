from api import api
from flask_restplus import Resource
from services.machine_service import MachineService
from utils.flask_models import FlaskModels
from utils.exception import AppException

ns = api.namespace('api/machine',
                   description='Operations related to Machine and tags')


@ns.route('')
class MachineController(Resource):

    # @api.expect(FlaskModels.machine_model, validate=True)
    def post(self):
        """
                """
        try:
            input_data = api.payload
            MachineService.create_machine(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in creating machine')
        return "OK"

    @api.expect(FlaskModels.delete_machine, validate=True)
    def delete(self):
        try:
            input_data = api.payload
            MachineService.delete_cluster(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in deleting machine')
        return "OK"

    # @api.expect(FlaskModels.machine_model, validate=True)
    def post(self):
        """
                """
        try:
            input_data = api.payload
            MachineService.create_tag(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in creating tag')
        return "OK"

    @api.expect(FlaskModels.delete_machine, validate=True)
    def delete(self):
        try:
            input_data = api.payload
            MachineService.delete_tag(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in deleting tag')
        return "OK"
