from pasta_chat import db
from pasta_chat.models import User

USERS = [
    {
        'username': 'username123',
        'chat_id': 1
    },
    {
        'username': 'user',
        'chat_id': 1
    },
    {
        'username': 'IvanIvanov',
        'chat_id': 1
    }
]


def create_user_example():
    for user in USERS:
        new_user = User(**user)
        db.session.add(new_user)
        db.session.flush()

    db.session.commit()
