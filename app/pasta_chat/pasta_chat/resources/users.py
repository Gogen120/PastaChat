from flask_restful import Resource
from pasta_chat import db
from pasta_chat.models import User


class UserResource(Resource):
    def get(self, user_id):
        user = db.session.query(User).get(user_id)
        return user


class UserListResource(Resource):
    def post(self, username):
        new_user = User(username)

        db.session.add(new_user)
        db.session.commit()
