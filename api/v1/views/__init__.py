#!/usr/bin/python3
from flask import Blueprint, render_template

app_views = Blueprint('poop', __name__, url_prefix='/api/v1')
from api.v1.views.index import *