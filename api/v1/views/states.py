#!/usr/bin/python3
"""
Handles all default RestFul API actions for State class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import state, storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_States():
    """get all states"""
    states = storage.all("State").values()
    states = [state.to_json() for state in states]
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_State_ID(state_id):
    """get state with specific ID"""
    state = storage.get("State", state_id)
    if state is None:
        return abort(404)
    return jsonify(state.to_json())



@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_State(state_id):
    """delete state using ID"""
    state = storage.get("State", state_id)
    if state is None:
        return abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)
