from pasta_chat import db
from pasta_chat.models import User


def create_user_example():
    user_data = {
        'username': 'username123'
    }
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
