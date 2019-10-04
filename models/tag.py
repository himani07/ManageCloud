from utils.utils import Utils
from sqlalchemy import and_
from models.machine import Machine


db = Utils.get_db()


class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column('TagId', db.Integer, primary_key=True)
    tag_name = db.Column('TagName', db.String)
    machine_id = db.Column('MachineId', db.Integer, db.ForeignKey(Machine.id))
    is_deleted = db.Column('IsDeleted', db.String)
    created_by = db.Column('CreatedBy', db.String)
    created_timestamp = db.Column('CreatedTimestamp', db.String)

    def __init__(self, tag_id, tag_name, machine_id):
        self.tag_id = tag_id
        self.tag_name = tag_name
        self.machine_id = machine_id

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self

    @classmethod
    def find_by_id(cls, id_):
        return cls.query.filter(and_(Tag.id == id_, Tag.is_deleted == 'N')).first()

    @staticmethod
    def delete(machine_id):
        tag = Tag.find_by_id(machine_id)
        if tag:
            tag.is_deleted = 'Y'

            db.session.flush()

    @staticmethod
    def commit():
        db.session.commit()
        return
