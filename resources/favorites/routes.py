from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_model import UserModel

from . import bp
from models.favorites_model import FavoritesModel 
from schemas import FavoritesScehma, UserSchema


@bp.route('/favorites/<pokemon_id>')
class Favorites(MethodView):
    @bp.post('/create_favorite')
    def create_favorite():
        favorites_data = request.get_json()
        pid = favorites_data['pokemon_id']
        uid = favorites_data['user_id']
        fav = FavoritesModel(uid, pid)
        fav.save_model()
        return { "message" : "user has favorite success!"}
    
    @bp.get('/favorites/<user_id>')
    def favorites(user_id):
        favorites = FavoritesModel.query.filter_by(user_id = int(user_id)).all()
        if favorites:
            return { "favorites" : favorites }
        return { 'msg' : 'favorites failure . . .'}
    
    def unfavorite(self, user_id):
        favorite = FavoritesModel.query.get(user_id)
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
