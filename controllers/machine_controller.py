from api import api
from flask_restplus import Resource
from services.machine_service import MachineService
from utils.flask_models import FlaskModels
from utils.exception import AppException
from utils.response import Response
from utils.constants import exception_message, MACHINE_CREATE_SUCCESS, MACHINE_DELETE_SUCCESS

ns = api.namespace('api/machine',
                   description='Operations related to Machines')


@ns.route('')
class MachineController(Resource):
    def get(self):
        """
        Fetch all machines
        :return:
        """
        try:
            machines = MachineService.get_machines()
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('FETCH_MACHINE_EXCEPTION'))
        return Response(True, machines).__dict__, 200

    @api.expect(FlaskModels.machine_model, validate=True)
    def post(self):
        """ Create machine with tags """
        try:
            input_data = api.payload
            MachineService.create_machine(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('CREATE_MACHINE_EXCEPTION'))
        return Response(True, MACHINE_CREATE_SUCCESS).__dict__, 200

    @api.expect(FlaskModels.delete_machine, validate=True)
    def delete(self):
        """ Delete Machine """
        try:
            input_data = api.payload
            MachineService.delete_machine(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('DELETE_MACHINE_EXCEPTION'))
        return Response(True, MACHINE_DELETE_SUCCESS).__dict__, 200


@ns.route('api/machine/operations')
class MachineOperations(Resource):

    @api.expect(FlaskModels.machine_commands, validate=True)
    def post(self):
        """ Perform start/stop/reboot operations """
        try:
            input_data = api.payload
            MachineService.update_machine_status(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('COMMAND_EXCEPTION'))
        return "OK"


