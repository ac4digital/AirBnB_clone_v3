#!/usr/bin/python3
"""app to connect to the API"""

import os
from api.v1.views import app_views
from models import storage
from flask import Flask, Blueprint


app = Flask(__name__)

app.register_blueprint(app.views)


@app.teardown_appcontext
def teardowm_appcontext(param):
    """teardown_appcontext"""
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
