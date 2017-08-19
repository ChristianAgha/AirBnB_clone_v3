#!flask/bin/python
"""
init defines app_views
"""
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1')
