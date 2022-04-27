from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()
migrate = Migrate()
engine = create_engine('')

Session = sessionmaker(bind=engine)
session = Session()


from api.models import NetflixOriginal


def create_app():
    api = Flask(__name__)
    db.init_app(api)
    migrate.init_app(api, db)
    with api.app_context():
        from . import index
        api.register_blueprint(index.api)
    return api
