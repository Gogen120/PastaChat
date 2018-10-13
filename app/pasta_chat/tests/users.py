import random


def create_example_user_data():
    return {
        'username': f'Username{int(random.random() * 1000)}'
    }
