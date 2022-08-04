# -*- coding: utf-8 -*-
__author__ = "SirHades696"
__email__ = "djnonasrm@gmail.com"

from flask import Flask
import secrets


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=secrets.token_hex(20))

    from . import home

    app.register_blueprint(home.bp)
    return app
