from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class FavoritesScehma(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    pokemon_id = fields.Int()

class CommentSchema(Schema):
    id = fields.Str(dump_only=True)
    body = fields.Str(required=True)
    user_id = fields.Int(required=True)
