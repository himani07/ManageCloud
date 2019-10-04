from flask_restplus import fields
from api import api


class FlaskModels:
    cluster_model = api.model('cluster_model', {
        'cluster_name': fields.String(required=True, description='This field defines the cluster name'),
        'cloud_region': fields.List(fields.String, required=True, description='This field defines cloud region ')
    })

    delete_cluster = api.model('delete_cluster', {
        'cluster_id': fields.String(required=True, description='This field defines the cluster id')
    })

    machine_model = api.model('machine_model', {
        'cluster_id': fields.String(required=True, description='This field defines the cluster id'),
        'machine_name': fields.String(required=True, description='This field defines the machine name'),
        'ip_address': fields.String(required=True, description='This field defines the ip address of machine'),
        'instance_type': fields.String(required=True, description='This field defines the machine instance type')
    })

    delete_machine = api.model('delete_machine', {
        'machine_id': fields.String(required=True, description='This field defines the machine id')
    })

    tag_model = api.model('tag_model', {
        'machine_id': fields.String(required=True, description='This field defines the machine id'),
        'tag_name': fields.String()
    })

    delete_tag = api.model('delete_tag', {
        'tag_id': fields.String(required=True, description='This field defines the tag id')
    })


