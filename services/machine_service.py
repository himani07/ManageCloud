from models.machine import Machine
from datetime import datetime
from models.tag import Tag
from utils.exception import AppException
from utils.constants import exception_message, INITIAL_MACHINE_STATE

class MachineService:

    @staticmethod
    def get_machines():
        """
        Fetches all machines details
        :return:
        """
        try:
            machines = Tag.get_machine_details()
        except:
            AppException(exception_message.get('FETCH_MACHINE_EXCEPTION'))
        machine_list = []
        dict_keys = ['machine_id', 'machine_name', 'tag_key', 'ip_address', 'instance_type',
                     'cluster_name', 'machine_status']
        for machine in machines:
            result_dict = dict(zip(dict_keys, machine))
            machine_list.append(result_dict)
        return machine_list

    @staticmethod
    def create_machine(input_data):
        """
        Create machine based on given requirements
        :param input_data:
        :return:
        """
        try:
            machine = Machine(input_data['machine_name'], input_data['cluster_id'],
                              input_data['ip_address'],  input_data['instance_type'],INITIAL_MACHINE_STATE,
                              is_deleted='N', created_by='himani.jain', created_timestamp=datetime.now()).save()
            machine_id = machine.id
        except:
            AppException(exception_message.get('CREATE_MACHINE_EXCEPTION'))
        try:
            Tag(input_data['tag_key'], input_data['tag_value'], machine_id, is_deleted='N',
                created_by='himani.jain', created_timestamp=datetime.now()).save()
        except:
            AppException(exception_message.get('CREATE_TAG_EXCEPTION'))
        Machine.commit()
        return

    @staticmethod
    def delete_machine(input_data):
        """
        Delete machine
        :param input_data:
        :return:
        """
        machine_id = input_data['machine_id']
        try:
            Machine.delete(machine_id)
        except:
            AppException(exception_message.get('DELETE_MACHINE_EXCEPTION'))
        try:
            Tag.delete(machine_id)
        except:
            AppException(exception_message.get('DELETE_TAG_EXCEPTION'))
        Machine.commit()
        return

    @staticmethod
    def update_machine_status(input_data):
        """
        Start stop reboot machine
        :param input_data:
        :return:
        """
        tag_name = input_data['tag_name']
        command = input_data['command'].lower()
        if command == 'start':
            try:
                Tag.start_machine(tag_name)
            except:
                raise AppException(exception_message.get('START_EXCEPTION'))
        elif command == 'stop':
            try:
                Tag.stop_machine(tag_name)
            except:
                raise AppException(exception_message.get('STOP_EXCEPTION'))
        elif command == 'reboot':
            try:
                Tag.stop_machine(tag_name)
                Tag.start_machine(tag_name)
            except:
                raise AppException(exception_message.get('REBOOT_EXCEPTION'))
        else:
            raise AppException(exception_message.get('INVALID_COMMAND_EXCEPTION'))
        Machine.commit()
        return
