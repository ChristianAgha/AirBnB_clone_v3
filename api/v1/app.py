#!/usr/bin/python
"""
register blueprint for flask app
"""
from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def app_teardown(err):
    return storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
