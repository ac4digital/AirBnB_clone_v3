#!/usr/bin/python3
"""index views"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return a JSON file with message status OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """return a count of classes"""
    for k, v in classes.items():
        classes[k] = storage.count(v)
    return jsonify(classes)
