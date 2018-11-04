from pasta_chat import db
from pasta_chat.models import Message


MESSAGES = [
    {
        'content': 'message #1',
        'user_id': 1,
        'chat_id': 1,
    },
    {
        'content': 'Hello',
        'user_id': 3,
        'chat_id': 1,
    },
    {
        'content': 'Goodbye',
        'user_id': 2,
        'chat_id': 1
    }
]


def create_message_example():
    for message in MESSAGES:
        new_message = Message(**message)
        db.session.add(new_message)
        db.session.flush()

    db.session.commit()
