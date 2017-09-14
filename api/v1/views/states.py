#!/usr/bin/python3
"""
Handles all default RestFul API actions for State class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.state import State


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


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_State():
    """ Creates and saves a new state """
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    name = request_data.get("name")
    if name is None:
        abort(400, 'Missing name')

    # passing dict to State which passes it as kwargs to BaseModel
    new_State = State(**request_data)
    new_State.save()

    return make_response(jsonify(new_State.to_json()), 201)
