from . import api
from api import session, engine
from api.models import NetflixOriginal
from flask import jsonify
from sqlalchemy import desc, text


@api.route("/netflix_originals/all", methods=['GET'])
def all_movies():
    try:
        result = session.query(NetflixOriginal).all()
        format_result = [r.serialize() for r in result]
        return jsonify(format_result)
    except Exception as e:
        status = "Error! = " + str(e)
    return status


@api.route("/netflix_originals/all/titles", methods=['GET'])
def all_titles():
    try:
        sql = 'select title from netflix_originals'
        result = engine.execute(sql)
        titles = [row[0] for row in result]
        return jsonify(titles)
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


@api.route("/netflix_originals/longest", methods=['GET'])
def longest():
    try:
        result = session.query(NetflixOriginal).order_by(desc(NetflixOriginal.runtime)).limit(10).all()
        format_result = [r.serialize() for r in result]
        return jsonify(format_result)
    except Exception as e:
        status = "Error! = " + str(e)
    return status


@api.route("/watched/<movie>/<rating>", methods=['POST'])
def record_watched(movie, rating):
    try:
        query = text(f"insert into watched (title, my_rating) values ('{movie}',{rating})")
        session.execute(query)
        session.commit()
        status = f'You gave {movie} a score of {rating}'
        return status
    except Exception as e:
        status = "Error! = " + str(e)
    return status
