#!/usr/bin/python3
"""
Handles all default RestFul API actions for City class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_All_Cities(state_id):
    """ Get all cities belonging to specific state """
    state = storage.get("State", state_id)
    if state is None:
        return abort(404)
    list = []
    cities = storage.all("City").values()
    city_list = [city.to_json() for city in cities]
    for city in city_list:
        if city.get("state_id") == state_id:
            list.append(city)
    if list is None:
        return abort(404)

    return jsonify(list)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_City(city_id):
    """ Get all cities belonging to specific state """

    cities = storage.get("City", city_id)
    if cities is None:
        return abort(404)

    return jsonify(cities.to_json())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_City(city_id):
    """ Delete city using ID """

    city = storage.get("City", city_id)
    if city is None:
        return abort(404)
    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """ Creates and saves a new city """

    state = storage.get("State", state_id)
    if state is None:
        return abort(404)

    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    city_Name = request_data.get("name")
    if city_Name is None:
        abort(400, 'Missing name')
    request_data["state_id"] = state_id
    new_City = City(**request_data)
    new_City.save()

    return make_response(jsonify(new_City.to_json()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def update_City(city_id):
    """ Updates a City object """

    city_to_update = storage.get("City", city_id)
    if city_to_update is None:
        return abort(404)
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')

    keys_to_ignore = ['id', 'state_id', 'created_at', 'updated_at']
    for k, v in request_data.items():
        if k not in keys_to_ignore:
            setattr(city_to_update, k, v)
    city_to_update.save()

    return make_response(jsonify(city_to_update.to_json()), 200)
