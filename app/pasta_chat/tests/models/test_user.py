import pytest

from pasta_chat import db
from pasta_chat.models import User
from ..data.users import create_example_user_data


@pytest.fixture(autouse=True)
def setup():
    db.session.query(User).delete()
    db.session.commit()
    yield


def test_user_creation():
    user = User(**create_example_user_data())
    db.session.add(user)
    db.session.commit()

    assert user
    assert db.session.query(User).get(user.id)


def test_user_deletion():
    user = User(**create_example_user_data())
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).delete()
    assert len(db.session.query(User).all()) == 0


def test_user_update():
    user = User(**create_example_user_data())
    db.session.add(user)
    db.session.commit()

    new_username = 'NewUsername'

    assert user.username != new_username

    user.username = new_username

    user_from_db = db.session.query(User).filter_by(username=user.username).first()
    user_from_db.username = new_username

    db.session.commit()

    assert user_from_db.username == new_username


def test_create_multiple_users():
    first_user = User(**create_example_user_data())
    second_user = User(**create_example_user_data())

    db.session.add_all([first_user, second_user])
    db.session.commit()

    assert len(db.session.query(User).all()) == 2
