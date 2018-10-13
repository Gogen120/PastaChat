from setuptools import setup

setup(
    name='pasta_chat',
    packages=['pasta_chat'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask_migrate',
        'psycopg2-binary',
        'pytest',
        'flask-restful',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'docker'
    ],
)
