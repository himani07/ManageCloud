from models.machine import Machine


class MachineService:

    @staticmethod
    def get_machines():
        """
        Fetches
        :return:
        """
        machines = Machine.get_all_machines()
        machine_list = []
        dict_keys = ["cluster_name", "cloud_region"]
        for machine in machines:
            result_dict = dict(zip(dict_keys, machine))
            machine_list.append(result_dict)
        return machine_list

    @staticmethod
    def create_machine(input_data):
        pass

    @staticmethod
    def delete_machine(input_data):
        pass

    @staticmethod
    def create_tag(input_data):
        pass

    @staticmethod
    def delete_tag(input_data):
        pass
