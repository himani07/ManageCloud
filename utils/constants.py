
DEBUG = True

APP_VERSION = "0.1.0"
APP_TITLE = "Manage Cloud"
APP_DESCRIPTION = "Manage Cloud using REST API"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
SWAGGER_UI_DOC_EXPANSION = 'list'
SWAGGER_UI_OPERATION_ID = True
ERROR_INCLUDE_MESSAGE = False
BUNDLE_ERRORS = True

INITIAL_MACHINE_STATE = 'Stopped'

exception_message = {
    'FETCH_CLUSTER_EXCEPTION': 'Error in fetching cluster details',
    'CREATE_CLUSTER_EXCEPTION': 'Error in creating Cluster',
    'DELETE_CLUSTER_EXCEPTION': 'Error in deleting Cluster',
    'FETCH_MACHINE_EXCEPTION': 'Error in fetching machine details',
    'CREATE_MACHINE_EXCEPTION': 'Error in creating Machine',
    'DELETE_MACHINE_EXCEPTION': 'Error in deleting Machine',
    'FETCH_TAG_EXCEPTION': 'Error in fetching tags',
    'CREATE_TAG_EXCEPTION': 'Error in creating Tag',
    'DELETE_TAG_EXCEPTION': 'Error in deleting Tag',
    'INVALID_COMMAND_EXCEPTION': 'Entered command is not a valid command.',
    'START_EXCEPTION': 'Error in starting machine',
    'STOP_EXCEPTION': 'Error in stopping machine',
    'REBOOT_EXCEPTION': 'Error in rebooting machine',
    'COMMAND_EXCEPTION': 'Error in performing start/stop/reboot machine',
    'EXISTING_MACHINE_EXCEPTION': 'Machine with this name already exists',

}
CLUSTER_CREATE_SUCCESS = 'Cluster created successfully'
CLUSTER_DELETE_SUCCESS = 'Cluster deleted successfully'
MACHINE_CREATE_SUCCESS = 'Machine Created Successfully'
MACHINE_DELETE_SUCCESS = 'Machine deleted successfully'
TAG_CREATE_SUCCESS = 'Tag Created Successfully'
TAG_DELETE_SUCCESS = 'Tag deleted successfully'
