from flask_restplus import fields
from api import api


class FlaskModels:
    cluster_model = api.model('cluster_model', {
        'cluster_name': fields.String(required=True, description='This field defines the cluster name'),
        'cloud_region': fields.String(required=True, description='This field defines cloud region ')
    })

    delete_cluster = api.model('delete_cluster', {
        'cluster_id': fields.Integer(required=True, description='This field defines the cluster id')
    })

    machine_model = api.model('machine_model', {
        'cluster_id': fields.Integer(required=True, description='This field defines the cluster id'),
        'machine_name': fields.String(required=True, description='This field defines the machine name'),
        'tag_key': fields.String(required=True, description='This field defines key of machine tag'),
        'tag_value': fields.String(required=True, description='This field defines value of machine tag'),
        'ip_address': fields.String(required=True, description='This field defines the ip address of machine'),
        'instance_type': fields.String(required=True, description='This field defines the machine instance type')
    })

    delete_machine = api.model('delete_machine', {
        'machine_id': fields.Integer(required=True, description='This field defines the machine id')
    })

    machine_commands = api.model('stop_machine', {
        'tag_key': fields.String(required=True, description='This field defines the tag key'),
        'command': fields.String(required=True, description='This field defines the machine command')
    })

    tag_model = api.model('tag_model', {
        'machine_id': fields.Integer(required=True, description='This field defines the machine id'),
        'tag_key': fields.String(required=True, description='This field defines the tag key'),
        'tag_value': fields.String(required=True, description='This field defines the tag value'),
    })

    delete_tag = api.model('delete_tag', {
        'tag_id': fields.Integer(required=True, description='This field defines the tag id')
    })


