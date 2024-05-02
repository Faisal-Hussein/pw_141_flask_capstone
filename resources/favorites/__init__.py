from flask_smorest import Blueprint

bp = Blueprint('favorites', __name__, description= "Routes for Favorites")

from . import routes