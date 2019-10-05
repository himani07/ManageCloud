from utils.utils import Utils
from sqlalchemy import and_

db = Utils.get_db()


class Cluster(db.Model):
    __tablename__ = 'Cluster'
    id = db.Column('ClusterId', db.Integer, primary_key=True)
    cluster_name = db.Column('ClusterName', db.String)
    cloud_region = db.Column('CloudRegion', db.String)
    is_deleted = db.Column('IsDeleted', db.String)
    created_by = db.Column('CreatedBy', db.String)
    created_timestamp = db.Column('CreatedTimestamp', db.String)

    def __init__(self, cluster_name, cloud_region, is_deleted, created_by, created_timestamp):
        self.cluster_name = cluster_name
        self.cloud_region = cloud_region
        self.is_deleted = is_deleted
        self.created_by = created_by
        self.created_timestamp = created_timestamp

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @staticmethod
    def get_all_clusters():
        return db.session.query(Cluster.id, Cluster.cluster_name, Cluster.cloud_region, Cluster.is_deleted)\
            .filter(Cluster.is_deleted == 'N').all()

    @staticmethod
    def find_by_id(id_):
        return db.session.query(Cluster).filter(and_(Cluster.id == id_, Cluster.is_deleted == 'N')).first()

    @staticmethod
    def delete(cluster_id):
        cluster = Cluster.find_by_id(cluster_id)
        if cluster:
            cluster.is_deleted = 'Y'
            db.session.flush()
        return

    @staticmethod
    def commit():
        db.session.commit()
        return
