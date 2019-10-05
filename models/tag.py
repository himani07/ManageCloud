from utils.utils import Utils
from models.machine import Machine
from models.cluster import Cluster


db = Utils.get_db()


class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column('TagId', db.Integer, primary_key=True)
    tag_key = db.Column('TagKey', db.String)
    tag_value = db.Column('TagValue', db.String)
    machine_id = db.Column('MachineId', db.Integer, db.ForeignKey(Machine.id))
    is_deleted = db.Column('IsDeleted', db.String)
    created_by = db.Column('CreatedBy', db.String)
    created_timestamp = db.Column('CreatedTimestamp', db.String)

    def __init__(self, tag_key, tag_value, machine_id, is_deleted, created_by, created_timestamp):
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.machine_id = machine_id
        self.is_deleted = is_deleted
        self.created_by = created_by
        self.created_timestamp = created_timestamp

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @staticmethod
    def get_all_tags():
        return db.session.query(Tag.id, Tag.tag_key, Tag.tag_value, Tag.machine_id).filter(
            Tag.is_deleted == 'N').all()

    @staticmethod
    def find_machine_by_tag(tag_name):
        return db.session.query(Machine).join(Tag).filter(
            Machine.id == Tag.machine_id,
            Tag.tag_key == tag_name).all()

    @staticmethod
    def start_machine(tag_name):
        machines = Tag.find_machine_by_tag(tag_name)
        if machines:
            for machine in machines:
                machine.machine_status = 'Running'
                db.session.flush()
        return

    @staticmethod
    def stop_machine(tag_name):
        machines = Tag.find_machine_by_tag(tag_name)
        if machines:
            for machine in machines:
                machine.machine_status = 'Stopped'
                db.session.flush()
        return

    @staticmethod
    def get_machine_details():
        return db.session.query(Machine.id, Machine.machine_name, Tag.tag_key, Machine.ip_address,
                                Machine.instance_type, Cluster.cluster_name, Machine.machine_status).\
            join(Cluster) .join(Tag).filter(Machine.cluster_id == Cluster.id,
                                            Machine.id == Tag.machine_id,
                                            Machine.is_deleted == 'N').all()

    @staticmethod
    def find_tag_by_tag_id(tag_ids):
        return db.session.query(Tag).filter(
            Tag.id.in_(tag_ids), Tag.is_deleted == 'N').all()

    @staticmethod
    def find_tag_by_machine_id(machine_ids):
        return db.session.query(Tag).filter(
            Tag.machine_id.in_(machine_ids), Tag.is_deleted == 'N').all()

    @staticmethod
    def delete(tag_ids):
        tags = Tag.find_tag_by_tag_id(tag_ids)
        if tags:
            for tag in tags:
                tag.is_deleted = 'Y'
                db.session.flush()
        return

    @staticmethod
    def commit():
        db.session.commit()
        return
