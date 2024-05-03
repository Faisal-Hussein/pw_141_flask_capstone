from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Config import Config
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models.user_model import UserModel

from resources.favorites import bp as favorites_bp
app.register_blueprint(favorites_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)