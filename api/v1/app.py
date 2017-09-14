#!/usr/bin/python
""" Register blueprint for flask app """
from api.v1.views import app_views, states
from flask import Flask, jsonify, Blueprint, make_response
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(self):
    """close storage files"""
    return storage.close()


@app.errorhandler(404)
def not_found(error):
    """returns error response"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host, port)
