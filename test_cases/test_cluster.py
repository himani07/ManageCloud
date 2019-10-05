from services.cluster_service import ClusterService
import unittest
from test_cases.base import BaseTestCase
from unittest.mock import Mock, patch
from utils.constants import CLUSTER_CREATE_SUCCESS, CLUSTER_DELETE_SUCCESS
from utils.utils import Utils


class TestCluster(BaseTestCase):

    mock_cluster_create_cluster = Mock(name='create_cluster')
    mock_cluster_create_cluster.return_value = CLUSTER_CREATE_SUCCESS

    mock_cluster_delete_cluster = Mock(name='delete_cluster')
    mock_cluster_delete_cluster.return_value = CLUSTER_DELETE_SUCCESS

    mock_flow_test_create_cluster = [
        patch.object(ClusterService, 'create_cluster', mock_cluster_create_cluster)
    ]
    mock_flow_test_delete_cluster = [
        patch.object(ClusterService, 'delete_cluster', mock_cluster_delete_cluster)
    ]

    @Utils.composed(*mock_flow_test_create_cluster)
    def test_create_cluster(self):
        ui_input = {'cluster_name': 'c1',
                    'cloud_region': 'us east 1',
                    }
        res = ClusterService.create_cluster(ui_input)
        self.assertEqual(res, CLUSTER_CREATE_SUCCESS)

    @Utils.composed(*mock_flow_test_delete_cluster)
    def test_delete_cluster(self):
        ui_input = {'cluster_id': 1}
        res = ClusterService.delete_cluster(ui_input)
        self.assertEqual(res, CLUSTER_DELETE_SUCCESS)


if __name__ == "__main__":
    unittest.main()
