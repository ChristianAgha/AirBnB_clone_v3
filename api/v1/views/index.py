#!/usr/bin/python3
""" Create routes for /status """
from api.v1.views import app_views
from flask import Blueprint, render_template, make_response, jsonify
from models import city, place, review, state, user
from models import storage, base_model, amenity


@app_views.route('/status')
def index():
    """Returns status"""
    return make_response(jsonify({'status': 'OK'}))


@app_views.route('/stats')
def stats():
    """Returns stats"""
    CNC = {
        'Amenity': "amenities",
        'City': "cities",
        'Place': "places",
        'Review': "reviews",
        'State': "states",
        'User': "users"
    }
    new_dict = {}
    for key, value in CNC.items():
        new_dict[value] = storage.count(key)

    return jsonify(new_dict)
