from services.tag_service import TagService
import unittest
from test_cases.base import BaseTestCase
from unittest.mock import Mock, patch
from utils.constants import TAG_CREATE_SUCCESS, TAG_DELETE_SUCCESS
from utils.utils import Utils


class TestTag(BaseTestCase):

    mock_cluster_create_tag = Mock(name='create_tag')
    mock_cluster_create_tag.return_value = TAG_CREATE_SUCCESS

    mock_cluster_delete_tag = Mock(name='delete_tag')
    mock_cluster_delete_tag.return_value = TAG_DELETE_SUCCESS

    mock_flow_test_create_tag = [
        patch.object(TagService, 'create_tag', mock_cluster_create_tag)
    ]
    mock_flow_test_delete_tag = [
        patch.object(TagService, 'delete_tag', mock_cluster_delete_tag)
    ]

    @Utils.composed(*mock_flow_test_create_tag)
    def test_create_tag(self):
        ui_input = {'machine_id': 1,
                    'tag_key': 'm1',
                    'tag_value': 'tag for m1'}
        res = TagService.create_tag(ui_input)
        self.assertEqual(res, TAG_CREATE_SUCCESS)

    @Utils.composed(*mock_flow_test_delete_tag)
    def test_delete_tag(self):
        ui_input = {'tag_id': 1}
        res = TagService.delete_tag(ui_input)
        self.assertEqual(res, TAG_DELETE_SUCCESS)


if __name__ == "__main__":
    unittest.main()
