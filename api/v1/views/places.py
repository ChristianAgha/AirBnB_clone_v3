#!/usr/bin/python3
"""
Handles all default RestFul API actions for Places class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.place import Place


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_All_Places(city_id):
    """ Get all places belonging to specific city """
    city = storage.get("City", city_id)
    if city is None:
        return abort(404)
    list = []
    places = storage.all("Place").values()
    place_list = [place.to_json() for place in places]
    for place in place_list:
        if place.get("city_id") == city_id:
            list.append(place)
    if list is None:
        return abort(404)

    return jsonify(list)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=Flase)
def get_Place(place_id):
    """ Get place belonging to specific ID """

    place = storage.get("Place", place_id)
    if place is None:
        return abort(404)

    return jsonify(place.to_json())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Place(place_id):
    """ Delete place using ID """

    place = storage.get("Place", place_id)
    if place is None:
        return abort(404)
    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_Place(city_id):
    """ Creates and saves a new place """

    city = storage.get("City", city_id)
    if city is None:
        return abort(404)

    request_data = request.get_json()
    if request_data is None:
        return abort(400, 'Not a JSON')

    place_Name = request_data.get("name")
    if place_Name is None:
        return abort(400, 'Missing name')

    user_id = request_data.get("user_id")
    if user_id is None:
        return abort(400, 'Missing user_id')

    user = storage.get("User", user_id)
    if user is None:
        return abort(404)

    request_data["city_id"] = city_id
    request_data["user_id"] = user_id
    new_Place = Place(**request_data)
    new_Place.save()

    return make_response(jsonify(new_Place.to_json()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_Place(place_id):
    """ Updates a Place object """

    place_to_update = storage.get("Place", place_id)
    if place_to_update is None:
        return abort(404)

    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')

    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for k, v in request_data.items():
        if k not in ignore:
            setattr(place_to_update, k, v)
    place_to_update.save()

    return make_response(jsonify(place_to_update.to_json()), 200)
