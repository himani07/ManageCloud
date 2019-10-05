from api import api
from flask_restplus import Resource
from services.cluster_service import ClusterService
from utils.flask_models import FlaskModels
from utils.utils import Utils
from utils.response import Response
from utils.exception import AppException
from utils.constants import exception_message


logger = Utils.get_logger(__name__)

ns = api.namespace('api/cluster',
                   description='Operations related to Cluster')


@ns.route('')
class ClusterController(Resource):

    def get(self):
        try:
            clusters = ClusterService.get_clusters()
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('FETCH_CLUSTER_EXCEPTION'))
        return Response(True, clusters).__dict__, 200

    @api.expect(FlaskModels.cluster_model, validate=True)
    def post(self):
        try:
            input_data = api.payload
            ClusterService.create_cluster(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('CREATE_CLUSTER_EXCEPTION'))
        return "Cluster created successfully."

    @api.expect(FlaskModels.delete_cluster, validate=True)
    def delete(self):
        try:
            input_data = api.payload
            ClusterService.delete_cluster(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('DELETE_CLUSTER_EXCEPTION'))
        return Response(True, "Cluster deleted successfully").__dict__, 200


