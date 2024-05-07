from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from Config import Config

app = Flask(__name__)

app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel
from models.favorites_model import FavoritesModel

from resources.favorites import bp as favorites_bp
app.register_blueprint(favorites_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)