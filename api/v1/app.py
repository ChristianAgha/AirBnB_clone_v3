#!/usr/bin/python
"""
register blueprint for flask app
"""
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
from api.v1.views import app_views, states

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(err):
    """close storage files"""
    return storage.close()


@app.errorhandler(404)
def not_found(error):
    """returns error response"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
