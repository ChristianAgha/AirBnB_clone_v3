#!/usr/bin/python3
"""
Handles all default RestFul API actions for Reviews class
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_All_Reviews(place_id):
    """ Get all reviews belonging to specific place """
    place = storage.get("Place", place_id)
    if place is None:
        return abort(404)
    reviews_list = []
    for review in place.reviews:
        reviews_list.append(review.to_json())

    return jsonify(reviews_list)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """ Get review object from ID """

    review = storage.get("Review", review_id)
    if review is None:
        return abort(404)

    return jsonify(review.to_json())


@app_views.route('reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Review(review_id):
    """ Delete review using ID """

    review = storage.get("Review", review_id)
    if review is None:
        return abort(404)
    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_Review(place_id):
    """ Creates and saves a new review """

    place = storage.get("Place", place_id)
    if place is None:
        return abort(404)

    request_data = request.get_json()
    if request_data is None:
        return abort(400, 'Not a JSON')

    user_id = request_data.get("user_id")
    if user_id is None:
        return abort(400, "Missing user_id")

    user_from_ID = storage.get("User", user_id)
    if user_from_ID is None:
        return abort(404)

    review_Text = request_data.get("text")
    if review_Text is None:
        return abort(400, "Missing text")

    request_data["place_id"] = place_id
    new_Review = Review(**request_data)
    new_Review.save()

    return make_response(jsonify(new_Review.to_json()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_Review(review_id):
    """ Updates a review Object """

    rev_to_update = storage.get("Review", review_id)
    if rev_to_update is None:
        return abort(404)
    request_data = request.get_json()
    if request_data is None:
        return abort(400, "Not a JSON")

    ignore = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for k, v in request_data.items():
        if k not in ignore:
            setattr(rev_to_update, k, v)
    rev_to_update.save()

    return make_response(jsonify(rev_to_update.to_json()), 200)
