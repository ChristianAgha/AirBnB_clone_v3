#!/usr/bin/python3
"""
Handles all default RestFul API actions for Amenity class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_User():
    """ get all users """

    all_users = storage.all("User").values()
    var = [user.to_json() for user in all_users]
    return jsonify(var)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_Users_by_ID(user_id):
    """ get user by ID """

    the_user = storage.get("User", user_id)
    if the_user is None:
        return abort(404)

    return jsonify(the_user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_User(user_id):
    """ delete user by ID """
    the_user = storage.get("User", user_id)
    if the_user is None:
        return abort(404)
    storage.delete(user_id)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_User():
    """ Create neew user """
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    name = request_data.get("name")
    if name is None:
        abort(400, 'Missing name')
    email = request_data.get("email")
    if email is None:
        abort(400, 'Missing email')
    password = request_data.get("password")
    if password is None:
        abort(400, 'Missing password')
    new_User = User(**request_data)
    new_User.save()

    return make_response(jsonify(new_User.to_json()), 201)


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_User(user_id):
    """ Updates User object """
    user_to_update = storage.get("User", user_id)
    if user_to_update is None:
        return abort(404)
    request_data = request.get_json()
    if request_data is None:
        abort(400, 'Not a JSON')
    keys_to_ignore = ['id', 'email', 'created_at', 'updated_at']
    for k, v in request_data.items():
        if k not in keys_to_ignore:
            setattr(user_to_update, k, v)
    user_to_update.save()

    return make_response(jsonify(user_to_update.to_json()), 200)
