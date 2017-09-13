#!/usr/bin/python
"""
Handles all default RestFul API actions for State class
"""
from flask import Flask, jsonify, Blueprint, make_response, render_template
from api.v1.views import app_views
from models import state, storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_States():
    """get all states"""
    all_st = [st.to_json() for st in storage.all("State").values()]
    return jsonify(all_st)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_State_ID(state_id=None):
    """get state with specific ID"""
    all_st = [st.to_json() for st in storage.all("State").values()]
    for state in all_st:
        if (state.get("id") == state_id):
            return jsonify(state)
    return not_found(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_State(state_id=None):
    """delete state using ID"""


@app_views.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)
