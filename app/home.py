# -*- coding: utf-8 -*-
__author__ = "SirHades696"
__email__ = "djnonasrm@gmail.com"

from flask import Blueprint, render_template, request
from . import rick_morty as rm

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def index():
    n = 1
    if request.method == "POST":
        n = int(request.form["counter"])
    results = rm.find_characters(n)
    return render_template("rick_morty/index.html", results=results, page=n)
