from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def create_app():

    # instantiate the app
    app = Flask(__name__)
    print(app)


    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)


    # setup extentensions
    db.init_app(app)

    # register blueprints
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    print(app)
    
    return app

    