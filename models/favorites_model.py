from app import db

class FavoritesModel(db.Model):

    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)
    
    def save_favorite(self):
        db.session.add(self)
        db.session.commit()

    def del_favorite(self):
        db.session.delete(self)
        db.session.commit()
    
    def from_dict(self, favorites_dict):
        for k , v in favorites_dict.items():
            if k != 'favorites':
                setattr(self, k, v)
            else:
                setattr(self, 'favorites')