from services.machine_service import MachineService
import unittest
from test_cases.base import BaseTestCase
from unittest.mock import Mock, patch
from utils.constants import MACHINE_CREATE_SUCCESS, MACHINE_DELETE_SUCCESS
from utils.utils import Utils


class TestCluster(BaseTestCase):

    mock_cluster_create_machine = Mock(name='create_machine')
    mock_cluster_create_machine.return_value = MACHINE_CREATE_SUCCESS

    mock_cluster_delete_machine = Mock(name='delete_machine')
    mock_cluster_delete_machine.return_value = MACHINE_DELETE_SUCCESS

    mock_flow_test_create_machine = [
        patch.object(MachineService, 'create_machine', mock_cluster_create_machine)
    ]
    mock_flow_test_delete_machine = [
        patch.object(MachineService, 'delete_machine', mock_cluster_delete_machine)
    ]

    @Utils.composed(*mock_flow_test_create_machine)
    def test_create_machine(self):
        ui_input = {'cluster_id': 1,
                    'machine_name': 'machine 1',
                    'tag_key': 'm1',
                    'tag_value': 'tag for machine 1',
                    'ip_address': '10.30.0.12',
                    'instance_type': 't2.nano'
                    }
        res = MachineService.create_machine(ui_input)
        self.assertEqual(res, MACHINE_CREATE_SUCCESS)

    @Utils.composed(*mock_flow_test_delete_machine)
    def test_delete_cluster(self):
        ui_input = {'cluster_id': 1}
        res = MachineService.delete_machine(ui_input)
        self.assertEqual(res, MACHINE_DELETE_SUCCESS)


if __name__ == "__main__":
    unittest.main()
