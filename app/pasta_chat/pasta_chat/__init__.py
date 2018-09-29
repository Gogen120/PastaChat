from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/postgres'.format('postgres', 'pasta', 'pasta_chat.postgres', '5432')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'null'

db = SQLAlchemy(app)
from pasta_chat.models import User, Chat, Message
migrate = Migrate(app, db)

from pasta_chat.resources.users import UsersResource, UserListResource

api.add_resource(UserResource, '/api/v1/users/<int:user_id>')
api.add_resource(UserListResource, '/api/v1/users')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
