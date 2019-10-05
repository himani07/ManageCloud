from services.tag_service import TagService
import unittest
from test_cases.base import BaseTestCase
from unittest.mock import Mock, patch
from models.cluster import Cluster


class TestTag(BaseTestCase):

    mock_share_pricing_task_check_share = Mock(name='check_get_cluster')
    mock_share_pricing_task_check_share.return_value = Cluster()

    mock_flow_test_get_cluster = [
        patch.object(TagService, 'check_get_cluster', mock_share_pricing_task_check_share)
    ]

    #@MockObjects.composed(*mock_flow_test_export)
    def test_create_tag(self):
        data = []
        input_data ={

        }
        res = TagService.create_tag()
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
