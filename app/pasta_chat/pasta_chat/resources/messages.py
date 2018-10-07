from flask_restful import Resource
from pasta_chat import db
from pasta_chat.models import Message
from pasta_chat.marshmallow_schemas import MessageSchema


class MessageListResource(Resource):
    def get(self):
        messages = db.session.query(Message).all()
        messages_json = MessageSchema(many=True).jsonify(messages)
        return messages_json
