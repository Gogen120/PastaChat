from datetime import datetime
from pasta_chat import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    messages = db.relationship('Message', backref='user')


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='chat')
    messages = db.relationship('Message', backref='chat')


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
