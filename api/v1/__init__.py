#!flask/bin/python
"""
doc
"""
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('poop', __name__, url_prefix='/api/v1')
