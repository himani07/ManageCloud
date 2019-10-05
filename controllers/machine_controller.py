from api import api
from flask_restplus import Resource
from services.machine_service import MachineService
from utils.flask_models import FlaskModels
from utils.exception import AppException
from utils.response import Response

ns = api.namespace('api/machine',
                   description='Operations related to Machines')


@ns.route('')
class MachineController(Resource):
    def get(self):
        try:
            machines = MachineService.get_machines()
        except AppException:
            raise
        except Exception:
            raise AppException('Error in fetching machines details')
        return Response(True, machines).__dict__, 200

    @api.expect(FlaskModels.machine_model, validate=True)
    def post(self):
        try:
            input_data = api.payload
            MachineService.create_machine(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in creating machine')
        return "Machine Created Successfully"

    @api.expect(FlaskModels.delete_machine, validate=True)
    def delete(self):
        try:
            input_data = api.payload
            MachineService.delete_machine(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in deleting machine')
        return "Machine deleted successfully"


@ns.route('api/machine/operations')
class MachineOperations(Resource):

    @api.expect(FlaskModels.machine_commands, validate=True)
    def post(self):
        try:
            input_data = api.payload
            MachineService.update_machine_status(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException('Error in performing start/stop/reboot machine')
        return "OK"


