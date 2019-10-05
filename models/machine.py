from utils.utils import Utils
from sqlalchemy import and_
from models.cluster import Cluster
db = Utils.get_db()


class Machine(db.Model):
    __tablename__ = 'Machine'
    id = db.Column('MachineId', db.Integer, primary_key=True)
    machine_name = db.Column('MachineName', db.String)
    cluster_id = db.Column('ClusterId', db.Integer, db.ForeignKey(Cluster.id))
    ip_address = db.Column('IPAddress', db.String)
    instance_type = db.Column('InstanceType', db.String)
    machine_status = db.Column('MachineStatus', db.String)
    is_deleted = db.Column('IsDeleted', db.String)
    created_by = db.Column('CreatedBy', db.String)
    created_timestamp = db.Column('CreatedTimestamp', db.String)

    def __init__(self, machine_name, cluster_id, ip_address, instance_type, machine_status,
                 is_deleted, created_by, created_timestamp):
        self.machine_name = machine_name
        self.cluster_id = cluster_id
        self.ip_address = ip_address
        self.instance_type = instance_type
        self.machine_status = machine_status
        self.is_deleted = is_deleted
        self.created_by = created_by
        self.created_timestamp = created_timestamp

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @staticmethod
    def find_by_id(id_):
        return db.session.query(Machine).filter(and_(Machine.id == id_, Machine.is_deleted == 'N')).first()


    @staticmethod
    def find_machine_id(id_):
        return db.session.query(Machine.id).filter(
                        and_(Machine.cluster_id == id_, Machine.is_deleted == 'N')).all()

    @staticmethod
    def delete(machine_id):
        machine = Machine.find_by_id(machine_id)
        if machine:
            machine.is_deleted = 'Y'
            db.session.flush()
        return

    @staticmethod
    def commit():
        db.session.commit()
        return
