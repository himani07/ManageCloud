from models.cluster import Cluster
from datetime import datetime
from utils.exception import AppException
from models.machine import Machine
from utils.constants import exception_message


class ClusterService:

    @staticmethod
    def get_clusters():
        """
        Fetches all the clusters
        :return:
        """
        try:
            clusters = Cluster.get_all_clusters()
        except:
            AppException(exception_message.get('FETCH_CLUSTER_EXCEPTION'))
        cluster_list = []
        dict_keys = ["cluster_id", "cluster_name", "cloud_region"]
        for cluster in clusters:
            result_dict = dict(zip(dict_keys, cluster))
            cluster_list.append(result_dict)
        return cluster_list

    @staticmethod
    def create_cluster(input_data):
        """
        Creates cluster based on given details
        :param input_data:
        :return:
        """
        try:
            Cluster(input_data['cluster_name'], input_data['cloud_region'], is_deleted='N',
                    created_by='himani.jain', created_timestamp=datetime.now()).save()
        except:
            AppException(exception_message.get('CREATE_CLUSTER_EXCEPTION'))
        Cluster.commit()
        return

    @staticmethod
    def delete_cluster(input_data):
        """
        Deletes cluster based on cluster id
        :param input_data:
        :return:
        """
        try:
            Cluster.delete(input_data['cluster_id'])
        except:
            raise AppException(exception_message.get('DELETE_CLUSTER_EXCEPTION'))
        try:
            machines = Machine.find_machine_id(input_data['cluster_id'])
            for machine in machines:
                Machine.delete(machine[0])
        except:
            AppException(exception_message.get('DELETE_MACHINE_EXCEPTION'))
        Cluster.commit()
        return
