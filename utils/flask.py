#!/usr/bin/python
"""
__version__     = "0.1"
__author__      = "Himani Jain"
"""
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from utils.utils import Utils
from api import api
from utils.constants import DEBUG

"""
Defining the Flask app
"""

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

"""
            ######################
            INITIATING APPLICATION
            ######################

"""
#################
# SETTING LOGGING
#################
#Logger.setup(Utils.get_log_dir(), None, 'DEBUG' if DEBUG else 'INFO')

#############################
# SETTING FLASK CONFIGURATION
#############################
_config = Utils.get_application_config()
app.config.update(**_config)
api.init_app(app)
api.namespaces.clear()
db = Utils.get_db()
db.init_app(app)


@app.route("/ping", methods=['GET'])
def ping():
    return "PONG | Hello World!"


