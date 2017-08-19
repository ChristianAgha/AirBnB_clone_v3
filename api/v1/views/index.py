#!/usr/bin/python3
"""
doc
"""
from flask import Blueprint, render_template, make_response, jsonify
from api.v1.views import app_views

@app_views.route('/status')
def index():
    return make_response(jsonify({'status': 'OK'}))
