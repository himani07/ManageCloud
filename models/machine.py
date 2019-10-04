from utils.utils import Utils
from sqlalchemy import and_

db = Utils.get_db()


class Machine(db.Model):
    __tablename__ = 'Machine'
    id = db.Column('MachineId', db.Integer, primary_key=True)
    machine_name = db.Column('MachineName', db.String)
    ip_address = db.Column('IPAddress', db.String)
    instance_type = db.Column('InstanceType', db.String)
    is_deleted = db.Column('IsDeleted', db.String)
    created_by = db.Column('CreatedBy', db.String)
    created_timestamp = db.Column('CreatedTimestamp', db.String)

    def __init__(self, machine_id, machine_name, ip_address, instance_type):
        self.machine_id = machine_id
        self.machine_name = machine_name
        self.ip_address = ip_address
        self.instance_type = instance_type

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @staticmethod
    def get_all_machines():
        return db.session.query(Machine.machine_name, Machine.ip_address, Machine.instance_type) \
            .filter(Machine.is_deleted == 'N').all()

    @staticmethod
    def find_by_id(id_):
        return db.session.query.filter(and_(Machine.id == id_, Machine.is_deleted == 'N')).first()

    @staticmethod
    def delete(machine_id):
        machine = Machine.find_by_id(machine_id)
        if machine:
            machine.is_deleted = 'Y'

            db.session.flush()

    @staticmethod
    def commit():
        db.session.commit()
        return
