#!/usr/bin/python
"""
Handles all default RestFul API actions for State class
"""
from flask import Flask, jsonify, Blueprint, make_response, render_template
from api.v1.views import app_views
from models import state, storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_States():
    all_states = [one_state.to_json() for one_state in storage.all("State").values()]
    return jsonify(all_states)
