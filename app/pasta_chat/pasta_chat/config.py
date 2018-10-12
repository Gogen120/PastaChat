import os


def apply_configs(app):
    config_functions = [
        apply_sqlalchemy_configs,
        apply_non_categorized_configs
    ]

    for config_function in config_functions:
        config_function(app)


def apply_sqlalchemy_configs(app):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{os.environ['PG_USER']}:{os.environ['PG_PASS']}@{os.environ['PG_HOST']}:{os.environ['PG_PORT']}/postgres"


def apply_non_categorized_configs(app):
    app.config['SECRET_KEY'] = 'super secret key'
    app.config['SESSION_TYPE'] = 'null'
