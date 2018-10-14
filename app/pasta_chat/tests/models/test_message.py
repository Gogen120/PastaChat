import pytest

from pasta_chat import db
from pasta_chat.models import Message
from ..data.messages import create_example_message_data


@pytest.fixture(autouse=True)
def setup():
    db.session.query(Message).delete()
    db.session.commit()
    yield


def test_message_creation():
    message = Message(**create_example_message_data())
    db.session.add(message)
    db.session.commit()

    assert message
    assert db.session.query(Message).get(message.id)


def test_message_deletion():
    message = Message(**create_example_message_data())
    db.session.add(message)
    db.session.commit()

    assert db.session.query(Message).delete()
    assert len(db.session.query(Message).all()) == 0


def test_message_update():
    message = Message(**create_example_message_data())
    db.session.add(message)
    db.session.commit()

    new_message_content = 'New message content'

    assert message.content != new_message_content

    message.content = new_message_content

    message_from_db = db.session.query(Message).filter_by(content=message.content)
    message_from_db.content = new_message_content

    db.session.commit()

    assert message_from_db.content == new_message_content


def test_create_multiple_messages():
    first_message = Message(**create_example_message_data())
    second_message = Message(**create_example_message_data())

    db.session.add_all([first_message, second_message])
    db.session.commit()

    assert len(db.session.query(Message).all()) == 2
