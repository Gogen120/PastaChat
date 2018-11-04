from pasta_chat import db
from pasta_chat.models import Chat


def create_chat_example():
    new_chat = Chat()
    db.session.add(new_chat)
    db.session.commit()
