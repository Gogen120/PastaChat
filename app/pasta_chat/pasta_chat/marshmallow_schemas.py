from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    messages = fields.Nested('MessageSchema')


class MessageSchema(Schema):
    id = fields.Int()
    content = fields.Str()
    user_id = fields.Int()
