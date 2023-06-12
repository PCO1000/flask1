from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate





login_manager = LoginManager()
#login_manager.init_app(app)
db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    #REGISTER Packages
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #Importing Blueprints
    from app.blueprints.main import main
    from app.blueprints.auth import auth
    #from app.blueprints.posts import posts

    #Login_Manager Settings

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You must be logged in to view this page!'
    login_manager.login_message_category = 'warning'



    #Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    #app.register_blueprint(posts)

    return app


#from app import routes, models

