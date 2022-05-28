#!/usr/bin/python3
"""index views"""

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return a JSON file with message status OK"""
    return jsonify({"status": "OK"})
