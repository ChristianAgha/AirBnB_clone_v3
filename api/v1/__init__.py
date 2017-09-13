#!flask/bin/python
"""
init defines app_views
"""
from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1')
