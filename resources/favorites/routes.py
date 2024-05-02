from flask.views import MethodView
from flask_smorest import abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_model import UserModel

from . import bp
from models.favorites_model import FavoritesModel 
from schemas import FavoritesScehma, UserSchema


@bp.route('/favorites/<pokemon_id>')
class LikePost(MethodView):

    @jwt_required()
    @bp.response(201, FavoritesScehma)
    def post(self, favorites_id):

        user_id = get_jwt_identity()
        favorite = FavoritesModel.query.get(favorites_id)
        user = UserModel.query.get(user_id)
        if user and favorite:
            faved_by_user = FavoritesModel.query.filter_by(favorites_id = favorites_id).filter_by(user_id = user_id).all()
            if faved_by_user:
                return favorite
            FavoritesModel = FavoritesModel(user_id=user_id, favorites_id=favorites_id)
            FavoritesModel.save()
            return favorite
        abort(400, message="Invalid User or Favorite")

    @jwt_required()
    def delete(self, pokemon_id):
        user_id = get_jwt_identity()
        pokemon = FavoritesModel.query.get(pokemon_id)
        user = UserModel.query.get(user_id)
        if user and pokemon:
            liked_by_user = FavoritesModel.query.filter_by(pokemon_id=pokemon_id).filter_by(user_id = user_id).all()
            
            for like in liked_by_user:
                like.delete()

            return {'message':"deleted"}, 201
        abort(400, message="Invalid User or Favorite")


    @bp.response(200, UserSchema(many=True))
    def get(self, pokemon_id):
        favorite = FavoritesModel.query.get(pokemon_id)
        if not favorite:
            abort(400, message="Invalid Favorite")

        faves = FavoritesModel.query.filter_by(pokemon_id = pokemon_id).all()

        return [UserModel.query.get(fav.user_id) for fav in faves]    