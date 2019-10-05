from services.cluster_service import ClusterService
import unittest
from test_cases.base import BaseTestCase
from unittest.mock import Mock, patch
from models.cluster import Cluster


class TestMachine(BaseTestCase):

    mock_share_pricing_task_check_share = Mock(name='check_get_cluster')
    mock_share_pricing_task_check_share.return_value = Cluster()

    mock_flow_test_get_cluster = [
        patch.object(ClusterService, 'check_get_cluster', mock_share_pricing_task_check_share)
    ]

    #@MockObjects.composed(*mock_flow_test_export)
    def test_get_cluster(self):
        data = []
        res = ClusterService.get_clusters()
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
