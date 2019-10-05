from api import api
from flask_restplus import Resource
from services.cluster_service import ClusterService
from utils.flask_models import FlaskModels
from utils.utils import Utils
from utils.response import Response
from utils.exception import AppException
from utils.constants import exception_message, CLUSTER_CREATE_SUCCESS, CLUSTER_DELETE_SUCCESS


logger = Utils.get_logger(__name__)

ns = api.namespace('api/cluster',
                   description='Operations related to Cluster')


@ns.route('')
class ClusterController(Resource):

    def get(self):
        """ Fetch all cluster details """
        try:
            clusters = ClusterService.get_clusters()
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('FETCH_CLUSTER_EXCEPTION'))
        return Response(True, clusters).__dict__, 200

    @api.expect(FlaskModels.cluster_model, validate=True)
    def post(self):
        """ Create new cluster """
        try:
            input_data = api.payload
            ClusterService.create_cluster(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('CREATE_CLUSTER_EXCEPTION'))
        return Response(True, CLUSTER_CREATE_SUCCESS).__dict__, 200

    @api.expect(FlaskModels.delete_cluster, validate=True)
    def delete(self):
        """ Delete cluster """
        try:
            input_data = api.payload
            ClusterService.delete_cluster(input_data)
        except AppException:
            raise
        except Exception:
            raise AppException(exception_message.get('DELETE_CLUSTER_EXCEPTION'))
        return Response(True, CLUSTER_DELETE_SUCCESS).__dict__, 200


