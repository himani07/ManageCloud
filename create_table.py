from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from utils.utils import Utils

engine = create_engine(Utils.get_db_uri(), echo=True)
meta = MetaData()

cluster = Table(
    'cluster', meta,
    Column('ClusterId', Integer, primary_key=True),
    Column('ClusterName', String),
    Column('CloudRegion', String),
    Column('IsDeleted', String),
    Column('CreatedBy', String),
    Column('CreatedTimestamp', String)
)

machine = Table(
    'machine', meta,
    Column('MachineId', Integer, primary_key=True),
    Column('MachineName', String),
    Column('ClusterId', String),
    Column('IPAddress', String),
    Column('InstanceType', String),
    Column('MachineStatus', String),
    Column('IsDeleted', String),
    Column('CreatedBy', String),
    Column('CreatedTimestamp', String)
)

tag = Table(
    'tag', meta,
    Column('TagId', Integer, primary_key=True),
    Column('TagKey', String),
    Column('TagValue', String),
    Column('MachineId', String),
    Column('IsDeleted', String),
    Column('CreatedBy', String),
    Column('CreatedTimestamp', String)
)
#meta.drop_all(engine)
meta.create_all(engine)
