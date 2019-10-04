import db
from models.cluster import Cluster
from datetime import datetime

class ClusterService:

    @staticmethod
    def get_clusters():
        """

        :return:
        """
        clusters = Cluster.get_all_clusters()
        cluster_list = []
        dict_keys = ["cluster_name", "cloud_region"]
        for cluster in clusters:
            result_dict = dict(zip(dict_keys, cluster))
            cluster_list.append(result_dict)
        return cluster_list

    @staticmethod
    def create_cluster(input_data):
        """

        :param input_data:
        :return:
        """
        Cluster(cluster_name='cluster1', cloud_region='sydney', is_deleted='N',
                created_by='himani.jain', created_timestamp=datetime.now()).save()
        Cluster.commit()
        return

    @staticmethod
    def delete_cluster(input_data):
        pass
