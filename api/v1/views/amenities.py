methods=['GET'],#!/usr/bin/python3
"""
Handles all default RestFul API actions for Amenity class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_Amenities():
    """ get all Amenities """
    all_amenities = storage.all("Amenity").values()
    jsond_all_amenities = [amenity.to_json() for amenity in all_amenities]

    return jsonify(jsond_all_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_Amenities_by_ID(amenity_id):
    """get all Amenities by ID """

    the_amenity = storage.get("Amenity", amenity_id)
    if the_amenity is None:
        return abort(404)

    return jsonify(the_amenity.to_json())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Amenity(amenity_id):
    """"delete amenity using ID"""
    the_amenity = storage.get("Amenity", amenity_id)
    if the_amenity is None:
        return abort(404)
    storage.delete(the_amenity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_Amenity():
    """ create amenity """
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    name = request_data.get("name")
    if name is None:
        abort(400, 'Missing name')
    new_Amenity = Amenity(**request_data)
    new_Amenity.save()

    return make_response(jsonify(new_Amenity.to_json()), 201)


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_Amenity(amenity_id):
    """ Updates Amenity objects """
    amenity_to_update = storage.get("Amenity", amenity_id)
    if amenity_to_update is None:
        return abort(404)
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    keys_to_ignore = ['id', 'created_at', 'updated_at']
    for k, v in request_data.items():
        if k not in keys_to_ignore:
            setattr(amenity_to_update, k, v)
    amenity_to_update.save()

    return make_response(jsonify(amenity_to_update.to_json()), 200)
