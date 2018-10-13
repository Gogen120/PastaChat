from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
api = Api(app)

from pasta_chat.config import apply_configs

apply_configs(app)

db = SQLAlchemy(app)

from pasta_chat.models import User, Chat, Message

migrate = Migrate(app, db)

from pasta_chat.resources.users import UserResource, UserListResource

api.add_resource(UserResource, '/api/v1/users/<int:user_id>')
api.add_resource(UserListResource, '/api/v1/users')


if __name__ == '__main__':
    app.run()
