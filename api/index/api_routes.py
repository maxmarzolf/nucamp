from . import api
from api import session
from api.models import NetflixOriginal
from flask import jsonify
from sqlalchemy import desc


@api.route("/netflix_originals/all", methods=['GET'])
def all_movies():
    try:
        result = session.query(NetflixOriginal).all()
        format_result = [r.serialize() for r in result]
        return jsonify(format_result)
    except Exception as e:
        status = "Error! = " + str(e)
    return status


@api.route("/netflix_originals/highest_rated", methods=['GET'])
def highest_rated():
    try:
        result = session.query(NetflixOriginal).order_by(desc(NetflixOriginal.imdb_score)).limit(1).all()
        format_result = [r.serialize() for r in result]
        return jsonify(format_result)
    except Exception as e:
        status = "Error! = " + str(e)
    return status
