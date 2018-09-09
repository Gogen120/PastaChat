from datetime import datetime
from pasta_chat import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    messages = db.relationship('Message', backref='user')
    chat_id =


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', secondary=chat_user, backref='chat')
    message_id = db.relationship('Message', secondary=chat_user, backref='chat')


chat_user = db.Table(
    'chat_user',
    db.Column('chat_id', db.Integer, db.ForeignKey('chat.id')),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'))
)


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
