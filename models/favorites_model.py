from app import db

class FavoritesModel(db.Model):

    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    