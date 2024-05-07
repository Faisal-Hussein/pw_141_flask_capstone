from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_model import UserModel

from . import bp
from models.favorites_model import FavoritesModel 
from schemas import FavoritesScehma, UserSchema


@bp.route('/favorites')
class Favorites(MethodView):
    def post(self):
        favorites_data = request.get_json()
        pid = favorites_data['pokemon_id']
        uid = favorites_data['user_id']
        fav = FavoritesModel(user_id = uid, pokemon_id = pid)
        fav.save_favorite()
        return { "message" : "user has favorite success!"}
    
    def get(self):
        favorites_data = request.get_json()
        uid = favorites_data['user_id']
        favorites = FavoritesModel.query.filter_by(user_id = int(uid)).all()
        if favorites:
            print([favorite.pokemon_id for favorite in favorites])
            return { "favorites" : [favorite.pokemon_id for favorite in favorites] }
        return { 'msg' : 'favorites failure . . .'}
    
    def delete(self):
        favorites_data = request.get_json()
        uid = favorites_data['user_id']
        favorite = FavoritesModel.query.get(uid)
        if favorite:
            favorite.del_favorite()
            return { "message" : "pokemon has been unfavorited"}
        return { 'message' : 'unfavorite failure . . .'}
    

    
    # def delete(self, id):
    #     user = UserModel.query.get(id)
    #     if user:
    #         user.del_user()
    #         return { "message": "user GONE GONE GONE"}, 200
    #     abort(400, message="not a valid user")


# create a favorite by saving pokemon id and user id
# querying favorites where id = user id
# unfavorites
