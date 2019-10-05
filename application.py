#!/usr/bin/python
"""
__version__     = "0.1"
__author__      = "Himani Jain"
"""
import json
from utils.response import Response
from utils.exception import AppException
from api import api
from controllers.cluster_controller import ns as cluster_namespace
from controllers.machine_controller import ns as machine_namespace
from controllers.tag_controller import ns as tag_namespace
from utils.flask import application


api.add_namespace(cluster_namespace)
api.add_namespace(machine_namespace)
api.add_namespace(tag_namespace)


@application.route("/health", methods=['GET'])
def hello():
    return "OK: Running"


@application.after_request
def rewrite_bad_request(response):
    if response.status_code == 400 and response.data.decode('utf-8').find('"title":') is not None:

        original = json.loads(response.data.decode('utf-8'))
        if 'error_message' not in response.json.keys():
            response.data = json.dumps(Response(False, error_message=list(original['errors'].values())[0]).__dict__)
        response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':

    try:
        application.run(host='0.0.0.0', port=5050, debug=True)
    except Exception as e:
        AppException('Error in starting server')

