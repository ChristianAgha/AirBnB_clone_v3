from flask import Blueprint, render_template
app_views = Blueprint('app_Views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *  # noqa
from api.v1.views import *  # noqa
